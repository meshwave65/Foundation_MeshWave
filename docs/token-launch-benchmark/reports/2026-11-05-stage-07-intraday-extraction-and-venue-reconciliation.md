# Relatório parcial — Etapa 07: extração intradiária e reconciliação de venues (HUMA / ASTER)

**Data:** 2026-11-05  
**Escopo:** avanço da coleta primária de preços e volume inaugural, identificação dos mercados efetivamente ativos no início de ASTER e validação do caminho técnico para candles históricos Binance.  
**Status:** evidência ampliada; extração bruta ainda bloqueada/incompleta. Não é dataset auditado.

## 1. Objetivo e método

Dar continuidade à etapa 06, priorizando:
- HUMA: validar o primeiro trade e os candles 1m do mercado Binance Spot HUMAUSDT a partir do horário oficial de listagem;
- ASTER: reconciliar a narrativa de “Aster DEX exclusiva” com venues centralizadas que possam ter aberto no mesmo dia;
- distinguir timestamp TGE, horário de negociação, primeiro trade observável, preço de abertura por venue, volume de token e volume de plataforma.

A pesquisa mantém a regra de não converter métricas publicadas por projetos ou agregadores em dados primários sem validar venue, período e definição.

## 2. HUMA — acesso a dados primários

### 2.1 Referência oficial e endpoint

Binance informa o início do spot HUMA em 26/05/2025 às 13:00 UTC. A documentação de Binance Public Data confirma que os arquivos de klines spot são derivados do endpoint `/api/v3/klines`, que as séries são disponibilizadas em arquivos diários/mensais e que, desde 01/01/2025, timestamps spot estão em microssegundos nos arquivos públicos.

Fontes:
- https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666
- https://github.com/binance/binance-public-data

### 2.2 Tentativa técnica desta etapa

Foi feita tentativa de obter a janela de candles 1m do par HUMAUSDT via REST, a partir do instante oficial de listagem. O serviço de extração retornou **HTTP 451** para a requisição direta. A resposta não forneceu candles nem dados de trades.

**Resultado:** não extraímos OHLCV bruto nesta etapa. Isso não comprova ausência de dados históricos no arquivo público Binance Vision; apenas registra que o endpoint API não foi acessível por esse canal de execução.

### 2.3 Consequência para o benchmark

Os valores secundários registrados na etapa 06 (preço inicial reportado e volumes divergentes) continuam contextuais. Não se confirma:
- preço do primeiro trade exato;
- OHLCV da janela inicial de 60 minutos;
- volume da primeira janela exata de 24h desde o primeiro trade;
- D+7 e D+30 relativos.

A próxima tentativa deve preferir o arquivo público mensal/dia de Binance Vision (ZIP de klines ou trades), verificar checksum e calcular as janelas em UTC com timestamps normalizados. Os arquivos Spot 2025+ devem ser tratados com cuidado quanto à precisão temporal (microssegundos).

## 3. ASTER — reconciliação de venues na data TGE

### 3.1 TGE e comunicado do projeto

A documentação oficial do projeto registra TGE/claim em 17/09/2025 e negociabilidade no Aster Spot após o TGE. Um comunicado da Aster distribuído via PRNewswire afirma que, nas primeiras 24h, o ASTER teve abertura a US$0,03015, máxima a US$0,528 e volume do token de US$371M; o mesmo texto descreve Aster DEX como venue exclusiva naquele período. Esses números são alegações publicadas pelo projeto e ainda não foram reproduzidos de trades/swap data independente.

Fontes:
- https://docs.asterdex.com/usdaster-token/tge
- https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561462.html

### 3.2 Evidência de CEX ativa no próprio dia

LBank inicialmente anunciou ASTER/USDT Spot para 17/09/2025 às 12:30 UTC, com depósitos desde 11:00 UTC, mas publicou um aviso explícito de adiamento no próprio dia. A listagem foi anunciada novamente para 22/09/2025 às 05:00 UTC, e a API pública de candles apresenta a primeira barra nesse horário. A série histórica extraída na Etapa 10 começa nessa data, não no dia do TGE.

Fontes:
- Anúncio inicial: https://www.lbank.com/support/articles/1968250114875064320
- Aviso de adiamento: https://www.lbank.com/support/articles/1968291802968489984
- Anúncio posterior: https://www.lbank.com/fr/support/articles/1969984335821930496
- Relatório quantitativo: ./2026-11-05-stage-10-aster-lbank-historical-candles.md

