# Etapa 15 — HUMA e ASTER: checkpoints D+7/D+30 em Spot

**Data de coleta:** 2026-11-06  
**Status:** checkpoints de candles 1m obtidos de fontes oficiais; SHA-256 de arquivos HUMA confirmados.  
**Escopo:** preço/volume pontual exatamente no mesmo horário UTC do primeiro candle negociado (âncora) e nos checkpoints de 7 e 30 dias. Não confundir esses checkpoints com fechamento de dia UTC.

## 1. Definição da metodologia

- Âncora: primeiro candle 1m não vazio disponível na venue estudada.
- D+7 e D+30: candle 1m com open-time exatamente 7 ou 30 dias depois da âncora, no mesmo horário UTC.
- Retorno close-to-close: (close do checkpoint / close do candle-âncora) − 1. Não é retorno calculado desde o open.
- Volume-base é quantidade do token; quote volume é notional em USDT. Não intercambiar unidades.
- O resultado representa apenas a venue e o par identificados.

## 2. Resultados comparáveis — checkpoints exatos

| Venue / par | Ponto | Open time UTC | Open | High | Low | Close | Base volume | Quote volume (USDT) |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Binance Spot HUMAUSDT | Âncora | 2025-05-26 13:00 | 0.01000000 | 0.10600000 | 0.01000000 | 0.08887000 | 63,402,250 | 5,910,044.746370 |
| Binance Spot HUMAUSDT | D+7 | 2025-06-02 13:00 | 0.03916000 | 0.03933000 | 0.03912000 | 0.03933000 | 822,789 | 32,263.230100 |
| Binance Spot HUMAUSDT | D+30 | 2025-06-25 13:00 | 0.03336000 | 0.03336000 | 0.03329000 | 0.03336000 | 84,791 | 2,826.363510 |
| Aster Spot ASTERUSDT | Âncora | 2025-09-17 12:00 | 0.03015 | 0.08990 | 0.03015 | 0.06897 | 2,996,183.85 | 218,450.73132 |
| Aster Spot ASTERUSDT | D+7 | 2025-09-24 12:00 | 2.27093 | 2.28550 | 2.25100 | 2.26388 | 517,659.74 | 1,172,794.20300 |
| Aster Spot ASTERUSDT | D+30 | 2025-10-17 12:00 | 1.07743 | 1.08132 | 1.07613 | 1.08132 | 49,168.10 | 53,064.69722 |

## 3. Variação do close contra a âncora

| Par / venue | D+7 close-to-close | D+30 close-to-close |
|---|---:|---:|
| HUMAUSDT — Binance Spot | -55.7443% | -62.4620% |
| ASTERUSDT — Aster Spot | +3,182.4126% | +1,467.8126% |

As variações são grandes e específicas desses casos; não constituem previsão de desempenho nem estimativa de resultado para MWN.

## 4. ASTER — barras diárias UTC, outra definição

A API também retorna candles diários rotulados pela data UTC. Esses pontos não são os checkpoints exatos de 12:00 UTC acima:

| Data UTC | Open | High | Low | Close | Base volume | Quote volume (USDT) | Trades |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025-09-17 (D0 calendário) | 0.03015 | 0.48700 | 0.03015 | 0.40182 | 1,024,842,943.38 | 226,232,883.15400 | 278,191 |
| 2025-09-24 (D+7 calendário) | 1.95557 | 2.42830 | 1.89000 | 2.30645 | 220,983,826.26 | 492,996,929.59892 | 1,066,258 |
| 2025-10-17 (D+30 calendário) | 1.25689 | 1.28874 | 1.02000 | 1.15903 | 139,417,812.95 | 155,238,027.11899 | 161,421 |

**Atenção:** o D0 calendário ASTER (00:00–24:00 UTC, com negociação começando às 12:00) é diferente da janela inaugural rolling de 24h (12:00–12:00) consolidada nas etapas 12–13.

## 5. Integridade e cobertura

### HUMA — Binance Vision
Arquivos oficiais de candles 1m; os timestamps de Spot para 2025 são em microssegundos, conforme documentação pública Binance.

