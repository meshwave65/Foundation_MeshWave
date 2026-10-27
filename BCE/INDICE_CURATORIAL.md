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
| DOM-01 | `BCE/temas/visao-geral-ecossistema-meshwave.md` | O que é o MeshWave, quais problemas resolve e como seus módulos se relacionam? | Lote 001–003; fontes primárias L001-01/L001-06/L002-04; L002-03; relatório F1.7; especificação arquitetural E011 e DOM-02 | REVISÃO — v0.3.7; E001–E007 e L002-03 auditadas diretamente em F3.1. L002-03 acrescenta roadmap de módulos/fases, sem implementação, código, teste ou cronograma aprovado. Claim encerrado após atualização de DOM-01/DOM-02; próxima fila requer reconciliação explícita. |
| DOM-02 | `BCE/temas/arquitetura-geral-e-implantacao.md` | Qual é a arquitetura lógica/física e como ocorre a implantação? | `01_arquitetura_geral_meshwave.md` e três conjuntos DOM-01 §13: “Fonte para Arquitetura e Operação”, “Complementar Módulos Faltantes do Diagrama de Implantação” e “Hierarquia de CLA Continental e Roteamento” | REVISÃO — v0.1.2; cinco camadas e roadmap conceitual documentados; L002-03 auditada em seis artefatos e confirma matriz de fases/módulos como roadmap; sem implantação/verificação operacional |
| DOM-03 | `BCE/temas/rede-mesh-comunicacao-e-roteamento.md` | Como nós, enlaces, CLA e roteamento operam em uma rede mesh? | Lote F2.3 fechado: 12 conjuntos sobre CLA/Geohash, Android/Bluetooth/Wi-Fi Direct, roteamento preditivo, Briar LAN, laser, simulador e GSM mesh | REVISÃO — v0.1.0; primeira síntese publicada, sem implementação, build, teste físico ou protocolo de transporte verificáveis |
| DOM-04 | `BCE/temas/identidade-dids-e-identificador-de-equipamento.md` | Como pessoas, dispositivos e nós são identificados e verificados? | Sete fontes do escopo F2.4: identificador, DID, DNA/ARC/PGC, SSI, organização de site e Android; reauditoria F3.1/L002-01 | REVISÃO — v0.2.1; L002-01 confirma contexto editorial de organização do site, sem nova especificação DID ou evidência independente; sem DID aprovado, implementação ou teste verificável |
| DOM-05 | `BCE/temas/arc-autenticacao-contextual-e-bayes.md` | Qual é o modelo ARC/PGC e como a inferência bayesiana participa da autenticação/roteamento? | “ARC - Autenticação Recessiva Contextual”, “DNA do Hardware”, “Roteamento Preditivo com Autenticação Contextual” | REVISÃO — v0.1.1; três fontes F2.5 e reauditoria direta E004 em F3.1; simulador Ktor/Vue e integração Android permanecem propostas; sem implementação, calibração ou teste verificável. Literais sensíveis redigidos. E005 não acrescenta evidência técnica ARC/Bayes. |

### P1 — Sistemas e módulos centrais

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-06 | `BCE/temas/sofia-agentes-missoes-e-oraculo.md` | O que é SOFIA, como agentes recebem/executam missões e como o conhecimento persiste? | Escopo F2.6: 23 fontes prioritárias de visão SOFIA, agentes, API, missões, oráculo, contexto, reabilitação e onboarding | REVISÃO — v0.3.6; 23/23 fontes auditadas em profundidade. F2.6-15 registra manual `sofia_opman` não verificável, claim/subtarefa narrados para tarefa 315 e interrupção por créditos em 3/4; nenhum estado de backend foi confirmado. F3.1/L002-05 reaudita a mesma unidade física de F2.6-02, com hashes 4/4 e sem evidência independente de patch/execução. Fila F2.6 encerrada; F3.1/L002-05 encerrada. |
| DOM-07 | `BCE/temas/persistencia-memoria-e-base-vetorial.md` | Como são armazenados, sincronizados, recuperados e atualizados os conhecimentos? | “Sistema de Persistência e Sincronização”, Chroma deployment, DB vetorial e Sofia API | PENDENTE |
| DOM-08 | `BCE/temas/aplicacao-appmeshwave-e-interfaces.md` | Quais são as funcionalidades, telas, fluxos e decisões de UX do aplicativo/site? | “AppMeshWave Funcionalidades”, protótipos Android, site colaborativo, mockups e imagens | PENDENTE |
| DOM-09 | `BCE/temas/simuladores-e-visualizacoes.md` | Quais simuladores existem, que modelos executam e como os resultados são visualizados? | “Criar site com simulador”, “Como criar um simulador gráfico”, inconsistências entre simulador e código, gráficos não exibidos | PENDENTE |
| DOM-10 | `BCE/temas/android-dispositivos-e-compatibilidade.md` | Como Android, dispositivos obsoletos, Bluetooth e versões de bibliotecas entram no sistema? | erros de build Android, dispositivos antigos, compatibilidade de bibliotecas/APIs | PENDENTE |

