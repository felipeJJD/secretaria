# Mapa de intenções

Use para classificar o pedido e saber **o que procurar** no catálogo
(`scripts/catalogo.py --busca "<palavras>"`). Os nomes de skill variam de pessoa
para pessoa: procure pelas palavras, não por um nome fixo.

| Intenção | Palavras para buscar no catálogo | Agentes e modelos | Prova de pronto |
|---|---|---|---|
| Criar app, site ou funcionalidade | frontend, design, react, next, api, tdd, test, plan | coordenador + 1 implementador; revisor no fim | build e testes passando, print da tela |
| Corrigir bug | debug, bug, diagnos, test, log | 1 agente; modelo forte só se o bug resistir | teste que falhava agora passa |
| Revisar código | review, security, audit, simplify | revisor só leitura, recebe o diff | lista de achados com arquivo:linha |
| Página bonita / landing | design, taste, ui, frontend, animation | 1 agente + revisão visual por print | print desktop e celular |
| Vídeo, Reels, edição | video, ffmpeg, caption, legenda, remotion, motion, audio | coordenador; render em segundo plano | vídeo final + quadros de conferência |
| Imagem, logo, criativo | image, logo, design, ads, creative | 1 agente | arquivo gerado aberto e conferido |
| Copy, marketing, anúncio | copy, marketing, ads, seo, email, launch | 1 agente; pesquisa barata antes | texto final + variações |
| Pesquisa | research, search, web, scrape, docs | subagentes baratos em paralelo, 1 síntese | resumo com fontes e datas |
| Dados, planilha, relatório | xlsx, csv, sql, data, chart, dashboard | 1 agente | arquivo + números conferidos |
| Documento, PDF, apresentação | pdf, docx, pptx, slides, docs | 1 agente | arquivo aberto e conferido |
| Automação, tarefa recorrente | schedule, cron, loop, n8n, workflow | 1 agente | execução de teste registrada |
| Infra, deploy, banco | deploy, docker, railway, vercel, supabase, postgres, migration | 1 agente; deploy só com pedido | health check / URL respondendo |
| Criar ou ajustar skill | skill, writing-skills, skill-creator | 1 agente | skill carrega e dispara no teste |
| Organizar ideia antes de fazer | brainstorm, grill, plan, spec | só a conversa | plano aprovado |

## Escada de custo (modelos)

1. **Rápido/barato** (ex.: Haiku, modelos mini/flash): busca, inventário, ler log,
   rodar comando e relatar, edição repetitiva já especificada.
2. **Padrão** (ex.: Sonnet, modelo principal do Codex): implementar, corrigir,
   testar, revisar uma tarefa.
3. **Mais forte** (ex.: Opus, modelos de raciocínio alto): arquitetura difícil,
   bug que resistiu, revisão final integrada.

Suba um degrau só quando o de baixo não der conta, e diga isso no "Usei".

## Quando usar subagentes

- Sim: partes independentes (pesquisa em paralelo, front e back separados),
  revisão com olhar limpo, tarefa mecânica longa.
- Não: tarefa pequena, passos que dependem um do outro, quando o contexto todo
  precisa ficar num lugar só.