| Data de arquivo | Linhas / cobertura | SHA-256 publicado e verificado |
|---|---|---|
| 2025-05-26 | 660 linhas, 13:00–23:59 UTC | 0c27f6bf1d69dcd61bc9fd131a48fb875866da965319aff49d488f42283219c4 |
| 2025-06-02 | 1,440 linhas, dia UTC completo | 2d5e535ca3bf419e5dba351db9451a6baaa97cca72dad45d3e1d5a89c8b6d44a |
| 2025-06-25 | 1,440 linhas, dia UTC completo | bbedaa2284d8c2b8ac59760a9ee622ea968977301bcfd27a603bd9b49e65a9f9 |
| 2025-06-26 | 1,440 linhas, dia UTC completo | 7f903e7b49fcd55adfd8b301de92df60e185792ce0f67f6baf0f2ef1001c15a6 |

Os arquivos de 25 e 26 de junho e seus checksums foram diretamente verificados. O arquivo de 26 de junho serve como controle de continuidade da coleta, não como ponto D+30.

### ASTER — Aster Spot API
- API oficial: endpoint `/api/v1/klines`; resposta em milissegundos, ordem de campos compatível com a estrutura de klines Binance: open time, OHLC, base volume, close time, quote volume, trades, taker-buy base e quote, campo reservado.
- `exchangeInfo` reporta listingTime 2025-09-16 23:32:11.852 UTC, mas consultas retornaram candles 1m vazios em 16/09 e antes de 12:00 UTC em 17/09. Primeiro candle não vazio: 17/09 12:00 UTC.
- O candle diário inicial é rotulado 17/09 00:00 UTC. Apresentamos tanto candles diários quanto checkpoints de 1m, com definições distintas.
- Limite documentado: máximo de 1,500 klines por requisição; não foi localizada retenção histórica oficial nem arquivo/checksum público comparável ao Binance Vision.

## 6. Fontes oficiais e endpoints

- [Binance public-data README](https://github.com/binance/binance-public-data) — precisão dos timestamps, campos de klines e validação CHECKSUM.
- [Binance Spot market-data endpoints](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints).
- [Índice Binance Vision HUMA 1m](https://data.binance.vision/?prefix=data/spot/daily/klines/HUMAUSDT/1m/).
- [HUMA 26/05 ZIP](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05-26.zip); [02/06 ZIP](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-06-02.zip); [25/06 ZIP](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-06-25.zip); [25/06 checksum](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-06-25.zip.CHECKSUM); [26/06 ZIP](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-06-26.zip); [26/06 checksum](https://data.binance.vision/data/spot/daily/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-06-26.zip.CHECKSUM).
- [Aster Spot market-data API docs](https://asterdex.github.io/aster-api-website/spot/market-data-api/).
- [Aster API — daily candles](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1d&startTime=1758067200000&endTime=1760745599999&limit=500).
- [Aster API — D+7 exact 1m candle](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758715200000&endTime=1758715259999&limit=1).
- [Aster API — D+30 exact 1m candle](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1760702400000&endTime=1760702459999&limit=1).
- [Aster API — exchangeInfo](https://sapi.asterdex.com/api/v1/exchangeInfo?symbol=ASTERUSDT).

## 7. Conclusões e próximos passos

1. D+7/D+30 já podem ser comparados por checkpoint exato, respeitando venue e método.
2. ASTER tem extrema diferença entre retorno pontual de 1m e fechamento de candles diários: não misturar esses eixos.
3. HUMA perde 55.74% do close-âncora até o checkpoint D+7 e 62.46% até D+30, nesta amostra Binance Spot.
4. ASTER registra +3,182.41% até D+7 e +1,467.81% até D+30, por close de checkpoint, mas ainda mantém ganho muito alto sobre a âncora; esse resultado não representa uma expectativa de lançamento.
5. Próxima coleta: estender checkpoints D+7/D+30 a outros casos do benchmark onde haja histórico bruto verificável; buscar também janelas completas 24h/D0/D1, sem substituir os pontos por barras de calendário.

**Limite:** dados observacionais de pares Spot específicos. Não representam volume global consolidado, preço de venda primária, captação, ou desempenho de todas as venues.
