# Etapa 10 — ASTER/USDT: LBank, correção do evento e candles inaugurais

**Execução:** 2026-11-06 UTC  
**Status:** candles históricos públicos recuperados pela API LBank; janela inaugural de 60 minutos e 24 horas agregada; continuidade temporal sem lacunas; alertas de consistência OHLC registrados.  
**Escopo:** ASTER/USDT Spot na LBank somente. Os números não representam volume global ASTER nem volume da Aster DEX.

## 1. Correção cronológica — anúncio inicial foi adiado

O anúncio inicial da LBank previa ASTER/USDT para **17/09/2025 às 12:30 UTC**, mas a exchange publicou um aviso explícito de adiamento no mesmo dia. Portanto, a data inicialmente anunciada não pode ser usada como início efetivo de negociação.

A LBank publicou posteriormente uma nova listagem indicando abertura em **22/09/2025 às 05:00 UTC**. A API de candles retornou a primeira barra observada exatamente nesse timestamp. Um agregador externo de listagens reporta 04:30 UTC; para este cálculo foi usada a âncora da LBank e o início da série API (05:00 UTC), deixando a diferença de 30 minutos como observação a reconciliar, não como dado resolvido.

Fontes:
- Anúncio inicial: https://www.lbank.com/support/articles/1968250114875064320
- Aviso de adiamento: https://www.lbank.com/support/articles/1968291802968489984
- Anúncio posterior de abertura: https://www.lbank.com/fr/support/articles/1969984335821930496
- Agregador externo com indicação 04:30 UTC: https://listedon.org/en/ticker/ASTER

## 2. API e aquisição

Endpoint público documentado:
`GET https://api.lbank.info/v2/kline.do?symbol=aster_usdt&size=2000&type=minute1&time=1758517200`

- Símbolo: `aster_usdt`
- Tipo: `minute1`
- `time`: 1758517200 (Unix seconds = 2025-09-22 05:00:00 UTC)
- `size`: 2.000 candles retornados
- Cobertura: 2025-09-22 05:00 UTC a 2025-09-23 14:19 UTC.
- Cada linha API contém [timestamp, open, high, low, close, volume]. Não há campo quote-volume nem trade count no payload Kline consultado.
- Documentação: https://www.lbank.info/docs/

O payload contém as 1.440 barras da primeira janela rolling de 24h. Os timestamps avançaram exatamente 60 segundos, sem lacunas na janela analisada.

## 3. Convenção de cálculo e qualidade

Janelas semiabertas [início, fim). Open é o primeiro open; Close é o último close; High/Low são os extremos observados, incluindo open/close de cada barra para não omitir valores extremos. O volume é a soma do campo volume da API, sem convertê-lo em USDT.

**Advertência de qualidade:** os dados brutos contêm candles que violam as relações OHLC convencionais (open/close fora do high-low declarado). Na primeira barra, por exemplo, open=0,7000 enquanto low=1,4518. A barra foi mantida, sinalizada, e os extremos agregados consideram open e close, daí low agregado 0,7000. Não se interpreta o campo Low isoladamente como se a série estivesse livre de anomalias.

## 4. Resultados calculados

| Janela UTC | Candles | Open (USDT) | High | Low agregado incluindo O/C | Close | Volume API | Cobertura |
|---|---:|---:|---:|---:|---:|---:|---|
| Primeiros 60 min: 22 set 05:00–06:00 | 60 | 0,7000 | 1,4866 | 0,7000 | 1,4001 | 772.121,62 | Completa; 1 candle OHLC inconsistente |
| Primeiras 24h: 22 set 05:00–23 set 05:00 | 1.440 | 0,7000 | 1,6571 | 0,7000 | 1,6254 | 30.022.287,03 | Completa; 9 candles OHLC inconsistentes |
| D0 calendário UTC: 22 set 00:00–24:00 | 1.140 observadas (05:00–24:00) | 0,7000 | 1,6571 | 0,7000 | 1,6366 | 26.652.692,51 | Parcial; 8 candles OHLC inconsistentes |
| D7 / D30 | — | — | — | — | — | — | Não calculados nesta etapa |

