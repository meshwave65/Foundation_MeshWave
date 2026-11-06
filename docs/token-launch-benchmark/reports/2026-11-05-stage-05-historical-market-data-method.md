# Relatório parcial — Etapa 05: método de coleta de OHLCV histórico

**Data:** 2026-11-05  
**Projeto:** benchmark externo de lançamentos de tokens para orientar estudos futuros de MWN  
**Status:** metodologia técnica preliminar; coleta quantitativa por ativo ainda não iniciada/concluída.

## 1. Objetivo da etapa

Definir uma estratégia reproduzível para recuperar preços e volumes de mercado nos períodos D0, D1, D7 e D30 dos tokens estudados, evitando comparar métricas de mercados diferentes como se fossem equivalentes.

Esta etapa NÃO determina preço, valuation, volume-alvo ou estratégia de lançamento de MWN.

## 2. Fontes técnicas avaliadas

### 2.1 Binance Spot — candles e arquivos públicos

A API Spot da Binance oferece candles (klines) identificados pelo horário de abertura, com parâmetros de símbolo, intervalo, startTime, endTime e limite. O endpoint documentado é `/api/v3/klines`; timestamps e janelas podem ser alinhados em UTC. A Binance também mantém repositório de dados públicos agregados em arquivos diários/mensais, incluindo candles e trades agregados.

Referências:
- API Spot oficial: https://developers.binance.com/en/docs/products/spot/rest-api
- Repositório de dados públicos: https://github.com/binance/binance-public-data

**Uso recomendado:** coletar candles do par específico da exchange, desde a listagem efetiva. Não tratar o candle diário UTC como “primeiro dia de negociação” se a listagem ocorreu durante o dia: preservar também candles intradiários quando disponíveis.

### 2.2 CoinGecko — série histórica agregada e dados on-chain

CoinGecko documenta dados históricos de mercado e endpoints OHLC/OHLCV, inclusive para tokens e pools on-chain via GeckoTerminal. A cobertura e granularidade dependem do plano e da disponibilidade histórica do ativo; as informações públicas do provedor descrevem histórico diário/horário em planos, e maior granularidade em planos específicos.

Referências:
- API e histórico: https://www.coingecko.com/en/api/
- Dados OHLC: https://www.coingecko.com/en/api/ohlc-data
- OHLCV on-chain e pool: https://www.coingecko.com/learn/how-to-pull-crypto-prices-from-dexs

**Uso recomendado:** fonte complementar para visão agregada ou pool DEX identificada. Não usar agregação como substituto automático do primeiro trade de uma venue.

### 2.3 CoinMarketCap — OHLCV histórico

A documentação do CMC apresenta endpoint de OHLCV histórico com intervalos diário e horário. A disponibilidade e os limites são dependentes do plano. Os candles diários representam períodos UTC; a fonte pode não oferecer granularidade suficiente para definir o primeiro preço negociado em uma listagem intradiária.

Referência:
- https://coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency

**Uso recomendado:** verificação independente e contexto agregado, não evidência única para preço inaugural.

## 3. Definições operacionais

Para cada token, manter mercados e referências separados:

- **Primeiro trade:** primeira negociação verificável no mercado/venue especificado; não equivale necessariamente ao “open” de um agregador.
- **Open D0:** abertura do candle UTC da data do TGE; pode anteceder ou suceder a primeira listagem, dependendo da convenção de data.
- **D0 relativo ao primeiro trade:** intervalo de 24 horas desde o primeiro trade confirmado.
- **D1:** segundo intervalo de 24 horas, imediatamente após D0 relativo ao primeiro trade.
- **D7 e D30:** métricas calculadas em janelas de 24h nos dias relativos 7 e 30, além de manter OHLCV acumulado quando a fonte permitir.
- **Volume spot:** volume do par/mercado à vista. Preferir volume em ativo de cotação (quote volume, por exemplo USD/USDT) e documentar conversões.
- **Derivativos:** coluna separada; nunca somar automaticamente com spot.
- **Pool DEX:** registrar pool, rede, endereço do contrato, par e liquidez; volume de pool não deve ser somado a agregadores que possam duplicar os mesmos trades.
- **Captação de venda:** métrica primária distinta de volume de mercado secundário.
- **TVL/liquidez:** snapshots independentes do giro negociado.

