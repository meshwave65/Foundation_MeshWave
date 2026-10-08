# Escopo físico — F2.6 SOFIA, agentes e missões

## Regra de processamento

Este arquivo fecha o lote antes da leitura profunda. Para cada caminho serão conferidos `content.txt`, `code_blocks.txt`, `links.txt` e todas as imagens associadas. Títulos, cartões de “tarefa concluída”, instruções de acesso, código transcrito e respostas de API não equivalem a execução bem-sucedida, autorização, persistência ou implantação.

A unidade prioriza o fluxo **SOFIA → obtenção de missão → decomposição/agente → execução → relatório/estado**. Persistência, ChromaDB, banco vetorial e operação remota entram apenas quando forem dependências diretas desse fluxo; a modelagem aprofundada de memória e armazenamento será consolidada em DOM-07.

## Fontes do lote prioritário

### A. Visão de sistema e passagem de contexto

1. `KNOWLEDGE/johann/20260422_175016_SOFIA and MeshWave Ecosystem Overview - Manus`
2. `KNOWLEDGE/johann/20260422_175100_SOFIA and MeshWave Ecosystem Documents - Manus`
3. `KNOWLEDGE/johann/20260422_175351_Uploaded Documents Related to SOFIA and MeshWave Ecosystem - Manus`
4. `KNOWLEDGE/johann/20260422_171657_Relatório de Passagem de Contexto Sistema SOFIA - Manus`
5. `KNOWLEDGE/meshwave65/20260422_Reabilitação do Sistema SOFIA - Manus`

### B. Agentes, execução e orquestração

6. `KNOWLEDGE/andressa/20260422_162534_Automatização e Estruturação de Agentes no Projeto Mesh Wave - Manus`
7. `KNOWLEDGE/johann/20260422_174331_Conhecimento sobre Meshwave, Sofia e módulos ARC-Bayes_ - Manus`
8. `KNOWLEDGE/mateus/20260422_173923_Files Related to Mission Report and AI Agent Manual - Manus`
9. `KNOWLEDGE/johann/20260422_174105_Diretrizes para a missão e solução de dúvidas - Manus`
10. `KNOWLEDGE/dinelson/20260422_154718_Instruções para Execução da Missão com Sistema Remoto - Manus`

### C. API SOFIA, tarefas e oráculo

11. `KNOWLEDGE/andressa/20260422_161931_Como acessar e concluir missões na API Sofia - Manus`
12. `KNOWLEDGE/dinecy/20260422_171255_Diretrizes para execução da tarefa no Sofia API - Manus`
13. `KNOWLEDGE/filipe/20260422_164903_Instruções para a missão via Sofia API - Manus`
14. `KNOWLEDGE/iury/20260422_161525_Como acessar e executar missões na API Sofia - Manus`
15. `KNOWLEDGE/iury/20260422_161704_Access Sofia API to Receive and Complete Missions - Manus`
16. `KNOWLEDGE/iury/20260422_161748_Como acessar e verificar missões na API Sofia - Manus`
17. `KNOWLEDGE/iury/20260422_161834_Como acessar e executar missões na API Sofia - Manus`
18. `KNOWLEDGE/iury/20260422_161913_Instruções para a Tarefa no Sofia API Oráculo - Manus`
19. `KNOWLEDGE/mateus/20260422_174112_Como usar a API Sofia para obter tarefas disponíveis_ - Manus`
20. `KNOWLEDGE/natalia/20260422_171420_Instruções para Missão via Sofia API Manual - Manus`
21. `KNOWLEDGE/natalia/20260422_171528_Como acessar sofia-api.meshwave.com.br e receber instruções - Manus`

### D. Projeto e onboarding SOFIA

22. `KNOWLEDGE/filipe/20260422_165023_Projeto Sofia_ Dossiê de Recrutamento e Onboarding - Manus`
23. `KNOWLEDGE/natalia/20260422_171636_Projeto Sofia_ Dossiê de Recrutamento e Onboarding - Manus`

## Fontes relacionadas, reservadas para DOM-07/DOM-13 salvo dependência direta

- `KNOWLEDGE/dinelson/20260422_154208_Sistema de Persistência e Sincronização para Agentes Manus - Manus`
- `KNOWLEDGE/natalia/20260422_171317_Manual Chroma Agentes - Manus`
- `KNOWLEDGE/nadir/20260422_171345_Acessando DB Vetorial e Sofia API via Cloudflare - Manus`
- `KNOWLEDGE/johann/20260422_173623_Getting Started with Chroma Deployment - Manus`
- `KNOWLEDGE/johann/20260422_173708_Getting Started with Chroma Deployment - Manus`
- `KNOWLEDGE/johann/20260422_173755_Getting Started with Chroma Deployment - Manus`
- `KNOWLEDGE/johann/20260422_173858_Getting Started with Chroma Deployment - Manus`
- `KNOWLEDGE/johann/20260422_174008_Getting Started with Chroma Deployment - Manus`
- `KNOWLEDGE/johann/20260422_174207_Getting Started with Chroma Deployment and Configuration - Manus`

## Justificativa de inclusão

O lote combina visões de sistema, relatos de passagem de contexto, manuais de agente, instruções de missão, tentativas de obtenção/verificação/conclusão de tarefas e propostas de onboarding. A sobreposição entre fontes é intencional: permitirá separar versões, duplicação interna, continuação candidata e divergências de API/estado.

A fonte de reabilitação do SOFIA foi incluída para capturar decisões operacionais e limites de recuperação. As fontes de persistência e Chroma foram reservadas porque seu domínio próprio exige tratamento de contratos de armazenamento, sincronização, recuperação e segurança, evitando misturar execução de missão com estado de conhecimento.

## Exclusões nesta unidade

- DID, identidade de equipamento e identidade soberana: DOM-04.
- ARC, PGC e inferência bayesiana: DOM-05; somente dependências de agente serão relacionadas.
- Topologia, CLA/CPA e roteamento: DOM-03.
- Implementação Android e compatibilidade de dispositivos: DOM-10.
- Especificação completa de ChromaDB, banco vetorial, memória e sincronização: DOM-07.
- Atualização, restauração, Cloudflare e operação de infraestrutura: DOM-13, salvo quando forem necessários para explicar um erro ou fluxo SOFIA.
- Conteúdo médico, comercial ou externo carregado como contexto de missão: preservar e classificar, mas não tratá-lo como requisito MeshWave sem evidência adicional.

## Resultado esperado

Produzir ou atualizar `BCE/temas/sofia-agentes-missoes-e-oraculo.md` com terminologia, papéis, estados de missão, contratos de API observados, fluxo supervisor/atômico, agentes, passagem de contexto, relatórios, falhas, segurança, evidências, conflitos e lacunas. Manter `REVISÃO` se não houver contratos, código, logs e execução verificáveis.

## Critério de fechamento do lote

Antes da leitura profunda, confirmar a existência dos 23 diretórios prioritários, registrar arquivos presentes e iniciar checkpoint. Depois da leitura, classificar cada fonte como visão, procedimento, transcrição, erro, resultado ou evidência operacional; não submeter APIs, missões, uploads ou alterações externas durante a curadoria.
