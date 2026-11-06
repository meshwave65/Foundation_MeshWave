# Etapa 20 — Cruzamento preço-volume e protocolo de ampliação da amostra

**Data:** 2026-11-06  
**Coorte quantitativa:** MANTA, ENA, OMNI, BIO e BERA — Binance Spot USDT.  
**Fontes de números:** relatórios das Etapas 18 e 19; os valores não foram recalculados a partir de novas fontes nesta etapa.

## 1. Cruzamento descritivo

A comparação usa retornos close-to-close dos checkpoints de 1 minuto da Etapa 18 e quote volume acumulado desde o timestamp D0 da Etapa 19. Para comparar escalas, o cálculo exploratório usa correlação de Pearson entre retorno e log10(quote volume), além de Spearman sobre os ranks.

| Token | Retorno D+7 | Volume quote D0→D+7 (USDT) | Retorno D+30 | Volume quote D0→D+30 (USDT) |
|---|---:|---:|---:|---:|
| ENA | +156.0158% | 5,418,194,458.988800 | +55.0296% | 12,682,625,163.155830 |
| MANTA | +53.7475% | 2,030,066,560.325919 | +51.5909% | 4,464,984,152.307641 |
| BERA | -20.8621% | 1,525,678,423.452275 | -8.1198% | 3,030,613,947.164876 |
| BIO | -39.0455% | 1,464,127,099.656450 | -78.4545% | 2,295,091,910.187170 |
| OMNI | -54.7307% | 680,373,938.069400 | -70.2253% | 1,079,472,650.714600 |

### Estatística exploratória da amostra (n=5)

| Comparação | Pearson r com log10(volume) | Spearman ρ |
|---|---:|---:|
| Retorno D+7 vs volume acumulado D0→D+7 | +0.9406 | +1.0000 |
| Retorno D+30 vs volume acumulado D0→D+30 | +0.8547 | +0.9000 |

**Interpretação limitada:** dentro destes cinco casos, maior volume acumulado acompanha retornos mais altos nos checkpoints. A ordenação de D+7 coincide exatamente; D+30 apresenta uma inversão entre BIO e OMNI. Isso é associação descritiva, não evidência causal ou preditiva. O n=5 é pequeno, tokens e regimes de mercado não são independentes, e o volume é simultâneo/relacionado ao próprio movimento de preço. Não extrapolar para o conjunto de lançamentos nem tratar os coeficientes como inferência estatística robusta.

O caso ENA é particularmente influente por ocupar o topo tanto em retorno quanto em volume. Com tão poucos pontos, uma análise posterior deve incluir correlação robusta, análise leave-one-out, controles de regime BTC/ETH, float/unlocks, market-making e liquidez.

## 2. O que o cruzamento permite concluir — e o que não permite

- **Volume alto não garante valorização:** volume também pode ser atividade de distribuição, rotação, volatilidade ou saída.
- **Volume baixo não demonstra ausência de interesse:** o recorte é uma única venue e par USDT.
- **Volume quote não é captação:** não é venda pública/IDO, receita, treasury proceeds, market depth, TVL ou liquidez disponível.
- **Preço checkpoint não é sale price:** retorno calculado usa close da vela de 1 minuto em horário UTC definido na coorte.
- O universo foi intencionalmente fixado em cinco projetos para validar a metodologia; a associação não deve virar premissa econômica para MWN.

## 3. Regra proposta para ampliar a amostra sem selecionar vencedores

A expansão deverá seguir critérios de inclusão definidos antes de calcular desempenho:

1. **Venue:** Binance Spot, exclusivamente; excluir Futures, Alpha e pre-market da âncora principal.
2. **Par:** USDT, com dados de 1m publicamente disponíveis no Binance Vision.
3. **Evento:** novo ativo/ticker em Spot; distinguir novo token de adição de um par a um ativo já listado.
4. **Timestamp:** usar horário de abertura Spot final do anúncio oficial, incluindo anúncio de adiamento. Registrar ambos — hora anunciada e hora efetiva — e adotar a hora efetiva.
5. **Período:** adotar inicialmente 2023–2025, com recorte cronológico. Não escolher ativos com base no retorno ou no volume posterior.
6. **Casos conjuntos:** quando dois ativos abrem no mesmo anúncio/hora (ex.: ACX e ORCA), manter ambos, mas identificá-los como evento de listing compartilhado; não assumir independência.
7. **Qualidade:** verificar arquivo mensal e checksum; exigir cobertura completa para as janelas de 1.440, 10.080 e 43.200 candles.
8. **Resultados:** calcular D0/D+7/D+30 e volumes rolling sempre pela mesma regra; incluir casos de desempenho negativo e ativos posteriormente removidos quando os dados históricos existirem.
9. **Dados ausentes:** excluir da estatística somente com motivo expresso, mantendo registro de exclusão; nunca preencher valores por estimativa.
10. **Relato:** publicar o universo elegível e a regra antes da leitura dos resultados.

## 4. Fila inicial de candidatos — elegibilidade documental, não ainda coorte quantitativa

| Token | Evento Binance Spot | Hora UTC indicada | Evidência primária / nota |
|---|---|---|---|
| ORDI | Listagem Spot; adiamento formal | 2023-11-07 12:00 | [Binance — adiamento](https://www.binance.com/en/support/announcement/detail/2078410f1b3749e081d0999feed12709). Horário original 10:00 foi adiado para 12:00; deve-se usar a hora efetiva. |
| PORTAL | Spot listing | 2024-02-29 10:00 | [Binance Launchpool announcement](https://www.binance.com/en/support/announcement/detail/0620f90f55f2420b89158808380b6c9d): lista PORTAL/USDT e horário de listagem. |
| SCR | Spot listing, após pré-market | 2024-10-22 09:00 UTC provisório | O anúncio da Binance sobre SCR informa pre-market, perp e Earn em horários separados; Spot é anunciado separadamente e foi adiado. Confirmar anúncio Spot final antes de incluir; não usar o horário de Futures ou pré-market. |
| ACX | Spot listing | 2024-12-06 13:00 | [Anúncio oficial Binance](https://www.binance.com/en/square/post/17194448398289): ACX/USDT, ORCA/USDT e Seed Tag. |
| ORCA | Spot listing, evento conjunto com ACX | 2024-12-06 13:00 | Mesmo anúncio oficial ACX/ORCA; marcar evento compartilhado. |

**Nota SCR:** fonte de adiamento localizada: [Binance announcement](https://www.binance.com/en/square/post/15202347143634), que informa atraso de 16:00 para 17:00 UTC+8 (09:00 UTC). O evento pre-market de SCR é distinto da negociação Spot; manter SCR em “pendente de confirmação final do anúncio Spot” até a captura da página Spot dedicada.

A lista acima não é uma amostra final representativa. Ela é uma fila de verificação documental; a sequência completa deverá ser extraída do histórico de anúncios Spot para cumprir a regra cronológica.

## 5. Próximo procedimento

- Confirmar e congelar o universo cronológico Binance Spot 2023–2025 (incluindo os casos do mesmo evento).
- Obter os horários Spot finais, pares e eventuais adiamentos diretamente dos anúncios primários.
- Verificar disponibilidade dos arquivos 1m e checksum, antes de computar preços/volumes.
- Recalcular correlações para amostra ampliada; publicar scatterplot, Spearman/Pearson, leave-one-out e separação por ano/condições de mercado.

## 6. Referências metodológicas

- [Etapa 17 — coorte e regra de âncora](./2026-11-06-stage-17-binance-spot-cohort-and-method.md)
- [Etapa 18 — preço D0/D+7/D+30](./2026-11-06-stage-18-binance-cohort-d0-d7-d30-data.md)
- [Etapa 19 — volume rolling 24h/7d/30d](./2026-11-06-stage-19-launch-volume-windows-24h-7d-30d.md)
- [Binance Public Data](https://github.com/binance/binance-public-data)

**Conclusão:** o cruzamento atual sugere que, na coorte pequena e específica observada, preço e giro de mercado caminham juntos nos checkpoints. A conclusão ainda não serve como regra de previsão nem como parâmetro de tokenomics. A prioridade científica é ampliar cronologicamente o universo e verificar a robustez antes de derivar recomendações para MWN.
