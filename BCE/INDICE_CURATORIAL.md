# Índice Curatorial Inicial — BCE MeshWave

## Propósito

Este índice define a arquitetura documental da Base de Conhecimento Evolutivo. Ele não afirma que todos os temas abaixo já foram validados; registra os documentos que deverão ser criados, as evidências candidatas e a ordem recomendada de curadoria.

## Legenda

- **P0**: fundação, identidade e arquitetura; bloquearão a interpretação de outros temas.
- **P1**: módulos centrais do produto/ecossistema.
- **P2**: implementação, operação e integração.
- **P3**: contexto estratégico, comercial, jurídico ou externo.
- `PENDENTE`: documento ainda não criado.
- `EM_CURADORIA`: fontes identificadas, leitura em andamento.
- `REVISÃO`: documento existente precisa ser confrontado com fontes e versões.
- `CONCLUÍDO`: cobertura e rastreabilidade auditadas.

## Documentos de governança da BCE

| ID | Documento | Finalidade | Status |
|---|---|---|---|
| GOV-01 | `BCE/ORIENTACAO_AGENTES.md` | Regras de operação, continuidade, evidências e commits | CONCLUÍDO |
| GOV-02 | `BCE/CONTROLE_MESTRE.md` | Backlog, status, checkpoints e próximo passo | CONCLUÍDO |
| GOV-03 | `BCE/INDICE_CURATORIAL.md` | Este mapa documental | EM_CURADORIA |
| GOV-04 | `BCE/REGISTRO_DECISOES.md` | Log de decisões e justificativas; DEC-BCE-008/009 permanecem pendentes de validação | CONCLUÍDO |
| GOV-05 | `BCE/temas/_TEMPLATE.md` | Modelo padrão de documento curado | CONCLUÍDO |
| GOV-06 | `BCE/fontes/INVENTARIO_FONTES.md` | Inventário técnico reproduzível de 273 conjuntos; não equivale a classificação semântica integral | CONCLUÍDO |
| GOV-07 | `BCE/artefatos/INDICE_IMAGENS_E_DIAGRAMAS.md` | Relação entre imagens e conceitos | CONCLUÍDO |
| GOV-08 | `BCE/sessoes/` | Checkpoints de sessões e transferências; atualizar a cada retomada | EM_CURADORIA |
| GOV-09 | `BCE/PROMPT_RETOMADA_AGENTE.md` | Prompt reutilizável para iniciar agentes sucessores | CONCLUÍDO |
| GOV-10 | `skills/meshwave-bce-curation/SKILL.md` | Skill reutilizável para auditoria, curadoria e retomada por agentes | CONCLUÍDO |

## Documentos de estado da arte

### P0 — Núcleo conceitual

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-01 | `BCE/temas/visao-geral-ecossistema-meshwave.md` | O que é o MeshWave, quais problemas resolve e como seus módulos se relacionam? | Lote 001–003; fontes primárias L001-01/L001-06/L002-04; relatório F1.7; especificação arquitetural E011 e DOM-02 | REVISÃO — v0.2.1; cobertura/amplitude ainda incompletas e relações de arquitetura não validadas |
| DOM-02 | `BCE/temas/arquitetura-geral-e-implantacao.md` | Qual é a arquitetura lógica/física e como ocorre a implantação? | `01_arquitetura_geral_meshwave.md` e três conjuntos DOM-01 §13: “Fonte para Arquitetura e Operação”, “Complementar Módulos Faltantes do Diagrama de Implantação” e “Hierarquia de CLA Continental e Roteamento” | REVISÃO — v0.1.0; cinco camadas e roadmap conceitual documentados; sem implantação/verificação operacional |
| DOM-03 | `BCE/temas/rede-mesh-comunicacao-e-roteamento.md` | Como nós, enlaces, CLA e roteamento operam em uma rede mesh? | Lote F2.3 fechado: 12 conjuntos sobre CLA/Geohash, Android/Bluetooth/Wi-Fi Direct, roteamento preditivo, Briar LAN, laser, simulador e GSM mesh | REVISÃO — v0.1.0; primeira síntese publicada, sem implementação, build, teste físico ou protocolo de transporte verificáveis |
| DOM-04 | `BCE/temas/identidade-dids-e-identificador-de-equipamento.md` | Como pessoas, dispositivos e nós são identificados e verificados? | Sete fontes do escopo F2.4: identificador, DID, DNA/ARC/PGC, SSI, organização de site e Android | REVISÃO — v0.2.0 (`4f7465e`); F2.4 concluída como curadoria; sem DID aprovado, implementação ou teste verificável |
| DOM-05 | `BCE/temas/arc-autenticacao-contextual-e-bayes.md` | Qual é o modelo ARC/PGC e como a inferência bayesiana participa da autenticação/roteamento? | “ARC - Autenticação Recessiva Contextual”, “DNA do Hardware”, “Roteamento Preditivo com Autenticação Contextual” | REVISÃO — v0.1.0 (`e349070`); três fontes processadas; sem implementação, calibração ou teste verificável |

