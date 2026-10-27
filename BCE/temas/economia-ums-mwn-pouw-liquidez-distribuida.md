# Modelo econômico da MeshWave: PoUW, UMS, MWN e liquidez distribuída

**Tipo de documento:** registro conceitual e arquitetural  
**Data de elaboração:** 2026-10-25  
**Estado:** consolidação de conclusões conceituais discutidas; não constitui especificação final nem comprovação de implementação  
**Escopo:** princípios de remuneração por trabalho útil, contabilização em UMS, conversão e circulação de MWN, gestão automática de saldos e integridade econômica.

---

## 1. Objetivo

Registrar de forma rastreável as conclusões conceituais alcançadas sobre a relação entre Proof of Useful Work (PoUW), UMS e MWN no ecossistema MeshWave, incluindo a analogia do reservatório hidrelétrico, os modos de gestão de saldo dos MeshWalkers e os riscos de fabricação artificial de demanda.

O documento distingue:
- **Princípios conceituais estabelecidos nesta discussão**;
- **Consequências arquiteturais derivadas desses princípios**;
- **Questões ainda abertas**, que precisam ser especificadas antes de qualquer implementação ou afirmação de garantia econômica.

Este registro não afirma que os mecanismos descritos já estejam implementados.

## 2. Conceitos fundamentais

### 2.1 PoW e PoUW não são equivalentes

**PoW (Proof of Work)**, no contexto desta discussão, comprova que determinado trabalho computacional foi realizado. A execução pode ser real, mensurável e tecnicamente correta, mas isso não demonstra, por si só, que a rede obteve utilidade.

**PoUW (Proof of Useful Work)** comprova que o trabalho realizado foi útil para a rede, atendendo a uma necessidade legítima e produzindo benefício efetivo verificável.

A distinção fundamental não é entre trabalho real e trabalho fictício apenas. Um trabalho pode ser computacionalmente real e ainda assim não ser útil ou economicamente legítimo para a rede.

### 2.2 Regra de remuneração por PoUW

Princípio estabelecido:

> Todo PoUW gera UMS. Se o trabalho foi comprovadamente útil para a rede, sua remuneração é obrigatória.

O critério de elegibilidade é a utilidade comprovada, e não o mero consumo de CPU, armazenamento, largura de banda, energia ou volume de pacotes.

A comprovação de utilidade determina que o trabalho é remunerável. Ela não implica, por si só, que todos os trabalhos úteis devam receber quantidades idênticas de UMS. A métrica e a escala de remuneração ainda precisam ser definidas.

Em contrapartida, nem todo PoW gera UMS: a execução computacional que não comprova utilidade efetiva não gera créditos apenas por ter ocorrido.

### 2.3 UMS

A UMS é a unidade interna de contabilização econômica do ecossistema. Registra valor atribuído a contribuições úteis e permite contabilizar o consumo ou a transferência de valor segundo as regras do protocolo.

Para a analogia usada nesta discussão, UMS representa **potencial econômico acumulado**. Não deve ser confundida com MWN em circulação nem com dinheiro fiduciário disponível.

### 2.4 MWN

MWN é o ativo fungível destinado à circulação de valor entre participantes e à conexão entre a economia interna da MeshWave e o mercado externo.

Nesta concepção, MWN não é a própria economia interna nem precisa representar todo o saldo de UMS existente. Sua função inclui servir como meio obrigatório para transferências entre participantes, se essa regra for adotada no protocolo.

A cotação externa de MWN é distinta da unidade de contabilização interna UMS. O preço em reais, dólares, euros ou outra moeda é determinado pelas condições de mercado e não fica automaticamente garantido por uma equivalência contábil interna.

### 2.5 Moedas e saldos distintos na carteira

A carteira de um MeshWalker pode expor pelo menos três saldos conceitualmente distintos:
1. UMS — contabilização interna;
2. MWN — ativo de circulação/conversão;
3. Saldos fiduciários — reais, dólares, euros ou outras moedas, quando efetivamente disponíveis por operações de liquidação.

