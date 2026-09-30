# AGENTS.md

Guia para agentes que trabalham neste repositório.

## Visão geral

Site de resumos de Física para o Ensino Médio (IFAM *Campus* Manaus Centro).
O conteúdo é escrito em **Org Mode** e publicado como HTML estático.

Fluxo: `content/*.org` → `build-site.el` (Emacs + `org-publish`) → `public/`.
O GitHub Actions (`.github/workflows/publish.yml`) roda `./build.sh` a cada
push em `master` e publica `public/` na branch `gh-pages`.

## Estrutura

- `content/` — fontes `.org` (aqui é onde se edita conteúdo).
- `content/pictures/`, `content/graphics/` — imagens e scripts de gráficos.
- `public/` — HTML **gerado**; não editar à mão.
- `build-site.el` — configuração de exportação (`org-publish-project-alist`).
- `build.sh` — atalho: `emacs -Q --script build-site.el`.
- `.packages/` — dependências Emacs instaladas localmente; não editar.

## Comandos

- Gerar o site: `./build.sh`
- Pré-visualizar localmente (dentro do Emacs): `M-x httpd-serve-directory` em
  `public/`.

## Convenções

- Idioma do conteúdo: **português (pt-BR)**.
- Arquivos de conteúdo em Org Mode (`.org`), codificação UTF-8.
- Preservar a estrutura de títulos e a linguagem já usados nos arquivos.
- Não usar HTML solto quando houver equivalente em Org.

## Regras importantes

- **Nunca** editar `public/` nem `.packages/` manualmente — são gerados.
- Para mudanças visíveis no site, editar `content/` e rodar `./build.sh`.
- Não commitar nem dar push sem pedido explícito do usuário.

## Registro de alterações

- O plugin `.opencode/plugin/changelog.ts` registra automaticamente cada
  arquivo editado em `CHANGELOG.org`, agrupado por data.
- Para um resumo legível, use o comando `/registrar-alteracao`.
- Comandos: `/build` gera o site.
