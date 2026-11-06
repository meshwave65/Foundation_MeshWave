# Relatório parcial — Etapa de reconciliação de métricas inaugurais

**Projeto:** benchmark de lançamentos de criptoativos externos para orientar, em etapa posterior, os drafts de lançamento MWN  
**Data:** 2026-11-05  
**Etapa:** reconciliação preliminar de preço, volume e liquidez de lançamento  
**Status:** persistido como relatório parcial; pesquisa não encerrada  
**Escopo:** MON, BERA, LINEA, ASTER, JUP, HYPE, KAITO, HUMA e MET

## 1. Objetivo desta etapa

Estabelecer uma base de evidências para comparar lançamentos de tokens de terceiros. O foco é identificar quais números são efetivamente comparáveis — preço inicial, volume D0/D1 e liquidez — e quais reportagens misturam conceitos, venues ou períodos.

Este levantamento **não** pretende investigar o preço de venda ou os parâmetros próprios do MWN, nem aprovar tokenomics, preço, exchange, liquidez ou data de lançamento da MeshWave. Os casos externos servem como benchmark.

## 2. Problema metodológico identificado

“Preço de lançamento” e “volume de lançamento” não são métricas únicas sem contexto. Cada observação deve identificar:

- ativo/token e contrato, quando disponível;
- venue/exchange e par de negociação;
- timestamp em UTC e janela medida;
- primeiro trade, preço de abertura, média, máxima ou fechamento — sem tratar esses campos como equivalentes;
- volume spot do próprio token, com derivativos separados;
- fonte, método de agregação e nível de confiança.

As distinções obrigatórias são:

1. Preço de venda pública/IDO ≠ primeiro preço de mercado.
2. Primeiro trade ≠ máxima intraday.
3. Captação/proceeds ≠ volume secundário negociado.
4. Volume de protocolo/agregador ≠ volume do token nativo.
5. TVL, reserva de pool ou liquidez de order book ≠ volume negociado.
6. Spot ≠ derivativos.
7. FDV ≠ market cap circulante.
8. Métricas de diferentes venues ou janelas não devem ser combinadas como se fossem uma observação homogênea.

## 3. Achados registrados

### BERA — Berachain

Arrakis reporta volume diário superior a US$ 2 bilhões em torno do lançamento, média de US$ 442,4 milhões/dia nos primeiros 30 dias e média de US$ 91,9 milhões/dia em maio de 2025. É uma referência útil de escala e trajetória, mas o recorte ainda não está normalizado por exchange, par e janela UTC. Outra fonte apresenta um “launch price” de US$ 8,16, o que não deve ser assumido como primeiro trade sem esclarecer definição e mercado.

**Conclusão provisória:** usar como estudo de volume reportado, não como benchmark normalizado de abertura.

### ASTER

A análise da MEXC reporta abertura de US$ 0,03015, máxima D1 de US$ 0,528 (+1.650%) e volume spot D1 acima de US$ 342 milhões; spot combinado com derivativos chega perto de US$ 1,5 bilhão. A TVL de aproximadamente US$ 1,005 bilhão não é volume. Os dados são de fonte ligada a exchange e precisam ser rotulados como tal.

**Conclusão provisória:** caso relevante de volatilidade e volume, desde que spot e derivativos fiquem em campos separados.

### JUP — Jupiter

The Block cita US$ 0,40 como preço inicial da pool nativa. CoinDesk menciona perpétuo pré-mercado em Aevo a US$ 0,65. São mercados/referências diferentes. A atividade de US$ 1,38 bilhão reportada para o agregador Jupiter é volume do produto, não volume negociado do token JUP.

**Conclusão provisória:** conservar os dois preços com seus contextos, sem declarar um único “opening price” consolidado.

### MON — Monad

A venda pública a US$ 0,025 é preço de venda. Os proceeds da venda não devem ser lançados como volume secundário. O preço inicial de mercado e o volume comparável D0/D1 ainda precisam de fonte e janela consistentes.

**Conclusão provisória:** registrar venda e mercado em métricas distintas.

### LINEA

Há referências de preço inicial perto de US$ 0,03 e volumes D1 divergentes — cerca de US$ 418 milhões versus mais de US$ 800 milhões. A divergência não foi resolvida por venue, par ou intervalo de 24 horas.

**Conclusão provisória:** manter como dado não reconciliado; não selecionar arbitrariamente uma cifra.

### HUMA — Huma Finance

Odaily associa a abertura de US$ 0,06683, fechamento do primeiro dia em US$ 0,05936 (-11,2%) e volume D1 de US$ 310,37 milhões à negociação iniciada na Binance às 13:00 UTC de 26/05/2025. A referência tem melhor ancoragem temporal/venue do que estimativas genéricas, mas continua sendo cobertura secundária.

**Conclusão provisória:** evidência útil provisória para o caso, a confirmar com candles/trades da venue.

### KAITO

