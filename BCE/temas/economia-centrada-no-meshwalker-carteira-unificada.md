# Economia centrada no MeshWalker e carteira unificada por DID

**Tipo:** princípio arquitetural e econômico informado pelo responsável  
**Data de registro:** 2026-11-05  
**Estado:** conceito registrado; especificação técnica e implementação não verificadas  
**Escopo:** relação entre DID, MeshWalker, nós/equipamentos agregados e contabilização de UMS.

## 1. Princípio central

A unidade econômica operacional da MeshWave é o **MeshWalker identificado por um DID único**, e não cada equipamento ou nó individualmente.

Cada identidade humana ou institucional possui uma carteira lógica unificada vinculada ao seu DID. Um MeshWalker pode agregar N nós/equipamentos — por exemplo, smartphone, PC gamer, servidores ou outros recursos —, mas esses nós não criam carteiras independentes nem exigem que o titular administre saldos separados.

A carteira unificada recebe os créditos e processa as necessidades econômicas de todos os nós associados àquela identidade.

> Nós são unidades operacionais de contribuição e consumo. O DID identifica o MeshWalker. A carteira unificada é a unidade de contabilização econômica.

## 2. Exemplo: nó superavitário e nó consumidor

Considere um MeshWalker que agrega:
- um PC gamer ligado continuamente, oferecendo capacidade significativa de CPU/GPU, armazenamento em vários TB e banda larga à rede;
- um smartphone que utiliza intensamente serviços de streaming e outros recursos, consumindo mais UMS do que produz individualmente.

O PC pode produzir um excedente de UMS enquanto o smartphone apresenta consumo líquido. Como ambos estão associados ao mesmo DID e à mesma carteira, o excedente de um nó cobre contabilmente as necessidades do outro.

Esse equilíbrio ocorre **dentro da carteira unificada**. Não há transferência de UMS entre os nós, porque eles não são titulares econômicos independentes: são recursos operacionais agregados ao mesmo MeshWalker.

O MeshWalker não precisa escolher, mover ou administrar manualmente UMS por equipamento para manter os nós operacionais.

## 3. Identidade, nós e carteira: responsabilidades

| Elemento | Responsabilidade |
|---|---|
| DID | Identificador único do MeshWalker humano ou institucional; não deve duplicar a identidade do titular |
| MeshWalker | Unidade de identidade e titularidade econômica do conjunto agregado |
| Carteira unificada | Consolida créditos, consumo, saldo e obrigações de UMS dos nós associados ao DID |
| Nó/equipamento | Unidade operacional que contribui com recursos, solicita serviços ou consome capacidade |
| Agregação de nós | Associação autorizada de múltiplos equipamentos à mesma identidade e carteira |
| Livro-razão/ledger | Registra eventos de crédito e consumo atribuídos à carteira, preservando a origem operacional do evento |

A identificação de um equipamento ou nó não deve ser confundida com o DID do MeshWalker nem com o identificador da carteira. A associação de um nó à identidade deve ser autorizada e auditável.

## 4. Regra de contabilização

A produção e o consumo são registrados no nível da carteira unificada, mantendo referência ao nó que originou cada evento para fins de medição, auditoria, atribuição e diagnóstico.

Em termos conceituais:
- contribuição útil de qualquer nó associado → crédito na carteira do DID;
- consumo de qualquer nó associado → débito/obrigação na carteira do DID;
- saldo econômico consolidado → resultado agregado dos eventos de todos os nós associados;
- compensação entre nós do mesmo DID → contabilização interna, não transferência entre carteiras.

A associação de titularidade, por si só, não torna uma atividade útil nem remunerável. Os critérios de PoUW, utilidade comprovada, prevenção de demanda artificial e contabilização íntegra continuam aplicáveis.

## 5. Segregação de UMS e movimentações entre carteiras

A carteira unificada não revoga a regra de segregação de UMS:
- transferências diretas de UMS entre carteiras comuns de MeshWalkers são proibidas;
- somente carteiras institucionais/administrativas do sistema, explicitamente autorizadas, podem enviar ou receber UMS em operações permitidas;
- correções, estornos ou modificações de operações devem seguir fluxo administrativo autorizado e auditável, sem migrar UMS diretamente entre carteiras comuns;
- a Genesis é uma carteira institucional do sistema; futuras carteiras institucionais devem ser cadastradas e autorizadas como tais, sem exceções genéricas baseadas apenas em nome ou tipo de operação.

O equilíbrio entre nós pertencentes ao mesmo DID não é uma transferência entre usuários: é o efeito da consolidação de contribuições e consumo em uma única carteira lógica.

## 6. Requisitos arquiteturais derivados

1. **Unicidade da identidade:** um MeshWalker humano ou institucional deve corresponder a um DID único, segundo o método de identidade aprovado.
2. **Carteira por DID:** a carteira lógica é vinculada à identidade, não ao hardware.
3. **Agregação múltipla:** o DID pode associar vários nós, com associação, desassociação e autorização controladas.
4. **Contabilização consolidada:** crédito e consumo dos nós associados afetam o saldo unificado.
5. **Proveniência preservada:** cada evento financeiro conserva identificação do nó, tarefa, tipo de evento e evidência de contribuição/consumo quando aplicável.
6. **Sem carteiras por equipamento:** equipamentos agregados não devem criar carteiras econômicas separadas automaticamente.
7. **Sem transferência comum-para-comum:** o ledger e as funções de movimentação devem impor estruturalmente a proibição de transferência direta entre MeshWalkers comuns.
8. **Operações institucionais autorizadas:** a legitimidade de envio/recebimento de UMS depende da classificação e permissão explícita da carteira institucional.
9. **Atomicidade e idempotência:** operações compostas, como aquisição e bônus, devem ser processadas sem créditos parciais e sem duplicação.
10. **Reconciliação:** saldo consolidado deve ser reconciliável com o histórico de eventos, incluindo ajustes administrativos.

## 7. Distinção entre princípio e implementação

Este documento registra uma definição arquitetural do responsável. Ele não afirma que o modelo de DID único, agregação de nós, carteira unificada, controle de autorização ou ledger já estejam completamente implementados ou verificados.

A especificação técnica deverá definir, entre outros pontos: esquema de associação DID↔nó, gestão de chaves e delegação, autorização de equipamentos, evento contábil de contribuição/consumo, política de nós offline, tratamento de nó desassociado, prevenção de dupla contabilização e operação administrativa de estorno.

## 8. Documentos relacionados

- [Identidade, DIDs e identificador de equipamento](identidade-dids-e-identificador-de-equipamento.md)
- [Modelo econômico da MeshWave: PoUW, UMS, MWN e liquidez distribuída](economia-ums-mwn-pouw-liquidez-distribuida.md)
- [Arquitetura geral e implantação](arquitetura-geral-e-implantacao.md)
- [Registro de decisões curatoriais](../REGISTRO_DECISOES.md)
