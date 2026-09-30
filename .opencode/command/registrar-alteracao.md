---
description: Registra um resumo legível das alterações no CHANGELOG.org
agent: build
---

Registre no `CHANGELOG.org` um resumo legível das alterações recentes.

Passos:

1. Inspecione as mudanças com `git status --short` e `git diff --stat`.
2. Escreva uma entrada descrita em português, agrupada pela data de hoje no
   formato de título de Org Mode `* AAAA-MM-DD` (use a data atual).
3. Cada item deve explicar **o que mudou** e **em quais arquivos**, de forma
   curta. Não repita o log automático linha a linha: resuma.
4. Se já existir o título de hoje, acrescente os itens sob ele. Senão, crie.
5. Não commite nem dê push.

Contexto adicional do usuário: $ARGUMENTS
