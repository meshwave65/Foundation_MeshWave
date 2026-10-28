# Checkpoint — clarificação do módulo Mercado

- **Data:** 2026-10-27
- **Tipo de trabalho:** atualização documental fora da fila ativa de curadoria F3.3; nenhuma fonte bruta em `KNOWLEDGE/` foi aberta.
- **Base consultada:** branch `main`; documento conceitual `BCE/temas/economia-ums-mwn-pouw-liquidez-distribuida.md`, índice curatorial, controle mestre e governança BCE.
- **Pedido:** registrar que Mercado é o integrador/exchange de fronteira; serviços internos usam UMS, saldos UMS permanecem isolados por usuário, e MWN conecta a negociação externa e a eventual reconversão para UMS de outra conta.
- **Atualizações:** seção 13 adicionada ao documento econômico; DOM-20 incluído no índice. Parceiro (por exemplo, Binance) é alternativa de execução externa, não operador de UMS. Estados de ordem e liquidação, idempotência, reconciliação, taxas, custódia e falhas estão marcados como requisitos operacionais.
- **Evidência:** esclarecimento do responsável pelo projeto nesta sessão. É uma clarificação da arquitetura pretendida, não verificação de código nem decisão sobre operador/parceiro.
- **Limite:** a documentação pesquisada no repositório não confirma que o simulador implemente o painel Mercado ou o fluxo descrito. Não se conclui inexistência fora da evidência inspecionada.
- **Última ação concluída:** registrar a clarificação no tema econômico e indexá-la como DOM-20.
- **Próximo passo exato:** inspecionar o código executável atual do simulador e reproduzir os fluxos de disponibilização, execução/liquidação externa e recompra/reconversão para confirmar o que já existe; atualizar DOM-20 com evidência observada.
- **Fila BCE preservada:** F3.3 continua em andamento com a próxima ação previamente registrada no controle mestre; esta atualização não abriu nem substituiu o escopo da fila.
- **Publicação:** commits de conteúdo/índice e checkpoint listados no controle mestre após a publicação.