## 4. Grade mínima por ativo e mercado

| Campo | Requisito |
|---|---|
| Token / contrato | Identificador inequívoco, ticker e contrato quando aplicável |
| Evento | TGE, airdrop, sale, primeira listagem ou abertura de pool |
| Timestamp inicial | UTC e URL que sustente o timestamp |
| Venue / mercado | Exchange ou DEX, par e tipo (spot/perp/pool) |
| Primeiro trade | Preço, timestamp e origem verificável; se ausente, marcar não confirmado |
| D0 / D1 | OHLCV em janelas definidas; explicitar se calendário UTC ou 24h relativo |
| D7 / D30 | OHLCV e volume com a mesma convenção da série anterior |
| Liquidez | Snapshot separado, timestamp e métrica (depth, reservas ou liquidez reportada) |
| Supply / valuation | Circulante, unlocks, market cap e FDV com timestamp e fonte |
| Evidência | URL, tipo de fonte, data de consulta e nível de confiança |
| Lacunas | Campos ausentes, discrepâncias e justificativa |

## 5. Procedimento de coleta

1. Fixar, para cada caso, data e hora do TGE/primeira negociação em UTC com fonte documental.
2. Identificar venues realmente negociadas no início; não escolher retrospectivamente apenas a venue com maior volume.
3. Buscar candles/trades específicos por venue e par; validar o primeiro registro contra a listagem e a fonte do evento.
4. Calcular janelas D0/D1/D7/D30 com a convenção declarada; manter também calendário UTC para permitir auditoria.
5. Separar spot, perpétuos, pool DEX, sale proceeds e métricas de protocolo.
6. Confrontar com agregadores e fontes jornalísticas; explicar divergências em vez de fundir números incompatíveis.
7. Atribuir confiança: **A** (dados primários/trades ou API oficial e janela clara), **B** (dados de venue/provedor com documentação parcial), **C** (reportagem secundária sem método integral), **D** (estimativa ou referência ambígua).
8. Persistir por etapa: dataset/grade, fontes, método, conclusões, ressalvas e próximo passo em relatório parcial separado.

## 6. Limitações encontradas

- O acesso a séries históricas, granularidade e cobertura varia entre APIs, planos e ativos.
- Candles diários podem ocultar o primeiro preço, pico e volatilidade das primeiras horas.
- Pares em USDT, USD e outros ativos de cotação não são diretamente comparáveis sem conversão temporal explícita.
- Tokens lançados inicialmente em DEX podem ter primeiro preço observável numa pool específica, antes de listagens CEX.
- Volume de agregador, volume de venue, derivativos, volume de protocolo e pool podem se sobrepor ou representar objetos diferentes.
- O documento de reconciliação existente contém números preliminares secundários; eles não serão tratados como série auditada nem completados por inferência.

## 7. Conclusão desta etapa

Há fontes técnicas adequadas para estruturar a coleta histórica, mas a coleta confiável exige definição token a token do mercado inicial e de seu timestamp. A estratégia é usar dados primários por venue/pool como núcleo, e agregadores como checagem. O relatório não apresenta valores numéricos novos de D0/D1/D7/D30, pois ainda não foram extraídos e reconciliados em uma base comparável.

## 8. Próxima etapa proposta

Construir a primeira tabela empírica por ativo, começando pelos casos com evidência mais ancorada em venue e horário (HUMA e ASTER), depois os casos DEX/pool (JUP e MET), e então MON, BERA, LINEA, KAITO e HYPE. Cada resultado e lacuna será persistido em novo relatório parcial antes de avançar.

## Referências consultadas

- Binance Spot REST API: https://developers.binance.com/en/docs/products/spot/rest-api
- Binance public market data: https://github.com/binance/binance-public-data
- CoinGecko API: https://www.coingecko.com/en/api/
- CoinGecko OHLC: https://www.coingecko.com/en/api/ohlc-data
- CoinGecko on-chain OHLCV: https://www.coingecko.com/learn/how-to-pull-crypto-prices-from-dexs
- CoinMarketCap OHLCV historical: https://coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency
- Documento-base de reconciliação: ../reconciliation-inaugural-metrics.md

---
**Natureza:** relatório técnico de pesquisa. Não é recomendação financeira, auditoria, nem aprovação de parâmetros de lançamento MWN.
