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

LBank publicou anúncio informando ASTER/USDT spot:
- depósitos a partir de 11:00 UTC de 17/09/2025;
- início de negociação às **12:30 UTC de 17/09/2025**.

Fonte:
- https://www.lbank.com/support/articles/1968250114875064320

Essa evidência é um alerta material: a narrativa de exclusividade da Aster DEX nas primeiras 24 horas precisa ser confrontada com a listagem da LBank. Ainda não temos confirmação independente do primeiro trade real da LBank nem da definição temporal usada pelo comunicado de Aster (horário UTC, janela exata e abrangência de venue). Não se deve declarar, sem reconciliação, que o volume de US$371M é volume global consolidado ou exclusivamente de uma única venue.

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
| ASTER | LBank Spot ASTER/USDT | Negociação anunciada para 17/09/2025 12:30 UTC | venue CEX concorrente documentada; first trade e volume pendentes |
| ASTER | PancakeSwap V3 ASTER/USDT | pool público conhecido criado em 20/09/2025 | posterior ao TGE; não serve como primeira venue |

## 5. Conclusões da etapa

1. HUMA: o caminho de API direta não entregou dados; é necessário usar o arquivo público histórico ou outro canal que permita obter e verificar o dataset.
2. ASTER: o comunicado do projeto não deve ser tomado como evidência suficiente de exclusividade da DEX. A listagem LBank em 12:30 UTC no próprio dia do TGE exige reconciliação.
3. O benchmark deve manter campos separados por venue: preço inicial, timestamp do primeiro trade, quote-volume e número de trades. Volume da plataforma e TVL ficam em campos próprios.
4. A comparação de D0/D1/D7/D30 ainda não pode ser marcada como calculada para nenhum dos dois ativos sem uma série verificável.

## 6. Próxima etapa recomendada

- obter ZIP Binance Vision HUMAUSDT 1m/trades de maio de 2025, checar checksum e extrair first trade + janelas;
- obter registros de negociação LBank ASTER/USDT para o dia TGE, e procurar documentação/trades do mercado Aster Spot;
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
