# Benchmark de lançamentos de tokens — MeshWave / MWN

**Status:** documentação de referência em evolução. **Versão inicial:** 2026-11-05.  
**Objetivo:** estudar lançamentos externos e converter aprendizados em drafts próprios para MWN. Estes documentos não são recomendação de investimento nem anunciam parâmetros aprovados da MeshWave.

## Como ler os dados
- **Preço de venda** (sale/IDO) não é necessariamente o preço de abertura do mercado.
- **Preço inicial** depende da venue e do instante de medição; picos intraday não devem ser chamados de preço de abertura.
- **Volume negociado** é giro secundário reportado; não equivale a capital captado.
- **Liquidez inicial** (reserva de pool/market depth) é distinta de volume negociado e TVL.
- FDV (fully diluted valuation) não é market cap circulante.
- Cada métrica deve carregar período, venue, moeda de cotação, fonte e qualidade (primária/secundária/estimada).
- Ausência de fonte pública será marcada como **não confirmado**, sem completar por inferência.

## Casos da amostra
| Projeto | Evento / estrutura | Métrica de referência inicial | Observação |
|---|---|---|---|
| [MON — Monad](./cases/MON.md) | Venda pública via Coinbase + distribuição | venda pública a $0,025; preço de mercado e volume inicial pendentes de reconciliação | Separar proceeds da venda e giro de mercado |
| [PUMP — Pump.fun](./cases/PUMP.md) | Venda pública | sale price $0,004; $500M captados em 12 min (não é volume secundário) | Grande venda e alta demanda inicial |
| [BERA — Berachain](./cases/BERA.md) | Airdrop + CEX | volume diário >$2B no lançamento, segundo Arrakis; FDV de abertura reportado $4,3B | Premium em relação à valuation da rodada; queda posterior |
| [LINEA](./cases/LINEA.md) | TGE + listagem | pico reportado $0,046; volume de negociação ~$418M em primeiro dia | Preço/pico não confundir com abertura |
| [ASTER](./cases/ASTER.md) | Lançamento DEX | fontes divergem sobre preço de abertura ($0,03015 vs cerca de $0,08) | PR do projeto versus cobertura secundária; validar |
| [JUP — Jupiter](./cases/JUP.md) | Airdrop + pool DEX | pool inicial citado a $0,40; 1,35B tokens (13,5%) circulantes no lançamento | Volume de plataforma Jupiter não é volume do token |
| [HYPE — Hyperliquid](./cases/HYPE.md) | Airdrop | abertura perto de $2; 310M tokens (31%) distribuídos; cotação perto de $9,80 em 1 dez 2024 | Movimento de preço não é volume |
| [KAITO](./cases/KAITO.md) | TGE / distribuição | dados de preço/volume inaugural a consolidar | Caso para estudar estrutura de distribuição e desempenho posterior |
| [HUMA — Huma Finance](./cases/HUMA.md) | Launchpool + listagem | abertura reportada $0,06683; volume do primeiro dia $310,37M | Dados de fonte secundária, validar venue e janela |
| [MET — Meteora](./cases/MET.md) | LGE + distribuição em LP | pool MET/USDC aberto a $0,50 (FDV indicada $500M) | Dados de relatório do projeto; volume inicial não confirmado |

## Pesquisa aprofundada complementar
- [Pesquisa ampliada 2024–2026](./research-expanded-2024-2026.md): evidências adicionais para FJO, PRCL, DRIFT, GRASS, PUFFER, VVV, NIL, ZORA, PUMP e GRAIL; inclui qualidade da evidência, distinções métricas e critérios de comparação. Este é um conjunto complementar — não substitui a lista inicial de casos.
- [Relatório externo completo](https://agent.tinyfish.ai/research/01a1ae29-fc3d-7fc4-9265-b65ab92af524): execução de pesquisa com fontes e ressalvas.

## Relatórios agregados
- [Memento Research — State of 2025 Token Launches](https://mementoresearch.com/reports/state-of-2025-token-launches-year-in-review): 118 lançamentos observados; 84,7% abaixo da valuation TGE em 20 dez 2025. Universo/metodologia próprios.
- [CoinGecko — Q2 2024 Crypto Industry Report](https://www.coingecko.com/research/publications/2024-q2-crypto-report): dados agregados sobre baixo float e FDV.
- [Arrakis — Lessons From H1 2025's Top Token Launches](https://arrakis.finance/blog/lessons-from-h1-2025-top-token-launches): BERA e volumes.
- [Unitypad — What Is a TGE?](https://unitypad.org/learn/what-is-a-tge/): exemplos de estrutura TGE 2024–25.
- [CryptoRank — Inside Successful TGEs](https://cryptorank.io/insights/analytics/inside-successful-tges-2024-2025): seleção baseada em volume e liquidez on-chain.

## Drafts MeshWave
Os textos em [drafts](./drafts/README.md) são esqueletos editáveis e **não aprovados para publicação**. Valores econômicos, tokenomics, claims, datas, exchange, liquidez, elegibilidade, riscos e aspectos legais permanecem como campos a validar.

## Próxima revisão
Completar dados comparáveis por caso: TGE UTC, preço inicial por venue, liquidez efetivamente provisionada, volume token-specific 24h/7d/30d, preço e volume em D+7/D+30, unlocks, fonte e confiança. Registrar metodologia e captura da fonte.

## Reconciliação de métricas
- [Reconciliação preliminar D0/D1 e protocolo de coleta](./reconciliation-inaugural-metrics.md): separa fontes de preços, volumes de token, volume de protocolo, captação e métricas de liquidez; explicita divergências e lacunas antes de criar uma tabela comparável.

## Relatórios parciais por etapa
Os relatórios são cumulativos por etapa e não substituem os arquivos de caso nem os drafts.

- [01 — Escopo e seleção inicial dos casos](./reports/2026-11-05-stage-01-benchmark-scope-and-case-selection.md): objetivo do benchmark externo, amostra inicial e estrutura documental.
- [02 — Pesquisa ampliada e lições de mercado](./reports/2026-11-05-stage-02-expanded-research-and-market-lessons.md): casos complementares, tendências agregadas, conclusões e limitações.
- [03 — Preparação dos drafts MWN](./reports/2026-11-05-stage-03-mwn-draft-materials.md): artefatos criados e guardrails para não inventar parâmetros de lançamento.
- [04 — Reconciliação preliminar das métricas inaugurais](./reports/2026-11-05-stage-reconciliation-inaugural-metrics.md): evidências por token, definições, lacunas e próxima coleta quantitativa.
- [05 — Método de coleta de OHLCV histórico](./reports/2026-11-05-stage-05-historical-market-data-method.md): fontes técnicas avaliadas, convenções de janelas, campos necessários, procedimento e limitações.


- [06 — Coleta empírica inicial: HUMA e ASTER](./reports/2026-11-05-stage-06-huma-aster-initial-data.md): eventos e horários, números publicados, discrepâncias entre fontes, conclusões e campos ainda não validados.
