# Catálogo de links e referências externas — Lotes 001–003 (F1.6)

## 1. Escopo e método

- **Data:** 2026-10-08 (UTC−03:00).
- **Pré-registro:** `BCE/fontes/ESCOPO_LINKS_F1_6.md`, publicado antes da leitura dos `links.txt`.
- **Escopo:** 29 diretórios físicos únicos (30 referências entre L001–L003; a fonte `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus` aparece em L001 e L003 e foi contada uma vez).
- Foram lidos os 29 `links.txt`, preservando `KNOWLEDGE/` sem alteração. Arquivos ausentes/vazios foram contados como vazios; nenhum destino foi inferido a partir do título ou da mera presença do link.
- Para 11 URLs públicas ordinárias foram feitas requisições **HEAD sem autenticação**, sem enviar dados e sem seguir redirecionamentos. Portanto, os status abaixo verificam resposta HTTP do destino/endereço, não o conteúdo semântico da página.
- URLs Google `grounding-api-redirect` têm identificadores opacos no caminho e foram contabilizadas sem reproduzir os valores nem segui-las. Links `manus.go.link` apontam para ação de assinatura/subscrição e não foram abertos. `localhost` não foi consultado. Caminho GitHub incompleto não foi reconstruído nem solicitado.

## 2. Resumo quantitativo observado

| Métrica | Resultado | Interpretação |
|---|---:|---|
| Diretórios físicos únicos examinados | 29 | Escopo pré-registrado, sem ampliação |
| `links.txt` não vazio | 13/29 (44,8%) | Arquivos com ao menos uma linha não vazia |
| `links.txt` vazio | 16/29 (55,2%) | Arquivo presente sem conteúdo textual útil |
| `links.txt` ausente | 0/29 | Nenhum ausente no caminho físico canônico |
| Ocorrências de URL web listadas | 27 | Contagem textual, incluindo repetições |
| Formas de referência distintas | 18 | Inclui quatro redirecionadores Google com identificadores ocultados; URLs repetidas normalizadas por destino literal |
| Destinos submetidos a HEAD público | 11 | Somente leitura; sem autenticação, corpo ou redirecionamento seguido |
| Respostas HEAD 200 | 6 | Resposta HTTP do host/path no instante da consulta; conteúdo não examinado |
| Respostas HEAD 301/302 | 3 | Redirecionamento identificado; destino final não seguido |
| Respostas HEAD 403/404 | 2 | Bloqueio do servidor / não encontrado na resposta HEAD, respectivamente |
| Falha de conexão/DNS | 1 | Destino não confirmado por indisponibilidade/erro de rede |
| Redirecionadores opacos não consultados | 4 | Estado do destino final não confirmado |
| Links de ação `manus.go.link` não consultados | 6 ocorrências | Repetidos em seis fontes; efeito final não confirmado |
| Link local não consultado | 1 | `http://localhost:8080/`; sem significado fora do ambiente de origem |
| URL GitHub incompleta | 1 ocorrência | Caminho interrompido após `.../midia/Evolu`; não reconstruído |

Os números substituem as estimativas anteriores **aproximadas** no resumo de F1.5 (`14/29` e `≈28` links), conforme leitura direta dos arquivos do escopo F1.6. A diferença é registrada como correção de inventário, sem inferir o método da estimativa anterior.

## 3. Inventário por fonte

`Rxx` remete ao inventário de referências da seção 4. `∅` significa que `links.txt` foi lido e estava vazio.

