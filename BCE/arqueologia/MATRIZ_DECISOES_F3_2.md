# BCE MeshWave — Matriz arqueológica de decisões — F3.2

## Metadados

| Campo | Valor |
|---|---|
| Unidade | F3.2 — reconstrução arqueológica das decisões |
| Versão | `0.1.0` |
| Data | `2026-10-26` |
| Estado | `BASE INICIAL — requer expansão e validação` |
| Escopo desta versão | Decisões, alternativas e descartes já publicados em DOM-01, DOM-02, DOM-04 e DOM-06; não abre fontes brutas novas |
| Regra de leitura | Um registro histórico de conversa, imagem ou classificação prova que uma formulação foi registrada; não prova aprovação normativa, release, implementação ou operação |

## 1. Como ler a matriz

A matriz separa cinco estados que frequentemente aparecem misturados no corpus: **observado** (o artefato existe), **relatado** (a fonte diz que algo foi feito ou decidido), **proposto** (há intenção de desenho), **roadmap** (o item foi alocado a uma fase) e **validado** (há evidência reproduzível de aprovação, código, teste ou operação). A maior parte das entradas abaixo chega somente aos quatro primeiros estados.

“Data” e “versão” são reproduzidas como rótulos históricos quando presentes; não são tratadas como releases sem commit, tag ou changelog verificável. “Descartado” significa rejeitado ou explicitamente não adotado dentro da curadoria atual; não significa que a ideia nunca possa reaparecer com nova evidência.

## 2. Matriz de decisões e evolução

| ID arqueológico | Tema | Formulação/estado inicial identificável | Alternativa, tensão ou evolução | Escolha/otimização/descartes observados | Evidência rastreável | Estado atual na BCE | Lacuna e próximo teste documental |
|---|---|---|---|---|---|---|---|
| A-01 | Identidade do equipamento | Um identificador compacto foi proposto para representar região, fabricante, equipamento e verificador; uma formulação histórica usa 4+8+1. | Formulação posterior `GGGGGGFFFEEEE-V`; imagens posteriores mostram registro mais rico com múltiplos Geohashes, perfil e timestamp. | A curadoria preserva 4+8+1 como formulação histórica e mantém `GGGGGGFFFEEEE-V` como candidato interno; nenhuma versão foi adotada como DID. | DOM-04 §§4, 7, 9, 10–11; decisões DEC-DOM04-001–002; fontes F2.4. | Proposta conflitante; sem esquema normativo. | Recuperar fonte original, método DID se houver, alfabeto, cálculo, vetores de teste, resolução e decisão formal.
| A-02 | Identidade versus localização | Geohash/GeoID aparece como parte do registro de identificação e como índice regional. | A curadoria separa identidade estável de localização atual/ativação, com TTL, controle e minimização. | Geohash permanente na identidade não foi adotado; localização deve ser vínculo atualizado, não necessariamente componente imutável. | DOM-04 §§4, 5, 11–12; DOM-03 e DOM-01 terminologia CLA/CPA/Geohash. | Melhoria curatorial explicitamente registrada; protocolo ausente. | Definir precisão, TTL, retenção, autorização, anti-rastreamento e contrato entre identidade e cache/roteamento.
| A-03 | DNA do hardware / ARC / PGC | Identidade resiliente é descrita metaforicamente como DNA do hardware, associada a ARC/PGC e presença contextual. | Pode ser metáfora de identidade, atestado físico, prova contextual ou autenticação bayesiana. | A curadoria mantém como hipótese; não transforma imagem ou narrativa em atestado, chave ou protocolo. ARC/PGC foram encaminhados a DOM-05. | DOM-04 §§3, 9–11; DEC-DOM04-003; DOM-05; fontes F2.4/F2.5. | Hipótese arquitetural/visual; sem implementação. | Especificar fonte de entropia, estabilidade, não clonabilidade, ameaça, privacidade, atestado e teste.
| A-04 | Arquitetura em camadas | O documento “Sistema MeshWave Versão 1.0” propõe cinco camadas: Aplicação, Rede Mesh, Otimização/IA, Integração e Segurança/Blockchain. | Um controlador SDN é descrito transversalmente, logicamente centralizado e fisicamente distribuído; o roadmap gráfico organiza segmentos e fases, não camadas. | A BCE mantém cinco camadas + SDN como decomposição conceitual, mas não os trata como deployments ou arquitetura vigente. | DOM-02 §§1, 4, 5 e 8; E011; histórico 2025-05-21. | Especificação conceitual proposta. | Localizar versão aprovada, fronteiras data/control plane, componentes, contratos, provisionamento e recuperação.
| A-05 | Descentralização versus controle | A visão deseja rede descentralizada/autônoma com nós e recursos distribuídos. | O modelo também depende de controlador SDN, edge/MCP, celular, LEO e conectores externos. | A tensão foi preservada, não resolvida; a BCE não escolhe entre controle central, federado ou totalmente distribuído. | DOM-02 C03, C08, §§4.1–4.3; DOM-01 C08. | Conflito arquitetural aberto. | Definir operação sem controlador, partições, eleição, confiança, fallback, governança e dependências externas.
| A-06 | CLA/CPA/Geohash e roteamento | Grades, células e regiões coloridas foram usadas como referência visual para hierarquia/roteamento. | A imagem pode representar Geohash, cache, CLA/CPA ou uma linguagem visual sem semântica formal; a planilha e contexto citados não estão presentes. | A imagem é conservada como evidência visual, mas não convertida em algoritmo, CRS, fórmula ou topologia. | DOM-01 C11, DOM-02 C07, E003/L001-03 e classificação F3.1/E003. | Referência visual não normativa. | Recuperar dados-fonte, legenda, CRS, escala, regra de agregação, vizinhança, algoritmo e teste reproduzível.
| A-07 | Roadmap e implantação | As fontes distribuem módulos por quatro fases, com horizontes aproximados de 12–36 meses e rótulos como 6G, DLT, quântico, SATSI e armazenamento P2P. | O texto de L002-03 relata roteiros concluídos, mas os roteiros não estão anexados; “implantação” pode ser confundida com planejamento. | A curadoria classifica os módulos como roadmap/proposta e não como componentes implantados; a duplicata de imagens não aumenta evidência. | DOM-02 §4.4, C01/C05/C06/C11; `CLASSIFICACAO_F3_1_L002-03.md`; E019. | Roadmap documental; implementação não confirmada. | Localizar roteiros, commits, critérios de aceite, código, testes, deployment e baseline de cronograma.
| A-08 | Identificador como título editorial | L002-01, apesar do título de identificador único, registra organização de abas, cronologias, históricos e downloads para uma base/site. | A página temática “Identificação (DIDs)” poderia ser confundida com uma decisão de identidade ou implementação. | A reauditoria F3.1 classifica o conjunto como contexto editorial; CSS transcrito e captura interrompida não alteram DEC-DOM04-001–003. | `CLASSIFICACAO_F3_1_L002-01.md`; DOM-04 E04-06/E04-10 e C04-08; checkpoint L002-01. | Proveniência histórica, sem evidência independente. | Localizar páginas/arquivos técnicos efetivamente versionados; não inferir método DID a partir da organização do site.
| A-09 | Integração MeshWave–SOFIA | Fontes de visão associam MeshWave à infraestrutura e SOFIA à inteligência/agentes/orquestração. | SOFIA também aparece em fontes próprias com missões, APIs e estados; os contratos de integração não acompanham as fontes de visão. | Relação é mantida como intenção/proposta; DOM-06 não declara implantação integrada, API ou persistência comprovada. | DOM-01 §§1, 4.1–4.4; DOM-06 v0.3.5; F2.6/F3.1. | Relação conceitual não verificada. | Obter contrato, autenticação, estados, payloads, observabilidade, teste ponta a ponta e política de falhas.
| A-10 | Código e interface como evidência | Conversas contêm trechos Kotlin, CSS, comandos, rótulos de versão e capturas com tarefas concluídas/interrompidas. | Esses fragmentos podem ser confundidos com código executável, build, produto ou operação. | A BCE classifica código transcrito como proposta/registro até haver repositório, dependências, build, teste, log ou execução reproduzível; capturas são UI/replay. | DOM-01 limites e C07/C10/C12/C14/C15; DOM-02 §7; classificações F3.1. | Regra metodológica consolidada. | Associar cada alegação a commit/arquivo, reproduzir build em ambiente controlado e preservar logs/artefatos.

