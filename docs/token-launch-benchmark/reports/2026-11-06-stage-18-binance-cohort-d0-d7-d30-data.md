# Etapa 18 — Coorte Binance Spot: coleta quantitativa D0/D+7/D+30

**Data da coleta:** 2026-11-06  
**Status:** coleta concluída para os cinco símbolos selecionados; 30 consultas exatas à API pública retornaram uma linha cada.  
**Escopo:** comparação por venue, Binance Spot, pares USDT. Todos os horários em UTC. Não representa “primeiro preço global” nem compara venues distintas.

## 1. Resultado comparável — candles de 1 minuto

Retorno calculado como `(close checkpoint / close D0) - 1`. O close D0 é o fechamento da vela de 1 minuto no horário de listagem adotado para cada símbolo. D+7 e D+30 são o mesmo horário UTC, sete e trinta dias depois.

| Token | D0 close | D+7 close | Retorno D+7 | D+30 close | Retorno D+30 |
|---|---:|---:|---:|---:|---:|
| MANTA | 1.89888000 | 2.91948000 | +53.7475% | 2.87853000 | +51.5909% |
| ENA | 0.50700000 | 1.29800000 | +156.0158% | 0.78600000 | +55.0296% |
| OMNI | 51.05000000 | 23.11000000 | -54.7307% | 15.20000000 | -70.2253% |
| BIO | 0.88000000 | 0.53640000 | -39.0455% | 0.18960000 | -78.4545% |
| BERA | 7.37700000 | 5.83800000 | -20.8621% | 6.77800000 | -8.1198% |

**Leitura restrita à amostra:** ENA apresenta a maior valorização nos checkpoints (+156.02% D+7; +55.03% D+30). OMNI e BIO registram as maiores quedas em D+30 (-70.23% e -78.45%). MANTA sobe ~51.6% em D+30 e BERA termina ~8.1% abaixo do close D0. Não é recomendação de investimento nem uma generalização estatística sobre todos os lançamentos.

## 2. Candles exatas de 1 minuto (OHLCV)

Campos: O/H/L/C = open/high/low/close; **base volume** é quantidade do token; **quote volume** é notional em USDT. A coluna trades representa número de negociações.

| Token | Checkpoint UTC | O / H / L / C | Base volume | Quote volume (USDT) | Trades |
|---|---|---|---:|---:|---:|
| MANTA | D0 · 2024-01-18 10:00 | 0.05000000 / 3.33300000 / 0.05000000 / 1.89888000 | 13851227.80000000 | 26408707.06808500 | 61669 |
| MANTA | D+7 · 2024-01-25 10:00 | 2.92979000 / 2.95404000 / 2.91820000 / 2.91948000 | 161204.40000000 | 473586.09102800 | 1998 |
| MANTA | D+30 · 2024-02-17 10:00 | 2.88000000 / 2.88241000 / 2.87793000 / 2.87853000 | 7647.50000000 | 22024.97510200 | 147 |
| ENA | D0 · 2024-04-02 08:00 | 0.30000000 / 0.84000000 / 0.30000000 / 0.50700000 | 81881212.43000000 | 43035647.63905000 | 68629 |
| ENA | D+7 · 2024-04-09 08:00 | 1.29100000 / 1.30000000 / 1.29000000 / 1.29800000 | 1173631.34000000 | 1519658.04025000 | 2278 |
| ENA | D+30 · 2024-05-02 08:00 | 0.78900000 / 0.78900000 / 0.78500000 / 0.78600000 | 92530.69000000 | 72810.40270000 | 184 |
| OMNI | D0 · 2024-04-17 12:00 | 1.00000000 / 55.50000000 / 1.00000000 / 51.05000000 | 918667.62000000 | 46896999.92250000 | 80746 |
| OMNI | D+7 · 2024-04-24 12:00 | 23.16000000 / 23.16000000 / 23.10000000 / 23.11000000 | 165.87000000 | 3834.84520000 | 38 |
| OMNI | D+30 · 2024-05-17 12:00 | 15.15000000 / 15.20000000 / 15.14000000 / 15.20000000 | 498.81000000 | 7567.58790000 | 84 |
| BIO | D0 · 2025-01-03 10:00 | 0.03000000 / 1.47700000 / 0.03000000 / 0.88000000 | 43780980.20000000 | 39315015.17666000 | 69260 |
| BIO | D+7 · 2025-01-10 10:00 | 0.53870000 / 0.53880000 / 0.53610000 / 0.53640000 | 93481.70000000 | 50240.10905000 | 235 |
| BIO | D+30 · 2025-02-02 10:00 | 0.19000000 / 0.19000000 / 0.18950000 / 0.18960000 | 19770.20000000 | 3753.10627000 | 39 |
| BERA | D0 · 2025-02-06 13:00 | 1.00000000 / 9.76000000 / 1.00000000 / 7.37700000 | 3595443.85400000 | 25253128.75169700 | 46198 |
| BERA | D+7 · 2025-02-13 13:00 | 5.85200000 / 5.85200000 / 5.82600000 / 5.83800000 | 971.70100000 | 5674.09304100 | 60 |
| BERA | D+30 · 2025-03-08 13:00 | 6.79000000 / 6.79500000 / 6.77700000 / 6.77800000 | 1381.01800000 | 9374.21836100 | 103 |

