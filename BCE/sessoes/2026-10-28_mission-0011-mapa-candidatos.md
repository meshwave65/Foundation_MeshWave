# Mapa de candidatos — MISSION_0011 / F3.3

- **Data:** 2026-10-28 23:23 (-03:00).
- **Commit-base:** `d078a90` após sincronização com `origin/main`.
- **Escopo consultado:** `BCE/CONTROLE_MESTRE.md`, `BCE/BLUEPRINT_F3_3_EXECUCAO_PARALELA.md`, DOM-03 §14.12, `BCE/fontes/ESCOPO_F2_3_REDE_MESH.md`, `INVENTARIO_FONTES.md/.csv` e locks.
- **Estado:** shortlist documental publicada; nenhum candidato selecionado; nenhum claim ativo; nenhuma fonte bruta aberta.

## Lacuna a responder

DOM-03 §14.12 pede localizar um simulador ou fonte de código auditável com versão/commit, dependências, entradas, testes, dados e logs. O pacote ID-229 foi encerrado e não contém o arquivo completo anunciado `meshwave_simulator.py`.

## Candidatos físicos não processados identificados no inventário

### ID-206 — candidato direto de simulador

- **Caminho:** `KNOWLEDGE/meshwave65/20260422_Desenvolvimento de simulador - Manus/`
- **Inventário:** 5 artefatos, 3 imagens, 2 arquivos de imagem adicionais; 219.713 bytes no inventário.
- **Metadados físicos observados sem leitura semântica:** `FULL.png` 123.518 bytes; `code_blocks.txt` 682 bytes; `content.txt` 10.927 bytes; `img_000.jpg` 84.564 bytes; `links.txt` 22 bytes.
- **SHA-256 do pré-mapeamento:** `FULL.png` `b4eccf72d35824d9ab80848de6b93a7b8b8cf831ebecac41fe89eeafc6873abc`; `code_blocks.txt` `3a64e3e4b0c15e1dac9c44111b6595fa3e376ead68b612a03e488e2754170e02`; `content.txt` `f03068434f639d9e9491029c24cad7bf3276aa54321ac9ac220af0466871f72f`; `img_000.jpg` `3552686377cb1c5555ec73ad0f5f1b9bd67fb53860efe9b3a3136e0213603b46`; `links.txt` `3794c198c4ad415f025776affe173db4e5a9078d4b01741d24477080aca13f5e`.
- **Justificativa documental:** título diretamente orientado a desenvolvimento de simulador; possui dois artefatos de imagem e um bloco de código; prioridade de inventário 5.
- **Limite:** título, contagem e metadados não provam que o fonte completo, testes ou logs existam.

### ID-262 — candidato direto de inconsistência código/resultado

- **Caminho:** `KNOWLEDGE/omaci2008/20260422_172245_Inconsistências nos Resultados do Simulador e Código-Fonte - Manus/`
- **Inventário:** 5 artefatos, 3 imagens, 2 arquivos de imagem adicionais; 478.632 bytes no inventário.
- **Metadados físicos observados sem leitura semântica:** `FULL.png` 164.403 bytes; `code_blocks.txt` 82 bytes; `content.txt` 93.419 bytes; `img_000.jpg` 220.646 bytes; `links.txt` 82 bytes.
- **SHA-256 do pré-mapeamento:** `FULL.png` `440e7a863e8741871948e9464ffe9a929d273b914d0bc0d3cbf1781a0012e03a`; `code_blocks.txt` `bac05d68b3356efb4e3c797691ff46cc56bd4dc843873e37688a5d176a3050ac`; `content.txt` `2393b8f07f13184e96375c6eca00da178e8815df674830fa0f391e4b6b2c3807`; `img_000.jpg` `80556b5232a80434a283049db505fc37f0f4b6237cca25457501b32b7305c239`; `links.txt` `e5793a973d6a4c0273281eb8d6a1e8bae6043e6e2912989671ff2e2ce6c8b783`.
- **Justificativa documental:** título diretamente relaciona inconsistências de resultados a código-fonte; possui imagens e um conjunto de links; prioridade de inventário 5.
- **Limite:** o bloco de código é pequeno e os metadados não provam existência de fonte, testes ou logs reproduzíveis.

## Itens não selecionados

Os demais nomes relacionados a simuladores no inventário foram mantidos fora da shortlist por serem descrições genéricas de criação de app/simulador ou por não terem relação documental tão direta com a lacuna do simulador MeshWave. Essa exclusão é apenas uma priorização documental, não uma classificação semântica nem autorização para ignorá-los definitivamente.

## Decisão pendente

O responsável deve selecionar explicitamente **ID-206** ou **ID-262** — ou designar outro ID/caminho físico exato. Depois da seleção, atualizar `MISSION_0011 - TASKS - PROGRESS.md` e `BCE/CONTROLE_MESTRE.md`, publicar o claim exclusivo e o pré-registro antes de abrir qualquer arquivo do candidato. Até lá, a missão permanece `BLOCKED`.
