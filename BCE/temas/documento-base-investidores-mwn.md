# MeshWave Network (MWN) — Documento-base preliminar para investidores

**Versão:** 0.1 — 2026-11-01  
**Estado:** documento conceitual inicial; sujeito a validação técnica, econômica e jurídica  
**Objetivo:** apresentar a proposta de ativo, sua infraestrutura atual em estágio inicial e a direção de evolução do mercado.

## 1. Resumo

A MeshWave Network está desenvolvendo um ecossistema distribuído no qual a MWN é o ativo destinado à circulação de valor e à conexão com mercados externos. A iniciativa combina uma blockchain própria em estágio rudimentar, uma plataforma de aquisição e uma carteira. A próxima frente de desenvolvimento é permitir que a estrutura evolua de aquisição primária para negociação de compra e venda entre participantes, com registros verificáveis e integração progressiva a canais externos.

A estratégia de evolução é pragmática: preservar a infraestrutura que já existe, comprovar funcionalidade em etapas e buscar visibilidade externa por meio de integrações que exijam o menor esforço técnico e financeiro viável. O estágio atual não deve ser confundido com uma exchange consolidada ou com liquidez externa estabelecida.

## 2. MWN e canais de aquisição

A MWN é o ticker adotado para o ativo MeshWave Network. A aquisição atualmente disponibilizada pela plataforma MeshWave deve ser descrita como **aquisição primária**, salvo quando uma operação específica comprovar negociação entre usuários independentes.

A plataforma própria poderá continuar sendo um canal de aquisição mesmo após a integração a uma exchange externa. A intenção é permitir coexistência entre:
- aquisição primária pela MeshWave;
- carteira e transferência do ativo;
- mercado secundário próprio, quando implementado;
- exchanges e canais externos, quando integrados;
- APIs e serviços de dados de mercado.

A carteira é a infraestrutura de saldo e transferência. Para ser exchange funcional, a plataforma também precisa de ordens, matching, execução, liquidação, controles e histórico verificável.

## 3. Direção de mercado

A evolução pretendida é estudar e implementar um mercado de MWN dentro da própria plataforma, de modo que usuários possam submeter ordens de compra e venda. Isso poderá gerar dados públicos de preço, negócios e volume efetivamente executados, permitindo avaliar candidaturas a agregadores e exchanges.

A presença em agregadores não é garantida pela existência da blockchain, carteira ou API. Cada serviço aplica critérios próprios de mercado, liquidez, integridade e elegibilidade. A MeshWave não apresentará compras primárias como volume de mercado secundário.

## 4. Princípio de proteção dos Meshwalkers

A MeshWave adota como princípio de governança que ordens de usuários (Meshwalkers) tenham prioridade sobre ordens próprias da organização.

A MeshWave não deverá priorizar a venda de reservas próprias ou compras institucionais enquanto houver ordens de usuários compatíveis e executáveis que devam ser atendidas primeiro segundo as regras publicadas. O princípio inclui operações ligadas a Genesis, tesouraria e reservas próprias.

Esse princípio deverá ser codificado no mecanismo de correspondência de ordens, com logs auditáveis. A regra detalhada e os requisitos pendentes estão no [documento de Governança do Mercado MWN](governanca-mercado-mwn-prioridade-meshwalkers.md).

## 5. Atividade inicial e evidências

O sistema principal MeshWave foi anteriormente reportado com registros de aquisições primárias validadas: 13 aquisições, 12 compradores, R$ 55,97 e 2.590,60402683 MWN. Esses números são um retrato documental informado e devem ser reconciliados com os registros de origem antes de sua utilização pública ou em materiais de captação.

Esses dados, se confirmados, demonstram aquisição inicial por participantes; não equivalem a volume negociado em exchange, liquidez secundária, preço de mercado independente ou garantia de valorização.

## 6. Princípios de transparência

A comunicação sobre MWN deverá separar claramente:
- emissões e distribuição primária;
- compras diretas pela plataforma;
- transferências entre carteiras;
- ordens abertas;
- negócios efetivamente executados;
- liquidação fiduciária, quando realmente concluída;
- operações próprias e de tesouraria;
- preço indicativo e preço de negócio executado.

A apresentação de números deverá informar fonte, período, metodologia e estado de reconciliação.

## 7. Plano de evolução em etapas

### Etapa A — Documentação e regras
Consolidar a descrição do ativo, a origem das emissões, a aquisição primária, os princípios de governança e os limites atuais de implementação.

### Etapa B — Mercado próprio mínimo
Especificar e demonstrar ordens de compra/venda entre usuários, prioridade de execução, bloqueio de saldo, execução parcial, liquidação e histórico verificável. A prioridade dos Meshwalkers deve ser aplicada desde o primeiro teste.

### Etapa C — Dados públicos
Disponibilizar informações verificáveis de ativo e mercado — preço, negócios, volume real, pares e endpoints — conforme a funcionalidade existente e sem simular atividade.

### Etapa D — Integração externa
Avaliar exchanges e agregadores com base em custo, requisitos técnicos, aceitação da blockchain nativa, qualidade de exposição e possibilidade de manter os canais próprios.

## 8. Riscos e questões abertas

O projeto permanece sujeito, entre outros, aos seguintes riscos:
- desenvolvimento e operação de blockchain e carteira ainda em estágio inicial;
- necessidade de demonstrar integridade e disponibilidade;
- baixa liquidez e volatilidade;
- aceitação incerta por exchanges e agregadores;
- riscos de custódia, segurança e execução;
- definição de modelo de preço, taxas e liquidação;
- conflitos de interesse entre emissor/tesouraria e usuários;
- enquadramento jurídico, regulatório e tributário aplicável;
- reconciliação independente de dados e registros.

Nenhuma afirmação neste documento representa promessa de retorno, valorização, liquidez, listagem, resgate ou garantia de execução.

## 9. Documentos relacionados

- [Governança do Mercado MWN — Prioridade dos Meshwalkers](governanca-mercado-mwn-prioridade-meshwalkers.md)
- [Modelo econômico: PoUW, UMS, MWN e liquidez distribuída](economia-ums-mwn-pouw-liquidez-distribuida.md)
- [Checkpoint documental de 2026-11-01](../sessoes/2026-11-01_governanca-e-mercado-mwn.md)

## 9.1 Consulta tributária sobre UMS e MWN

A MeshWave documenta uma consulta apresentada à Receita Federal do Brasil sobre a natureza tributária da conversão UMS → MWN e a distinção entre realização de receita da atividade e eventual ganho de capital em alienação posterior. A consulta foi protocolada em 14/10/2025, no processo e-Processo nº 10265.426240/2025-40. **Até o registro documental atual, não há resposta formal positiva ou negativa da RFB**; a tese permanece identificada como entendimento submetido pela consulente, não como posição oficial confirmada.

A consulta usa uma analogia com programas de fidelidade/milhagem para explicar a diferença entre crédito interno de utilidade e ativo com valor de mercado. Consulte o [documento temático completo](consulta-rfb-ums-mwn-natureza-tributaria.md). Esta referência não substitui análise jurídica e não constitui garantia de tratamento fiscal.

## 10. Limite de uso

Este documento é um ponto de partida para diálogo e preparação de materiais. Antes de apresentação pública a investidores, as métricas, afirmações de funcionamento, regras de emissão e aspectos jurídicos devem ser atualizados e validados. Não constitui oferta de investimento, prospecto, aconselhamento financeiro ou parecer jurídico.
