# Etapa 19 — Volume de mercado em janelas rolling de 24h, 7d e 30d

**Coorte:** MANTA, ENA, OMNI, BIO e BERA — Binance Spot, pares USDT  
**Data de coleta:** 2026-11-06  
**Status:** concluída para as janelas ancoradas no horário de lançamento adotado na Etapa 17.  
**Unidade:** quote volume em USDT e base volume em tokens.

## 1. Método

Para cada ativo, foram somados candles oficiais de 1 minuto dentro de janelas rolling com início inclusivo e fim exclusivo:

- 24 horas: 1.440 candles;
- 7 dias: 10.080 candles;
- 30 dias: 43.200 candles.

A filtragem usa o timestamp de abertura do candle: `open_time >= start` e `open_time < end`. Base volume e quote volume são somados separadamente. A verificação confirmou exatamente o número esperado de timestamps únicos em todas as 15 janelas primárias, sem duplicatas ou candles ausentes.

As somas vêm dos campos de volume das Binance Spot klines arquivadas (campos CSV de volume-base e volume-quote, equivalentes aos campos 5 e 7 da resposta REST). Os 15 arquivos mensais necessários foram baixados e os checksums oficiais `.CHECKSUM` foram validados.

## 2. Resultados — janelas a partir do lançamento

| Token | Janela | UTC início (inclusivo) | UTC fim (exclusivo) | Candles | Quote volume (USDT) | Base volume |
|---|---|---|---|---:|---:|---:|
| MANTA | 24h | 2024-01-18 10:00 | 2024-01-19 10:00 | 1.440/1.440 | 619,376,700.734257 | 274,833,738.700000 |
| MANTA | 7d | 2024-01-18 10:00 | 2024-01-25 10:00 | 10.080/10.080 | 2,030,066,560.325919 | 822,339,516.300000 |
| MANTA | 30d | 2024-01-18 10:00 | 2024-02-17 10:00 | 43.200/43.200 | 4,464,984,152.307641 | 1,607,490,993.000000 |
| ENA | 24h | 2024-04-02 08:00 | 2024-04-03 08:00 | 1.440/1.440 | 1,344,020,075.772550 | 1,883,531,184.070000 |
| ENA | 7d | 2024-04-02 08:00 | 2024-04-09 08:00 | 10.080/10.080 | 5,418,194,458.988800 | 5,587,817,270.490000 |
| ENA | 30d | 2024-04-02 08:00 | 2024-05-02 08:00 | 43.200/43.200 | 12,682,625,163.155830 | 12,335,817,745.030000 |
| OMNI | 24h | 2024-04-17 12:00 | 2024-04-18 12:00 | 1.440/1.440 | 389,231,375.364500 | 11,633,786.800000 |
| OMNI | 7d | 2024-04-17 12:00 | 2024-04-24 12:00 | 10.080/10.080 | 680,373,938.069400 | 23,029,308.770000 |
| OMNI | 30d | 2024-04-17 12:00 | 2024-05-17 12:00 | 43.200/43.200 | 1,079,472,650.714600 | 44,503,900.750000 |
| BIO | 24h | 2025-01-03 10:00 | 2025-01-04 10:00 | 1.440/1.440 | 716,762,667.059610 | 892,495,738.700000 |
| BIO | 7d | 2025-01-03 10:00 | 2025-01-10 10:00 | 10.080/10.080 | 1,464,127,099.656450 | 2,017,293,604.000000 |
| BIO | 30d | 2025-01-03 10:00 | 2025-02-02 10:00 | 43.200/43.200 | 2,295,091,910.187170 | 4,629,208,209.200000 |
| BERA | 24h | 2025-02-06 13:00 | 2025-02-07 13:00 | 1.440/1.440 | 1,007,414,048.168778 | 104,713,369.981000 |
| BERA | 7d | 2025-02-06 13:00 | 2025-02-13 13:00 | 10.080/10.080 | 1,525,678,423.452275 | 188,826,396.629000 |
| BERA | 30d | 2025-02-06 13:00 | 2025-03-08 13:00 | 43.200/43.200 | 3,030,613,947.164876 | 397,316,982.952000 |

## 3. Leituras comparativas

| Janela desde o lançamento | Maior quote volume da amostra | Volume USDT |
|---|---|---:|
| 24h | ENA | 1,344,020,075.772550 |
| 7d | ENA | 5,418,194,458.988800 |
| 30d | ENA | 12,682,625,163.155830 |

ENA lidera o giro reportado nesta coorte Binance Spot nos três períodos. BIO e BERA também registram giro expressivo, mas a comparação isolada de volume não demonstra liquidez efetiva nem profundidade de livro. O número deve ser lido como volume transacionado na venue e janela observadas.

## 4. Evidência, arquivos e verificabilidade

Fonte oficial: [Binance Public Data repository](https://github.com/binance/binance-public-data) e arquivos mensais de klines Spot.

Arquivos mensais principais consultados (os períodos podem atravessar meses; os arquivos auxiliares correspondentes também foram usados):

- [MANTAUSDT 1m — Jan/2024](https://data.binance.vision/data/spot/monthly/klines/MANTAUSDT/1m/MANTAUSDT-1m-2024-01.zip)
- [ENAUSDT 1m — Abr/2024](https://data.binance.vision/data/spot/monthly/klines/ENAUSDT/1m/ENAUSDT-1m-2024-04.zip)
- [OMNIUSDT 1m — Abr/2024](https://data.binance.vision/data/spot/monthly/klines/OMNIUSDT/1m/OMNIUSDT-1m-2024-04.zip)
- [BIOUSDT 1m — Jan/2025](https://data.binance.vision/data/spot/monthly/klines/BIOUSDT/1m/BIOUSDT-1m-2025-01.zip)
- [BERAUSDT 1m — Fev/2025](https://data.binance.vision/data/spot/monthly/klines/BERAUSDT/1m/BERAUSDT-1m-2025-02.zip)

Archives adicionais utilizados para cobrir janelas de 30 dias que atravessam meses:
- MANTAUSDT: Fev e Mar/2024;
- ENAUSDT: Mai e Jun/2024;
- OMNIUSDT: Mai e Jun/2024;
- BIOUSDT: Fev e Mar/2025;
- BERAUSDT: Mar e Abr/2025.

Todos os 15 arquivos envolvidos foram validados contra os arquivos de checksum oficiais. A metodologia e os arquivos são públicos e replicáveis. O relatório HTML e o JSON de verificação foram produzidos na execução de pesquisa; os valores e a lógica de validação essenciais estão transcritos aqui.

## 5. Distinções e limitações

- **Volume de mercado** não é valor de venda pública, capital captado, treasury inflow ou receita do emissor.
- **Volume** não equivale a liquidez disponível: book depth, spread, slippage e market-making são métricas distintas.
- Volume de token/protocolo ou TVL não deve ser misturado com quote volume do par Spot USDT.
- Os números se referem à Binance Spot. Não são volume global de todas as exchanges.
- A janela é rolling desde o timestamp de lançamento adotado, não um dia UTC inteiro nem a métrica genérica “volume do primeiro dia”.
- A amostra de cinco tokens é exploratória; não deve ser tratada como distribuição representativa de todos os lançamentos.

## 6. Próxima análise

Combinar os volumes rolling desta etapa com retornos D0/D+7/D+30 da Etapa 18 e, em seguida, ampliar a amostra com uma regra de inclusão uniforme. Só depois fazer inferências sobre o padrão de lançamento; manter separado o desenho econômico proposto para MWN.