A representação de um saldo em moeda fiduciária não deve ser confundida com a capacidade de resgatar esse valor sem recursos, comprador ou liquidez efetivamente disponíveis.

## 3. PoUW como base de integridade econômica

O sistema não deve remunerar simplesmente o volume de atividade computacional. Caso contrário, seria possível tentar produzir UMS artificialmente por meio de transferências fictícias, tráfego redundante, solicitações sem finalidade ou processamento repetido sem benefício adicional.

O protocolo precisa distinguir pelo menos três dimensões:

1. **Execução:** o trabalho foi realmente realizado?
2. **Utilidade:** a tarefa respondeu a uma necessidade legítima da rede e produziu um resultado útil verificável?
3. **Integridade econômica:** a demanda foi criada legitimamente ou foi fabricada para extrair remuneração do sistema?

A existência de execução verificável não prova automaticamente utilidade. A utilidade alegada também não deve ser aceita apenas porque há dispositivos, pacotes, tarefas ou registros diferentes envolvidos.

### 3.1 Trabalho entre dispositivos do mesmo participante

Se um participante gera uma solicitação em um dispositivo sob seu controle e a atende por outro dispositivo também sob seu controle, a atividade pode representar apenas uma movimentação interna de custos e receitas. Se não houver utilidade efetiva para a rede, não deve gerar UMS líquidas por mera produção de demanda.

A análise deve considerar a operação em seu conjunto, sem presumir que todo trabalho entre dispositivos do mesmo titular seja inútil. Se existir uma necessidade legítima e benefício verificável para a rede, a relação de titularidade, isoladamente, não invalida o trabalho.

### 3.2 Exploração de dispositivos de terceiros

Um risco mais sofisticado ocorre quando um participante induz demanda computacional em dispositivos de terceiros e direciona a execução remunerada para dispositivos que controla. O processamento pode ser real, mas a demanda pode ter sido artificialmente provocada para capturar remuneração enquanto terceiros suportam os custos.

O protocolo deve procurar evidências de autorização, legitimidade da demanda, benefício produzido e padrões de coordenação abusiva. A análise não deve classificar automaticamente toda operação entre participantes distintos como fraude, nem presumir fraude apenas porque um participante obtém lucro.

### 3.3 Consequência

O princípio é:

> A MeshWave remunera a contribuição útil comprovada, e não a capacidade de provocar consumo computacional ou fabricar demanda.

A prevenção de fraude deve também considerar duplicidade de contabilização, repetição de resultados, autoindução de demanda e conluio. Os critérios de detecção, contestação e resolução continuam pendentes de especificação técnica.

## 4. UMS como potencial econômico: analogia do reservatório hidrelétrico

A analogia construída na discussão é a de uma hidrelétrica:

| Elemento da analogia | Correspondência conceitual na MeshWave |
|---|---|
| Chuva | Fluxo de PoUW realizado continuamente, conforme a atividade real da rede |
| Reservatório de água | Saldo acumulado de UMS |
| Água potencialmente disponível para geração | UMS elegíveis para conversão, depois de reservas e obrigações |
| Comportas | Regras, autorizações, limites e mecanismo de conversão |
| Turbinas/geração | Materialização ou disponibilização de MWN para atender às necessidades de circulação |
| Distribuição de eletricidade | Circulação de MWN entre participantes e, quando possível, interação com o mercado externo |
| Água que pode retornar ao reservatório | Reconversão de MWN em UMS, conforme as regras do protocolo |

### 4.1 A diferença decisiva em relação à hidrelétrica

Na hidrelétrica convencional, a água que passou pelas turbinas não retorna ao reservatório espontaneamente em condições economicamente equivalentes; bombeá-la de volta exige energia.

Na MeshWave, a conversão é protocolar e pode ter um caminho inverso: MWN pode ser reconvertido em UMS. A reconversão não é uma impossibilidade física nem requer que se trate o ativo como energia física consumida. Ela depende das regras contábeis e econômicas do sistema.

Por isso, a analogia representa o fluxo, o estoque e a gestão de potencial — não uma equivalência física entre UMS e MWN.

