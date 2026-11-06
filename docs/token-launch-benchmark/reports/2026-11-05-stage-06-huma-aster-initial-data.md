# Relatório parcial — Etapa 06: coleta empírica inicial de HUMA e ASTER

**Data de pesquisa:** 2026-11-05  
**Escopo:** evidência de mercado inaugural para HUMA e ASTER; separar TGE, primeira negociação por venue, métricas de calendário e janela relativa de 24 horas.  
**Status:** levantamento inicial persistido; não constitui dataset consolidado/auditado.

## 1. Objetivo

Iniciar a coleta com dois ativos da lista benchmark, priorizados pela presença de fontes com horário de listagem ou informação inaugural. A etapa documenta evidências disponíveis, esclarece referências conflitantes e indica o que falta extrair de dados primários.

## 2. HUMA — Huma Finance

### 2.1 Evento e supply

Binance anunciou HUMA Launchpool em 22/05/2025 e informou oficialmente que o spot trading começaria em **26/05/2025 às 13:00 UTC**, com pares HUMA/USDT, HUMA/USDC, HUMA/BNB, HUMA/FDUSD e HUMA/TRY. A oferta também informa 1,733,333,333 HUMA de circulação inicial (17,33% do supply máximo de 10 bilhões) e 250 milhões de recompensas Launchpool (2,5%).  
Fonte primária: https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666

### 2.2 Números secundários publicados

A cobertura Odaily previamente localizada informa, para Binance, abertura em US$0,06683, fechamento do primeiro dia em US$0,05936 (-11,2%) e volume D1 de US$310,37M.  
Fonte: https://www.odaily.news/en/post/5204939

Uma segunda série pública de resumo semanal do mercado HUMAUSDT da Binance apresenta para 26/05/2025: open US$0,0100, high US$0,1060, low US$0,0100, close US$0,0669 e volume notional de US$113,15M; para 27/05: open US$0,0669, close US$0,0593 e volume US$69,13M. A mesma página indica 7 sessões com volume total US$326,46M.  
Fonte: https://www.tradervilla.com/public/coin/humausdt/week-summary/week-22-2025

**Divergência crítica:** os valores de “open” publicados não são compatíveis diretamente. O US$0,0100 da série diária parece representar um preço inicial/floor da vela ou um problema de cobertura, enquanto a referência Odaily de US$0,06683 pode corresponder ao primeiro preço de mercado após abertura. O volume de US$310,37M também não coincide com o volume de calendário da série (US$113,15M para 26/05). Não selecionar nenhum valor como definitivo sem trades/candles de API e definição exata da janela.

### 2.3 Resultado HUMA desta etapa

- **TGE/listagem Binance spot:** 26/05/2025 13:00 UTC — confirmado por fonte primária.
- **Mercado inicial conhecido:** Binance spot; par HUMA/USDT e demais pares anunciados.
- **Preço inaugural:** reportado US$0,06683 pela cobertura, mas precisa validar contra primeiro trade.
- **Volume:** não reconciliado; US$310,37M reportado para “primeiro dia” não coincide com calendário/venue summary.
- **D0/D1 relativo de 24h, D7, D30:** ainda não extraídos com metodologia de primeiro trade.

## 3. ASTER — Aster

### 3.1 TGE e mercado inicial

A documentação oficial da Aster informa que o TGE/claim abriu em **17/09/2025** e que o token poderia ser negociado diretamente no Aster Spot após o TGE. O total de tokens liberados para claim na abertura foi 704 milhões (8,8% do supply).  
Fonte primária: https://docs.asterdex.com/usdaster-token/tge

A data de TGE não deve ser confundida com a listagem CEX posterior. A Binance anunciou ASTER spot para 06/10/2025 (horário indicado no anúncio localizado em Kyiv time), e a MEXC anunciou ASTER/USDT para 19/09/2025 03:35 UTC.  
Fontes:
- Binance: https://www.binance.com/en/square/post/33522900091450
- MEXC: https://www.mexc.com/announcements/article/initial-listing-mexc-will-list-aster-aster-in-innovation-zone-with-convert-feature-17827791530065

### 3.2 Métricas de TGE publicadas

Comunicado da Aster distribuído por PRNewswire (19/09/2025) reporta para a janela inaugural de 24h na Aster DEX: abertura de US$0,03015, máxima US$0,528 e US$371M de volume específico do token. O comunicado também menciona volume total da plataforma perto de US$1,5B e TVL de US$1,005B; estas duas métricas não são volume spot do ASTER e devem ficar separadas.  
Fonte de divulgação do projeto: https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561462.html

