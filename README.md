# 🗂️ Secretária — a IA que escolhe as ferramentas por você

Você tem dezenas (ou centenas) de skills instaladas e não lembra qual usar?
A **Secretária** resolve isso. Você escreve a ideia do jeito que pensa, bagunçada mesmo, e ela:

1. **descobre sozinha** as skills, plugins e MCPs que *você* tem instalados;
2. faz **no máximo 4 perguntas**, cada uma já com a resposta que ela recomenda;
3. monta o **plano**: quais skills, quais agentes, qual modelo em cada parte (o mais barato que resolve);
4. entrega um **prompt pronto** para copiar e colar;
5. explica **por que escolheu** cada ferramenta e **o que deixou de fora**.

Funciona com **Claude Code**, **Codex** e qualquer agente que leia skills no formato `SKILL.md`.
Não guarda nem envia nada: só lê os nomes e descrições das suas skills.

---

## Instalar

### Jeito fácil: peça para a sua IA

Cole isto no Claude Code ou no Codex:

```
Instale a skill "secretaria" de https://github.com/felipeJJD/secretaria para mim.
Descubra se você é o Claude Code ou o Codex. Clone o repositório na pasta de skills
do usuário: ~/.claude/skills/secretaria (Claude Code) ou ~/.agents/skills/secretaria (Codex).
Se a pasta já existir, só atualize com git pull. Confira que o SKILL.md está lá, rode
"python scripts/catalogo.py" dentro dela para testar (deve listar as minhas skills) e me diga para
reiniciar a sessão e chamar /secretaria (Claude Code) ou $secretaria (Codex).
```

### Jeito manual

**Claude Code** (macOS / Linux):

```bash
git clone https://github.com/felipeJJD/secretaria ~/.claude/skills/secretaria
```

**Claude Code** (Windows, PowerShell):

```powershell
git clone https://github.com/felipeJJD/secretaria "$HOME\.claude\skills\secretaria"
```

**Codex**: troque a pasta por `~/.agents/skills/secretaria`.

Sem git? Baixe o [ZIP](https://github.com/felipeJJD/secretaria/archive/refs/heads/main.zip),
extraia e renomeie a pasta para `secretaria` dentro da pasta de skills.

Reinicie o agente depois de instalar.

## Usar

```
/secretaria quero um site pra minha barbearia com agendamento e quero postar no ar hoje
```

(no Codex: `$secretaria ...`)

Ela vai responder com as perguntas, depois com o plano, o prompt pronto, a lista
**Usei** / **Deixei de fora** e um "Executo aqui?".

## O que tem aqui

| Arquivo | Para quê |
|---|---|
| `SKILL.md` | as instruções da secretária |
| `scripts/catalogo.py` | lista suas skills, plugins e MCPs (só nomes e descrições; Python 3.8+, sem dependências) |
| `references/mapa.md` | intenção → que tipo de skill, agente e modelo procurar |
| `references/prompt-modelo.md` | o formato do prompt entregue |

Teste o catálogo sozinho:

```bash
python scripts/catalogo.py --busca "video legenda"
```

## Privacidade

- O catálogo lê só o `name` e a `description` de cada `SKILL.md` e os **nomes** dos
  servidores MCP. Nunca lê chaves, tokens ou senhas.
- Nada sai do seu computador.

---

Feito por [@astro_lipenation](https://instagram.com/astro_lipenation). Licença MIT.
