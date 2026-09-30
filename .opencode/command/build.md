---
description: Gera o site rodando ./build.sh a partir de content/*.org
agent: build
---

Rode o build do site com o comando:

```
./build.sh
```

Depois:

1. Verifique no final se a mensagem `Build complete!` apareceu.
2. Liste os arquivos HTML alterados em `public/` (use `git status --short public`).
3. Se houver erro, mostre a mensagem relevante e sugira a correção no
   `content/` ou em `build-site.el`.

Não edite nada em `public/` manualmente.
