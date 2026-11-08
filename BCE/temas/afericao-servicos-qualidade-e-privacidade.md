# Módulo MeshWave — Aferição de Serviços, Qualidade e Privacidade por Adesão

**Identificador documental:** DOM-23 (módulo conceitual de roadmap)  
**Data de registro:** 2026-11-08  
**Estado:** conceito registrado; especificação técnica, governança formal, homologação e implementação pendentes  
**Origem:** definição do responsável pelo projeto nesta conversa  
**Relações:** DOM-02 (arquitetura e roadmap), DOM-14 (segurança, privacidade e governança), DOM-15 (APIs e integrações), DOM-20 (PoUW, UMS e economia MeshWave)

## 1. Objetivo

Registrar a possibilidade de oferecer no ecossistema MeshWave um serviço opcional de aferição da qualidade, disponibilidade e cumprimento de compromissos contratados por provedores independentes.

O serviço pode ser operado pela própria MeshWave ou por terceiros homologados pela MeshWave. O modelo busca apoiar a confiança entre clientes e fornecedores e, de forma sistêmica, incentivar maior cuidado das empresas com a entrega efetiva do que foi acordado.

Este documento registra uma proposta conceitual para o roadmap. Não afirma que o módulo, seus aferidores, protocolos, comissão ou mecanismos de compensação estejam implementados ou formalmente aprovados.

## 2. Autonomia comercial e adesão opcional

A aferição individual não é obrigatória para todos os serviços ou clientes.

- Cada provedor mantém autonomia para definir seus preços, condições e níveis de serviço.
- O cliente decide se a aferição individual é relevante para sua operação e se deseja contratá-la.
- A tolerância do cliente a instabilidade, degradação ou indisponibilidade pode variar conforme a finalidade do serviço.
- Quando não houver adesão ao monitoramento individual, não haverá redução dos valores contratados por falhas individualmente aferidas: o cliente aceita tacitamente a prestação segundo os termos contratados.
- Quando houver adesão, a aferição e eventuais ajustes seguem critérios expressamente acordados, transparentes e aplicáveis àquela contratação.

A existência da possibilidade de aferição pode produzir pressão reputacional e econômica para que fornecedores entreguem o que prometeram, mesmo quando determinado cliente não contrata monitoramento individual. Esse efeito sistêmico não deve ser confundido com penalidade individual automática.

## 3. Aferição contínua ou amostral

A aferição poderá ocorrer de forma contínua ou amostral, conforme o serviço, o contrato, o nível de rigor escolhido e a viabilidade técnica.

Um mecanismo de aferição pode combinar, quando aplicável:

- telemetria do próprio serviço;
- sondagens independentes;
- evidências fornecidas por usuários ou clientes;
- registros assinados e verificáveis;
- medição de qualidade e disponibilidade;
- regras contratuais para falhas, degradação e recuperação;
- mecanismos de contestação quando a evidência for insuficiente ou divergente.

Exemplos de dimensões mensuráveis incluem disponibilidade, latência, perda de pacotes, vazão, continuidade, integridade, execução de recursos e qualidade observada. Indicadores e limites devem ser específicos ao tipo de serviço; não se presume uma métrica universal.

## 4. Protocolos abertos e homologação

Os protocolos, métodos, indicadores e critérios de aferição devem ser abertos e verificáveis. Empresas participantes devem poder examinar os métodos e concordar com os critérios e procedimentos aplicáveis.

A MeshWave poderá:

1. oferecer diretamente um serviço de aferição; e/ou
2. homologar serviços de aferição operados por terceiros.

Homologação significa conformidade com requisitos publicados e verificáveis, não garantia absoluta de ausência de erro. A especificação futura deve tratar independência das sondagens, autenticidade e integridade das evidências, calibração, prevenção de manipulação, transparência metodológica e limites de responsabilidade.

## 5. Comissão permanente de governança

É proposta uma comissão permanente com representantes das empresas participantes para acompanhar e revisar a legitimidade e a precisão dos métodos.

Seu escopo conceitual inclui:
- revisar protocolos, métodos e indicadores;
- avaliar se os métodos aferem corretamente os serviços e suas condições operacionais;
- manter critérios de homologação públicos e consistentes;
- tratar evolução metodológica e divergências;
- preservar neutralidade entre fornecedores e clientes.

A comissão não define os preços dos serviços e não substitui os acordos entre cliente e provedor. Composição, representação, quórum, conflitos de interesse, processo decisório, recurso e força normativa permanecem pendentes de especificação.

## 6. PoUW e remuneração

