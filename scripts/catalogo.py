"""Catálogo do setup de IA: skills, skills de plugins e MCPs instalados nesta máquina.

Uso:
  python catalogo.py                     # lista tudo (uma linha por item)
  python catalogo.py --busca "video ffmpeg legenda"   # as 40 que mais casam com as palavras
  python catalogo.py --json              # saída em JSON

Mostra só NOMES e DESCRIÇÕES. Nunca lê nem imprime valores de configuração
(chaves, tokens, senhas, URLs de servidores MCP). Só biblioteca padrão, Python 3.8+.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

HOME = Path.home()
CWD = Path.cwd()

SKILL_ROOTS = [
    ("claude", HOME / ".claude" / "skills"),
    ("agents", HOME / ".agents" / "skills"),
    ("codex", HOME / ".codex" / "skills"),
    ("cursor", HOME / ".cursor" / "skills"),
    ("gemini", HOME / ".gemini" / "skills"),
    ("projeto", CWD / ".claude" / "skills"),
    ("projeto", CWD / ".agents" / "skills"),
    ("projeto", CWD / ".codex" / "skills"),
]
if os.environ.get("CLAUDE_CONFIG_DIR"):
    SKILL_ROOTS.insert(0, ("claude", Path(os.environ["CLAUDE_CONFIG_DIR"]) / "skills"))

PLUGIN_ROOTS = [HOME / ".claude" / "plugins", HOME / ".codex" / "plugins"]
if os.environ.get("CLAUDE_CONFIG_DIR"):
    PLUGIN_ROOTS.insert(0, Path(os.environ["CLAUDE_CONFIG_DIR"]) / "plugins")


def frontmatter(md: Path):
    """name e description do bloco --- do SKILL.md (aceita description em várias linhas)."""
    try:
        text = md.read_text(encoding="utf-8", errors="replace")[:6000]
    except OSError:
        return None, None
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    block = m.group(1)
    name = re.search(r"^name:\s*['\"]?([^'\"\n]+)", block, re.M)
    desc = None
    d = re.search(r"^description:\s*(.*)$", block, re.M)
    if d:
        first = d.group(1).strip()
        if first in ("|", ">", "|-", ">-", ""):
            rest = block[d.end():].split("\n")
            lines = []
            for ln in rest:
                if ln.startswith((" ", "\t")):
                    lines.append(ln.strip())
                elif ln.strip():
                    break
            desc = " ".join(lines)
        else:
            desc = first.strip("'\"")
    return (name.group(1).strip() if name else md.parent.name), desc


def skills():
    seen, out = set(), []
    for origem, root in SKILL_ROOTS:
        if not root.is_dir():
            continue
        for md in sorted(root.glob("*/SKILL.md")):
            name, desc = frontmatter(md)
            if not name or name in seen:
                continue
            seen.add(name)
            out.append({"tipo": "skill", "nome": name, "descricao": desc or "", "origem": origem})
    for root in PLUGIN_ROOTS:
        if not root.is_dir():
            continue
        for md in sorted(root.glob("**/skills/*/SKILL.md")):
            name, desc = frontmatter(md)
            if not name or name in seen:
                continue
            seen.add(name)
            out.append({"tipo": "skill", "nome": name, "descricao": desc or "", "origem": "plugin"})
    return out


def mcps():
    """Só os NOMES dos servidores MCP configurados."""
    names = {}

    def add(n, origem):
        names.setdefault(n, origem)

    for p, origem in [(HOME / ".claude.json", "claude"), (CWD / ".mcp.json", "projeto"),
                      (HOME / ".cursor" / "mcp.json", "cursor"), (HOME / ".gemini" / "settings.json", "gemini")]:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for n in (data.get("mcpServers") or {}):
            add(n, origem)
        proj = (data.get("projects") or {}).get(str(CWD)) or {}
        for n in (proj.get("mcpServers") or {}):
            add(n, "projeto")
    toml = HOME / ".codex" / "config.toml"
    try:
        for n in re.findall(r"^\[mcp_servers\.([A-Za-z0-9_\-\"]+)\]", toml.read_text(encoding="utf-8"), re.M):
            add(n.strip('"'), "codex")
    except OSError:
        pass
    return [{"tipo": "mcp", "nome": n, "descricao": "", "origem": o} for n, o in sorted(names.items())]


def norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def main(argv):
    busca = None
    if "--busca" in argv:
        i = argv.index("--busca")
        busca = [norm(w) for w in " ".join(argv[i + 1:i + 2]).split() if w]
    itens = skills() + mcps()
    if busca:  # mais palavras casando (no nome vale 3) = mais acima; no máximo 40
        def nota(x):
            nome, desc = norm(x["nome"]), norm(x["descricao"])
            return sum(3 * (w in nome) + (w in desc) for w in busca)
        itens = sorted((x for x in itens if nota(x)), key=nota, reverse=True)[:40]
    if "--json" in argv:
        print(json.dumps(itens, ensure_ascii=False, indent=1))
        return
    n_sk = sum(1 for x in itens if x["tipo"] == "skill")
    n_mcp = len(itens) - n_sk
    print(f"# Catálogo: {n_sk} skills, {n_mcp} MCPs" + (f" (busca: {' '.join(busca)})" if busca else ""))
    for x in itens:
        d = re.sub(r"\s+", " ", x["descricao"])
        d = d if len(d) <= 180 else d[:177] + "..."
        print(f"- [{x['tipo']}/{x['origem']}] {x['nome']}" + (f" — {d}" if d else ""))
    if not itens:
        print("(nada encontrado — instale skills em ~/.claude/skills ou ~/.agents/skills)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        main(sys.argv[1:])
    except BrokenPipeError:  # saída cortada por head/less
        sys.stderr.close()