## 3. Candles diárias UTC — séries distintas

Cada linha é uma vela diária completa, 00:00:00–23:59:59.999 UTC. **A candle diária de data D0 não equivale ao checkpoint intraminuto de abertura**: por exemplo, ENA tem sua candle diária de 2 abril, mas D0 close do método é a vela 08:00 UTC. As duas métricas são apresentadas separadamente.

| Token | Data UTC | O / H / L / C | Base volume | Quote volume (USDT) |
|---|---|---|---:|---:|
| MANTA | 2024-01-18 | 0.05000000 / 3.33300000 / 0.05000000 / 2.17085000 | 219306575.70000000 | 496832448.66092400 |
| MANTA | 2024-01-25 | 3.24676000 / 3.33000000 / 2.84971000 / 2.97699000 | 85748986.20000000 | 264389280.79525600 |
| MANTA | 2024-02-17 | 2.96506000 / 3.02000000 / 2.76581000 / 2.91007000 | 15528185.10000000 | 44717777.00181400 |
| ENA | 2024-04-02 | 0.30000000 / 0.91300000 / 0.30000000 / 0.77500000 | 1550711911.76000000 | 1071118927.27685000 |
| ENA | 2024-04-09 | 1.29300000 / 1.40500000 / 1.19200000 / 1.24100000 | 428924416.69000000 | 556725321.64215000 |
| ENA | 2024-05-02 | 0.79900000 / 0.83200000 / 0.76500000 / 0.79800000 | 137247628.94000000 | 110697720.62923000 |
| OMNI | 2024-04-17 | 1.00000000 / 55.50000000 / 1.00000000 / 27.14000000 | 8490145.87000000 | 310709169.15470000 |
| OMNI | 2024-04-24 | 23.17000000 / 23.64000000 / 21.18000000 / 21.48000000 | 1381428.59000000 | 31214522.02570000 |
| OMNI | 2024-05-17 | 14.21000000 / 15.70000000 / 14.13000000 / 15.14000000 | 572837.59000000 | 8652333.88580000 |
| BIO | 2025-01-03 | 0.03000000 / 1.47700000 / 0.03000000 / 0.81440000 | 731838941.50000000 | 591607008.27191000 |
| BIO | 2025-01-10 | 0.52070000 / 0.54540000 / 0.44630000 / 0.46330000 | 166961733.60000000 | 82253640.09825000 |
| BIO | 2025-02-02 | 0.19100000 / 0.19640000 / 0.14760000 / 0.16030000 | 158452495.20000000 | 27521960.36367000 |
| BERA | 2025-02-06 | 1.00000000 / 15.50000000 / 1.00000000 / 8.71700000 | 89366500.44700000 | 886182293.58922400 |
| BERA | 2025-02-13 | 5.88700000 / 6.30600000 / 5.55000000 / 5.59800000 | 6448828.17100000 | 38106787.35477000 |
| BERA | 2025-03-08 | 6.62900000 / 6.90400000 / 6.50200000 / 6.77000000 | 2592021.84600000 | 17410331.21946800 |