**Correção de interpretação:** o anúncio de 17/09 era uma programação que foi adiada, não evidência de CEX efetivamente ativa no dia do TGE. A afirmação de exclusividade de Aster Spot nas primeiras 24h permanece a ser verificada com swaps/trades on-chain independentes; não deve ser contestada usando a série LBank que começa cinco dias depois.

### 3.3 ASTER DEX on-chain versus pools externos

As buscas identificaram pools ASTER/USDT em PancakeSwap V3 criados em 20/09/2025 e pools Uniswap V3 reportados a partir de 19/09/2025. Esses dados não identificam o mercado inicial Aster Spot de 17/09 e não podem substituir seu registro de trades. Contrato de token BNB Chain citado por fontes públicas: `0x000ae314e2a2172a039b26378814c252734f556a`; endereço de token deve ser confirmado contra documentação oficial antes de qualquer uso analítico.

Fontes exploratórias:
- https://dexpaprika.com/bsc/pool/0x7e58f160b5b77b8b24cd9900c09a3e730215ac47
- https://www.lbank.com/support/articles/1968250114875064320

## 4. Evidência atualizada — quadro

| Ativo | Evento / venue | Informação confirmada ou publicada | Estado |
|---|---|---|---|
| HUMA | Binance Spot | Listagem oficial em 26/05/2025 13:00 UTC; endpoint histórico testado retornou HTTP 451 no canal de pesquisa | horário confirmado; série bruta pendente |
| ASTER | Aster TGE / Spot | TGE 17/09/2025; projeto publicou $0,03015 open, $0,528 high, $371M em 24h | dados divulgados pelo projeto, ainda não reproduzidos |
| ASTER | LBank Spot ASTER/USDT | Anúncio inicial 17/09 foi adiado; listagem posterior anunciada e primeira candle observada a partir de 22/09/2025 05:00 UTC | não constitui CEX ativa no TGE; volume da LBank separado (Etapa 10) |
| ASTER | PancakeSwap V3 ASTER/USDT | pool público conhecido criado em 20/09/2025 | posterior ao TGE; não serve como primeira venue |

## 5. Conclusões da etapa

1. HUMA: o caminho de API direta não entregou dados; é necessário usar o arquivo público histórico ou outro canal que permita obter e verificar o dataset.
2. ASTER: o anúncio inicial LBank para 17/09 foi adiado. A série LBank disponível começa em 22/09; ela não é contraponto de venue ativa na primeira janela do TGE. A exclusividade e os números do comunicado da Aster exigem verificação on-chain independente.
3. O benchmark deve manter campos separados por venue: preço inicial, timestamp do primeiro trade, quote-volume e número de trades. Volume da plataforma e TVL ficam em campos próprios.
4. A comparação de D0/D1/D7/D30 ainda não pode ser marcada como calculada para nenhum dos dois ativos sem uma série verificável.

## 6. Próxima etapa recomendada

- obter ZIP Binance Vision HUMAUSDT 1m/trades de maio de 2025, checar checksum e extrair first trade + janelas;
- recuperar trades/swaps on-chain do Aster Spot na janela TGE de 17/09; para LBank, estudar separadamente o mercado após sua abertura em 22/09;
- estabelecer a hora inicial efetiva do ASTER na Aster Spot; comparar trades agregados e declaração de US$371M, sem dupla contagem;
- somente então gerar tabelas D0, D1, D7 e D30, com métodos e timestamps registrados.

## 7. Fontes consultadas

- Binance Launchpool/listing HUMA: https://www.binance.com/en/support/announcement/detail/515c45c283ea44c59b7f4623a3512666
- Binance Public Data docs: https://github.com/binance/binance-public-data
- Aster TGE docs: https://docs.asterdex.com/usdaster-token/tge
- Aster / PRNewswire day-one release: https://www.prnewswire.com/news-releases/aster-tge-day-one-performance-shines-exclusive-aster-dex-launch-drives-371-million-trading-volume-and-nearly-330-000-new-users-302561462.html
- LBank ASTER listing: https://www.lbank.com/support/articles/1968250114875064320
- DEXPaprika ASTER/USDT pool: https://dexpaprika.com/bsc/pool/0x7e58f160b5b77b8b24cd9900c09a3e730215ac47

---
**Classificação:** relatório parcial. Nenhuma cifra derivada foi inventada; resultados pendentes estão explicitamente identificados.