### 4.2 A “chuva” de PoUW

A geração de PoUW é a fonte contínua potencial de novas UMS: quando a rede recebe trabalho útil comprovado, o protocolo deve atribuir a remuneração correspondente.

A chuva pode variar em intensidade. A emissão de UMS depende de trabalho útil efetivamente realizado, não de uma promessa de fluxo invariável. O volume de PoUW e a quantidade de UMS geradas dependem da atividade real da rede e das regras de mensuração e remuneração.

### 4.3 Consequência estrutural

A MeshWave não precisa manter todo o potencial econômico contabilizado em UMS permanentemente materializado em MWN. A conversão pode ocorrer conforme a demanda por transferências e a disponibilidade elegível.

Assim, o tamanho do saldo interno em UMS pode ser diferente do estoque de MWN em circulação.

## 5. Transferências entre participantes por meio de MWN

Uma regra considerada nesta discussão é que UMS não podem ser transferidas diretamente de um participante para outro. A transferência de valor deve passar obrigatoriamente pela conversão em MWN.

Fluxo conceitual:
1. O participante remetente possui UMS elegíveis.
2. O protocolo converte o montante autorizado em MWN.
3. O MWN é transferido ao destinatário.
4. O destinatário pode manter MWN ou reconvertê-lo em UMS, conforme as regras.
5. Se a conversão de retorno for realizada, o saldo interno do destinatário é atualizado segundo a regra de conversão.

Essa regra torna MWN o instrumento obrigatório de circulação entre participantes, e não apenas uma ponte opcional para o mercado externo.

### 5.1 Demanda transacional não significa saldo obrigatório

Como conversão e reconversão podem ser automáticas, o participante não precisa manter um saldo positivo permanente de MWN. Pode manter saldo zero e autorizar o protocolo a converter UMS elegíveis quando houver demanda e capacidade para atender à operação.

É necessário distinguir:
- **Demanda transacional:** MWN necessário para executar uma transferência;
- **Estoque circulante:** MWN efetivamente disponível em determinado momento;
- **Saldo mínimo de MWN:** parâmetro opcional configurado pelo participante;
- **Demanda especulativa:** compra de MWN motivada pela expectativa de valorização.

A obrigatoriedade de utilizar MWN em transferências cria uma necessidade de uso transacional. Não garante, isoladamente, um estoque mínimo permanente, uma demanda constante por saldo, liquidez externa ou valorização do ativo.

## 6. Gestão de saldos pelo MeshWalker

A gestão de UMS e MWN é independente. O participante pode optar por administração manual ou automática de cada saldo, de acordo com as funcionalidades oferecidas pelo protocolo.

### 6.1 Gestão de MWN

O participante pode, por exemplo, definir um saldo mínimo de 2 MWN e máximo de 5 MWN. Também pode definir saldo mínimo e máximo iguais a zero e permitir conversões sob demanda, desde que possua UMS elegíveis suficientes e tenha autorizado as operações.

Os limites configurados são políticas de saldo; não significam garantia de execução se faltarem UMS, demanda atendível, capacidade operacional ou condições exigidas pelo protocolo.

### 6.2 Gestão de UMS

O participante também escolhe entre:
- **Modo manual:** administra suas próprias conversões e reservas. Pode ficar sem UMS utilizáveis para uma operação interna, mesmo que tenha MWN ou saldo fiduciário, se não realizar a conversão necessária. Isso pode levar a uma requisição não atendida até que ele próprio intervenha.
- **Modo automatizado:** autoriza o protocolo a administrar reservas e conversões dentro de limites definidos. O sistema pode estimar a necessidade pessoal com base no histórico de consumo e preservar uma reserva mínima, disponibilizando apenas o excedente elegível para atender às demandas de conversão da rede.

### 6.3 Exemplo de reserva pessoal

Um MeshWalker tem 180.000 UMS e configura ou autoriza uma reserva pessoal de 100.000 UMS:
- Reserva pessoal: 100.000 UMS;
- Excedente potencialmente elegível: 80.000 UMS.

