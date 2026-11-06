# Etapa 09 — Inspeção do arquivo bruto HUMA/USDT (Binance)

**Data:** 2026-11-05  
**Status:** arquivo extraído e estrutura verificada; cálculos de janelas agregadas e checksum criptográfico ainda pendentes.  
**Escopo:** validar conteúdo do arquivo mensal de candles de 1 minuto para HUMA/USDT; não representa volume global de HUMA em todas as venues.

## Fonte primária e arquivo

- Arquivo: [HUMAUSDT-1m-2025-05.zip](https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip)
- Dataset de Binance Public Data: [README técnico](https://github.com/binance/binance-public-data)
- Tamanho do ZIP informado na extração browser: 315.539 bytes.
- Conteúdo: um CSV, `HUMAUSDT-1m-2025-05.csv`, 7.860 linhas de dados, 1.138.687 bytes; sem cabeçalho literal.
- Campo de timestamp em microsegundos, convenção Spot documentada para 2025.
- A primeira linha da série está em 2025-05-26 13:00:00 UTC, que coincide com o horário oficial de abertura Spot da Binance para HUMA.
- Última linha disponível no arquivo: 2025-05-31 23:59:00 UTC. O arquivo mensal contém, portanto, somente o trecho posterior à listagem de maio, não o mês completo.

## Estrutura CSV (12 campos)

Open time, open, high, low, close, base asset volume, close time, quote asset volume, number of trades, taker-buy base volume, taker-buy quote volume, ignore.

## Primeira vela de um minuto

Timestamp: 2025-05-26 13:00:00 UTC.

| Métrica | Valor |
|---|---:|
| Open | 0,01000000 USDT |
| High | 0,10600000 USDT |
| Low | 0,01000000 USDT |
| Close | 0,08887000 USDT |
| Volume base | 63.402.250 HUMA |
| Volume cotado | 5.910.044,74637 USDT |
| Número de negócios | 21.473 |
| Taker buy base | 31.867.194 HUMA |
| Taker buy quote | 2.988.728,54012 USDT |

A vela revela uma amplitude muito grande no primeiro minuto. O high da vela não deve ser apresentado como preço de abertura; o volume-base não deve ser confundido com giro em USDT.

## Última vela disponível

2025-05-31 23:59:00 UTC: open 0,03701; high 0,03717; low 0,03701; close 0,03715 USDT; base volume 230.310 HUMA; quote volume 8.544,1583 USDT; 132 negócios.

## Interpretação e limites

1. A série primária da Binance foi recuperada e o CSV lido; esta etapa supera a barreira anterior do HTTP 451 da API REST, usando o arquivo público histórico.
2. A evidência é específica de HUMA/USDT na Binance. Não é o volume de mercado consolidado.
3. O ZIP e o CSV foram extraídos e inspecionados no browser. Ainda não foi possível confirmar o SHA-256 do arquivo contra o arquivo `.CHECKSUM` no ambiente local.
4. A linha inicial é a vela da listagem (13:00 UTC), não o registro de cada trade individual. Para preço do primeiro negócio exato e slippage/ordem do livro, serão necessárias fontes de trades/book.
5. As métricas agregadas de primeira hora, D0, D1, D7 e D30 ainda não foram calculadas neste relatório. Não inferir resultados a partir da primeira vela.

## Próxima etapa

- Obter os bytes do ZIP e checksum no ambiente de cálculo, validar integridade e reproduzir as 7.860 linhas.
- Agregar janelas fixas a partir de 13:00 UTC e janelas de calendário UTC explicitamente separadas; reportar OHLC, volume base, volume quote e trade count.
- Em paralelo, obter candles/trades de ASTER na LBank e manter volumes por venue e período segregados.

## Evidência bruta citada

Primeira linha do CSV:
`1748264400000000,0.01000000,0.10600000,0.01000000,0.08887000,63402250.00000000,1748264459999999,5910044.74637000,21473,31867194.00000000,2988728.54012000,0`

Última linha:
`1748735940000000,0.03701000,0.03717000,0.03701000,0.03715000,230310.00000000,1748735999999999,8544.15830000,132,199886.00000000,7414.10778000,0`
