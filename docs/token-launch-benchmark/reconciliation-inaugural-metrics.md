# Reconciliação de métricas de lançamento

Data de revisão: 2026-11-05. Escopo: MON, BERA, LINEA, ASTER, JUP, HYPE, KAITO, HUMA e MET.

## Regras de comparabilidade

A referência comparável deve ser token + venue + par + janela UTC. Não misturar preço de venda com primeira negociação; pico com abertura; captação com volume secundário; volume de protocolo com volume do token; TVL ou liquidez de pool com volume.

## Achados confirmados nesta revisão

- BERA: análise Arrakis reporta volume diário acima de US$2B no lançamento, média de US$442,4M/dia nos primeiros 30 dias e US$91,9M/dia em maio de 2025. Esses dados são reportados pelo artigo, mas ainda falta metodologia de agregação por exchange e período UTC.
- ASTER: MEXC publica abertura de US$0,03015, máxima D1 de US$0,528 (+1.650%) e volume spot D1 acima de US$342M; volume spot+derivativos próximo de US$1,5B. A separação spot/derivativos é crucial. Fonte é análise de exchange.
- JUP: The Block reporta preço inicial de US$0,40 na pool do Jupiter, enquanto CoinDesk cita perpétuo pré-mercado em Aevo a US$0,65 — são referências diferentes, não uma cotação única de abertura. O volume de US$1,38B do agregador Jupiter é atividade do produto, não volume do token JUP.
- MON: a venda pública a US$0,025 deve ser registrada como preço de venda; proceeds não equivalem a volume de mercado secundário.
- LINEA: fontes reportam preço inicial próximo de US$0,03 e volume D1 discrepante (cerca de US$418M versus >US$800M); ainda sem normalização de venues e janela.
- HUMA: Odaily atribui os números de abertura US$0,06683, fechamento D1 US$0,05936 (-11,2%) e volume D1 US$310,37M à negociação iniciada na Binance às 13:00 UTC de 26/05/2025. Melhor ancoragem de venue/time do que a referência anterior; ainda é cobertura secundária.
- MET: preço inaugural da pool de US$0,50 (FDV implícita US$500M) é preço de pool/LGE, não necessariamente preço de mercado consolidado; volume inicial permanece não confirmado.
- KAITO: CMC Reflexivity Research relata queda a aproximadamente US$0,90 no dia do lançamento e máxima de US$2,03 no dia seguinte; volume >US$1B na primeira semana, mas não oferece uma janela D0/D1 consolidada por venue. CoinLore calcula preço de lançamento diferente ($1,60), o que demonstra que “launch price” depende do recorte.
- HYPE: evidência disponível é insuficiente para estabelecer preço e volume consolidados D0/D1 com metodologia uniforme.

## Grade para coleta comparável

Para cada token, registrar timestamp do primeiro trade em UTC; venue e par; preço do primeiro trade; OHLCV para primeiras 24h, 24–48h, D7 e D30; volume spot token-specific sem duplicação; derivativos em coluna separada; liquidez de pool/order book em snapshots; float, unlocks e FDV nos mesmos timestamps; URL da fonte e confiança.

## Fontes

- Arrakis, BERA H1 2025: https://arrakis.finance/blog/lessons-from-h1-2025-top-token-launches
- MEXC, ASTER: https://blog.mexc.com/token-reviews/aster-token-price-surge-analysis-ecosystem-outlook/
- The Block, Jupiter: preço inicial de pool e volume do agregador (não volume token): https://www.theblock.co/news/ecosystems/2024-02-01-jupiter-daily-volume-record-jup-airdrop-275531
- CoinDesk, JUP initial circulating supply / Aevo pre-market: https://www.coindesk.com/markets/2024/01/31/solana-dex-jupiters-jup-token-to-debut-with-135b-circulating-supply
- CMC Reflexivity Research, KAITO listing trajectory: https://coinmarketcap.com/academy/article/reflexivity-research-february-2025-in-review
- Odaily, HUMA Binance launch timestamp and D1: https://www.odaily.news/en/post/5204939
- Phemex, MON sale context: https://phemex.com/blogs/monad-price-prediction-2025-presale-mainnet
- The Defiant, LINEA launch: https://thedefiant.io/news/blockchains/linea-token-launches-at-usd500-million-market-capitalization
- HUMA historical launch coverage: https://markets.coinpedia.org/huma-finance/
- Blockworks, MET LGE: https://blockworks.com/news/meteora-met

## Status

Preliminary evidence ledger. Not an audited market dataset, not financial advice, and not material for external promotion until fields are reconciled.