O excedente não é automaticamente convertido. A conversão depende da demanda efetiva, das regras, das autorizações e de outras obrigações.

Se o histórico de consumo indicar que a necessidade pessoal pode aumentar, o sistema pode recomendar ou, quando expressamente autorizado, ajustar a reserva. O protocolo deve deixar claro se a reserva é um limite rígido ou uma recomendação adaptativa.

### 6.4 Condições mínimas para conversão automática

A conversão automática deve considerar, no mínimo:
1. demanda real por MWN;
2. saldo de UMS disponível;
3. reservas pessoais e obrigações;
4. autorização e limites definidos pelo participante;
5. disponibilidade operacional e regras de conversão;
6. prevenção de dupla utilização do mesmo saldo em operações concorrentes.

A automação é uma opção de gestão, não uma garantia de que toda requisição será atendida.

## 7. Conversão, reconversão e equilíbrio econômico

O modelo contempla dois sentidos de ajuste:

- **UMS → MWN:** materializa parte do saldo interno quando é necessário atender a transferências ou outras operações autorizadas;
- **MWN → UMS:** retira MWN da função circulante daquele participante e devolve o valor correspondente à contabilização interna, segundo as regras do protocolo.

Se MWN estiver escasso diante de demanda real, o preço externo pode subir. Isso pode tornar a conversão de UMS em MWN mais atrativa para participantes que tenham autorizado a operação. A conversão pode aumentar a oferta circulante e atenuar a escassez.

Se houver excesso de MWN ou baixa demanda, o preço pode cair e alguns titulares podem preferir reconverter MWN em UMS, reduzindo o estoque circulante, se as regras permitirem.

Esses são mecanismos potenciais de feedback, não garantias de equilíbrio automático. O resultado depende de utilidade real, demanda, liquidez, regras de conversão e reconversão, incentivos, limites de emissão e capacidade da rede.

### 7.1 UMS interna e preço externo de MWN

A unidade de contabilização interna e a cotação externa não devem ser confundidas. Um parâmetro interno de conversão não fixa necessariamente o preço de MWN no mercado externo.

Uma taxa protocolar fixa e incondicional entre UMS e MWN, combinada com preço de mercado livre, pode criar oportunidades persistentes de arbitragem, pressão de conversão ou resgate. O desenho definitivo precisa explicar como os dois lados se conciliam.

### 7.2 Circulação zero

É conceitualmente possível que o estoque circulante de MWN chegue a zero se todos os tokens forem reconvertidos e invalidados/queimados, caso esse seja o mecanismo adotado. Se os tokens retornarem a uma reserva para reemissão futura, o estoque circulante pode ser zero sem que a oferta total do protocolo seja zero.

A economia interna em UMS poderia continuar operando sem MWN circulante somente se o protocolo permitir essa operação e houver outro caminho para as atividades internas que não exijam transferências entre participantes. Como transferências diretas de UMS foram consideradas proibidas neste modelo, o comportamento do sistema sem MWN circulante precisa ser especificado para evitar contradição operacional.

## 8. Registro monetário em reais, dólares ou euros

A carteira pode mostrar saldos fiduciários associados a operações, mas uma conversão interna UMS/MWN não cria, por si só, dinheiro fiduciário.

É preciso distinguir:
- valor de mercado estimado do MWN;
- valor fiduciário efetivamente recebido por uma venda;
- crédito de remuneração concedido pelo protocolo;
- saldo fiduciário liquidado e disponível para saque ou pagamento.

Se o participante recebe moeda fiduciária pela venda efetiva de MWN ou por uma remuneração definida pelo sistema, o saldo pode aumentar conforme a operação realizada. Não se deve creditar automaticamente moeda fiduciária apenas porque houve uma conversão interna ou porque o MWN tem uma cotação observável.

## 9. Princípios conceituais consolidados

