# Etapa 16 — Expansão da amostra: seleção de tokens e trilha de validação

**Data da pesquisa:** 2026-11-06  
**Status:** triagem documental concluída; coleta de OHLCV por candles ainda não validada nesta etapa.

## Objetivo

Ampliar a comparação para além de HUMA e ASTER sem misturar eventos distintos: lançamento de token/TGE, abertura de negociação em uma exchange, primeiro candle disponível, D+7 e D+30. As etapas anteriores mostram que a hora efetiva de abertura e a venue são determinantes.

## Candidatos priorizados

| Ativo | Evento spot documentado | Venue e par | Hora UTC documentada | Evidência |
|---|---|---|---|---|
| JUP | Binance anuncia abertura em 31 jan 2024 | Binance Spot, JUP/USDT (também FDUSD, TRY) | 15:30 | Anúncio oficial Binance: https://www.binance.com/en/support/announcement/detail/7b5c643c3d8a4c9a9d443b1ceefb0015 |
| BERA | Spot trading começa 6 fev 2025; há call auction antes | OKX Spot, BERA/USDT | 13:00 (call auction 12:00–13:00) | Anúncio oficial OKX: https://www.okx.com/en-eu/help/okx-to-list-bera-berachain-for-spot-trading |
| LINEA | Spot trading começa 10 set 2025; call auction antes | OKX Spot, LINEA/USDT | 15:00 (call auction 14:00–15:00) | Anúncio oficial OKX: https://www.okx.com/pt-br/help/okx-to-list-linea-linea-for-spot-trading-and-convert-pre-market-futures-to |

### Fontes adicionais de confirmação cruzada

- KuCoin anuncia JUP/USDT às 15:00 UTC de 31 jan 2024: https://www.kucoin.com/announcement/en-jupiter-jup-gets-listed-on-kucoin-world-premiere
- KuCoin anuncia BERA/USDT às 13:00 UTC de 6 fev 2025: https://www.kucoin.com/announcement/id-berachain-bera-gets-listed-on-kucoin-world-premiere
- KuCoin anuncia LINEA/USDT às 15:00 UTC de 10 set 2025: https://www.kucoin.com/announcement/my-linea-linea-gets-listed-on-kucoin-world-premiere
- MEXC documenta LINEA/USDT às 14:26 UTC (abertura antecipada em relação a várias exchanges): https://www.mexc.com/announcements/article/initial-listing-mexc-will-list-linea-linea-in-innovation-zone-with-convert-feature-17827791529907

## Observações metodológicas

1. A hora de negociação inicial é específica da exchange. Não tratar o primeiro preço da Binance como preço universal do token.
2. Para LINEA, a existência de listagens às 14:26 UTC (MEXC) e às 15:00 UTC (OKX/KuCoin) torna inadequado um único “D0 global” sem convenção.
3. Para BERA, distinguir negociação Spot de futures/perpetuals e respeitar a call auction.
4. JUP possui mercado DEX/Solana e múltiplas listagens CEX; volume do agregador Jupiter/protocolo não equivale a volume do token JUP.
5. A seleção aqui é uma triagem de fontes de lançamento, não uma validação de candles, volumes ou retornos.

## Limitação desta etapa

A coleta de candles e os cálculos D0/D+7/D+30 por API não foram concluídos. A sessão de navegação automatizada que poderia consultar endpoints públicos não ficou disponível por limite de créditos; as tentativas de abrir endpoints REST diretamente no mecanismo de busca também não forneceram os payloads. Nenhum OHLCV foi estimado ou inventado.

## Próximo procedimento quantitativo

- Selecionar uma venue primária por caso (JUP: Binance Spot; BERA: OKX Spot; LINEA: OKX Spot, com MEXC como comparação de hora de abertura).
- Obter candles de 1 minuto na hora anunciada e nos checkpoints exatos +7 e +30 dias, em UTC.
- Obter agregados diários UTC e janela móvel de 24h separadamente.
- Registrar OHLC, base volume, quote volume, número de trades, endpoint, parâmetros e eventual lacuna de candles.
- Comparar retorno close-to-close apenas na mesma venue e mesma hora; separar volume spot de volume de derivativos, protocolo e pool DEX.

## Conclusão

A triagem estabelece três candidatos e suas fontes primárias de hora de abertura. Ainda não permite conclusões quantitativas de volume, retorno ou “sucesso” do lançamento. Esses resultados só devem ser acrescentados após capturar e verificar dados brutos de mercado.