CMC Reflexivity Research relata preço perto de US$ 0,90 no dia do lançamento, máxima de US$ 2,03 no dia seguinte e volume superior a US$ 1 bilhão na primeira semana. CoinLore publica um “launch price” de US$ 1,60. A diferença evidencia que o termo pode designar momentos/mercados distintos. Ainda falta uma série normalizada D0/D1 por venue.

**Conclusão provisória:** não combinar preço do CMC e CoinLore sem identificar timestamp, venue e definição.

### MET — Meteora

O valor de US$ 0,50 e FDV indicada de US$ 500 milhões correspondem à referência da pool/LGE. Isso não comprova preço de abertura consolidado de mercado. Volume inaugural comparável não foi confirmado.

**Conclusão provisória:** tratar como referência de pool/LGE, com volume em aberto.

### HYPE — Hyperliquid

As fontes compiladas até aqui não permitem definir preço e volume consolidados D0/D1 sob uma metodologia homogênea.

**Conclusão provisória:** lacuna explícita; não preencher por inferência.

## 4. Grade de dados para a etapa de coleta quantitativa

Para cada ativo, coletar e guardar separadamente:

- timestamp do primeiro trade em UTC;
- venue e par;
- preço do primeiro trade e, se disponível, preço de abertura da janela;
- OHLCV da janela D0 (primeiras 24 horas), D1 (24–48 horas), D7 e D30;
- volume spot token-specific;
- volume de derivativos em coluna separada;
- snapshots de liquidez de pool/order book;
- circulating float, unlocks e FDV nos mesmos timestamps;
- URL e tipo da fonte;
- método, observações e confiança.

**Regra:** quando uma fonte não disponibilizar o dado ou não permitir reconstruir a janela, registrar “não confirmado” e descrever a lacuna. Não estimar silenciosamente.

## 5. Fontes de evidência atualmente registradas

- Arrakis — BERA e lançamentos H1 2025: https://arrakis.finance/blog/lessons-from-h1-2025-top-token-launches
- MEXC — análise ASTER: https://blog.mexc.com/token-reviews/aster-token-price-surge-analysis-ecosystem-outlook/
- The Block — Jupiter: https://www.theblock.co/news/ecosystems/2024-02-01-jupiter-daily-volume-record-jup-airdrop-275531
- CoinDesk — JUP, oferta circulante e perpétuo pré-mercado: https://www.coindesk.com/markets/2024/01/31/solana-dex-jupiters-jup-token-to-debut-with-135b-circulating-supply
- CMC Reflexivity Research — KAITO: https://coinmarketcap.com/academy/article/reflexivity-research-february-2025-in-review
- Odaily — HUMA: https://www.odaily.news/en/post/5204939
- Phemex — MON e venda: https://phemex.com/blogs/monad-price-prediction-2025-presale-mainnet
- The Defiant — LINEA: https://thedefiant.io/news/blockchains/linea-token-launches-at-usd500-million-market-capitalization
- Coinpedia — HUMA: https://markets.coinpedia.org/huma-finance/
- Blockworks — MET LGE: https://blockworks.com/news/meteora-met

A pesquisa ampliada e o relatório externo também estão relacionados no README do benchmark:
- Pesquisa ampliada: `research-expanded-2024-2026.md`
- Relatório externo: https://agent.tinyfish.ai/research/01a1ae29-fc3d-7fc4-9265-b65ab92af524

## 6. Conclusões desta etapa

1. A documentação atual é um **ledger de evidências preliminares**, não uma base auditada de OHLCV.
2. Alguns casos têm dados úteis, mas não comparáveis de forma direta por diferenças de definição, venue e janela.
3. Nenhum número conflitante deve ser resolvido por preferência subjetiva; precisa de reconciliação com dados de mercado e timestamps.
4. O benchmark deve manter separadas métricas de venda, mercado spot, derivativos, liquidez e atividade de protocolo.
5. Os resultados externos não autorizam concluir qual preço, volume ou estrutura MWN deverá adotar.

## 7. Limitações e pendências

- Falta reconstruir séries D0/D1/D7/D30 em UTC para todos os casos.
- Falta confirmar contratos e pares de negociação para cada venue.
- Algumas fontes são secundárias, afiliadas a exchanges ou autorrelatos de protocolo.
- As cifras divergentes de LINEA, ASTER, KAITO e BERA permanecem com ressalvas.
- O escopo ainda não define um conjunto final de comparáveis para o futuro lançamento MWN.

## 8. Próxima etapa proposta

**Coleta quantitativa de histórico de mercado**, escolhendo fontes e venues por ativo e reconstruindo as janelas D0, D1, D7 e D30, com dados spot e derivativos segregados. O resultado deve ser um relatório parcial novo, acompanhado de tabelas de observações e trilha de fontes; somente depois disso avançar para síntese comparativa.

## 9. Persistência e continuidade

Este documento é um relatório parcial autônomo. Cada etapa subsequente deverá gerar seu próprio relatório detalhado no repositório, e o índice do benchmark deverá apontá-lo. O relatório anterior não será substituído: a evolução ficará registrada por arquivos e commits sucessivos.

**Aviso:** material de pesquisa; não é recomendação de investimento nem publicação promocional aprovada.
