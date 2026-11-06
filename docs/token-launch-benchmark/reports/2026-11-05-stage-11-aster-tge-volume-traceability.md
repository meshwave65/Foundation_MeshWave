# Etapa 11 — ASTER TGE: rastreabilidade do volume inaugural

**Data:** 2026-11-05  
**Status:** investigação documental; volume inaugural on-chain não reconciliado.  
**Escopo:** ASTER no TGE de 17/09/2025. Não usar dados da LBank (listagem posterior em 22/09) como substitutos.

## 1. Pergunta de pesquisa

A comunicação da Aster atribuiu ao ASTER **US$ 371 milhões de volume nas primeiras 24 horas**, preço inicial de **US$ 0,03015** e máxima de **US$ 0,528**. O comunicado distribuído pela PR Newswire em 19/09/2025 afirma que o volume seria “according to on-chain data”. Esses números são uma declaração do projeto reproduzida por um canal de press release, não uma série bruta independente validada nesta etapa.

Fonte: [PR Newswire / Aster — 19/09/2025](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html); [AAP republicação](https://www.aap.com.au/aapreleases/cision20250919ae77744/).

## 2. Evento e venue

A documentação oficial informa:
- ASTER TGE e abertura de claims em **17/09/2025**;
- tokens distribuídos para a conta **Aster Spot**;
- possibilidade de negociar ASTER diretamente na Aster Spot após o TGE, ou retirar para carteira on-chain.

Fonte: [Aster Docs — TGE](https://docs.asterdex.com/usdaster-token/tge).

Essa arquitetura exige separar o livro de negociação Aster Spot do mercado on-chain aberto (pools AMM e swaps em DEXs externas). O contrato BEP-20 ASTER da BNB Chain é indicado como `0x000Ae314E2A2172a039B26378814C252734f556A`; isso identifica o token, mas não é por si só uma fonte da fita de negociações do livro Spot.

Referência do contrato: [Binance listing announcement](https://www.binance.com/en-PH/support/announcement/detail/ff209dd797b2418198c312a1a266e73a), publicado em outubro de 2025.

## 3. Evidência sobre a natureza dos dados de volume

A página pública de [DefiLlama — Aster Spot](https://defillama.com/protocol/aster-spot) classifica seu volume DEX em **“Off Chain”**, e descreve a métrica como volume de swaps spot do DEX. A página informa que Aster Spot opera em BSC, Aster e Off Chain. Isso é evidência de que a atividade do produto não é integralmente representada por eventos de swap públicos em uma única cadeia.

A mesma página apresenta atualmente dados cumulativos e recentes, não a série bruta histórica do primeiro dia. Portanto, não é possível usar esses números atuais para validar retroativamente os US$ 371M do TGE.

## 4. Pools on-chain externos — não equivalem à venue inaugural

Agregadores apontam pools ASTER/USDT de PancakeSwap V3 criados em **20/09/2025**, depois do TGE:
- Pool `0x7e58f160b5b77b8b24cd9900c09a3e730215ac47`;
- ASTER: `0x000Ae314E2A2172a039B26378814C252734f556A`;
- USDT BNB Chain: `0x55d398326f99059fF775485246999027B3197955`.

Fontes secundárias de pool: [DexPaprika](https://dexpaprika.com/bsc/pool/0x7e58f160b5b77b8b24cd9900c09a3e730215ac47), [WhatToFarm](https://whattofarm.io/pairs/bnb-chain-pancakeswapv-aster-usdt-created-2025-09-20).

Como a pool foi criada três dias depois do TGE, seus dados não medem a negociação inaugural de 17/09. Não se deve agregar pools externas, CEX ou ASTER perpétuo à métrica de ASTER Spot sem declarar cada venue e a janela.

## 5. Conclusão provisória

1. **TGE e venue inicial confirmados:** 17/09/2025; negociação em Aster Spot.
2. **US$ 371M / 24h:** claim divulgado pelo projeto; não validado independentemente nesta etapa.
3. **Preço inicial US$ 0,03015 e máxima US$ 0,528:** reportados pela mesma fonte do projeto; falta série transacional primária que confirme preço, janela e metodologia.
4. A descrição “on-chain” no comunicado não basta para reproduzir o volume. O painel DefiLlama classifica parte do volume da Aster Spot como Off Chain.
5. LBank: separado, abertura em 22/09/2025; não serve como proxy para o TGE de 17/09.
6. Sem arquivo histórico de trades / API arquivada / método público que permita recomputar a fita, classificar o volume do TGE como **não confirmado independentemente**.

## 6. Próxima coleta

Buscar especificamente uma fonte primária de histórico de trades da Aster Spot que exponha (a) timestamp UTC, (b) par, (c) preço e quantidade, (d) unidade de volume, (e) identificação de trades agregados/duplicados e (f) janela exata. Em paralelo, avaliar os eventos on-chain de distribuição/retirada apenas como trilha de transferências, não como volume de negociação.

## Fontes consultadas

- [Aster TGE docs](https://docs.asterdex.com/usdaster-token/tge)
- [Aster / PR Newswire — US$371M](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html)
- [AAP — republicação do comunicado](https://www.aap.com.au/aapreleases/cision20250919ae77744/)
- [DefiLlama — Aster Spot volume classification](https://defillama.com/protocol/aster-spot)
- [Binance ASTER listing / contract](https://www.binance.com/en-PH/support/announcement/detail/ff209dd797b2418198c312a1a266e73a)
- [DexPaprika — ASTER/USDT pool](https://dexpaprika.com/bsc/pool/0x7e58f160b5b77b8b24cd9900c09a3e730215ac47)
- [WhatToFarm — ASTER/USDT pool](https://whattofarm.io/pairs/bnb-chain-pancakeswapv-aster-usdt-created-2025-09-20)

**Limitação:** pesquisa documental nesta etapa; não foi coletado arquivo de trades do Aster Spot nem recomputado o volume on-chain de 17/09.
