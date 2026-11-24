# Checkpoint — decisões e continuidade de execução SOFIA/SCP

> Registro lateral da BCE, fora da fila de curadoria de fontes e sem criação de missão. Consolida decisões explícitas do responsável e evidências operacionais observadas nesta conversa. Não representa implementação concluída.

## Metadados

| Campo | Valor |
|---|---|
| Data | 2026-11-24 |
| Repositório de persistência | `meshwave65/Foundation_MeshWave` |
| Natureza | Checkpoint de decisões e continuidade |
| Tema relacionado | DOM-06 — SOFIA, agentes, missões e orquestração |
| Estado | REGISTRADO — implementação pendente |
| Escopo | Seleção oportunista de ferramentas, execução de missões, agentes SCP/Sandbox e continuidade documental |

## 1. Motivo do registro

A conversa produziu decisões arquiteturais e operacionais relevantes para SOFIA/SCP, mas elas estavam permanecendo apenas no histórico conversacional. O responsável determinou que esse conhecimento seja persistido na BCE mesmo quando não estiver vinculado a uma missão formal.

Este checkpoint é um registro lateral. Não abre, assume ou altera a fila de curadoria BCE, não cria missão SCP e não declara execução técnica concluída.

## 2. Decisões explícitas — seleção de ferramentas e consumo de recursos

### 2.1 Capacidade necessária, não ferramenta imposta

O SOFIA deve receber da missão a capacidade necessária e selecionar o executor compatível. A missão não deve ficar acoplada a um fornecedor, navegador, modelo ou conector específico.

### 2.2 Processamento oportunista e otimizado

**Decisão do responsável:** o SOFIA não deve utilizar a ferramenta mais poderosa apenas porque ela está disponível no plano. Deve escolher a alternativa de menor custo que consiga entregar o mesmo resultado com eficiência, qualidade, confiabilidade e segurança suficientes.

Consequências operacionais:

- preferir automação determinística quando ela resolve a tarefa;
- não chamar LLM quando regras determinísticas forem suficientes;
- preferir modelo menor quando atingir os mesmos critérios de aceite;
- usar ferramenta gratuita ou limitada quando ela for suficiente para o resultado exigido;
- escalar para ferramenta/modelo mais sofisticado somente quando a alternativa econômica não atender aos requisitos;
- considerar custo, latência, confiabilidade, qualidade, limites, segurança e possibilidade de recuperação;
- registrar desempenho e falhas para melhorar seleções futuras.

A disponibilidade de recursos em um plano mais sofisticado amplia as opções, mas não obriga o SOFIA a consumir os recursos mais caros.

### 2.3 Planos e provedores

A arquitetura deve comportar, sem bifurcar o produto por fornecedor:

- planos gratuitos: ferramentas gratuitas, open source ou com limites de uso;
- planos intermediários: ferramentas com limites e capacidades ampliados;
- planos avançados: provedores comerciais, recursos premium e maior configurabilidade;
- escolha/configuração do usuário: conectores e provedores próprios, credenciais próprias e preferências, conforme permissões e plano.

O plano define o universo de capacidades habilitadas; o seletor do SOFIA continua escolhendo a opção suficiente de menor custo.

### 2.4 Ferramentas de navegador — candidatas, não dependências

Foram consideradas como alternativas a avaliar:

- Playwright — automação determinística e execução própria;
- Browser Use — navegação controlada por agente;
- Stagehand — automação assistida por linguagem natural sobre navegador;
- Steel Browser — infraestrutura de navegador auto-hospedável;
- Anchor Browser — opção gerenciada a avaliar conforme limites e condições do plano.

Essas opções não foram homologadas nesta conversa. A escolha deve resultar de comparação prática de adequação, custo total, estabilidade, segurança, manutenção e qualidade do resultado.

**TinyFish não é ferramenta adotada pelo projeto e não deve ser introduzida como dependência ou pressuposto de execução.**

A gratuidade do navegador não garante gratuidade de modelos ou serviços auxiliares. O princípio de suficiência e menor custo aplica-se também ao modelo que interpreta páginas e decide ações.

## 3. Decisões explícitas — agentes e relação SCP original/Sandbox

### 3.1 Fonte de verdade dos agentes

- O SCP original é a fonte de verdade e o único ambiente de cadastro/administração de agentes.
- O Sandbox não cadastra, edita, remove nem administra agentes.
- O Sandbox apenas consulta e exibe uma projeção dos agentes existentes no SCP original.
- A sincronização de agentes é unidirecional: SCP original → Sandbox.

