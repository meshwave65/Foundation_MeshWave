# ASTER

**TGE:** 17 set 2025. Aster Spot ASTER/USDT: primeira candle observada em 17/09/2025 12:00 UTC (20:00 UTC+8), open US$0,03015.

## Dados primários da API Spot oficial

Janela [17/09 12:00 UTC, 18/09 12:00 UTC), 1.440 candles de 1 minuto:
- OHLC: **0,03015 / 0,52800 / 0,03015 / 0,44550 USDT**
- Volume-base: **1.374.581.953,34 ASTER**
- Volume cotado: **US$379.894.660,36485**
- Trades: **460.041**
- Continuidade: sem lacunas; nenhum candle OHLC inconsistente na janela.

Primeira hora (12:00–13:00 UTC): high US$0,08990, close US$0,07130, volume cotado US$6.947.477,92737, 13.289 trades.

D0 UTC (17/09 12:00–24:00, parcial): volume cotado US$226.232.883,15400. D1 calendário UTC (18/09): volume cotado US$410.868.936,74480.

D7 rolling (até 24/09 12:00 UTC): close US$2,27317, high US$2,42830, volume cotado US$3.523.536.657,80201, 5.861.544 trades.

D30 rolling (até 17/10 12:00 UTC): close US$1,07766, high US$2,42830, volume cotado US$8.465.046.217,27698, 12.735.759 trades.

**Método:** API pública oficial Aster Spot `GET /api/v1/klines`, símbolo ASTERUSDT; 1m para 60m/24h e 1h para D7/D30, janelas semiabertas e timestamps UTC. A API informa volume-base e quote-volume separadamente. Estes dados são da Aster Spot API, não um agregado multi-venue nem reconstrução independente de swaps on-chain.

## Reconciliação com a publicação do projeto

A PRNewswire release da Aster reporta abertura US$0,03015, high US$0,528 e volume de primeiro dia US$371M. A API oficial reproduz exatamente open e high; quote-volume calculado de US$379,895M difere em cerca de US$8,895M (+2,40%). A discrepância de volume pode decorrer de corte temporal/metodologia; não deve ser atribuída sem uma análise on-chain independente.

O valor secundário próximo de US$0,08 não corresponde à abertura da primeira candle; a primeira hora alcançou high US$0,08990, o que pode explicar uma cotação intrahora.

## LBank (venue separada)

O anúncio inicial de LBank para 17/09/2025 12:30 UTC foi adiado. A LBank anunciou abertura posterior para 22/09/2025 05:00 UTC; candles e anomalias OHLC estão no [relatório Etapa 10](../reports/2026-11-05-stage-10-aster-lbank-historical-candles.md). Não somar essa série ao volume do TGE de 17/09.

## Fontes

- [Aster Spot API docs](https://github.com/asterdex/api-docs/blob/master/V1%28Legacy%29/EN/aster-finance-spot-api.md)
- [Aster TGE docs](https://docs.asterdex.com/usdaster-token/tge)
- [Aster PRNewswire release](https://www.prnewswire.co.uk/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561466.html)
- [LBank delay notice](https://www.lbank.com/support/articles/1968291802968489984)
- [LBank later listing notice](https://www.lbank.com/fr/support/articles/1969984335821930496)
- [Stage 12 quantitative report](../reports/2026-11-05-stage-12-aster-tge-official-spot-api-reconciliation.md)