| # | Fonte relativa | Referências observadas |
|---:|---|---|
| 1 | `KNOWLEDGE/info/20260422_171119_O que é o projeto Meshwave_ - Manus` | R01–R04 (quatro redirecionamentos Google com identificadores opacos; não seguidos) |
| 2 | `KNOWLEDGE/info/20260422_165052_Fonte para Arquitetura e Operação da Rede MeshWave - Manus` | ∅ |
| 3 | `KNOWLEDGE/info/20260422_165701_Hierarquia de CLA Continental e Roteamento - Manus` | ∅ |
| 4 | `KNOWLEDGE/info/20260422_165745_ARC - Autenticação Recessiva Contextual com inferência Bayesiana - Manus` | R05–R06 |
| 5 | `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus` | ∅ |
| 6 | `KNOWLEDGE/johann/20260422_174331_Conhecimento sobre Meshwave, Sofia e módulos ARC-Bayes_ - Manus` | R07 |
| 7 | `KNOWLEDGE/info/20260422_173855_Identificador Único do Equipamento na Rede - Manus` | R07, R08 |
| 8 | `KNOWLEDGE/info/20260422_174130_Definição do identificador único do equipamento na rede - Manus` | R07 |
| 9 | `KNOWLEDGE/info/20260422_174348_Complementar Módulos Faltantes do Diagrama de Implantação - Manus` | ∅ |
| 10 | `KNOWLEDGE/johann/20260422_175016_SOFIA and MeshWave Ecosystem Overview - Manus` | R07 |
| 11 | `KNOWLEDGE/johann/20260422_175100_SOFIA and MeshWave Ecosystem Documents - Manus` | ∅ |
| 12 | `KNOWLEDGE/andressa/20260422_162449_Desenvolvimento do Aplicativo MeshWave para Android - Manus` | ∅ |
| 13 | `KNOWLEDGE/andressa/20260422_161744_Title unclear without content - Manus` | ∅ |
| 14 | `KNOWLEDGE/andressa/20260422_161931_Como acessar e concluir missões na API Sofia - Manus` | R08–R15 (R08 é redirecionador de ação; R09–R15 são referências médicas/saúde e um vídeo; fora do escopo técnico MeshWave aparente) |
| 15 | `KNOWLEDGE/dinecy/20260422_171255_Diretrizes para execução da tarefa no Sofia API - Manus` | ∅ |
| 16 | `KNOWLEDGE/dinelson/20260422_154208_Sistema de Persistência e Sincronização para Agentes Manus - Manus` | R08, R16–R17 |
| 17 | `KNOWLEDGE/filipe/20260422_164903_Instruções para a missão via Sofia API - Manus` | ∅ |
| 18 | `KNOWLEDGE/filipe/20260422_165238_Criar interface para projeto no Android Studio - Manus` | ∅ |
| 19 | `KNOWLEDGE/info/20260422_170852_Prosseguimento no Projeto Android Bluetooth - Manus` | ∅ |
| 20 | `KNOWLEDGE/info/20260422_172056_Análise e continuidade sobre dispositivos Android antigos - Manus` | ∅ |
| 21 | `KNOWLEDGE/iury/20260422_161704_Access Sofia API to Receive and Complete Missions - Manus` | R08 |
| 22 | `KNOWLEDGE/iury/20260422_161913_Instruções para a Tarefa no Sofia API Oráculo - Manus` | ∅ |
| 23 | `KNOWLEDGE/iury/20260422_162213_Resource Not Found Error in Android Build - Manus` | R08 |
| 24 | `KNOWLEDGE/iury/20260422_162301_Resource Not Found Error in Android Build Process - Manus` | R07 |
| 25 | `KNOWLEDGE/omaci2008/20260422_173034_Melhor forma de criar DIDs para rede mesh global - Manus` | ∅ |
| 26 | `KNOWLEDGE/natalia/20260422_171420_Instruções para Missão via Sofia API Manual - Manus` | ∅ |
| 27 | `KNOWLEDGE/natalia/20260422_171728_Erro no Prototipo Android_ Análise dos Arquivos - Manus` | R08 |
| 28 | `KNOWLEDGE/meshwave65/20260422_Analise do erro com arquivos do projeto Android - Manus` | ∅ |
| 29 | `KNOWLEDGE/iury/20260422_161432_Como sincronizar repositório local com GitHub via SSH - Manus` | R18 |

### Conferência da numeração da fonte 14

A fonte 14 contém oito URLs ao todo: uma ocorrência de R08 e sete destinos distintos nas categorias saúde/vídeo (R09–R15). A tabela de referências tem quinze IDs R01–R18 porque há quatro redirecionadores separados e duas formas de repetição; as referências da fonte 14 são **R08–R15**, exatamente oito IDs.

## 4. Inventário de destinos/referências distintas

