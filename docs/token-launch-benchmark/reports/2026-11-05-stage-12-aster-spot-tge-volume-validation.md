# Etapa 12 — ASTER Spot: validação quantitativa do volume do TGE

**Data:** 2026-11-05  
**Status:** cálculo reproduzido a partir da API pública Spot; diferença em relação ao claim do projeto ainda não reconciliada.  
**Escopo:** ASTERUSDT na Aster Spot. Sem misturar ASTER perpétuo, Binance, LBank, pools externas ou volumes de protocolo.

## 1. Fonte e acesso

A documentação oficial Aster Spot V3 indica base URL `https://sapi.asterdex.com`, com endpoints públicos de klines e trades. Foram executadas consultas GET públicas e somente leitura.

- [API oficial — Spot V3](https://github.com/asterdex/api-docs/blob/master/V3%28Recommended%29/EN/aster-finance-spot-api-v3.md)
- [exchangeInfo — ASTERUSDT](https://sapi.asterdex.com/api/v1/exchangeInfo)
- [API endpoint — klines](https://sapi.asterdex.com/api/v1/klines)

A resposta `exchangeInfo` indicou:
- Símbolo: `ASTERUSDT`, status `TRADING`;
- `listingTime`: `1758012731852` = 2025-09-16 08:52:11.852 UTC;
- `baseAssetAddress`: `0x000Ae314E2A2172a039B26378814C252734f556A`.

O timestamp metadata não equivale necessariamente ao primeiro trade. A consulta de klines de 1 minuto no entorno desse `listingTime` retornou zero candles. A primeira candle efetivamente preenchida observada foi em **2025-09-17 12:00:00 UTC**.

## 2. Método de agregação

Foram consultadas candles de 1 minuto em blocos com intervalo explícito, removendo a candle duplicada em fronteiras inclusivas. Para janela `[início,fim)`:
- Open: abertura da primeira candle;
- High / Low: máximo / mínimo das candles;
- Close: fechamento da última candle;
- Base volume: soma do campo 5;
- Quote volume: soma do campo 7;
- Trade count: soma do campo 8;
- Taker-buy base/quote: soma dos campos 9/10.

A cobertura 24h foi validada por 1.440 candles consecutivas, sem lacunas. A janela inicia no primeiro timestamp com dados disponíveis, não no horário presumido do TGE.

## 3. Resultados — 17/09/2025 UTC (dia-calendário parcial)

**Janela disponível:** 12:00:00–23:59:00 UTC; 720 candles.  
**Ausente na resposta:** 00:00–11:59 UTC; 720 minutos. Sem gaps internos no trecho retornado.

| Métrica | Resultado |
|---|---:|
| Open | 0.03015 USDT |
| High | 0.48700 USDT |
| Low | 0.03015 USDT |
| Close | 0.40182 USDT |
| Volume base | 1,024,842,943.38 ASTER |
| Volume quote | 226,232,883.154 USDT |
| Trades | 278,191 |
| Taker-buy base | 574,631,655.85 ASTER |
| Taker-buy quote | 131,268,295.69964 USDT |

A janela 00:00–01:00 UTC retornou zero candles; seus OHLC são indefinidos e totais aditivos retornam zero na resposta observada. Isso não deve ser interpretado como prova de que não houve negociação em outros sistemas/venues.

## 4. Primeiras 24h a partir da primeira candle observada

**Janela exata:** `[2025-09-17 12:00:00, 2025-09-18 12:00:00) UTC`  
**Coverage:** 1.440 candles, sem gaps.

| Métrica | Resultado |
|---|---:|
| Open | 0.03015 USDT |
| High | 0.52800 USDT |
| Low | 0.03015 USDT |
| Close | 0.44550 USDT |
| Volume base | 1,374,581,953.34 ASTER |
| Volume quote | 379,894,660.36485 USDT |
| Trades | 460,041 |
| Taker-buy base | 754,799,805.71 ASTER |
| Taker-buy quote | 211,192,450.79996 USDT |

## 5. Reconciliação com o claim de US$371M

O comunicado da Aster distribuído pela PR Newswire afirma volume de **US$371 milhões** nas primeiras 24 horas e preço de abertura **US$0.03015**, máxima **US$0.528**. Fonte: [PR Newswire / Aster — 19/09/2025](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html).

O cálculo das candles Spot na janela 12:00–12:00 UTC produz **379,894660M USDT**, cerca de **2,40% acima** do valor divulgado (diferença nominal de 8,895M USDT). Os valores de abertura e máxima coincidem com os valores reportados no comunicado.

**Interpretação:** forte correspondência de preço e ordem de grandeza do volume; não é reconciliação exata. Possíveis diferenças de janela, fonte de avaliação USD/USDT, tratamento de trades ou metodologia não foram resolvidas. Não atribuir a diferença a uma causa sem evidência.

## 6. URLs de coleta

- [exchangeInfo](https://sapi.asterdex.com/api/v1/exchangeInfo)
- [Klines 17/09 00:00–12:00 UTC](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758067200000&endTime=1758110400000&limit=1000)
- [Klines 17/09 12:00–24:00 UTC](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758110400000&endTime=1758153600000&limit=1000)
- [Klines 18/09 00:00–12:00 UTC](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758153600000&endTime=1758196800000&limit=1000)
- [Klines 17/09 00:00–01:00 UTC](https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758067200000&endTime=1758070800000&limit=1000)
- [AggTrades query (1000 rows)](https://sapi.asterdex.com/api/v1/aggTrades?symbol=ASTERUSDT&startTime=1758067200000&endTime=1758153600000&limit=1000)
- [Historical trades probe](https://sapi.asterdex.com/api/v1/historicalTrades?symbol=ASTERUSDT&limit=1000) — HTTP 401, `API-key format invalid`; no authentication attempted.

## 7. Limitações e próximo passo

- O conjunto público testado começa às 12:00 UTC de 17/09; candles anteriores estão ausentes nessa API. O horário não deve ser descrito como “o horário exato do TGE” sem confirmação adicional.
- `historicalTrades` anônimo retornou HTTP 401. `aggTrades` público retornou apenas 1.000 registros na consulta, não suficiente para reconstruir sozinho o dia completo.
- Klines agregadas permitem comparação de volume e OHLC, mas não auditoria trade a trade nem recomposição da metodologia USD do comunicado.
- Próxima coleta: verificar se a janela oficial do claim corresponde a 12:00 UTC; buscar export histórico/arquivo de negócios da Aster Spot ou outra fonte primária com trades completos para explicar a diferença de 2,40%.

**Conclusão:** dado inaugural mais forte obtido até aqui: ASTER Spot 24h de 12:00 UTC 17/09 a 12:00 UTC 18/09 — **379,894660M USDT**, preço de abertura 0.03015 e máxima 0.528. Reportar como cálculo de API Spot com cobertura verificada, e não como confirmação perfeita do claim de US$371M.