### P2 — Implementação, operações e segurança

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-11 | `BCE/temas/hardware-identidade-e-infraestrutura.md` | Quais equipamentos, clusters, placas e recursos físicos sustentam o ecossistema? | “Como montar placas de vídeo para cluster”, “DNA do Hardware”, equipamentos Android, impacto em data centers; L002-03 como roadmap de Hardware MeshWave, aceleradores de IA, hardware otimizado e módulo quântico | PENDENTE — L002-03 apenas mapeia vocabulário de roadmap; não há evidência de hardware |
| DOM-12 | `BCE/temas/desenvolvimento-repositorios-e-versionamento.md` | Como o código, repositórios, branches, scripts e versões são organizados? | README, scripts de extração, instruções GitHub/SSH, código de categorias, versões alfa | PENDENTE |
| DOM-13 | `BCE/temas/implantacao-atualizacao-e-operacao.md` | Como atualizar, restaurar, instalar e diagnosticar os módulos? | “MeshWave System Update Guide/Process”, reorganização Linux, gráficos ausentes, relatórios de consolidação | PENDENTE |
| DOM-14 | `BCE/temas/seguranca-privacidade-lgpd-e-governanca.md` | Quais princípios de segurança, privacidade, LGPD, controle e governança existem? | material LGPD, autenticação, identidade, persistência, exposição de credenciais e práticas operacionais | PENDENTE |
| DOM-15 | `BCE/temas/apis-integracoes-e-protocolos.md` | Quais APIs, protocolos e integrações conectam os módulos? | Sofia API, DafsAPI, APIs de desenvolvedores, MWC/UMS, Briar e Chroma; L002-03 como mapa de Integração 6G, SDN, SATSI, LEO e interface terahertz | PENDENTE — L002-03 fornece somente rótulos de integração/roadmap, sem contratos ou protocolos verificáveis |

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
- DOM-01 (v0.3.7): F2.1/F2.2, auditoria F3.1 E001–E007 e integração L002-03; segue em `REVISÃO`. E002 não comprova POC; E003 carece de semântica espacial/algoritmo; E004 é design/código transcrito; E005 plano editorial; E006 plano visual sem saída íntegra; E007 reauditoria truncada sem API/teste/integração. Amostra semântica: 29/273. F3.1/L002-05 reaudita F2.6-02 em DOM-06/12/13.
- DOM-02 (v0.1.2): cinco camadas, SDN e roadmap conceituais; E002 não comprova POC e E003 não fornece legenda, CRS ou algoritmo para a grade CLA. L002-03 integra matriz de fases/módulos; sem implantação ou cronograma validado. Segue em `REVISÃO`.
- DOM-03 (v0.1.0): síntese das 12 fontes separa proposta, protótipo alegado, código transcrito e hipótese GSM/LTE; não confirma implementação, build, teste físico, interoperabilidade ou resultados de roteamento.
- A classificação deve ser revisada após a leitura integral de `content.txt`, `code_blocks.txt`, `links.txt` e imagens.
- Um documento-alvo pode ser dividido ou fundido somente com decisão registrada em `BCE/REGISTRO_DECISOES.md`.
- Nenhuma fonte deve ser considerada processada apenas porque seu título aparece neste índice.

## Matriz arqueológica de decisões

