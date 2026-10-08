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
| GOV-04 | `BCE/REGISTRO_DECISOES.md` | Log de decisões e justificativas | PENDENTE |
| GOV-05 | `BCE/temas/_TEMPLATE.md` | Modelo padrão de documento curado | PENDENTE |
| GOV-06 | `BCE/fontes/INVENTARIO_FONTES.md` | Catálogo reproduzível das fontes | PENDENTE |
| GOV-07 | `BCE/artefatos/INDICE_IMAGENS_E_DIAGRAMAS.md` | Relação entre imagens e conceitos | PENDENTE |
| GOV-08 | `BCE/sessoes/` | Checkpoints de sessões e transferências | PENDENTE |

## Documentos de estado da arte

### P0 — Núcleo conceitual

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-01 | `BCE/temas/visao-geral-ecossistema-meshwave.md` | O que é o MeshWave, quais problemas resolve e como seus módulos se relacionam? | títulos contendo “O que é o projeto Meshwave”, “SOFIA and MeshWave Ecosystem Overview”, revisões/apresentações | PENDENTE |
| DOM-02 | `BCE/temas/arquitetura-geral-e-implantacao.md` | Qual é a arquitetura lógica/física e como ocorre a implantação? | `01_arquitetura_geral_meshwave.md`, diagramas de arquitetura, “Fonte para Arquitetura e Operação”, “Complementar Módulos Faltantes do Diagrama de Implantação” | PENDENTE |
| DOM-03 | `BCE/temas/rede-mesh-comunicacao-e-roteamento.md` | Como nós, enlaces, CLA e roteamento operam em uma rede mesh? | “Hierarquia de CLA e Roteamento”, “Roteamento preditivo”, “Capacidade de uma rede GSM Mesh”, estudos de laser e Briar | PENDENTE |
| DOM-04 | `BCE/temas/identidade-dids-e-identificador-de-equipamento.md` | Como pessoas, dispositivos e nós são identificados e verificados? | “Definição do identificador único”, “Melhor forma de criar DIDs”, imagens de identidade soberana | PENDENTE |
| DOM-05 | `BCE/temas/arc-autenticacao-contextual-e-bayes.md` | Qual é o modelo ARC/PGC e como a inferência bayesiana participa da autenticação/roteamento? | “ARC - Autenticação Recessiva Contextual”, “DNA do Hardware”, “Roteamento Preditivo com Autenticação Contextual” | PENDENTE |

### P1 — Sistemas e módulos centrais

| ID | Documento-alvo | Pergunta central | Fontes candidatas observadas | Status |
|---|---|---|---|---|
| DOM-06 | `BCE/temas/sofia-agentes-missoes-e-oraculo.md` | O que é SOFIA, como agentes recebem/executam missões e como o conhecimento persiste? | “SOFIA and MeshWave Ecosystem Documents/Overview”, instruções da Sofia API, relatórios de passagem de contexto, sistema de persistência | PENDENTE |
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
- A classificação deve ser revisada após a leitura integral de `content.txt`, `code_blocks.txt`, `links.txt` e imagens.
- Um documento-alvo pode ser dividido ou fundido somente com decisão registrada em `BCE/REGISTRO_DECISOES.md`.
- Nenhuma fonte deve ser considerada processada apenas porque seu título aparece neste índice.
