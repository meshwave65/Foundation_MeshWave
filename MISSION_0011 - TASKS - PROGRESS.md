# MISSION_0011 — TASKS — PROGRESS

**Repositório canônico:** `https://github.com/meshwave65/Foundation_MeshWave`
**Blueprint:** `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md`
**Protocolo de handoff:** `BCE/PROTOCOLO_MISSOES_E_HANDOFF.md`
**Último checkpoint remoto confirmado:** `origin/main@3f69a04`; fechamento do ID-262 registrado em `BCE/sessoes/2026-10-28_f3-3-id262-fechamento.md`
**Estado da missão:** `PROGRESS`

| ID | Tarefa | Status | Instância | Repositório/artefato | Próxima ação única |
|---|---|---|---|---|---|
| F3.3-COORD-001 | Reconciliar fila e obter seleção/aprovação de um novo caminho físico para responder à lacuna DOM-03 §14.12 | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | Mapa `BCE/sessoes/2026-10-28_mission-0011-mapa-candidatos.md`; seleção ID-206 | Claim ID-206 publicado após seleção explícita; prosseguir somente no caminho reivindicado |
| F3.3-UNIT-001 | Auditar a unidade física selecionada com lock exclusivo | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | `BCE/fontes/CLASSIFICACAO_F3_3_ID206.md`; hashes 5/5 | ID-206 encerrado; não reabrir |
| F3.3-CLOSE-001 | Integrar classificação, fechar lock e emitir handoff | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | DOM-03 `65ee2e2`; índice `1d97910`; fechamento | Unidade concluída e lock encerrado; reconciliar próximo contato |
| F3.3-COORD-002 | Reconciliar fila após ID-206 e selecionar o próximo contato físico | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | Claim ID-262 publicado em `7afc87f` | Unidade ID-262 reivindicada após reconciliação sem corrida |
| F3.3-UNIT-002 | Auditar a unidade física ID-262 com lock exclusivo | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | `BCE/fontes/CLASSIFICACAO_F3_3_ID262.md`; hashes 5/5 | ID-262 encerrado; não reabrir |
| F3.3-CLOSE-002 | Integrar classificação, fechar lock e emitir handoff | DONE | Manus / sandbox:root:9a8vVvOkKgNlcDNLamYLk7 | DOM-03 `fa003f9`; índice `3f69a04`; fechamento | Unidade concluída; reconciliar próximo caminho físico |
| F3.3-COORD-003 | Reconciliar fila restante e selecionar o próximo contato físico | STAGED | — | Inventário/classificações F3.3; nenhum claim ativo após ID-262 | Sincronizar `origin/main`, mapear somente metadados e publicar novo claim antes da leitura |

## Regra de assunção

Assumir somente a próxima linha `STAGED` após confirmar que não há instância concorrente. ID-206 e ID-262 estão encerrados; a coordenação seguinte deve mapear candidatos apenas por inventário/metadados, escolher um único caminho e publicar claim antes de qualquer leitura semântica.

## Critérios de fechamento

A coordenação fecha quando houver seleção formal ou bloqueio explicitamente renovado com motivo. A unidade fecha quando os artefatos mínimos do blueprint estiverem publicados, os hashes coincidirem, nenhum segredo tiver sido copiado, o lock estiver `ENCERRADO` e o handoff apontar uma única próxima ação.
