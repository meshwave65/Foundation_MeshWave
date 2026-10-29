# MISSION_0011 — TASKS — PROGRESS

**Repositório canônico:** `https://github.com/meshwave65/Foundation_MeshWave`
**Blueprint:** `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md`
**Protocolo de handoff:** `BCE/PROTOCOLO_MISSOES_E_HANDOFF.md`
**Último checkpoint remoto confirmado na abertura:** `origin/main@f99069e`
**Estado da missão:** `BLOCKED`

| ID | Tarefa | Status | Instância | Repositório/artefato | Próxima ação única |
|---|---|---|---|---|---|
| F3.3-COORD-001 | Reconciliar fila e obter seleção/aprovação de um novo caminho físico para responder à lacuna DOM-03 §14.12 | BLOCKED | — | `BCE/CONTROLE_MESTRE.md`; `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md` | Não abrir `KNOWLEDGE/`; verificar `origin/main`/locks e solicitar ou registrar a seleção formal de ID + caminho |
| F3.3-UNIT-001 | Auditar a unidade física selecionada com lock exclusivo | STAGED | — | `BCE/locks/`, `BCE/sessoes/`, `BCE/fontes/` | Só iniciar após F3.3-COORD-001 sair de `BLOCKED` e o claim ser publicado |
| F3.3-CLOSE-001 | Integrar classificação, fechar lock e emitir handoff | STAGED | — | DOM de destino, índice e controle mestre | Executar somente após classificação publicada e hashes/commits validados |

## Regra de assunção

Assumir somente `F3.3-COORD-001` enquanto ela estiver `BLOCKED` e sem instância concorrente. Se um responsável publicar seleção/aprovação, atualizar a linha com o ID, caminho, instância e commit do checkpoint antes de reivindicar o contato. Não converter `STAGED` em leitura por inferência numérica.

## Critérios de fechamento

A coordenação fecha quando houver seleção formal ou bloqueio explicitamente renovado com motivo. A unidade fecha quando os artefatos mínimos do blueprint estiverem publicados, os hashes coincidirem, nenhum segredo tiver sido copiado, o lock estiver `ENCERRADO` e o handoff apontar uma única próxima ação.
