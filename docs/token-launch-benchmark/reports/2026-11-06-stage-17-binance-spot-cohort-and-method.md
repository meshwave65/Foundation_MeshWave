# Etapa 17 — Coorte de comparação consistente via Binance Spot

**Data da pesquisa:** 2026-11-06  
**Status:** seleção de coorte e método de coleta definidos; números de candles ainda não capturados nesta etapa.

## Resultado principal

Para comparação D0/D+7/D+30, usar uma única venue (Binance Spot) e definir D0 pelo início anunciado de negociação Spot, não pelo TGE, airdrop, claim, call auction, Binance Alpha ou primeiro preço global. A coorte recomendada:

| Token | Início Spot Binance (UTC) | Par | D+7 | D+30 |
|---|---|---|---|---|
| MANTA | 2024-01-18 10:00 | MANTA/USDT | 2024-01-25 10:00 | 2024-02-17 10:00 |
| ENA | 2024-04-02 08:00 | ENA/USDT | 2024-04-09 08:00 | 2024-05-02 08:00 |
| OMNI | 2024-04-17 12:00 | OMNI/USDT | 2024-04-24 12:00 | 2024-05-17 12:00 |
| BIO | 2025-01-03 10:00 | BIO/USDT | 2025-01-10 10:00 | 2025-02-02 10:00 |
| BERA | 2025-02-06 13:00 | BERA/USDT | 2025-02-13 13:00 | 2025-03-08 13:00 |

## Fontes primárias e documentação técnica

- Binance MANTA: https://www.binance.com/en/support/announcement/introducing-manta-manta-on-binance-launchpool-farm-manta-by-staking-bnb-and-fdusd-d408406a0b594b2d82206f7ea9ca60bc
- Binance ENA: https://www.binance.com/en/support/announcement/introducing-ethena-ena-on-binance-launchpool-farm-ena-by-staking-bnb-and-fdusd-6c216f219f0e42adb1849759dee3fbd9
- Binance OMNI: https://www.binance.com/en/support/announcement/introducing-omni-network-omni-on-binance-launchpool-farm-omni-by-staking-bnb-and-fdusd-3954d04933da443ab539ca38616013de
- Binance BIO: https://www.binance.com/en/support/announcement/introducing-bio-protocol-bio-on-binance-launchpool-farm-bio-by-locking-bnb-and-fdusd-f4717985d5d549c8adf284ef4fbd9107
- Binance BERA: https://www.binance.com/en/support/announcement/introducing-berachain-bera-on-binance-hodler-airdrops-earn-bera-with-retroactive-bnb-simple-earn-subscriptions-5a3a946a51674cc09132696645b42d79
- Binance Spot REST documentation: https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md
- Binance historical archives documentation: https://github.com/binance/binance-public-data/blob/master/README.md

## Data collection procedure

1. Verify pair/symbol using public exchangeInfo.
2. For exact one-minute checkpoint t (epoch milliseconds), request: GET https://data-api.binance.vision/api/v3/klines?symbol=ENAUSDT&interval=1m&startTime=t&endTime=t+59999&limit=1 (replace symbol and t).
3. Capture OHLC, base volume, quote volume, trade count, taker-buy volumes and returned open time.
4. Obtain official monthly ZIP from Binance Vision and sibling .CHECKSUM; validate checksum. Example: https://data.binance.vision/data/spot/monthly/klines/BERAUSDT/1m/BERAUSDT-1m-2025-02.zip
5. UTC calendar-day volume: interval=1d&timeZone=0. Exact launch-relative 24h volume: aggregate 1,440 minute bars in [t, t+24h). Do not substitute current rolling ticker values.
6. Keep returns close-to-close at same venue and same UTC minute; do not forward-fill missing bars.

## Other candidates and exclusions

- JUP: Binance trading ultimately postponed to 16:00 UTC; other CEXes opened earlier. Usable as Binance-venue sample, not first-market anchor.
- LINEA: Binance Spot start at 16:00 UTC; Binance Alpha traded earlier. Keep Spot and Alpha separate.
- HYPE: native genesis trading is a different venue; official candle API retention is limited to latest 5,000 candles, so it is not a robust historical archive for old checkpoints.
- MON: no Binance Spot listing found in reviewed sources; use another venue only as a separate venue cohort.

## Limitation and next step

This report identifies a comparable cohort and reproducible extraction recipe; it does not claim that OHLCV checkpoints have already been downloaded or calculated. The next report should include raw archive references/checksums and computed D0/D+7/D+30 OHLC plus exact 24-hour volumes. No candle values or performance returns were estimated.