A API não entrega quote-volume (USDT) nem trade count no formato Kline retornado; portanto, o volume acima não é apresentado como giro em USDT. Para calcular turnover cotado e quantidade de negócios, será necessário um feed de trades com histórico suficiente ou outra fonte verificável.

### Primeira candle retornada (22/09/2025 05:00 UTC)

`[1758517200, 0.7, 1.465, 1.4518, 1.4538, 41744.09]`

Campos na ordem documentada: timestamp, open, high, low, close, volume. O open de 0,7 é inferior ao low publicado (1,4518), indicando anomalia na barra.

## 5. Interpretação — sem mistura de venues

1. A evidência inicial de 17/09 era um anúncio programado, depois adiado; não é a data real de abertura da LBank.
2. A série LBank observada começa em 22/09 às 05:00 UTC, consistente com a listagem posterior da própria exchange. A diferença frente ao agregador externo que indica 04:30 UTC permanece registrada.
3. A janela rolling de 24h apresenta 30,02 milhões de unidades no campo Volume da API, mas não se pode converter esse número em USDT sem quote-volume verificável.
4. O preço inicial de 0,7000 USDT derivado da primeira barra deve ser tratado com cuidado, dado o erro OHLC na primeira barra e outras inconsistências observadas. É o open reportado na API, não prova independente do primeiro trade.
5. Estes dados são da LBank Spot. Não são comparáveis diretamente ao volume de US$371M auto-reportado pela Aster DEX no primeiro dia do TGE (17/09) porque venue, evento e janela temporal diferem. A listagem LBank ocorreu cinco dias depois.
6. Para medir TGE ASTER em 17/09, a linha prioritária segue sendo recuperar trades/swaps do Aster Spot on-chain desde a abertura efetiva, e não usar a série LBank de 22/09 como substituto.

## 6. Atualização dos relatórios anteriores

- Etapa 07: a frase sobre LBank ativa no dia TGE foi corrigida para refletir anúncio inicial, adiamento e abertura posterior em 22/09.
- Etapa 08: a rota de coleta LBank foi atualizada com a aquisição real da série e a nova cronologia.
- A cronologia ASTER passa a distinguir TGE/Spot da Aster em 17/09 de ASTER/USDT Spot na LBank em 22/09.

## 7. Próxima etapa

- Recuperar a série on-chain da Aster Spot para o TGE em 17/09/2025: identificar contrato/pool e trades/swaps oficiais, horário de abertura e cálculo independente da cifra de US$371M.
- Para LBank, buscar fonte de trades com quoteQty e trade count para reconciliar os candles Kline e as anomalias.
- Manter D7/D30 ASTER por venue como campos em aberto até recuperação dos dados completos.
- Corrigir e consolidar o comparativo HUMA/ASTER somente após harmonizar evento, venue, intervalo, unidade de volume e qualidade.

## 8. Fontes técnicas e cronológicas

- LBank API docs: https://www.lbank.info/docs/
- LBank Kline endpoint: https://api.lbank.info/v2/kline.do?symbol=aster_usdt&size=2000&type=minute1&time=1758517200
- LBank initial announcement: https://www.lbank.com/support/articles/1968250114875064320
- LBank delay notice: https://www.lbank.com/support/articles/1968291802968489984
- LBank later ASTER listing notice: https://www.lbank.com/fr/support/articles/1969984335821930496
- External listing time cross-check: https://listedon.org/en/ticker/ASTER
- Aster TGE docs: https://docs.asterdex.com/usdaster-token/tge
- Project day-one volume release (project-sourced): https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561462.html

---
**Persistência:** etapa de LBank registrada com cronologia corrigida, 60m/24h/D0 quantitativos e qualidade do dado explícita. Aster Spot TGE on-chain e quote-volume LBank continuam pendentes.