| Ref. | Destino textual (sem segredo) | Tipo/relação aparente | Estado observado |
|---|---|---|---|
| R01–R04 | `https://vertexaisearch.cloud.google.com/grounding-api-redirect/` (quatro caminhos distintos; identificadores omitidos) | Redirecionadores de busca/fontes; destino final não legível sem seguir ID opaco | **Não consultado por segurança; destino final não confirmado** |
| R05 | `https://start.ktor.io/` | Gerador inicializador de projeto Ktor; referência técnica externa | HEAD **404**; não encontrado na resposta verificada. Conteúdo não consultado |
| R06 | `http://localhost:8080/` | Endpoint local no ambiente de origem | **Não verificado**; não acessado |
| R07 | `https://help.manus.im/` | Ajuda/serviço Manus; repetido em cinco fontes | HEAD **302**; redirecionamento identificado, destino final não seguido; conteúdo não verificado |
| R08 | `https://manus.go.link/iW6sB?action=open-subscription` | Redirecionador para ação de subscrição/assinatura; seis ocorrências em seis fontes | **Não consultado**; efeito/destino final não confirmado |
| R09 | `https://www.drugs.com/cg_esp/desfibrilador-cardioversor-implantable.html` | Informação médica externa; aparentemente fora do escopo MeshWave | HEAD **403**; servidor recusou a requisição; conteúdo não verificado |
| R10 | `https://www.dracaciocardoso.com.br/ablacao` | Saúde/ablação; aparentemente fora de escopo | HEAD falhou com erro de rede/DNS; destino **não confirmado** |
| R11 | `https://ge.globo.com/eu-atleta/saude/noticia/2024/08/23/o-que-e-ablacao-procedimento-que-tite-fara-apos-arritmia.ghtml` | Notícia de saúde; aparentemente fora de escopo | HEAD **200**; somente resposta HTTP, conteúdo não examinado |
| R12 | `https://www.brunahenares.com.br/ablacao-de-arritmia/` | Saúde/ablação; aparentemente fora de escopo | HEAD **200**; somente resposta HTTP, conteúdo não examinado |
| R13 | `https://www.youtube.com/watch?v=Z1K1SvuWBN4` | Vídeo externo, associado na fonte à referência de saúde | HEAD **200**; somente resposta HTTP, conteúdo/vídeo não examinado |
| R14 | `https://medlineplus.gov/spanish/ency/article/007370.htm` | MedlinePlus/saúde; aparentemente fora de escopo | HEAD **200**; somente resposta HTTP, conteúdo não examinado |
| R15 | `https://cardiologistadf.com.br/arritmia-cardiaca-o-que-e-qual-o-tratamento-tem-cura/` | Saúde/cardiologia; aparentemente fora de escopo | HEAD **200**; somente resposta HTTP, conteúdo não examinado |
| R16 | `https://github.com/meshwave65/MeshWave-Roadmap-Images` | Repositório GitHub de imagens/roadmap | HEAD **200**; resposta HTTP do repositório, conteúdo não consultado |
| R17 | `https://github.com/meshwave65/Foundation_MeshWave/blob/main/midia/Evolu…` | Caminho GitHub para mídia, gravado/truncado após `Evolu` na fonte | **Não verificado**; URL incompleta, caminho não reconstruído |
| R18 | `https://github.com/meshwave65/AppMeshWave.git` | Repositório GitHub de app | HEAD **301**; redirecionamento identificado, destino final não seguido; conteúdo não consultado |

### Repetição entre fontes

- `https://help.manus.im/`: **5 ocorrências / 5 fontes** — itens 6, 7, 8, 10 e 24 da tabela da seção 3.
- `https://manus.go.link/iW6sB?action=open-subscription`: **6 ocorrências / 6 fontes** — itens 7, 14, 16, 21, 23 e 27. A URL foi preservada como referência textual; não foi aberta por indicar ação de subscrição.
- As demais referências aparecem uma vez cada. As quatro URLs Google têm identificadores opacos distintos, contabilizados individualmente sem transcrever os IDs.

## 5. Conflitos, classificação e limites

1. **Estimativa anterior versus contagem observada:** o resumo F1.5 indicava 14/29 arquivos não vazios e aproximadamente 28 URLs. A leitura direta desta unidade encontrou 13/29 e 27 ocorrências. Atualizar a estimativa no resumo F1.5/controle; a contagem anterior era aproximada.
2. **Caminho da fonte de DID:** o registro anterior em `BCE/CONTROLE_MESTRE.md` e `BCE/fontes/CLASSIFICACAO_LOTE_003.md` usa `KNOWLEDGE/nadir/...`, que não existe. O inventário CSV e o catálogo F1.5 indicam o caminho físico `KNOWLEDGE/omaci2008/...`, que existe e cujo `links.txt` está vazio. Corrigir os caminhos documentais e preservar a discrepância nesta nota; não alterar a fonte bruta.
3. **Links listados versus destinos:** o status HTTP HEAD confirma apenas resposta do host/path no momento da consulta. Não confirma autoria, conteúdo, validade técnica, segurança, relacionamento MeshWave ou disponibilidade de páginas além do HEAD. Nenhuma página/arquivo remoto foi baixado.
4. **Classificação do conteúdo:** `start.ktor.io`, localhost e GitHub parecem tecnicamente relacionados por seus destinos nominais, mas os destinos não foram validados em conteúdo. Links de saúde da fonte Sofia API parecem contexto externo/ruído em relação ao tema técnico; não foram descartados nem reclassificados destrutivamente.
5. **Segurança e preservação:** nenhum token, senha, assinatura ou identificador opaco foi reproduzido. Nenhum formulário/API de ação foi submetido. Os links e artefatos brutos permanecem intactos.

## 6. Próximo passo

F1.6 pode ser concluída depois de indexar este catálogo, corrigir a inconsistência `nadir` → caminho físico `omaci2008` nos documentos de controle/classificação, reconciliar a estimativa quantitativa F1.5, e publicar um checkpoint próprio. Depois, iniciar somente F1.7 — relatório consolidado de lacunas e qualidade das fontes, cobrindo F1.4–F1.6, conforme o controle mestre.
