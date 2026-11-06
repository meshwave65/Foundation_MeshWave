# Etapa 11 — ASTER TGE: reconciliação quantitativa pela API Spot oficial da Aster

**Execução:** 2026-11-06 UTC  
**Status:** série pública oficial recuperada e agregada para 60m, D0 UTC parcial, D1 UTC, janela rolling 24h, D7 e D30. Continuidade validada; nenhum gap nem candle OHLC inconsistente nas janelas examinadas.  
**Escopo:** mercado ASTER/USDT Spot da própria Aster (API de mercado), não LBank, não volume global multi-venue e não prova de swaps on-chain.

## 1. Evento e horário

A documentação oficial Aster confirma o TGE/claim de ASTER em 17/09/2025 e a negociação na Aster Spot após a distribuição. Cobertura contemporânea informa trading às 20:00 UTC+8, que equivale a **12:00 UTC**. A primeira candle do endpoint oficial `ASTERUSDT` começa exatamente às 12:00 UTC e abre a **0,03015 USDT**, correspondendo ao preço de abertura citado pelo projeto.

- TGE docs: https://docs.asterdex.com/usdaster-token/tge
- Horário de trading reportado como 20:00 UTC+8: https://www.gate.com/de/blog/12297/aster-aster-token-has-been-listed-for-trading-on-aster-spot
- API metadata: https://sapi.asterdex.com/api/v1/exchangeInfo
- A API metadata lista o símbolo antes do TGE; `listingTime` do cadastro do par não deve ser confundido com a primeira negociação. Para o evento usamos a primeira candle e o horário de abertura corroborado.

## 2. Fonte e método

