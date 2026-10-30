# Modelo do prompt entregue

Preencha só as seções que se aplicam e corte as vazias. Alvo: 20–50 linhas.
Escreva como instrução direta ao executor, sem citar a conversa.
Sintaxe de skill: `/nome` no Claude Code, `$nome` no Codex, nome por extenso nos outros.

```
# <Título curto do trabalho>

## Objetivo
<1–2 frases com o resultado concreto>. Pronto quando: <critério verificável>.

## Contexto
- Projeto: <nome> — <caminho>, branch <b>. <estado relevante em 1 linha>
- Ler primeiro: <README/AGENTS.md/CLAUDE.md do projeto, só a seção X>
- Premissas: <decisões assumidas na entrevista>

## Como executar
- Coordenador: <agente> com <modelo>. Decide e integra.
- Subagentes (se houver):
  - <modelo> → <parte independente> (arquivos: <quais>)
- Skills, nesta ordem: <skill> — <para quê>; <skill> — <para quê>
- Ferramentas/MCP: <nome> — <para quê>

## Passos
1. <fase> → mostrar <o quê> antes de seguir
2. ...

## Verificação
- <comando, teste, print ou render que prova o pronto, com o resultado esperado>

## Restrições
- Não mexer em: <...>
- Sem commit, push, deploy, migração, gasto ou envio externo sem pedido explícito.
- Nunca colocar chaves, senhas ou dados pessoais em prompts, logs ou arquivos.

## Entrega
Resumo curto: o que mudou, as verificações com a saída, o que ficou pendente.
```