## 3. Linha arqueológica resumida

1. **Formulação conceitual:** MeshWave é descrito como ecossistema de comunicação mesh com identidade, roteamento, confiança e evolução por fases.
2. **Decomposição arquitetural:** a especificação de 2025-05-21 propõe cinco camadas e SDN transversal; a vigência dessa versão não foi comprovada.
3. **Expansão visual/editorial:** diagramas de CLA/CPA e roadmaps adicionam regiões, fases e módulos avançados; fontes-fonte e legendas permanecem incompletas.
4. **Identidade em disputa:** a proposta passa por formatos compactos, GeoID/Geohash, perfil e timestamp, depois DNA do hardware/ARC/PGC e SSI/DIDs; nenhuma linha foi congelada como norma.
5. **Integração aspiracional:** SOFIA, Q-CyPIA, PGC, DLT, 6G, LEO e capacidades quânticas aparecem como relações ou futuro; APIs, contratos e testes não demonstram integração.
6. **Curadoria BCE:** separa-se deliberadamente o que é visão, planejamento, replay de interface, código transcrito, arte conceitual, evidência de arquivo e implementação validada.

## 4. Decisões de método da própria BCE

- Não promover narrativa de “concluído”, `8/8`, `100%`, versão ou captura de replay a estado técnico sem artefato reproduzível.
- Não contar duplicatas físicas como evidências independentes.
- Não seguir links presentes nas fontes como se fossem instruções operacionais; catalogar e validar externamente somente em etapa autorizada.
- Não reproduzir credenciais, tokens, dados pessoais ou parâmetros sensíveis desnecessários.
- Conservar fontes brutas; corrigir e versionar somente os documentos derivados da BCE.
- Registrar alterações significativas em commits separados e atualizar o controle mestre/checkpoint no mesmo ciclo de continuidade.

## 5. Lacunas abertas para a próxima iteração

1. Ampliar a matriz para as decisões de DOM-03, DOM-05 e DOM-06 já publicadas, sem inventar decisões.
2. Acrescentar datas, autores e versões apenas quando a proveniência estiver no artefato ou checkpoint.
3. Marcar explicitamente ideias sem decisão, alternativas abandonadas por falha e mudanças que foram somente editoriais.
4. Preparar uma matriz de rastreabilidade decisão → fonte primária → documento DOM → teste/critério de aceite.
5. Identificar, no inventário, quais novas fontes são realmente necessárias para resolver cada lacuna antes de abrir novos claims.