CoinLore, em sua série histórica diária agregada, registra para 17/09/2025 open US$0,0977, high US$0,4821, low US$0,0844, close US$0,3882 e volume US$225,3M. Para 18/09 registra volume US$414,0M e para 19/09 US$588,8M. Esta série tem agregação própria e não é a mesma janela/venue do comunicado de Aster; não deve substituir o dado de pool/DEX.  
Fonte: https://www.coinlore.com/coin/aster/historical-data/1735689600/1773721248

### 3.3 Resultado ASTER desta etapa

- **TGE:** 17/09/2025 — confirmado pela documentação oficial.
- **Primeiro mercado documentado:** Aster Spot/DEX, conforme projeto; CEXs começaram depois.
- **D0 publicado pelo projeto:** US$0,03015 de abertura e US$371M de volume em 24h, mas fonte é comunicado do projeto, não uma extração independente dos trades.
- **Série agregada:** CoinLore mostra preço de abertura diário muito diferente (US$0,0977) e volume US$225,3M em 17/09; janela UTC/agregação não esclarecidas o bastante para reconciliar.
- **CEX:** MEXC ASTER/USDT em 19/09 03:35 UTC; Binance spot em outubro. Portanto, métricas CEX posteriores não são “abertura TGE”.
- **D0/D1 relativo, D7, D30 independentes:** não calculados ainda.

## 4. Comparação nesta etapa

| Token | Evento de referência | Evidência inaugural mais forte | Estado da métrica |
|---|---|---|---|
| HUMA | Binance spot 26/05/2025 13:00 UTC | anúncio oficial do horário; duas séries secundárias discordantes | timestamp confirmado; preço/volume não reconciliados |
| ASTER | TGE Aster Spot 17/09/2025 | documentação oficial TGE; comunicado do projeto com 24h; série agregada discrepante | data confirmada; preço/volume reportados, ainda não validados independentemente |

## 5. Conclusões

1. Definir a data do TGE/listagem não basta para obter métricas comparáveis. É necessário capturar o primeiro trade e as janelas de 24h que começam naquele instante.
2. HUMA oferece um horário CEX exato, porém há discrepância material entre o relato de abertura/volume e o resumo de candles diários.
3. ASTER exige distinguir a negociação inicial na própria DEX em 17/09 da posterior listagem em exchanges centralizadas. Volume de plataforma e TVL são métricas diferentes do volume do token.
4. Dados secundários serão mantidos como evidência contextual; não preencherão automaticamente os campos primários do benchmark.

## 6. Lacunas / próxima coleta

- Recuperar trades ou candles intradiários específicos da Binance HUMAUSDT a partir de 26/05/2025 13:00 UTC; testar pares adicionais sem somar volumes indevidamente.
- Identificar o mercado/pool inicial de ASTER no Aster Spot (contrato, par, timestamp e fonte on-chain); extrair swaps/trades e calcular 24h exatas.
- Calcular D0, D1, D7 e D30 desde o primeiro trade definido, preservando em paralelo os candles UTC.
- Registrar volume quote (USDT/USD), trades, OHLC, liquidez e método de conversão.
- Fazer validação cruzada com CoinGecko/CMC sem substituir a fonte primária.

## 7. Fontes principais

- Binance HUMA Launchpool/listing (primária): https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666
- Odaily HUMA (secundária): https://www.odaily.news/en/post/5204939
- Trader Villa HUMAUSDT week 22 (resumo de mercado): https://www.tradervilla.com/public/coin/humausdt/week-summary/week-22-2025
- Aster TGE docs (primária): https://docs.asterdex.com/usdaster-token/tge
- Aster/PRNewswire day-one statement (comunicado do projeto): https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561462.html
- CoinLore ASTER historical (agregado): https://www.coinlore.com/coin/aster/historical-data/1735689600/1773721248
- MEXC ASTER listing: https://www.mexc.com/announcements/article/initial-listing-mexc-will-list-aster-aster-in-innovation-zone-with-convert-feature-17827791530065
- Binance ASTER listing: https://www.binance.com/en/square/post/33522900091450

---
**Classificação:** relatório parcial de evidência, não dataset auditado nem recomendação financeira.