API pública oficial Spot:
- Host: `https://sapi.asterdex.com`
- Endpoint: `GET /api/v1/klines`
- Símbolo: `ASTERUSDT`
- Intervalos usados: `1m` para primeira hora, D0 parcial e rolling 24h; `1h` para D1 UTC, D7 e D30.
- Referência de especificação: [Aster Spot API V1 (legacy), documentação oficial do endpoint público consultado](https://github.com/asterdex/api-docs/blob/master/V1%28Legacy%29/EN/aster-finance-spot-api.md).

O schema oficial retorna open time, OHLC, volume-base, close time, quote-asset volume, trade count, taker-buy base/quote e campo de controle. Portanto, o quote-volume é somado diretamente em USDT; não foi estimado multiplicando preço por volume-base.

### Janelas e qualidade
- Âncora do evento: 2025-09-17 12:00:00 UTC.
- Janela 24h: [2025-09-17 12:00, 2025-09-18 12:00) UTC, 1.440 candles de 1 minuto.
- D7: [2025-09-17 12:00, 2025-09-24 12:00) UTC, 168 candles de 1 hora.
- D30: [2025-09-17 12:00, 2025-10-17 12:00) UTC, 720 candles de 1 hora.
- Candles foram filtradas em intervalos semiabertos [início, fim). OHLC = primeiro open, máximo high, mínimo low, último close. Volumes e trades são somas.
- Nenhuma lacuna de 1 minuto na primeira hora/24h; nenhuma lacuna horária em D7/D30; nenhum candle com open/close fora da faixa high-low nas janelas examinadas.
- API retorna volume-base ASTER e volume cotado USDT separadamente.

## 3. Resultados calculados

| Janela | Barras | Open (USDT) | High | Low | Close | Volume ASTER (base) | Volume USDT (quote) | Trades |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Primeira hora: 17 set 12:00–13:00 UTC | 60 × 1m | 0,03015 | 0,08990 | 0,03015 | 0,07130 | 91.430.298,71 | 6.947.477,92737 | 13.289 |
| D0 calendário: 17 set 12:00–24:00 UTC (parcial) | 720 × 1m | 0,03015 | 0,48700 | 0,03015 | 0,40182 | 1.024.842.943,38 | 226.232.883,15400 | 278.191 |
| Primeiras 24h rolling: 17 set 12:00–18 set 12:00 UTC | 1.440 × 1m | 0,03015 | 0,52800 | 0,03015 | 0,44550 | 1.374.581.953,34 | 379.894.660,36485 | 460.041 |
| D1 calendário: 18 set 00:00–24:00 UTC | 24 × 1h | 0,40171 | 0,79000 | 0,37000 | 0,61274 | 759.934.637,26 | 410.868.936,74480 | 422.680 |
| D7 rolling: 17 set 12:00–24 set 12:00 UTC | 168 × 1h | 0,03015 | 2,42830 | 0,03015 | 2,27317 | 3.957.813.104,42 | 3.523.536.657,80201 | 5.861.544 |
| D30 rolling: 17 set 12:00–17 out 12:00 UTC | 720 × 1h | 0,03015 | 2,42830 | 0,03015 | 1,07766 | 6.842.771.604,40 | 8.465.046.217,27698 | 12.735.759 |

### Primeira candle do TGE

`[1758110400000,"0.03015","0.08990","0.03015","0.06897","2996183.85",1758110459999,"218450.73132",538,"1538055.32","126041.55037","0"]`

Timestamp Unix ms: 2025-09-17 12:00:00 UTC. A abertura da primeira candle corresponde a US$0,03015. A máxima 0,08990 e fechamento 0,06897 pertencem à mesma primeira vela de 1 minuto.

## 4. Reconciliação com a publicação do projeto

A Aster publicou via PRNewswire:
- abertura: US$0,03015;
- máxima do primeiro dia: US$0,528;
- volume reportado: US$371 milhões.

Fonte: https://www.prnewswire.co.uk/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561466.html

Confronto com API Spot oficial, janela exata de 24h desde 12:00 UTC:
- **Open US$0,03015 — coincide**.
- **High US$0,528 — coincide**.
- **Quote-volume API US$379.894.660,36**, cerca de **US$8.894.660,36 (+2,40%)** acima dos US$371M divulgados.
- API registra 460.041 trades e 1,3746B ASTER de volume-base.

A correspondência de open/high é forte evidência de que a API oficial captura o mercado ASTER Spot do TGE. A diferença de volume, porém, não deve ser apagada nem chamada de erro sem prova: pode refletir corte temporal, regra de cálculo ou metodologia on-chain usada no comunicado. O valor da API é quote-volume agregado de candles da Spot; o release descreve volume segundo dados on-chain. São conceitos que precisam ser reconciliados antes de rotular ambos como a mesma métrica.

O valor secundário próximo de US$0,08 pode representar uma cotação intrahora: a primeira hora teve high de US$0,08990. Não é a abertura observada na primeira candle.

## 5. Conclusões

1. A janela correta do TGE para a série pública Aster Spot é 17/09/2025 12:00 UTC (20:00 UTC+8), não 20:00 UTC. A primeira candle começa no horário convertido e seu open coincide com US$0,03015.
2. O preço inicial e a máxima de US$0,528 citados pelo projeto são reproduzidos na API oficial. A divergência de “~US$0,08 como abertura” parece resultar de usar um valor intrahora ou fonte/definição diferente; permanece como discrepância secundária.
3. O quote-volume oficial Spot de 24h calculado é US$379,895M, enquanto o release reporta US$371M. Diferença aproximada de 2,40%; registrar ambos com suas metodologias.
4. D7 e D30 passam a ter resultados calculados por candles de 1h da mesma API Spot. Esses valores são venue-specific e não volume consolidado de todas as exchanges.
5. A API Spot pública não equivale, por si só, a uma reconstrução de swaps on-chain. Para auditar o claim “on-chain” do release, uma fonte de blockchain/trades independente continua sendo uma etapa separada.
6. A listagem inicialmente programada pela LBank para 17/09 foi adiada; sua série começa em 22/09 e deve permanecer separada deste TGE.

## 6. Próxima etapa

- Comparar a API Spot oficial com dados independentes on-chain ou trades agregados, para explicar o delta de volume de ~2,40% no primeiro dia.
- Atualizar ASTER case study e o quadro comparativo geral com estes valores, mantendo fonte, venue, janela, quote asset e qualidade.
- Não somar a série LBank de 22/09 ao primeiro dia ASTER TGE de 17/09.

## 7. Fontes e reprodução

- Aster Spot API docs: https://github.com/asterdex/api-docs/blob/master/V3%28Recommended%29/EN/aster-finance-spot-api-v3.md
- Public exchange metadata: https://sapi.asterdex.com/api/v1/exchangeInfo
- Public 1m kline API (TGE start): `https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1m&startTime=1758110400000&endTime=1758196800000&limit=1000` (recovery paginated; use half-open interval).
- Public 1h kline API (D7/D30): `https://sapi.asterdex.com/api/v1/klines?symbol=ASTERUSDT&interval=1h&startTime=1758110400000&endTime=1760702400000&limit=1000`.
- Aster TGE docs: https://docs.asterdex.com/usdaster-token/tge
- Aster project release (PRNewswire): https://www.prnewswire.co.uk/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561466.html
- Time-zone cross-check: https://www.gate.com/de/blog/12297/aster-aster-token-has-been-listed-for-trading-on-aster-spot
- Aster Spot launch report: https://www.chaincatcher.com/en/article/2206344

---
**Persistência:** relatório de mercado oficial Spot ASTER do TGE registrado com janela inicial, D0/D1/D7/D30, volumes base/quote e reconciliação contra o release do projeto. A diferença de volume está documentada, não normalizada por inferência.