### P1 — Sistemas e módulos centrais

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-06 | `BCE/temas/sofia-agentes-missoes-e-oraculo.md` | O que é SOFIA, como agentes recebem/executam missões e como o conhecimento persiste? | Escopo F2.6: 23 fontes prioritárias de visão SOFIA, agentes, API, missões, oráculo, contexto, reabilitação e onboarding | REVISÃO — v0.2.7; 15/23 com auditoria profunda (itens 1–7 e 16–23); itens 8–15 ainda só com primeira passagem textual. F2.6-05 propõe log local `task_blocks`; F2.6-06 propõe ACR/AGF, especialistas e automação GitHub sem código/configuração verificados; F2.6-07 propõe curadoria via Git, dossiê mestre e acesso remoto, sem demonstrar que ocorreram. Contrato/API, execução e acesso ao DB permanecem não confirmados. Próximo: F2.6-08. |
| DOM-07 | `BCE/temas/persistencia-memoria-e-base-vetorial.md` | Como são armazenados, sincronizados, recuperados e atualizados os conhecimentos? | “Sistema de Persistência e Sincronização”, Chroma deployment, DB vetorial e Sofia API | PENDENTE |
| DOM-08 | `BCE/temas/aplicacao-appmeshwave-e-interfaces.md` | Quais são as funcionalidades, telas, fluxos e decisões de UX do aplicativo/site? | “AppMeshWave Funcionalidades”, protótipos Android, site colaborativo, mockups e imagens | PENDENTE |
| DOM-09 | `BCE/temas/simuladores-e-visualizacoes.md` | Quais simuladores existem, que modelos executam e como os resultados são visualizados? | “Criar site com simulador”, “Como criar um simulador gráfico”, inconsistências entre simulador e código, gráficos não exibidos | PENDENTE |
| DOM-10 | `BCE/temas/android-dispositivos-e-compatibilidade.md` | Como Android, dispositivos obsoletos, Bluetooth e versões de bibliotecas entram no sistema? | erros de build Android, dispositivos antigos, compatibilidade de bibliotecas/APIs | PENDENTE |

### P2 — Implementação, operações e segurança

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-11 | `BCE/temas/hardware-identidade-e-infraestrutura.md` | Quais equipamentos, clusters, placas e recursos físicos sustentam o ecossistema? | “Como montar placas de vídeo para cluster”, “DNA do Hardware”, equipamentos Android, impacto em data centers | PENDENTE |
| DOM-12 | `BCE/temas/desenvolvimento-repositorios-e-versionamento.md` | Como o código, repositórios, branches, scripts e versões são organizados? | README, scripts de extração, instruções GitHub/SSH, código de categorias, versões alfa | PENDENTE |
| DOM-13 | `BCE/temas/implantacao-atualizacao-e-operacao.md` | Como atualizar, restaurar, instalar e diagnosticar os módulos? | “MeshWave System Update Guide/Process”, reorganização Linux, gráficos ausentes, relatórios de consolidação | PENDENTE |
| DOM-14 | `BCE/temas/seguranca-privacidade-lgpd-e-governanca.md` | Quais princípios de segurança, privacidade, LGPD, controle e governança existem? | material LGPD, autenticação, identidade, persistência, exposição de credenciais e práticas operacionais | PENDENTE |
| DOM-15 | `BCE/temas/apis-integracoes-e-protocolos.md` | Quais APIs, protocolos e integrações conectam os módulos? | Sofia API, DafsAPI, APIs de desenvolvedores, MWC/UMS, Briar e Chroma | PENDENTE |

### P3 — Estratégia, implantação institucional e contexto externo

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-16 | `BCE/temas/parcerias-patentes-e-propriedade-intelectual.md` | Quais ativos, parceiros, patentes e estratégias de proteção foram propostos? | materiais para patentes, busca INPI, parceiros/protocolos, OJFD/Turbulence | PENDENTE |
| DOM-17 | `BCE/temas/modelo-de-negocio-e-implantacao-institucional.md` | Como o MeshWave é apresentado a governos, parceiros e mercados? | materiais para Nigéria, Inovarse, fintech/blockchain, estratégia MWC/UMS | PENDENTE |
| DOM-18 | `BCE/temas/impacto-ambiental-social-e-recursos.md` | Quais impactos ambientais, sociais e de infraestrutura foram considerados? | environmental impact, data centers, uso de dispositivos obsoletos | PENDENTE |
| DOM-19 | `BCE/temas/temas-externos-e-fora-de-escopo.md` | Quais fontes não pertencem ao núcleo MeshWave e como devem ser isoladas? | saúde, instalação elétrica, academia, aluguel, tanque Osório, política e demais temas externos | PENDENTE |