### 3.2 Dados permitidos no espelho

O Sandbox pode exibir nome, estado operacional, créditos e outros campos genéricos expressamente permitidos. E-mail, senha, tokens, chaves, credenciais, ciphertext e configurações secretas não devem ser copiados nem disponibilizados no Sandbox.

A projeção deve usar allowlist explícita. A existência de colunas sensíveis legadas no schema Sandbox não autoriza preenchê-las ou servi-las.

### 3.3 Execução solicitada pelo Sandbox

O comportamento-alvo definido é: o Sandbox pode apresentar e acompanhar missões, mas a execução deve utilizar a autoridade operacional e os agentes administrados pelo SCP original. A solicitação de execução deve ser segura, autenticada, idempotente e rastreável; credenciais permanecem no ambiente original. Resultados e estados devem retornar ao Sandbox por mecanismo de sincronização controlado.

Esse fluxo é requisito arquitetural definido; sua implementação integral ainda não foi comprovada.

## 4. Objetivo operacional em andamento — duas provas de ciclo completo

O responsável solicitou duas provas, nesta ordem:

1. Retomar e concluir automaticamente a missão existente no Sandbox que possui TR aprovado, sem inventar evidências ou marcar etapas como concluídas sem execução comprovada.
2. Criar uma missão sistêmica simples de teste, com TR aprovado automaticamente, e verificar se todo o ciclo — despacho, execução, documentos, etapas, persistência e conclusão — ocorre sem intervenção humana.

A missão de teste deve ser sistêmica, não uma missão humana que aguarda aprovação manual. A prova só será considerada válida quando houver evidências persistidas e estado final confirmado.

## 5. Evidências operacionais observadas em 2026-11-24

### 5.1 SCP original — agentes

Consulta ao projeto Supabase original `ufylccbdjfzydbwhpmpp`, schema `sofia`, tabela `agents`:

- 19 registros de agentes retornados com status `online`;
- 17 estavam com `connectionStatus=connected`;
- 2 estavam com `connectionStatus=configured`;
- 16 agentes conectados tinham saldo registrado de 300 créditos; um agente conectado (`meshwave`) tinha saldo 0; os dois agentes configurados não tinham saldo registrado;
- os horários de atualização de créditos observados eram de 20 a 22/11/2026.

Esses dados são uma fotografia da consulta, não uma garantia de disponibilidade no momento de uma execução posterior.

**Regra de elegibilidade já esclarecida pelo responsável:** a idade da última consulta de créditos, isoladamente, não deve excluir um agente operacional com saldo conhecido suficiente. Atualização de saldo deve ocorrer em background. Saldo desconhecido não deve ser tratado como suficiente.

### 5.2 Tarefa 46 no SCP original

Consulta à tabela `sofia.tasks` retornou:

- ID interno: 46;
- chave: `SCP-TASK-000046`;
- título: “Conciliação documental e garantia de TR na gênese de missões do SCP”;
- `statusId=1` (estado STAGED conforme mapeamento conhecido);
- `agentId=18`, agente INFO;
- `agentPinned=false`;
- `creatorType=user`;
- `manusTaskId=null`;
- `manusStatus=dispatch_pending`.

A tarefa não estava comprovadamente executada no momento da consulta. A última atualização de créditos do agente INFO retornada pelo banco era de 2026-11-22; isso não é, por si só, motivo para torná-lo inelegível.

O histórico anterior desta sessão registrou TR versão 5 como VALIDATED e Blueprint versão 3 como READY para essa tarefa; esses estados precisam ser reconfirmados antes de qualquer execução.

### 5.3 Sandbox — despacho e persistência

Na inspeção do repositório `meshwave65/SofiaControlPanel-Sandbox` foram observados:

- a migração `drizzle/0003_automatic_task_dispatch.sql` está desabilitada no Sandbox;
- `server/dispatchEndpoint.ts` contém endpoint interno que delega a `SofiaOrchestrator.startTask`;
- o código de execução existente ainda está acoplado ao serviço Manus, não ao modelo de seleção oportunista de executores definido neste registro;
- a persistência/espelhamento GitHub do Sandbox foi identificada em inspeção anterior como desabilitada;
- a tabela/modelo de agentes Sandbox contém campos sensíveis legados, que não devem receber credenciais do SCP original.

A consulta SQL ao banco Sandbox expirou por timeout nesta sessão. Portanto, não foi possível reconfirmar os registros e documentos da missão Sandbox nesta data.

