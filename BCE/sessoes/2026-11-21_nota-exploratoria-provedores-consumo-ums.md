# Nota conceitual exploratória — provedores, consumo de serviços e referência em UMS

- **Data:** 2026-11-21
- **Natureza:** registro de ideias preliminares surgidas em discussão com o responsável pelo ecossistema.
- **Classificação:** hipótese / proposta em avaliação.
- **Status:** não aprovada, não normativa e não implementada.
- **Escopo:** reflexão inicial sobre a possível abstração de provedores externos e a representação do consumo de serviços no ecossistema MeshWave.

## 1. Abstração de provedores e variação de custo

Diferentes provedores externos podem oferecer serviços semelhantes usando unidades de consumo, métricas, limites e modelos comerciais distintos.

Uma mesma tarefa ou resultado pretendido pode apresentar custos diferentes dependendo do provedor selecionado. A escolha do provedor, portanto, pode influenciar o custo efetivo da execução, mesmo quando a finalidade da tarefa é equivalente.

Essa possibilidade sugere estudar uma camada de abstração capaz de relacionar:
- a tarefa ou capacidade solicitada;
- o provedor efetivamente utilizado;
- sua unidade e métrica de consumo;
- o custo correspondente segundo o modelo comercial vigente;
- diferenças de custo, qualidade, desempenho, disponibilidade e adequação entre provedores.

Não se estabelece que provedores devam ser intercambiáveis em qualquer circunstância, nem que o menor preço deva determinar sozinho a seleção. Equivalência funcional, qualidade, latência, confiabilidade, privacidade, limites contratuais e outros critérios ainda precisariam ser avaliados.

## 2. Possível referência comum de consumo

Como hipótese, o ecossistema poderia estudar uma forma de expressar em UMS o custo associado ao uso de serviços externos, mesmo quando cada fornecedor utiliza unidades próprias.

A conversão exigiria conhecer e manter os preços, franquias, limites e condições comerciais efetivamente aplicáveis a cada provedor, além da referência econômica adotada para UMS. Não há, neste registro, fórmula aprovada, taxa fixada, margem definida ou obrigação de conversão.

A referência em UMS não deve apagar a informação de origem: provedor, unidade nativa, quantidade consumida, preço de referência, data de vigência e condições do plano continuariam relevantes para permitir comparação e revisão.

## 3. Possíveis políticas de acesso

Foi levantada, apenas como hipótese, a possibilidade de oferecer uma franquia gratuita limitada, com renovação periódica, e alternativas pagas para usuários que necessitem de maior capacidade ou disponibilidade.

Os limites, periodicidade, critérios de renovação, serviços abrangidos, elegibilidade e eventual estrutura de planos não foram definidos. O exemplo de franquia Manus discutido nesta conversa é ilustrativo e não constitui parâmetro aprovado para o MeshWave.

## 4. MW Gate

Também foi mencionada a possibilidade de a MW Gate funcionar como ponto de acesso para aquisição ou conversibilidade de UMS no ecossistema, sem posicionamento prematuro como exchange.

A finalidade, os ativos envolvidos, os fluxos permitidos, os requisitos técnicos, operacionais e jurídicos e o próprio escopo da MW Gate permanecem sujeitos a estudo separado. Este registro não autoriza operação financeira nem define a MW Gate como mecanismo já implementado.

## 5. Limites e estado das ideias

Este documento preserva premissas iniciais para eventual avaliação futura. Ele:
- não cria política econômica, comercial, tarifária ou de acesso;
- não altera tokenomics, parâmetros, contratos ou regras de UMS/MWN;
- não determina seleção automática de provedores;
- não aprova franquias, planos pagos, conversões ou cobranças;
- não declara integração ou capacidade implementada na SOFIA, no MeshWave ou na MW Gate.

Todas as hipóteses podem ser refinadas, substituídas por alternativas mais adequadas ou integralmente descartadas se a avaliação técnica, econômica, operacional, jurídica ou estratégica demonstrar inviabilidade ou recomendar outro caminho.

## 6. Próxima avaliação possível

Se o tema for retomado, começar por comparar provedores reais para uma mesma classe de tarefa, documentando unidades nativas, preços e condições verificáveis, diferenças de qualidade/desempenho e limitações de equivalência. Só depois avaliar se existe uma métrica comum útil e como ela poderia ser representada em UMS.

Nenhuma implementação é solicitada ou autorizada por esta nota.