## Matriz de dependências

```text
DOM-01 Visão geral
 ├── DOM-02 Arquitetura
 │    ├── DOM-03 Rede e roteamento
 │    ├── DOM-08 Aplicações
 │    ├── DOM-09 Simuladores
 │    └── DOM-11 Hardware
 ├── DOM-04 Identidade
 │    └── DOM-05 ARC/Bayes
 ├── DOM-06 SOFIA
 │    ├── DOM-07 Persistência
 │    └── DOM-15 APIs/integrações
 ├── DOM-12 Desenvolvimento/versionamento
 ├── DOM-13 Operação/atualização
 └── DOM-14 Segurança/governança

DOM-16 a DOM-19 dependem da consolidação técnica dos domínios acima.
```

## Ordem recomendada de curadoria

1. GOV-04, GOV-05 e GOV-06;
2. inventário reproduzível de `KNOWLEDGE`;
3. DOM-01 e DOM-02;
4. DOM-03, DOM-04 e DOM-05;
5. DOM-06, DOM-07 e DOM-15;
6. DOM-08, DOM-09 e DOM-10;
7. DOM-11, DOM-12, DOM-13 e DOM-14;
8. DOM-16, DOM-17, DOM-18 e DOM-19;
9. mapa de relações, auditoria de cobertura e revisão cruzada.

## Critério de inclusão no núcleo MeshWave

Uma fonte entra no núcleo de um documento quando contém pelo menos um dos elementos abaixo:

- conceito ou requisito explicitamente associado ao MeshWave, SOFIA ou seus módulos;
- arquitetura, código ou diagrama do sistema;
- decisão de produto, protocolo, identidade, segurança ou operação;
- evidência de protótipo/experimento do ecossistema;
- histórico de evolução de uma ideia MeshWave.

Fontes que apenas mencionam o projeto sem conteúdo técnico devem ser registradas como contexto. Fontes sem relação devem ir para DOM-19, sem serem apagadas.

## Estado do índice

- Este é um mapa inicial baseado em títulos e inventário preliminar.
- DOM-01 recebeu revisão F2.1 e referência cruzada F2.2 (`0.2.1`), mas permanece em `REVISÃO`: descreve visão e relações propostas, não estado de arte implementado, e se apoia em amostra semântica de 29/273 conjuntos.
- DOM-02 recebeu primeira síntese F2.2 (`0.1.0`), permanece em `REVISÃO`: a fonte principal é uma especificação conceitual e um roadmap; sem código, teste, deployment ou cronologia formalmente validados. O documento relaciona conflitos e lacunas e marca F2.3 como próximo passo.
- DOM-03 recebeu primeira síntese F2.3 (`0.1.0`): as 12 fontes foram lidas em texto, blocos, links e imagens quando presentes. A síntese separa proposta, protótipo alegado, transcrição de código e hipótese GSM/LTE; não confirma implementação, build, teste físico, interoperabilidade ou resultados de roteamento.
- A classificação deve ser revisada após a leitura integral de `content.txt`, `code_blocks.txt`, `links.txt` e imagens.
- Um documento-alvo pode ser dividido ou fundido somente com decisão registrada em `BCE/REGISTRO_DECISOES.md`.
- Nenhuma fonte deve ser considerada processada apenas porque seu título aparece neste índice.

## Classificações de fontes publicadas