1. **Utilidade antes da remuneração:** PoUW é trabalho útil comprovado, não apenas trabalho computacional realizado.
2. **Remuneração obrigatória:** todo PoUW elegível gera UMS; a remuneração é parte da definição operacional do PoUW na MeshWave.
3. **PoW não é suficiente:** trabalho computacional sem utilidade comprovada não gera UMS apenas por consumir recursos.
4. **UMS é contabilização interna:** representa valor reconhecido dentro da economia da rede.
5. **MWN é ativo de circulação e conexão externa:** não é sinônimo de UMS nem da economia inteira.
6. **Materialização sob demanda:** UMS elegíveis podem permanecer não convertidas até que exista necessidade.
7. **Conversão reversível:** o protocolo pode converter UMS em MWN e reconverter MWN em UMS segundo suas regras.
8. **Transferência obrigatoriamente via MWN:** conforme a regra considerada, UMS não são transferidas diretamente entre participantes.
9. **Saldo MWN opcional:** automação permite saldo zero ou limites mínimos/máximos configurados, sujeito à disponibilidade de UMS.
10. **Gestão individual de UMS:** o participante pode optar por gestão manual ou automática, com consequências operacionais distintas.
11. **Reserva pessoal antes do excedente:** em modo automatizado, somente UMS elegíveis após reservas e obrigações podem ser consideradas para conversão a serviço da rede.
12. **Prevenção de demanda artificial:** a remuneração depende de utilidade efetiva e demanda legítima, não do volume bruto de atividade.
13. **Liquidez distribuída potencial:** os participantes podem autorizar a disponibilização de UMS elegíveis, sem exigir uma reserva central única de MWN.
14. **Equilíbrio não garantido:** mecanismos de feedback podem moderar escassez ou excesso, mas não garantem preço estável nem valorização.
15. **Cotação externa não é garantia fiduciária:** preço de mercado e conversão interna são dimensões distintas.
16. **Validação de consenso é trabalho elegível à PoUW:** a avaliação e o voto sobre operações e blocos podem constituir uma categoria própria de trabalho útil, desde que a participação seja registrada conforme o protocolo.
17. **O voto comprova a participação:** um voto autenticado, vinculado à operação designada e registrado dentro do prazo é a evidência operacional da execução da tarefa de validação. Não se exige uma segunda prova independente de que o validador analisou a operação.
18. **Ausência de voto não gera UMS pela tarefa:** se o validador não registrar resposta dentro do prazo, não recebe a recompensa de validação daquela requisição; a ausência também alimenta a avaliação de disponibilidade e credibilidade.
19. **A recompensa não depende de concordar com a maioria:** votos válidos pela aprovação ou rejeição podem ser remuneráveis. O resultado coletivo do consenso e o reconhecimento econômico da participação são decisões distintas.
20. **Credibilidade dinâmica dos validadores:** respostas válidas e consistentes preservam ou recuperam credibilidade; ausências recorrentes podem reduzir prioridade, suspender a condição de validador primário e, abaixo de um limite, retirar a elegibilidade para validar.
21. **Crédito único e atribuição verificável:** votos devem ser autenticados, vinculados à tarefa e contabilizados de forma idempotente, para que retransmissões não gerem UMS duplicadas.
22. **Consenso não basta para provar utilidade econômica da operação:** o protocolo deve distinguir a validade formal de uma transação/bloco da elegibilidade econômica do trabalho que ela representa, para limitar operações fabricadas ou conluio voltado à obtenção de UMS.

## 10. Questões em aberto para especificação futura

Este relatório registra conceitos, não fecha as regras de implementação. Os seguintes pontos permanecem abertos:

### 10.1 Remuneração de PoUW
- Como medir a utilidade e atribuir a quantidade de UMS por tipo de trabalho?
- Como evitar duplicidade de créditos para um mesmo resultado?
- Como tratar utilidade parcial, tarefas compostas, falhas, retrabalho e resultados posteriormente invalidados?

### 10.2 Legitimidade da demanda e antifraude
- Como provar autorização e finalidade de uma tarefa?
- Quais evidências serão usadas para distinguir demanda genuína de autoindução ou conluio?
- Como lidar com privacidade, falsos positivos, contestação e recurso?
- Como contabilizar custos e receitas entre dispositivos ou participantes relacionados sem presumir que toda relação seja abusiva?

