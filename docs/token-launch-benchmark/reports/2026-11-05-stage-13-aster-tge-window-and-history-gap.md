# Etapa 13 — ASTER: definição da janela de TGE e lacuna histórica da API

**Data:** 2026-11-05  
**Status:** verificação da janela de lançamento concluída; API Spot não possui dados pré-12:00 UTC no período testado.  
**Escopo:** ASTERUSDT na Aster Spot; somente endpoints públicos, leitura.

## 1. Conclusão cronológica — distinguir claim TGE de início de trading

A expressão “TGE” foi usada para mais de um marco no rollout:
- **Claim do airdrop:** documentação oficial de orientação informa abertura em **17/09/2025 às 09:00 UTC**. [Aster — How to claim your airdrop](https://docs.asterdex.com/usdaster-token/tge/how-to-claim-your-airdrop)
- **Negociação ASTER Spot:** primeira candle oficial pública abre em **17/09/2025 às 12:00:00 UTC**; o primeiro aggregate trade tem timestamp **12:00:00.019 UTC**, preço 0.03015 e ID 1. [Aster Spot API V3 market data](https://asterdex.github.io/aster-api-website/spot-v3/market-data/)
- O horário de claim é oficial; a associação do início do mercado à hora de 12:00 UTC é corroborada pela API e por um relato de anúncio de lançamento. [PANews schedule report](https://www.panews.io/articles/b01c005c-5794-4b15-81d2-78aff59038b6)

A página oficial TGE marca a data de claim 17/09, mas seu texto indica que o horário exato seria divulgado posteriormente. A documentação de claim é a fonte que estabelece 09:00 UTC. [Aster TGE page](https://docs.asterdex.com/usdaster-token/tge)

## 2. Teste histórico antes do início Spot

Foram consultadas seis janelas contíguas de candles 1m, cada uma de 6 horas, abrangendo 2025-09-16 00:00 UTC até 2025-09-17 12:00 UTC. **Todas retornaram arrays vazios.** A consulta de aggregate trades antes do corte também retornou vazia.

O campo de metadados listingTime=1758012731852 (= 2025-09-16 08:52:11.852 UTC) é anterior ao início do mercado observado, mas não prova existência de trades: não há candle/trade retornado para esse intervalo.

Primeira candle:
- timestamp: 2025-09-17 12:00:00.000 UTC
- OHLC: 0.03015 / 0.08990 / 0.03015 / 0.06897
- volume base: 2,996,183.85 ASTER
- volume quote: 218,450.73132 USDT
- trades: 538

Primeiro aggregate trade:
- ID a=1
- timestamp: 2025-09-17 12:00:00.019 UTC
- preço 0.03015, quantidade 3,973.33 ASTER
- paginação fromId confirmada: páginas iniciaram em IDs 1, 1001 e 2001, limite 1.000.

## 3. Interpretação da declaração de US$371 milhões

O comunicado da Aster afirma “within the first 24 hours of its TGE”, com volume de **US$371M**, preço de abertura de US$0.03015 e máxima de US$0.528. Não define timezone nem timestamp inicial/final. [PR Newswire release](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html)

A janela de negociação mais bem apoiada pelo conjunto de dados é **17/09/2025 12:00 UTC → 18/09/2025 12:00 UTC**: começa no primeiro trade Spot registrado e cobre 24 horas contínuas. A soma de quote volume de candles para essa janela dá **379,894660M USDT**. É uma inferência sobre a janela de volume, não um limite explicitamente declarado no release.

A discrepância de aproximadamente **2,40%** contra US$371M permanece não reconciliada. Não inferir causa (conversão USD/USDT, metodologia on-chain, janela, arredondamento etc.) sem evidência. Preço inicial e máxima coincidem com a declaração do projeto, mas isso não torna o volume uma reprodução exata.

## 4. Fontes e URLs de evidência

- [Aster exchangeInfo](https://sapi.asterdex.com/api/v3/exchangeInfo)
- [Klines 1m — janela pré-TGE (amostra 6h)](https://sapi.asterdex.com/api/v3/klines?symbol=ASTERUSDT&interval=1m&startTime=1758002400000&endTime=1758023999999&limit=1000)
- [Klines 1m — primeira janela com dados](https://sapi.asterdex.com/api/v3/klines?symbol=ASTERUSDT&interval=1m&startTime=1758110400000&endTime=1758131999999&limit=1000)
- [Aggregate trades — consulta pré-cutoff](https://sapi.asterdex.com/api/v3/aggTrades?symbol=ASTERUSDT&startTime=1758002400000&endTime=1758023999999&limit=1000)
- [Aggregate trade ID 1, primeira página](https://sapi.asterdex.com/api/v3/aggTrades?symbol=ASTERUSDT&fromId=1&limit=1000)
- [Aggregate trades próxima página](https://sapi.asterdex.com/api/v3/aggTrades?symbol=ASTERUSDT&fromId=1001&limit=1000)
- [Documentação Spot V3](https://asterdex.github.io/aster-api-website/spot-v3/market-data/)
- [Aster TGE docs](https://docs.asterdex.com/usdaster-token/tge)
- [Guia oficial do claim](https://docs.asterdex.com/usdaster-token/tge/how-to-claim-your-airdrop)
- [Relato do cronograma de trading](https://www.panews.io/articles/b01c005c-5794-4b15-81d2-78aff59038b6)
- [Release de US$371M](https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330000-new-users-302561462.html)

## 5. Efeito sobre os registros anteriores

Esta etapa complementa a Etapa 12. A janela usada em seu cálculo (12:00 UTC a 12:00 UTC do dia seguinte) é agora sustentada como a janela contínua do primeiro dia de negociação Spot, pois:
1. primeiro candle abre às 12:00:00 UTC;
2. primeiro aggregate trade ocorre às 12:00:00.019 UTC;
3. API não apresenta candles nem aggregate trades no período anterior testado;
4. claim de airdrop começou às 09:00 UTC, mas é um evento distinto da abertura do livro Spot.

Ainda assim, o claim de US$371M permanece uma cifra do projeto com janela e metodologia não explicitadas; portanto, não classificar como reproduzida exata.
