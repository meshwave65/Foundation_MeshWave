# Identidade, DIDs e identificador de equipamento

## Metadados

| Campo | Valor |
|---|---|
| ID curatorial | `DOM-04` |
| Status | `EM_CURADORIA` |
| Versão | `0.1.0` |
| Última atualização | `2026-10-08` |
| Confiança geral | `baixa-média` |
| Fontes principais | Lote 001 e Lote 002 |

## 1. Resumo executivo

As fontes indicam que o MeshWave precisa distinguir identidade lógica, identidade de equipamento e localização/região. O material do Lote 002 propõe uma identificação espacial com Geohash, uma representação regional dual por CPA e CLA, um registro em cache e atualização dinâmica conforme disponibilidade. Outras fontes mencionam DID e `ANDROID_ID` como possíveis referências de identidade.

O estado atual, porém, ainda é conceitual. Não foi encontrado neste lote um esquema normativo que defina campos, codificação, autoridade emissora, ciclo de vida, revogação, migração entre dispositivos ou relação formal entre DID, identificador físico e coordenadas.

## 2. Modelo conceitual provisório

A separação mínima sugerida pelas fontes é:

| Camada | Função | Estado da evidência |
|---|---|---|
| Identidade lógica | representar uma entidade de forma independente de uma sessão ou endereço | proposta; DID aparece como referência |
| Identidade do equipamento | distinguir um dispositivo/nó na rede | requisito aparente; esquema não confirmado |
| Localização/região | associar o equipamento a células, CPA/CLA e Geohash | planejamento conceitual |
| Registro operacional | armazenar e consultar identidade, posição e disponibilidade | planejamento de cache |
| Confiança | avaliar autenticidade/contexto por evidências | relacionado ao ARC, ainda em outro documento |

Esta separação é uma síntese curatorial e não uma especificação oficial.

## 3. Evidência do modelo espacial

A fonte de definição do identificador planeja um mapa de divisão Geohash nos níveis 6 e 9, um diagrama de identificação regional dual CPA/CLA e um infográfico de densidade de equipamentos em escala de 0 a 9. Também prevê uma estrutura de registro em cache, ordenamento dinâmico por disponibilidade, busca, atualização de localização e ativação de usuários.

Esses itens sugerem que a identificação não é apenas um valor estático: ela pode ser indexada espacialmente e acompanhada de estado operacional. Ainda faltam as regras que definem quando a mudança de posição cria um novo registro, quando apenas atualiza atributos e como conflitos entre células são resolvidos.

## 4. Interoperabilidade esperada

Uma implementação interoperável precisaria definir, no mínimo:

1. formato canônico do identificador;
2. relação entre DID, identificador do equipamento e endereço de rede;
3. precisão e versão do Geohash utilizado;
4. campos CPA e CLA e sua hierarquia;
5. timestamp e origem da localização;
6. indicador de disponibilidade e sua escala;
7. mecanismo de atualização, expiração e revogação;
8. proteção contra falsificação, replay e associação indevida;
9. política de resolução quando o mesmo equipamento aparece em regiões incompatíveis;
10. APIs ou eventos de consulta e atualização.

Nenhum desses contratos está suficientemente demonstrado nas fontes processadas.

## 5. Relação com ARC

O ARC fornece uma possível camada de confiança contextual: um identificador poderia ser apresentado junto com evidências de sincronização, desafio contextual e dados de contexto. A fonte ARC diferencia medições reais de placeholders e evita usar um placeholder como evidência de latência. Isso é compatível com a necessidade de não tratar um registro de identidade meramente presente no cache como automaticamente autêntico.

A relação exata entre o identificador e o segredo/challenge do ARC permanece aberta. Não se deve assumir que `ANDROID_ID`, DID ou qualquer identificador de hardware seja um segredo criptográfico.

## 6. Arqueologia da ideia

| Momento | Formulação | Evolução observada |
|---|---|---|
| referências iniciais | `ANDROID_ID` e `Decentralized Identifier` aparecem associados a versões alfa | identidade do dispositivo e identidade descentralizada são consideradas juntas |
| fase de modelagem visual | Geohash, CPA, CLA, densidade e registros de cache são planejados | identidade passa a incluir contexto espacial e operacional |
| fase de documentação | são planejados diagramas de registro, busca e atualização | preocupação com explicabilidade e interface humana |
| fase BCE | identidade é separada de roteamento e ARC | evita colapsar identificador, localização e confiança em um único conceito |

## 7. Alternativas e riscos

- **Usar apenas `ANDROID_ID`:** simples para protótipo Android, mas não resolve identidade global, migração, privacidade ou outros tipos de nó. Não há evidência de que seja a escolha final.
- **Usar somente DID:** oferece uma identidade lógica mais portátil, mas não substitui o vínculo verificável com equipamento, chave, região e ciclo de vida.
- **Usar Geohash como identidade:** inadequado; Geohash representa localização aproximada, não identidade persistente.
- **Usar o registro de cache como fonte de verdade:** inadequado sem assinatura, autoridade, expiração e reconciliação.

## 8. Lacunas prioritárias

1. localizar as fontes específicas de DID e identificador único;
2. localizar código do registro em cache e seus testes;
3. confirmar se CPA e CLA são regiões, caches, autoridades ou funções distintas;
4. definir o ciclo de vida e a revogação;
5. analisar as imagens geradas para verificar se representam um modelo implementável;
6. relacionar identidade com ARC e com a camada de roteamento.

## 9. Evidências

- `KNOWLEDGE/info/20260422_171119_O que é o projeto Meshwave_ - Manus/` — marcadores de versão, DID e `ANDROID_ID`.
- `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus/` — título, mas conteúdo predominantemente operacional; baixa utilidade técnica.
- `KNOWLEDGE/info/20260422_173855_Identificador Único do Equipamento na Rede - Manus/` — planejamento de organização e documentação; baixa utilidade normativa.
- `KNOWLEDGE/info/20260422_174130_Definição do identificador único do equipamento na rede - Manus/` — Geohash, CPA/CLA, cache, densidade e fluxos previstos.
- `KNOWLEDGE/info/20260422_165745_ARC - Autenticação Recessiva Contextual com inferência Bayesiana - Manus/` — relação conceitual com confiança contextual.

## 10. Próximo passo

Processar as fontes adicionais de DID, Android, cache e identificação, localizar código ou contratos de dados e atualizar este documento somente com campos e regras sustentados por evidência.
