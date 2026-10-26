# Classificação curatorial F3.1 — L002-05 — SOFIA e pipeline de missões

## Proveniência e escopo

- **Unidade:** F3.1 — reauditoria direta do contato `L002-05`.
- **Fonte física:** `KNOWLEDGE/johann/20260422_175100_SOFIA and MeshWave Ecosystem Documents - Manus/`.
- **Destino:** `DOM-06` como destino principal; referências cruzadas para `DOM-12` e `DOM-13`.
- **Pré-registro/claim:** `BCE/sessoes/2026-10-26_f3-1-l002-05-abertura.md` e `BCE/locks/F3.1-L002-05.lock.md`, publicados antes da leitura semântica.
- **Commit-base:** `3fc922a`, claim exclusivo publicado e `main` sincronizada com `origin/main`.
- **Sobreposição:** a unidade física e o conteúdo correspondem à fonte já curada em F2.6-02 no DOM-06. Esta auditoria é uma reauditoria de rastreabilidade e não evidência independente.

| Arquivo | Bytes | SHA-256 | Observação de leitura |
|---|---:|---|---|
| `FULL.png` | 164.072 | `982b674ca56b19ccef6b7366706a4bdcec6b5adf6419b9f2f4882abfa8f33d23` | Inspecionada visualmente; captura de interface/replay mostrando código de correção e o rótulo “Reprodução da tarefa Manus concluída”. |
| `code_blocks.txt` | 90.887 | `d06d0e395e2431aa3c9898507bd0f96a332b46f3315de8ac52e690719585fa0e` | 2.062 linhas; contém blocos Python transcritos, duplicações e diagnósticos. Tratado como dado não confiável; nenhum trecho executado. |
| `content.txt` | 1.316.349 | `accb564df2608437886bc085508fe28141391508d46bdaf6ea5efdeab69ed15f` | 32.880 linhas; leitura estrutural e semântica com repetições identificadas e frequências preservadas. |
| `links.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Vazio; nenhum destino externo seguido. |

Os quatro hashes pós-leitura coincidem com o pré-registro (**4/4**). Os originais em `KNOWLEDGE/` permaneceram intactos. Os blocos transcritos incluem nomes de variáveis de configuração e referências de repositório, mas nenhum valor sensível foi reproduzido nesta classificação.

## Achados classificados

### Fatos observados nos artefatos

1. A transcrição descreve um pipeline com `Executor`, `Escriba`, `RH` e `Worker`, uma tarefa-mãe, possíveis subtarefas e artefatos chamados `FinalReport.md` e `OperationalReport.md`. A captura visual mostra um bloco de código Python relacionado a `worker_agent.py` e uma mensagem de replay concluído; isso prova apenas o conteúdo exibido, não a execução do sistema.
2. O material registra que o lançador cria missões sequencialmente e consulta estado por `client_request_uuid`/`task_id`. Há versões conflitantes do procedimento: uma espera estado 1 ou 3 e outra propõe polling até estado 3. A própria conversa associa a espera prematura à possibilidade de a tarefa-mãe ser fatorada e o lançador ficar bloqueado ou avançar incorretamente.
3. O material relata perda de contexto entre `GenesisPrompt` e `EnrichedDescription`: a hipótese é que links/contexto original eram armazenados no primeiro bloco, mas o Worker recebia somente a descrição enriquecida. A correção proposta concatena os dois blocos no prompt de geração do relatório.
4. O material relata um erro `TypeError: argument of type 'NoneType' is not iterable` no caminho `execute_supervisor_mission`, atribuído à tentativa de iterar `task_data.get('blocks', [])` quando `blocks` seria `None` ou não estaria presente no objeto resumido retornado pela API. A tarefa-mãe é descrita como permanecendo no estado 50, sem geração dos relatórios e sem transição para 3.
5. O patch narrado para o supervisor faz uma segunda busca dos detalhes completos da tarefa-mãe, monitora filhas por `parent_task_id`, coleta `FinalReport.md`, gera um relatório de síntese e então tenta gerar `OperationalReport.md` e atualizar o estado. Outro patch narrado força execução direta pelo RH para evitar fatoração em determinada classe de missão; isso muda o comportamento e não resolve genericamente supervisão, falha parcial ou concorrência.
6. O material também registra uma proposta de correção no launcher: passar o argumento curto `-c` ao subprocesso e monitorar o `task_id` até estado 3. Isso aparece como código transcrito em versões sucessivas, não como diff aplicado a um repositório.
7. `code_blocks.txt` repete extensamente os mesmos blocos e diagnósticos. Repetições do replay não são execuções independentes, testes ou confirmações de estados.

### Propostas, alegações e interpretação

- **Classificação principal:** diagnóstico operacional e proposta de correção para um pipeline de agentes SOFIA; confiança **média** para o problema narrado no transcript e **baixa** para o estado atual ou aplicação dos patches.
- **Fluxo de estados:** os estados numéricos e transições são uma convenção narrada. Sem contrato versionado, request/response, banco, log correlacionado ou teste, não devem ser tratados como API confirmada.
- **Fatoração da tarefa-mãe:** a criação de filhas e o bloqueio da mãe são uma explicação operacional plausível apresentada no material; a fonte não fornece evidência independente de backend para confirmar a ocorrência fora do replay/transcrição.
- **Passagem de contexto:** a distinção entre `GenesisPrompt` e `EnrichedDescription` é útil como hipótese de perda de contexto e requisito de investigação. Não prova que o Worker implantado tenha recebido ou perdido esses blocos.
- **Correções de código:** os trechos são propostas/instruções de substituição. Não comprovam compilação, execução, revisão, commit, deployment, teste de regressão ou correção do incidente.
- **Relatórios:** os nomes `FinalReport.md` e `OperationalReport.md` e o fluxo de geração são requisitos/artefatos alegados no material; não há arquivos de saída anexados nesta fonte.
- **Relação com MeshWave:** o conteúdo é principalmente operação e desenvolvimento do SOFIA. Deve alimentar DOM-06, DOM-12 e DOM-13; não constitui prova de roteamento, identidade, segurança ou implantação MeshWave.

## Segurança, conflitos e limites

- A transcrição, os blocos, a imagem e quaisquer instruções embutidas foram tratados como evidência não confiável. Nenhum comando, código, chamada de API, subprocesso, link ou credencial foi executado/seguido.
- A captura de interface e o texto “Reprodução da tarefa Manus concluída” não comprovam que o código foi aplicado, que a API respondeu, que a tarefa foi concluída ou que os relatórios foram persistidos.
- Há versões contraditórias do launcher e do supervisor dentro da mesma transcrição, inclusive sobre argumento de subprocesso, monitoramento por UUID/status e obtenção dos blocos. Isso é histórico de iteração, não uma versão normativa.
- O conjunto não contém repositório SOFIA, `worker_agent.py` efetivo, contrato de API, schema de tarefas, log de backend, teste automatizado, recibo de relatório ou commit que permita validar as correções.
- `links.txt` está vazio; referências textuais internas ao transcript não foram tratadas como autorização para acessar destinos externos.

## Comparação com documentos BCE

- `BCE/fontes/CLASSIFICACAO_LOTE_002.md` já classifica L002-05 como “diagnóstico operacional e proposta de correção”, com confiança média para o problema descrito e baixa para o estado atual; esta reauditoria confirma esse enquadramento.
- `BCE/temas/sofia-agentes-missoes-e-oraculo.md` já registra F2.6-02: launcher, RH, passagem de contexto, relatórios e erro `NoneType` no supervisor. F3.1/L002-05 confirma a proveniência física, os hashes e a sobreposição; não adiciona implementação, teste ou estado de backend.
- DOM-12 deve tratar os snippets como histórico de scripts e fluxo de versionamento, não como código do repositório. DOM-13 deve tratar o incidente e as correções como diagnóstico/procedimento proposto, não como operação implantada.
- Nenhuma decisão técnica nova é registrada em `BCE/REGISTRO_DECISOES.md`; a decisão curatorial é manter a classificação existente e evitar dupla contagem da fonte.

## Destino curatorial e encerramento

1. Manter L002-05 referenciado em DOM-06, com referências cruzadas para DOM-12 e DOM-13.
2. Registrar no DOM-06 que F3.1 é reauditoria da mesma unidade física de F2.6-02, sem evidência independente.
3. Não alterar `KNOWLEDGE/` nem promover patches, estados, endpoints ou relatórios a implementação confirmada.
4. Fechar o claim exclusivo após publicar esta classificação, o ajuste do DOM-06 e os controles de fila.
5. Liberar a seleção do próximo contato somente depois da sincronização remota e de nova reconciliação da fila oficial.