## 4. Procedimento e rastreabilidade

- Fonte primária: Binance public Spot kline API, endpoint oficial de dados públicos: [Binance Vision API](https://data-api.binance.vision/api/v3/klines).
- As 30 consultas foram feitas com `interval=1m` e `interval=1d`, selecionando cada candle por seu timestamp UTC exato; todas retornaram uma linha.
- Os timestamps foram comparados com os horários fixados na Etapa 17. D+7/D+30 mantêm o mesmo relógio UTC, não uma seleção por data local.
- Para volume, a resposta mantém os campos base e quote separados; quote é USDT, não capital captado nem liquidez em livro.
- Host `api.binance.com` mostrou restrição geográfica na sessão; o host oficial `data-api.binance.vision` retornou as linhas solicitadas.
- A lista completa de URLs GET exatas de cada candle (30 checkpoints de minuto + 15 candles diárias) é reconstituível pelos parâmetros abaixo. A coleta bruta foi preservada em tabelas neste relatório.

### Requisições exatas — checkpoints de minuto

| Símbolo | Timestamp D0 (ms) | D+7 (ms) | D+30 (ms) |
|---|---:|---:|---:|
| MANTAUSDT | 1705572000000 | 1706176800000 | 1708164000000 |
| ENAUSDT | 1712044800000 | 1712649600000 | 1714636800000 |
| OMNIUSDT | 1713355200000 | 1713960000000 | 1715947200000 |
| BIOUSDT | 1735898400000 | 1736503200000 | 1738490400000 |
| BERAUSDT | 1738846800000 | 1739451600000 | 1741438800000 |

Para cada timestamp `t`, a consulta usa `symbol=<símbolo>&interval=1m&startTime=t&endTime=t+60000&limit=1`. As consultas diárias usam a data UTC `d`: `interval=1d&startTime=midnight(d)&endTime=midnight(d+1)&limit=1`.

## 5. Limitações

1. Esta é uma coorte por listing Binance Spot e não uma reconstrução de “primeira negociação mundial”; outras venues podem ter aberto antes/depois.
2. D0 é a vela de 1 minuto selecionada pelo horário oficial adotado na Etapa 17. O open/high da candle, por si só, não é tratado como preço de sale/IDO nem como preço universal de abertura.
3. Retornos calculados são close-to-close, não retorno a partir de sale price, preço de anúncio, média, VWAP ou primeiro trade global.
4. As comparações D+7/D+30 não controlam mercado geral, unlocks, airdrops, float, market-making ou condições macro.
5. Volume é giro transacionado observado na Binance Spot. Não significa receita do projeto, fundos captados, liquidez disponível nem volume agregado de todas as exchanges.

## 6. Referências

- [Binance Spot market-data endpoints — klines](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints)
- [Binance Public Data repository — arquivos e convenções](https://github.com/binance/binance-public-data)
- [Binance Vision — API pública](https://data-api.binance.vision/api/v3/klines)
- [Relatório da Etapa 17 — coorte e método](./2026-11-06-stage-17-binance-spot-cohort-and-method.md)

**Conclusão da etapa:** a coleta D0/D+7/D+30 por candle de minuto e as candles diárias UTC estão concluídas para MANTA, ENA, OMNI, BIO e BERA. A etapa seguinte pode ampliar o conjunto comparável ou analisar volume agregado em janelas rolling (24h/7d/30d), sem misturar candles diárias com checkpoints intraminuto.
