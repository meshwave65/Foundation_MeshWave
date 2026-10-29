# MISSION_0011 — TASKS — PROGRESS

**Repositório canônico:** `https://github.com/meshwave65/Foundation_MeshWave`
**Blueprint:** `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md`
**Protocolo de handoff:** `BCE/PROTOCOLO_MISSOES_E_HANDOFF.md`
**Último checkpoint remoto confirmado:** `origin/main@91f20d2`; seleção formal do ID-206 registrada em `BCE/sessoes/2026-10-28_f3-3-id206-abertura.md`
**Estado da missão:** `PROGRESS`

| ID | Tarefa | Status | Instância | Repositório/artefato | Próxima ação única |
|---|---|---|---|---|---|
| F3.3-COORD-001 | Reconciliar fila e obter seleção/aprovação de um novo caminho físico para responder à lacuna DOM-03 §14.12 | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | Mapa `BCE/sessoes/2026-10-28_mission-0011-mapa-candidatos.md`; seleção ID-206 | Claim ID-206 publicado após seleção explícita; prosseguir somente no caminho reivindicado |
| F3.3-UNIT-001 | Auditar a unidade física selecionada com lock exclusivo | PROGRESS | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | `BCE/locks/F3.3-ID206.lock.md`; `BCE/sessoes/2026-10-28_f3-3-id206-abertura.md` | Revalidar os cinco SHA-256 e então ler somente os cinco artefatos pré-registrados |
| F3.3-CLOSE-001 | Integrar classificação, fechar lock e emitir handoff | STAGED | — | DOM de destino, índice e controle mestre | Executar somente após classificação publicada e hashes/commits validados |

## Regra de assunção

Assumir somente `F3.3-COORD-001` enquanto ela estiver `BLOCKED` e sem instância concorrente. Se um responsável publicar seleção/aprovação, atualizar a linha com o ID, caminho, instância e commit do checkpoint antes de reivindicar o contato. Não converter `STAGED` em leitura por inferência numérica.

## Critérios de fechamento

A coordenação fecha quando houver seleção formal ou bloqueio explicitamente renovado com motivo. A unidade fecha quando os artefatos mínimos do blueprint estiverem publicados, os hashes coincidirem, nenhum segredo tiver sido copiado, o lock estiver `ENCERRADO` e o handoff apontar uma única próxima ação.
