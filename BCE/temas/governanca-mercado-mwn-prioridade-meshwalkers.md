# Governança do Mercado MWN — Prioridade dos Meshwalkers

**Tipo:** princípio de governança e base preliminar para regulamento operacional  
**Data:** 2026-11-01  
**Estado:** princípio definido pelo responsável; regras de implementação ainda não verificadas  
**Escopo:** mercado próprio MeshWave, ordens da tesouraria e emissões/reservas próprias.

## 1. Objetivo

Formalizar o compromisso de que a MeshWave não utilizará sua posição de emissora, operadora da carteira ou administradora do mercado para obter prioridade de negociação sobre usuários — os **Meshwalkers**.

A MeshWave poderá manter canal próprio de aquisição primária e, futuramente, mercado secundário de compra e venda. Esses canais não deverão impedir a negociação em plataformas externas nem conferir à organização preferência de execução.

## 2. Princípio de prioridade dos Meshwalkers

Ordens de compra e venda submetidas por Meshwalkers têm prioridade de execução sobre ordens próprias da MeshWave, incluindo ordens ligadas à Genesis, reservas institucionais, tesouraria, distribuição ou alienação de MWN própria.

A MeshWave não poderá priorizar a venda de suas reservas enquanto existirem ordens de venda de usuários compatíveis e executáveis em condições iguais ou melhores. Da mesma forma, não poderá priorizar suas próprias compras quando houver ordens de compra de usuários compatíveis e executáveis em condições iguais ou melhores.

A prioridade aplica-se a contas e operações sob controle direto ou indireto da MeshWave. A organização não poderá contornar a regra por meio de contas relacionadas, ordens fracionadas, mudança artificial de origem ou outro expediente equivalente.

## 3. Regra de execução a ser refletida no matching engine

A regra deverá ser implementada no mecanismo de correspondência de ordens (*matching engine*), e não apenas na interface ou em procedimentos manuais.

Como requisito mínimo:

1. Ordens de usuários devem ser identificadas como tais, com origem rastreável.
2. Entre ordens de usuários, a regra de preço e, em seguida, tempo de entrada deverá ser definida e aplicada de forma consistente.
3. Uma ordem própria da MeshWave não poderá executar contra uma ordem de usuário se houver uma ordem de usuário compatível que, segundo as regras publicadas de preço e prioridade, deva ser atendida primeiro.
4. Ordens próprias não poderão ser inseridas ou executadas para ultrapassar ordens de usuários pendentes.
5. Execuções parciais, cancelamentos, alterações de preço, falhas e concorrência de ordens deverão preservar a prioridade e gerar registros auditáveis.
6. A plataforma deverá distinguir ordens próprias, ordens de usuários e operações de emissão/distribuição; emissão não deverá ser apresentada como negociação secundária.

A especificação técnica deverá definir o comportamento exato para livro de ofertas, preço de execução, prioridade temporal, ordens parcialmente executadas e compatibilidade entre pares. Esta declaração não substitui tal especificação.

## 4. Exemplo operacional

- Um Meshwalker possui uma ordem de venda de MWN a preço compatível com uma ordem de compra.
- A MeshWave também possui MWN em tesouraria e uma ordem de venda.
- O sistema não pode executar a ordem própria da MeshWave antes da ordem compatível do Meshwalker.
- O mesmo princípio vale para ordens de compra próprias: a tesouraria não pode avançar à frente de ordens de compra de usuários compatíveis e executáveis.

A ordem de usuário não precisa ser integralmente executada quando a liquidez disponível é insuficiente; execução parcial e saldo remanescente devem ser informados de modo claro.

## 5. Transparência e prevenção de conflitos

A MeshWave deverá manter registros que permitam verificar, pelo menos:
- origem/categoria da ordem;
- par negociado;
- lado (compra/venda);
- preço e quantidade;
- instante de submissão, alteração, cancelamento e execução;
- execução parcial ou total;
- taxas aplicadas;
- regra de prioridade usada;
- identificação de operações próprias e institucionais.

A divulgação pública deverá proteger dados pessoais e credenciais, mas permitir auditoria razoável da integridade do mercado.

A MeshWave não deverá simular liquidez, demanda ou volume por meio de operações próprias apresentadas como atividade independente. Ordens próprias e operações entre contas relacionadas deverão ser identificadas e tratadas conforme regras transparentes.

## 6. Emissões, Genesis e tesouraria

Emissões Genesis e eventuais emissões futuras devem ser documentadas com quantidade, finalidade, destinação e registro. A emissão ou a titularidade de MWN própria não confere prioridade de negociação.

A distribuição primária de MWN pela MeshWave deve ser separada contabilmente e na apresentação pública do volume de negociação secundária entre usuários.

## 7. Relação com canais externos

A plataforma MeshWave poderá coexistir com exchanges e canais externos. A integração externa não deverá, por si só, monopolizar ou extinguir os canais próprios de compra e venda.

A prioridade aqui definida aplica-se ao mercado operado ou controlado pela MeshWave. As condições de interoperabilidade, custódia, depósitos, saques, liquidação e reconciliação com plataformas externas serão objeto de especificação separada.

## 8. Requisitos ainda pendentes

Antes da implementação operacional, devem ser especificados e testados:
- modelo de livro de ofertas e tipos de ordem;
- prioridade de preço/tempo e sua relação com prioridade de usuário;
- reserva/bloqueio de saldo ao abrir ordens;
- execução parcial, cancelamento e alteração;
- liquidação atômica ou mecanismo de compensação;
- prevenção de gasto duplo e operações duplicadas;
- taxas, limites, suspensão e tratamento de falhas;
- registros e API pública de mercado;
- controles de conflito de interesse;
- requisitos jurídicos, regulatórios, tributários e de custódia aplicáveis.

## 9. Natureza e limite

Este documento registra o princípio de governança definido pelo responsável e serve de base para o regulamento operacional e para a especificação do mecanismo de negociação. Não afirma que uma exchange própria já esteja implementada, que ordens já possam ser negociadas entre usuários ou que os controles descritos estejam ativos.

A publicação e operação do mercado devem ser precedidas de avaliação jurídica e regulatória aplicável.
