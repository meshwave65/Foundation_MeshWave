# Bloqueio exclusivo de contatos BCE

Este arquivo define o protocolo de concorrência para curadoria de fontes. O bloqueio é por **um contato físico por vez** e deve ser publicado no Git antes da leitura semântica.

## Protocolo obrigatório

1. Sincronize `main` e confirme `git status --short --branch`.
2. Leia `BCE/CONTROLE_MESTRE.md` e escolha somente o próximo contato exato registrado na fila.
3. Antes de abrir `content.txt`, `code_blocks.txt`, `links.txt` ou imagens, crie um arquivo de claim em `BCE/locks/` com nome seguro, por exemplo:
   `BCE/locks/F3.1-DOM01-E007.lock.md`.
4. O claim deve registrar contato, caminho físico, agente/sessão, data/hora, commit-base e estado `ATIVO`.
5. Faça commit e push do claim. O primeiro claim publicado para aquele contato vence. Se o push falhar por divergência, atualize a árvore e não force; se já existir claim ativo, abandone o contato e continue somente após o próximo item oficial.
6. Enquanto o claim estiver ativo, processe somente o caminho nele registrado. Não leia ou mapeie outro contato em paralelo.
7. Ao concluir, faça commits separados para classificação, integração e controle/checkpoint quando aplicável; depois substitua o claim por um fechamento `CONCLUÍDO` ou remova-o no mesmo commit do checkpoint, deixando no controle mestre o próximo contato exato.
8. Se a sessão for interrompida, mantenha o claim `ATIVO` por no máximo o período documentado no próprio arquivo. O agente sucessor deve verificar idade, commit e estado remoto antes de assumir; nunca apagar um claim ativo sem registrar a recuperação no controle.

## Formato mínimo do claim

```text
Contato: F3.1/E007/L002-04
Caminho físico: KNOWLEDGE/...
Estado: ATIVO
Agente/sessão: <identificador>
Abertura: <ISO-8601 com fuso>
Commit-base: <hash>
Próximo passo: <ação única>
```

`KNOWLEDGE/` permanece imutável. O lock protege a unidade de processamento e não autoriza editar a fonte bruta.