### 10.3 Regras de conversão
- A conversão UMS/MWN terá taxa fixa, variável ou combinação?
- Como são calculadas taxas, arredondamentos, custos e limites?
- A reconversão destrói/queima MWN, devolve-o a uma reserva ou utiliza outro mecanismo?
- Como tratar conversões simultâneas e impedir dupla utilização de UMS?

### 10.4 Liquidez e atendimento de demanda
- O que ocorre quando a demanda por MWN excede todas as UMS elegíveis autorizadas?
- Qual é a ordem de prioridade entre requisições?
- Existem limites por participante, por período ou por concentração?
- Como se define o comportamento quando o estoque circulante de MWN é zero?

### 10.5 Gestão automatizada
- A reserva baseada no histórico é rígida, adaptativa ou recomendada?
- Como o usuário autoriza alterações automáticas?
- Como o protocolo protege saldos reservados contra operações concorrentes?
- Como são apresentados consentimento, histórico, limites e possibilidade de interrupção da automação?

### 10.6 Validação de consenso e credibilidade dos nós
- Quais são os prazos de resposta, os critérios para considerar um voto válido e o tratamento de votos tardios?
- Como serão calculados os níveis de credibilidade, as janelas de avaliação, os limites de prioridade, a suspensão e a remoção de validadores?
- Como o sistema distingue indisponibilidade do nó de falhas de comunicação ou de infraestrutura compartilhada, sem conceder UMS por uma tarefa sem voto registrado?
- Como a seleção e a distribuição de tarefas reduzem o risco de identidades sob controle comum formarem um quórum para fabricar operações remuneráveis?
- Qual será a política de recompensa por participação, sem vincular o pagamento à aprovação da operação nem permitir crédito duplicado?

### 10.6 Liquidação fiduciária e mercado externo
- Como se distinguem cotação indicativa, ordem de venda e liquidação efetiva?
- Quem provê liquidez fiduciária e sob quais condições?
- Como a interface evita sugerir que MWN garante resgate ou poder de compra externo?

## 11. Conclusão

O modelo conceitual discutido separa a geração de valor útil, sua contabilização interna e sua materialização para circulação:

**PoUW útil comprovado → remuneração obrigatória em UMS → conversão de UMS elegíveis em MWN conforme a demanda → transferência de MWN → eventual reconversão para UMS.**

A analogia do reservatório expressa a ideia de que a economia interna pode acumular potencial em UMS sem materializar todo esse valor em MWN ao mesmo tempo. O PoUW alimenta o reservatório; as regras de conversão controlam a passagem para a circulação; e a reconversão permite o retorno contábil do valor.

A validação de consenso também pode ser reconhecida como categoria própria de PoUW: o voto autenticado e registrado comprova a participação do validador; a ausência de voto não gera UMS pela tarefa e afeta sua credibilidade. A credibilidade determina a prioridade e a permanência no conjunto de validadores, enquanto o consenso determina a validade da operação. Essas funções devem permanecer separadas.

A integridade do modelo depende de remunerar a utilidade efetiva e impedir que atividade computacional ou demanda fabricada seja confundida com contribuição útil. A gestão automatizada de reservas e conversões pode distribuir a liquidez entre participantes, preservando a autonomia de quem escolhe o modo manual.

Essas conclusões formam uma base conceitual para especificação posterior. Não equivalem a prova de viabilidade econômica, garantia de estabilidade de preço ou descrição de mecanismos já implementados.

---

## 12. Proveniência e limite deste registro

Este documento foi elaborado a partir da discussão conceitual realizada em 25 de outubro de 2026. Ele registra as definições e hipóteses explicitamente estabelecidas durante essa conversa, organiza suas consequências arquiteturais e lista questões ainda não resolvidas.

Não foram realizadas, como parte deste registro, validação de código, auditoria de contratos inteligentes, simulação quantitativa, parecer jurídico/financeiro ou verificação independente de implementação.