A aferição de serviços pode constituir uma atividade útil ao ecossistema e, se reconhecida conforme critérios futuros, ser remunerada em UMS por PoUW. Isso não significa que qualquer aferição, auto declaração ou relatório gere UMS automaticamente.

A PoUW deve reconhecer utilidade e contribuição comprovadas; o módulo de aferição fornece evidências para avaliar entrega de serviços, mas não define os preços comerciais nem cria sozinho as regras de emissão.

No caso de contratos monitorados, a aferição poderá apoiar liquidação proporcional ou ajustes por entrega efetiva conforme as condições contratuais acordadas. A regra econômica específica, unidade de medida, apuração, contestação e prevenção de dupla remuneração ainda precisam ser definidas.

## 7. Privacidade: observabilidade sistêmica versus individual

A MeshWave deve separar monitoramento sistêmico do ecossistema e aferição individual vinculada a um cliente.

### 7.1 Sem adesão ao monitoramento individual

- Módulos MeshWave podem continuar observando a saúde e os indicadores sistêmicos do ecossistema.
- A telemetria referente à operação daquele usuário não deve ser persistida de forma identificável.
- Essa telemetria individual é descartada e não pode ser recuperada posteriormente.
- Não há ajuste da remuneração do serviço com base em aferição individual não contratada.

### 7.2 Com adesão ao monitoramento individual

- A identificação individual para aferição ocorre no escopo autorizado pelo usuário.
- O monitoramento deve se limitar à finalidade e aos indicadores contratados.
- Eventuais ajustes de pagamento dependem de evidência e regras contratuais previamente acordadas.

A intenção de privacidade é que a MeshWave não consiga identificar o usuário individualmente apenas por possuir infraestrutura de observabilidade: essa capacidade decorre da adesão ao monitoramento de performance. A implementação deverá demonstrar que a telemetria não aderida não é persistida, vinculada a identidade ou reconstruível por outros módulos. Indicadores agregados também devem ser protegidos contra reidentificação indireta, especialmente em grupos pequenos ou operações singulares.

A formulação “aceitação tácita” da prestação sem aferição individual é um princípio comercial conceitual registrado nesta conversa; termos contratuais, consentimento, bases legais, direitos dos titulares e requisitos LGPD devem ser avaliados antes da implementação.

## 8. Fluxo conceitual

1. O provedor publica ou oferece o serviço, preço e condições de entrega.
2. O cliente escolhe o provedor e decide se contrata aferição individual.
3. Sem adesão, não se mantém telemetria individual identificável; a observabilidade permanece sistêmica/agregada.
4. Com adesão, um aferidor compatível mede o serviço segundo o protocolo e os critérios acordados.
5. Evidências sustentam avaliação da entrega, eventuais ajustes e contestação.
6. A metodologia e os aferidores podem ser revisados por mecanismos de governança e homologação.
7. A atividade de aferição pode ser elegível a PoUW/UMS somente conforme critérios formais futuros.

## 9. Questões abertas

- Quais indicadores e perfis de aferição serão definidos por classe de serviço?
- Como combinar telemetria, sondagens independentes e evidências de usuários?
- Como lidar com erro de aferição, correlação entre sondagens, fraude, falha de rede e indisponibilidade do próprio aferidor?
- Como o usuário ativa, suspende e revoga a adesão? Qual o tratamento dos dados durante transições?
- Como garantir descarte irrecuperável da telemetria individual não aderida e prevenir inferência por agregados?
- Como funcionará a homologação, sua auditoria e eventual suspensão?
- Como será formada e governada a comissão permanente, incluindo conflitos de interesse e recursos?
- Como contratos definem tolerâncias, períodos de amostragem, falhas, degradação, recuperação, crédito e contestação?
- Como aferição útil será reconhecida pela PoUW e remunerada em UMS, sem dupla contagem?
- Como os fornecedores concordarão com protocolos abertos sem criar um requisito universal para todo cliente?

## 10. Estado e próximos passos

**Estado atual: proposta conceitual registrada para o roadmap.** Não há neste registro especificação final, cronograma, fase aprovada, código, aferidor operacional, comissão constituída ou homologação vigente.

Próxima etapa documental/técnica, quando priorizada: transformar os princípios em requisitos verificáveis, mapear dependências com DOM-02, DOM-14, DOM-15 e DOM-20, e submeter desenho de privacidade, contrato de aferição, protocolo de evidências e governança a validação antes de qualquer implementação.

## Histórico

- **2026-11-08:** registrado o conceito de aferição opcional de serviços, protocolos abertos, aferidores MeshWave ou terceiros homologados, comissão permanente, efeito sistêmico de incentivo à qualidade, PoUW/UMS e privacidade por adesão.
