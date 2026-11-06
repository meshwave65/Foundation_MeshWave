# Relatório parcial — Etapa 08: rota de aquisição histórica e APIs de mercado

**Data:** 2026-11-05  
**Escopo:** especificar caminhos verificáveis para aquisição de dados históricos de HUMA (Binance Spot) e ASTER (LBank Spot), após o bloqueio geográfico da API Binance na tentativa anterior.  
**Status:** método e endpoints documentados; arquivos brutos ainda não baixados nem processados. Não é dataset empírico consolidado.

## 1. Objetivo

A etapa 07 deixou claro que não foi possível obter candles diretamente da Binance REST API no ambiente atual (HTTP 451). Esta etapa documenta fontes alternativas e um plano tecnicamente executável de aquisição, evitando afirmar extração concluída antes de ter os arquivos e seus checksums.

## 2. HUMA — Binance Vision

### 2.1 Fonte de arquivo primária

O repositório oficial `binance/binance-public-data` informa que a Binance Data Collection distribui dados públicos Spot em arquivos diários e mensais. Os arquivos de klines são derivados do endpoint `/api/v3/klines`; cada ZIP possui um arquivo `.CHECKSUM` para integridade. Spot a partir de 01/01/2025 utiliza timestamps em microssegundos.

Fonte:
- https://github.com/binance/binance-public-data

Padrão oficial de arquivo mensal:
```
https://data.binance.vision/data/spot/monthly/klines/{SYMBOL}/{INTERVAL}/{SYMBOL}-{INTERVAL}-YYYY-MM.zip
```

Arquivo a testar para a janela de lançamento:
```
https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip
https://data.binance.vision/data/spot/monthly/klines/HUMAUSDT/1m/HUMAUSDT-1m-2025-05.zip.CHECKSUM
```

Este caminho é especificado a partir do padrão publicado; **não afirmamos que o arquivo HUMAUSDT específico foi baixado ou validado**. Próximo procedimento:
1. baixar ZIP e CHECKSUM;
2. validar SHA-256 conforme instrução oficial;
3. importar CSV com timestamp em microssegundos;
4. filtrar desde 26/05/2025 13:00 UTC;
5. separar candle diário UTC de janelas relativas desde o primeiro trade definido;
6. manter OHLC, base volume, quote volume, trade count e taker volumes.

A listagem oficial da Binance define 26/05/2025 13:00 UTC como o início do spot HUMA; esse timestamp é âncora de evento, não necessariamente substituto do timestamp do primeiro trade efetivamente gravado.

## 3. ASTER — LBank Spot

### 3.1 Documentação de API pública

A documentação oficial LBank declara que market-data APIs são públicas e incluem dados históricos. Ela documenta:
- `GET /v2/kline.do` — candles por par, intervalo, tamanho e timestamp (segundos);
- `GET /v2/supplement/trades.do` — trades recentes, com `symbol`, `size` e `time`; retorna price, qty, quoteQty, trade ID, timestamp e isBuyerMaker.

Fonte:
- https://www.lbank.info/docs/

A documentação expõe candles com OHLC e volume, mas o endpoint K-line documentado recebe um timestamp em segundos e um tamanho de 1–2000 barras. A API de trades descrita é de registros recentes, portanto não se assume que ela, isoladamente, permita paginação arbitrária até setembro de 2025.

### 3.2 Listagem ASTER na LBank

Anúncio de listagem registrado na etapa 07: ASTER/USDT trading em 17/09/2025 12:30 UTC. A janela inicial de análise LBank será alinhada ao horário do anúncio, mas preço inicial calculado só após recuperar candle/trade histórico verificável.

Fonte:
- https://www.lbank.com/support/articles/1968250114875064320

## 4. Evidência disponível e limite de execução

| Mercado | Fonte | Método | Estado |
|---|---|---|---|
| HUMAUSDT Spot | Binance Vision archive | ZIP mensal de klines 1m + SHA-256; timestamps µs em 2025 | caminho documentado; arquivo ainda não baixado/validado |
| ASTER/USDT Spot | LBank public market API | kline endpoint; histórico de trades conforme disponibilidade e janela do endpoint | documentação localizada; candles/trades não extraídos |
| ASTER Aster Spot | Documentação/projeto + venue data ainda por localizar | determinar API/contrato/pool e recuperar swaps/trades | pendente; números do comunicado permanecem auto-reportados |

Não foram calculados OHLCV, volume quote, D0/D1/D7/D30 ou preços de first trade nesta etapa. O próximo passo técnico requer um canal que permita baixar ZIP público e/ou solicitar API histórica, seguido de cálculo local e registro dos dados brutos ou de seus hashes e fontes.

## 5. Conclusões

1. O HTTP 451 da Binance REST não significa que o arquivo histórico público inexista; Binance publica o padrão de arquivos públicos e checksum.
2. Para HUMA, arquivo mensal Spot de maio de 2025 deve cobrir o evento, mas precisa ser baixado e validado antes de qualquer número calculado.
3. Para ASTER/LBank, API pública documentada é uma rota promissora para candles; a cobertura histórica e parâmetros reais precisam ser testados. Não se assume que o endpoint de trades recentes permita obter todo o histórico de TGE.
4. A fonte para o mercado inicial da própria Aster Spot continua pendente; não é substituível por dados de CEX posterior nem por volume total do protocolo.

## 6. Próxima etapa

- adquirir o ZIP HUMAUSDT maio/2025 e verificar o checksum;
- recuperar LBank ASTER/USDT candles para 17–18/09/2025 e testar disponibilidade de janela histórica;
- identificar a API ou o pool de ASTER Spot e recuperar os swaps;
- só após isso consolidar comparativo por venue e janela.

## 7. Fontes

- Binance Public Data — especificação de arquivos, colunas, timestamps e checksums: https://github.com/binance/binance-public-data
- Binance Data Collection: https://data.binance.vision/
- LBank API docs: https://www.lbank.info/docs/
- LBank ASTER listing announcement: https://www.lbank.com/support/articles/1968250114875064320
- Binance HUMA launch announcement: https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666

---
**Classificação:** relatório de método e aquisição; não há extração bruta nem resultado quantitativo validado nesta etapa.