| Artefato | Escopo | Resultado e limites |
|---|---|---|
| `BCE/arqueologia/MATRIZ_DECISOES_F3_2.md` | F3.2 — arqueologia de decisões e alternativas | v0.2.0; 17 registros (A-01–A-17), revisão documental de DOM-01–DOM-06. `KNOWLEDGE/`, fontes primárias e links não foram reabertos nesta unidade; referências primárias citadas nos DOMs são mediadas, não auditoria direta. Nenhuma proposta foi promovida a implementação ou decisão normativa. |

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
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E001.md` | F3.1 — DOM-01/E001/L001-01 | Quatro artefatos auditados diretamente; hashes 4/4; distingue visão, homônimos, roadmap e identidade proposta de implementação confirmada. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E002.md` e checkpoint de abertura | F3.1 — DOM-01/E002/L001-02 | Cinco artefatos auditados diretamente; hashes 5/5; roadmap e alegação de POC separados da ausência de código, teste ou resultado verificável. O checkpoint E002 indicou E003 como próximo contato; E003 está agora concluído e registrado na linha seguinte. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E003.md` e checkpoint de abertura | F3.1 — DOM-01/E003/L001-03 | Cinco artefatos auditados diretamente; hashes 5/5; a grade visual e a preferência registrada são separadas de CRS, algoritmo, planilha e contexto não disponíveis. Próximo contato E004/L001-04. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E004.md` e checkpoints de abertura/fechamento | F3.1 — DOM-01/E004/L001-04 | Quatro artefatos auditados diretamente; hashes 4/4; design ARC/Bayes, simulador Ktor/Vue e integração Android classificados como proposta/código transcrito; captura de conversa, links não seguidos e literais sensíveis redigidos. O contato seguinte, E005/L001-06, foi concluído e está registrado na linha seguinte. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E005.md` e checkpoints de abertura/fechamento (`BCE/sessoes/2026-10-20_f3-1-dom01-e005-abertura.md`, `BCE/sessoes/2026-10-20_f3-1-dom01-e005-fechamento.md`) | F3.1 — DOM-01/E005/L001-06 | Quatro artefatos auditados diretamente; hashes 4/4; reauditoria da fonte já coberta em F2.6-07; visão de sinergia e plano editorial sem integração, acesso ou execução comprovados. O contato seguinte E006 foi concluído. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E006.md` | F3.1 — DOM-01/E006/L002-02 | Cinco artefatos, 462.562 bytes, hashes 5/5; plano editorial/visual de 14 gráficos, sem código ou esquema normativo; imagem de registro ilegível, replay em 3/7, sem saídas gráficas íntegras no conjunto. Integrado em DOM-01 v0.3.5. |
| `BCE/sessoes/2026-10-20_f3-1-dom01-e006-abertura.md` | F3.1 — DOM-01/E006/L002-02 | Cinco artefatos pré-registrados, hashes 5/5 confirmados novamente após leitura; nenhum comando executado ou link seguido. |
| `BCE/fontes/CLASSIFICACAO_F3_1_DOM01_E007.md` | F3.1 — DOM-01/E007/L002-04 | Quatro artefatos, 218.674 bytes, hashes 4/4; reauditoria da fonte F2.6-01; narrativa de Q-CyPIA/SDN, multipath/anonimato e ARC-Bayes/PGC sem código, contrato, teste ou resultado verificável. Integrado inicialmente em DOM-01 v0.3.6; versão atual v0.3.7 também incorpora L002-03. |
| `BCE/sessoes/2026-10-26_f3-1-dom01-e007-abertura.md` | F3.1 — DOM-01/E007/L002-04 | Pré-registro de quatro artefatos; hashes 4/4 revalidados antes/depois da leitura; nenhum link seguido/código executado. |
| `BCE/sessoes/2026-10-26_f3-1-dom01-e007-fechamento.md` | F3.1 — DOM-01/E007/L002-04 | Fechamento da auditoria e commits; hashes 4/4; documenta a nova regra de claim publicada após a leitura, ausência de claim ativo e próximo passo de reconciliação da fila antes de outra fonte. |
| `BCE/temas/arquitetura-geral-e-implantacao.md` | F2.2/F3.1 — DOM-02, arquitetura geral e implantação | Versão atual v0.1.2; cinco camadas, SDN, roadmap e módulos permanecem conceituais. L002-03 foi integrada como matriz de fases/módulos, sem implantação, teste ou cronograma aprovado. DOM-02 segue em `REVISÃO`. |
| `BCE/fontes/ESCOPO_F2_3_REDE_MESH.md` | F2.3 — lote fechado de 12 conjuntos de rede, comunicação e roteamento | Escopo físico registrado antes da leitura; consultar DOM-03 para a síntese, rastreabilidade, conflitos e lacunas. |
| `BCE/fontes/ESCOPO_F2_5_ARC_BAYES.md` | F2.5 — lote fechado de ARC/PGC, DNA do hardware e inferência bayesiana | Três conjuntos processados em paralelo; consultar DOM-05 para a síntese e limitações. |
| `BCE/sessoes/2026-10-08_f2-4-fechamento.md` | F2.4 — checkpoint de fechamento explícito | Sete fontes e 12 imagens conferidas; F2.4 concluída como unidade de curadoria; próximo passo F2.6. |
| `BCE/temas/rede-mesh-comunicacao-e-roteamento.md` | F2.3 — DOM-03 v0.1.0 | Primeira síntese do lote: descoberta, Wi‑Fi Direct/Bluetooth, `ClaCache`, sucessão, CLA/CPA/Geohash, roteamento preditivo, fallback, GSM/LTE, laser, Briar e simulador. Mantém `REVISÃO` porque nenhum artefato de rede executável ou teste reproduzível foi confirmado. |
| `BCE/temas/sofia-agentes-missoes-e-oraculo.md` | F2.6 — DOM-06 v0.3.5 | Auditoria profunda completa das 23 fontes. F2.6-15 registra busca do `sofia_opman.md`, tarefa 315, subtarefa e interrupção por créditos; claim, manual, subtarefa, backend e persistência não confirmados. Fila F2.6 encerrada; próximo: F3.1; status `REVISÃO`. |

As classificações são inventários de evidência e qualidade, não documentos de estado da arte. Elas não promovem alegações de conversa, capturas de interface, código incompleto ou rótulos de conclusão a fatos de implementação, build, upload ou produção. Consultar cada documento para conflitos, fontes ausentes e próximas verificações.
