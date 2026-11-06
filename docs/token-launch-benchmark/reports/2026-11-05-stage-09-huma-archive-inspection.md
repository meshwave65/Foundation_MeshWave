# Etapa 09 — HUMA/USDT: validação do arquivo e agregação inaugural (Binance)

**Execução:** 2026-11-06 UTC. **Status:** checksum validado; CSV sem lacunas; primeira hora, janela rolling de 24h e D0 UTC parcial calculados. D7/D30 não estão completos no arquivo de maio.  
**Escopo:** apenas HUMA/USDT Spot na Binance; volumes não representam mercado consolidado entre venues.

## Fonte e integridade
- [ZIP Binance Vision](https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip) (315.539 bytes), um CSV: `HUMAUSDT-1m-2025-05.csv`, 7.860 registros, 1.138.687 bytes, 12 campos/linha, sem cabeçalho.
- [Checksum publicado](https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip.CHECKSUM). SHA-256 calculado: `4b09ada623991c01a4072968b42985738cef277430bf210e69077d409ca397d1`; **correspondência confirmada**.
- Especificação: [Binance Public Data README](https://github.com/binance/binance-public-data). Timestamps Spot de 2025 interpretados em microssegundos UTC.
- Cobertura 2025-05-26 13:00 UTC a 2025-05-31 23:59 UTC; 7.860 velas consecutivas, sem lacunas. Primeira vela coincide com o horário de abertura spot anunciado.

## Convenção
Janelas semiabertas [início, fim). Open = abertura da primeira vela; High/Low = extremos; Close = fechamento da última; volume base HUMA, volume cotado USDT e trade count = somas. D0 é dia civil UTC de 26 mai (00:00–24:00) e é parcial porque o arquivo começa 13:00. Rolling 24h (13:00–13:00 seguinte) é uma métrica diferente.

## Resultados agregados
| Janela UTC | Velas | Open | High | Low | Close | Volume HUMA | Volume USDT | Trades | Estado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Primeiros 60 min: 26 mai 13:00–14:00 | 60 | 0,01000000 | 0,10600000 | 0,01000000 | 0,07355000 | 650.168.504 | 51.666.564,23182 | 244.557 | Completa |
| Primeiras 24h: 26 mai 13:00–27 mai 13:00 | 1.440 | 0,01000000 | 0,10600000 | 0,01000000 | 0,06166000 | 2.200.528.634 | 155.019.454,50601 | 913.794 | Completa |
| D0 calendário: 26 mai 00:00–27 mai 00:00 | 660 observadas (13:00–24:00) | 0,01000000 | 0,10600000 | 0,01000000 | 0,06693000 | 1.538.894.126 | 113.149.865,88865 | 633.257 | Parcial |
| D7 UTC | — | — | — | — | — | — | — | — | Não disponível integralmente no ZIP de maio |
| D30 UTC | — | — | — | — | — | — | — | — | Não disponível neste ZIP |

## Primeira vela (13:00 UTC)
O/H/L/C: 0,01000000 / 0,10600000 / 0,01000000 / 0,08887000 USDT; volume base 63.402.250 HUMA; volume cotado 5.910.044,74637 USDT; 21.473 trades; taker-buy base 31.867.194 HUMA; taker-buy quote 2.988.728,54012 USDT.

Linha CSV:
`1748264400000000,0.01000000,0.10600000,0.01000000,0.08887000,63402250.00000000,1748264459999999,5910044.74637000,21473,31867194.00000000,2988728.54012000,0`

Última vela (31 mai 23:59 UTC): O/H/L/C 0,03701 / 0,03717 / 0,03701 / 0,03715 USDT; base 230.310 HUMA; quote 8.544,1583 USDT; 132 trades.

## Conclusões e ressalvas
1. Binance Vision superou o bloqueio HTTP 451 da REST: o arquivo público foi baixado, extraído, validado e agregado.
2. A primeira hora apresentou 51,67M USDT de giro; primeira janela de 24h, 155,02M USDT. Soma de volume cotado das velas de 1m.
3. D0 civil (parcial) não deve ser comparado sem ressalva a uma janela rolling de 24h nem a outro venue. Divergências de fonte secundária podem ser efeito de período, venue ou definição.
4. High 0,106 é máxima da janela, não preço de abertura. Candles não identificam trade individual, spread ou slippage.
5. Não extrapolar D7/D30: buscar arquivos seguintes. ASTER/LBank deve ser adquirido e reportado separadamente; não misturar venue/volume de protocolo.

## Próxima etapa
- Obter e analisar ASTER/USDT candles históricos na LBank para 17–18/09/2025; validar a cobertura e unidade de volume.
- Identificar a fonte primária do mercado Aster Spot no TGE e recuperar trades/swaps.
- Obter arquivos Binance subsequentes para HUMA D7/D30.
- Consolidar somente após normalizar evento UTC, venue, par/quote, período e qualidade de evidência.

## Fontes
- Binance archive: https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip
- Checksum: https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip.CHECKSUM
- Technical README: https://github.com/binance/binance-public-data
- Official HUMA listing: https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666
- Secondary comparison only: https://www.odaily.news/en/post/5204939

---
**Registro de estado:** checksum e métricas de janelas acima verificados; D7/D30 e ASTER seguem em aberto até aquisição dos dados específicos.
