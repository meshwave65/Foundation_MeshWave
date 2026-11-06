# Etapa 11 — ASTER TGE: rastreabilidade do volume inaugural

**Data:** 2026-11-05  
**Status atualizado (2026-11-06):** a API pública oficial Aster Spot foi recuperada. O preço de abertura (US$0,03015) e a máxima (US$0,528) do release foram reproduzidos; quote-volume de 24h calculado foi US$379,895M contra US$371M divulgados (+2,40%). O claim específico “on-chain” ainda não foi reconciliado independentemente.  
**Escopo:** ASTER no TGE de 17/09/2025. Não usar dados da LBank (listagem posterior em 22/09) como substitutos.


## Atualização empírica posterior — API pública Aster Spot

A documentação oficial de Spot e o endpoint público `GET /api/v1/klines` permitem recuperar a série histórica ASTERUSDT. O horário do mercado foi reportado como 20:00 UTC+8 (12:00 UTC), e a primeira candle observada inicia em 17/09/2025 12:00 UTC com open US$0,03015.

Janela rolling exata [17/09 12:00, 18/09 12:00 UTC), 1.440 candles de 1 minuto:
- OHLC: **0,03015 / 0,52800 / 0,03015 / 0,44550 USDT**.
- Volume-base: **1.374.581.953,34 ASTER**.
- Quote-volume: **US$379.894.660,36485**.
- Trades: **460.041**; série sem lacunas nem inconsistências OHLC.

O quote-volume da API é aproximadamente US$8,895M (+2,40%) acima do release de US$371M. A API é dado primário de mercado Spot, mas não é por si só uma auditoria da metodologia “on-chain” do comunicado. Os agregados completos D0/D1/D7/D30 estão no [relatório quantitativo Etapa 12](./2026-11-05-stage-12-aster-tge-official-spot-api-reconciliation.md).

Fonte técnica: [Aster Spot API V1](https://github.com/asterdex/api-docs/blob/master/V1%28Legacy%29/EN/aster-finance-spot-api.md); endpoint: https://sapi.asterdex.com/api/v1/klines.

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
3. **Preço inicial US$ 0,03015 e máxima US$ 0,528:** agora reproduzidos pela API pública oficial Spot para a janela do TGE; quote-volume da API de US$379,895M diverge em ~2,40% do claim de US$371M. A diferença de metodologia on-chain continua aberta.
4. A descrição “on-chain” no comunicado não basta para reproduzir o volume. O painel DefiLlama classifica parte do volume da Aster Spot como Off Chain.
5. LBank: separado, abertura em 22/09/2025; não serve como proxy para o TGE de 17/09.
6. A API pública de candles Spot já fornece a série de mercado e permite reproduzir OHLCV por janela. O claim específico de volume on-chain ainda não está confirmado independentemente; a API de mercado não substitui a auditoria on-chain.

## 6. Próxima coleta

Para explicar a diferença de ~2,40%, buscar fonte independente de trades/swaps e definição exata do volume on-chain do release; manter timestamps UTC, par, venue, preço/quantidade, unidade de volume, duplicação/agregação e janela explícitos. Transferências de claim/retirada não são volume de negociação.

## Fontes consultadas

- [Aster TGE docs](https://docs.asterdex.com/usdaster-token/tge)
- [Aster / PR Newswire — US$371M](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html)
- [AAP — republicação do comunicado](https://www.aap.com.au/aapreleases/cision20250919ae77744/)
- [DefiLlama — Aster Spot volume classification](https://defillama.com/protocol/aster-spot)
- [Binance ASTER listing / contract](https://www.binance.com/en-PH/support/announcement/detail/ff209dd797b2418198c312a1a266e73a)
- [DexPaprika — ASTER/USDT pool](https://dexpaprika.com/bsc/pool/0x7e58f160b5b77b8b24cd9900c09a3e730215ac47)
- [WhatToFarm — ASTER/USDT pool](https://whattofarm.io/pairs/bnb-chain-pancakeswapv-aster-usdt-created-2025-09-20)

**Limitação atual:** candles históricas oficiais Spot foram recuperadas e agregadas; ainda não foi reproduzido independentemente o volume descrito como on-chain no release.