| Artefato | Escopo | Resultado e limites |
|---|---|---|
| `BCE/fontes/CLASSIFICACAO_LOTE_001.md` | Lote 001 | Classificação semântica inicial; consultar o documento para os caminhos e limites de cada fonte. |
| `BCE/fontes/CLASSIFICACAO_LOTE_002.md` | Lote 002 | Identidade, implantação e SOFIA; planos e alegações não são tratados como implementação confirmada. |
| `BCE/fontes/CLASSIFICACAO_LOTE_003.md` | Lote 003 (19 conjuntos de DID/Android, Sofia API, persistência e contexto operacional) | F1.3 concluído em 2026-10-08. Há repetição interna nos conjuntos; nenhuma duplicata entre fontes foi comprovada. Relações entre grupos são apenas sobreposição/continuação candidata. F1.4 concluído: 35 imagens catalogadas em `BCE/artefatos/INDICE_IMAGENS_E_DIAGRAMAS.md`; nenhuma duplicata exata confirmada. |
| `BCE/artefatos/INDICE_IMAGENS_E_DIAGRAMAS.md` | F1.4 — 35 imagens dos 19 caminhos do Lote 003 | SHA-256, pHash, dimensões e descrições catalogados; origem/licença não confirmadas quando ausentes e OCR automático não executado. Capturas semelhantes por moldura de interface não foram promovidas a duplicatas. |
| `BCE/fontes/CATALOGO_CODIGO_E_IMPLEMENTACAO_LOTES_001_003.md` | F1.5 — 29 diretórios físicos únicos referenciados pelos Lotes 001–003 | 30 referências registradas, com `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus` repetida entre L001/L003 e analisada uma vez. Nenhum código executável anexado ou resultado verificável de build/teste/execução/upload/produção foi confirmado; trechos em transcrições, inclusive código substancial, não comprovam implementação. Uma leitura integral ficou limitada pelo tamanho da transcrição em uma fonte e está explicitamente marcada no catálogo. |
| `BCE/fontes/CATALOGO_LINKS_LOTES_001_003.md` | F1.6 — `links.txt` dos mesmos 29 diretórios físicos únicos | 13 arquivos não vazios, 16 vazios; 27 ocorrências e 18 referências distintas. HEAD público foi usado apenas em 11 destinos sem autenticação; páginas não foram lidas. Redirecionadores opacos, links de ação e `localhost` não foram seguidos. Contagens F1.5 anteriores eram estimativas aproximadas. Caminho DID `nadir/` em registros anteriores conflita com o caminho físico `omaci2008/` do inventário/catalogação. |
| `BCE/fontes/RELATORIO_LACUNAS_E_QUALIDADE_F1_7.md` | F1.7 — síntese F1.2–F1.6 contra inventário de 273 conjuntos | Amostra integrada de 29/273 (10,62%); 0/29 com implementação verificável no material revisado; lacunas priorizadas por cobertura, reprodutibilidade, API, identidade, privacidade, Android, imagens, links, duplicatas e contexto externo. Não generalizar a amostra nem interpretar ausência de evidência como prova de inexistência do produto. |
| `BCE/temas/arquitetura-geral-e-implantacao.md` | F2.2 — DOM-02, arquitetura geral e implantação | Primeira síntese (v0.1.0) das cinco camadas e do controlador SDN propostos, roadmap 2025–2032, representação CLA e evidências/ausências; não comprova implementação. Próximo: F2.3. |
| `BCE/fontes/ESCOPO_F2_3_REDE_MESH.md` | F2.3 — lote fechado de 12 conjuntos de rede, comunicação e roteamento | Escopo físico registrado antes da leitura; consultar DOM-03 para a síntese, rastreabilidade, conflitos e lacunas. |
| `BCE/fontes/ESCOPO_F2_5_ARC_BAYES.md` | F2.5 — lote fechado de ARC/PGC, DNA do hardware e inferência bayesiana | Três conjuntos processados em paralelo; consultar DOM-05 para a síntese e limitações. |
| `BCE/sessoes/2026-10-08_f2-4-fechamento.md` | F2.4 — checkpoint de fechamento explícito | Sete fontes e 12 imagens conferidas; F2.4 concluída como unidade de curadoria; próximo passo F2.6. |
| `BCE/temas/rede-mesh-comunicacao-e-roteamento.md` | F2.3 — DOM-03 v0.1.0 | Primeira síntese do lote: descoberta, Wi‑Fi Direct/Bluetooth, `ClaCache`, sucessão, CLA/CPA/Geohash, roteamento preditivo, fallback, GSM/LTE, laser, Briar e simulador. Mantém `REVISÃO` porque nenhum artefato de rede executável ou teste reproduzível foi confirmado. |
| `BCE/temas/sofia-agentes-missoes-e-oraculo.md` | F2.6 — DOM-06 v0.2.7 | Integra auditoria profunda dos itens 1–7 e 16–23 (15/23); F2.6-05 registra proposta de continuidade local via `task_blocks`; F2.6-06 registra guia proposto de automação e questões de permissões; F2.6-07 registra propostas de curadoria/dossiê e instruções de acesso Git/remoto como conteúdo histórico, não autorização ou evidência de execução. Contrato/API, implantação e acesso ao DB não confirmados; itens 8–15 aguardam auditoria canônica; status `REVISÃO`. |

As classificações são inventários de evidência e qualidade, não documentos de estado da arte. Elas não promovem alegações de conversa, capturas de interface, código incompleto ou rótulos de conclusão a fatos de implementação, build, upload ou produção. Consultar cada documento para conflitos, fontes ausentes e próximas verificações.
