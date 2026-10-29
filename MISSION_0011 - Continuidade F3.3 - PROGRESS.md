# MISSION_0011 — Continuidade F3.3 — PROGRESS

## Identificação

- **Missão:** `MISSION_0011`
- **Objetivo:** retomar a F3.3 do BCE com governança compatível com o SofiaControlPanel, sem duplicar contatos e sem abrir fonte bruta enquanto não houver caminho físico designado.
- **Blueprint:** `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md`
- **Protocolo:** `BCE/PROTOCOLO_MISSOES_E_HANDOFF.md`
- **Repositório de execução:** `https://github.com/meshwave65/Foundation_MeshWave`
- **Repositório de diretrizes consultado:** `https://github.com/meshwave65/SofiaControlPanel`, `main@9d6bab8`, `AGENTS.md`
- **Skill BCE:** `meshwave-bce-curation` — consultar a versão/commit vigente no checkout antes de executar.
- **Estado:** `BLOCKED`
- **Gatilho curto:** “Retome a MISSION_0011 — F3.3 a partir do último checkpoint.”

## Estado atual e autoridade

O último estado remoto do BCE é `origin/main@f99069e` no momento da criação desta missão. O controle mestre registra F3.3/ID-229 concluída, nenhum claim ativo e ausência de próximo caminho físico inequívoco. O `SofiaControlPanel` possui uma `MISSION_0010` ativa para ARC/PGC, mas ela é um pipeline diferente e não autoriza misturar contatos, fontes ou alterações com a BCE.

A autoridade para continuidade é, nesta ordem: `origin/main` do BCE, este arquivo e seu arquivo de tarefas, o blueprint F3.3, `BCE/CONTROLE_MESTRE.md`, locks publicados e checkpoints mais recentes. A conversa não é fonte de estado.

## Escopo e não escopo

A missão coordena a seleção e auditoria de uma unidade física da F3.3. Ela não autoriza desenvolver o simulador, buscar fora do caminho designado o arquivo anunciado por ID-229, alterar `KNOWLEDGE/`, acessar APIs externas, abrir contatos por semelhança, ou modificar o `SofiaControlPanel`.

Se o trabalho passar a executar uma tarefa no SofiaControlPanel, o agente deve aplicar também `operational-task-lifecycle`, criar OR no SCP com `oracle_status: PENDING` e registrar o OR-ID no checkpoint BCE. Até lá, esta missão é exclusivamente documental no BCE.

## Critérios de aceite

A missão só pode sair de `BLOCKED` quando um responsável designar/aprovar um caminho físico novo ou uma decisão formal publicar essa seleção. Depois disso, cada contato deve deixar claim, pré-registro, hashes, classificação, integração temática, índice, checkpoint, lock encerrado e controle mestre atualizados. Todos os commits devem estar confirmados em `origin/main`, com árvore limpa e `git diff --check` aprovado.

## Handoff

O agente sucessor deve ler `MISSION_0011 - TASKS - PROGRESS.md`, sincronizar o BCE, confirmar que não há corrida ou lock ativo, reler o blueprint F3.3 e executar somente a próxima ação daquela tarefa. Se a linha continuar `BLOCKED`, não deve abrir nenhuma fonte; deve registrar a necessidade de seleção/aprovação e encerrar o handoff no mesmo ponto seguro.