### 5.4 Ferramentas de navegador

Playwright, Browser Use, Stagehand, Steel Browser e Anchor Browser foram citados como candidatos. Não foi realizado benchmark nem homologação nesta sessão. Nenhuma dessas opções foi configurada ou implantada.

## 6. Separação entre decisões, evidências e pendências

| Item | Classificação | Estado |
|---|---|---|
| Selecionar ferramenta suficiente de menor custo | Decisão explícita do responsável | ADOTADA |
| Escalonar somente quando necessário | Decisão explícita do responsável | ADOTADA |
| Planos com diferentes capacidades e conectores configuráveis | Diretriz arquitetural explícita | ADOTADA |
| TinyFish como dependência | Alternativa rejeitada/não adotada | NÃO UTILIZAR COMO PREMISSA |
| SCP original como fonte de verdade dos agentes | Decisão explícita do responsável | ADOTADA |
| Sandbox como espelho read-only de agentes | Decisão explícita do responsável | ADOTADA |
| Não replicar credenciais para Sandbox | Decisão explícita do responsável | ADOTADA |
| Execução de missões Sandbox via autoridade do SCP original | Requisito operacional definido | IMPLEMENTAÇÃO NÃO CONFIRMADA |
| Playwright/Browser Use/Stagehand/Steel/Anchor | Opções candidatas | NÃO HOMOLOGADAS |
| Concluir missão existente do Sandbox | Objetivo operacional | PENDENTE |
| Criar e concluir missão sistêmica de teste | Objetivo operacional | PENDENTE |
| Persistência e conclusão automática integral | Resultado esperado | NÃO DEMONSTRADO |

## 7. Restrições de execução e governança

- Não declarar missão concluída sem ORs, documentos, artefatos e estado final verificáveis.
- Não criar documentos ou resultados fictícios para preencher etapas.
- Não copiar credenciais entre projetos.
- Não fazer alterações em banco, código ou produção sem a autorização correspondente do responsável.
- Não confundir o repositório Foundation_MeshWave/BCE com o pipeline operacional do SofiaControlPanel. Este registro é documentação de conhecimento e decisões; não substitui OR, FOR, TR, Blueprint, Checkpoint ou Handoff canônicos do SCP.
- Preservar a distinção entre estado observado, decisão, requisito, proposta e implementação.

## 8. Próximas ações

1. Reconfirmar no banco Sandbox qual é a única missão com TR aprovado e recuperar TR, Blueprint, documentos e estado atuais.
2. Diagnosticar a indisponibilidade de consulta SQL ao Sandbox sem alterar políticas RLS ou estruturas por inferência.
3. Definir e implementar, após autorização, o caminho mínimo autenticado Sandbox → SCP original → executor → retorno de resultados.
4. Comparar executores gratuitos adequados e selecionar o de menor custo que satisfaça os critérios da missão; não introduzir TinyFish.
5. Executar a missão existente até o fim, registrando evidências reais.
6. Criar a missão sistêmica simples e comprovar o ciclo sem intervenção humana.
7. Atualizar este registro e DOM-06 com resultados, falhas e decisões efetivamente verificadas.

## 9. Referências de implementação consultadas

- [SofiaControlPanel original — dispatchEndpoint.ts](https://github.com/meshwave65/SofiaControlPanel/blob/main/server/dispatchEndpoint.ts)
- [SofiaControlPanel original — schema.ts](https://github.com/meshwave65/SofiaControlPanel/blob/main/drizzle/schema.ts)
- [SofiaControlPanel Sandbox — dispatchEndpoint.ts](https://github.com/meshwave65/SofiaControlPanel-Sandbox/blob/main/server/dispatchEndpoint.ts)
- [SofiaControlPanel Sandbox — sofiaOrchestrator.ts](https://github.com/meshwave65/SofiaControlPanel-Sandbox/blob/main/server/sofiaOrchestrator.ts)
- [SofiaControlPanel Sandbox — githubMissionMirror.ts](https://github.com/meshwave65/SofiaControlPanel-Sandbox/blob/main/server/githubMissionMirror.ts)
- [SofiaControlPanel Sandbox — schema.ts](https://github.com/meshwave65/SofiaControlPanel-Sandbox/blob/main/drizzle/schema.ts)

## 10. Histórico

| Data | Alteração |
|---|---|
| 2026-11-24 | Registro inicial das decisões de seleção oportunista de ferramentas, planos/provedores, governança de agentes SCP/Sandbox e objetivo de duas provas de execução automática. |

