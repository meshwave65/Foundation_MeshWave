# Classificação de fonte — F3.3/ID-117

## Metadados

| Campo | Valor |
|---|---|
| Contato | `F3.3/ID-117` |
| Fonte física | `KNOWLEDGE/info/20260422_175452_Como criar um simulador gráfico com execução simplificada - Manus/` |
| Tema relacionado | DOM-03 — rede mesh, comunicação e roteamento; relação operacional com simulador gráfico e execução local |
| Data/hora da auditoria | `2026-10-31 10:46 (-03:00)` |
| Claim | `BCE/locks/F3.3-ID117.lock.md`, publicado em `5618459` |
| Pré-registro | `BCE/sessoes/2026-10-31_f3-3-id117-abertura.md`, publicado em `5618459` |
| Estado | Classificação concluída; replay de criação de atalho `.desktop` para um script de simulador, sem script ou aplicação anexada |
| Hashes pós-leitura | 4/4 correspondem ao pré-registro; artefatos brutos preservados |

## Síntese

ID-117 registra uma tarefa para criar e entregar um atalho de desktop para execução de um “Simulador de Rede”. O conteúdo do atalho declara `Name=Simulador de Rede`, `Comment=Executa o simulador de roteamento em rede` e um comando `Exec` que muda para `$(xdg-user-dir DESKTOP)/simulation_app` e executa `./run_simulator_ubuntu.sh`. O terminal fica visível (`Terminal=true`) para permitir observação de logs.

`FULL.png` mostra a interface Manus com instruções sobre o ícone genérico, o uso do terminal, a importância do caminho do script e a necessidade de informar um caminho alternativo se a pasta não estiver na Área de Trabalho. A tela mostra o cartão `simulador_rede.desktop`, a etapa “Create and deliver a desktop shortcut file for execution” e o rótulo “Tarefa concluída”. Isso documenta a entrega/replay do atalho, não a execução do simulador.

`code_blocks.txt` contém essencialmente o mesmo conteúdo `.desktop`, repetido, incluindo o comando para executar `run_simulator_ubuntu.sh`. Não há o próprio script, o diretório `simulation_app`, código Python/JavaScript, dependências, dados, logs ou saída de execução. `links.txt` está vazio.

## Artefatos e integridade

| Artefato | Bytes | SHA-256 | Observação da auditoria |
|---|---:|---|---|
| `content.txt` | 10.988 | `c2783c46e3b1dee27919754cc0169fa25bd1ef5e47e2700086920860191e0200` | Transcrição repetitiva da criação/entrega do atalho e da tarefa Manus concluída. |
| `code_blocks.txt` | 680 | `aa59d3dfc87a555bd6254322cd8a8264f4573e9d37501717a75734878b52d131` | Bloco `.desktop` repetido; aponta para script externo não anexado. |
| `links.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Vazio. |
| `FULL.png` | 186.228 | `520520fa7a60305eded372b9424dfa7f673aa3073f14cfc9c505134b7fb51c0f` | Captura 1280×845 px da instrução de atalho e do estado visual de tarefa concluída. |

Os quatro hashes foram recalculados antes e depois da leitura e correspondem ao pré-registro. Nenhum arquivo em `KNOWLEDGE/` foi alterado.

## Achados por categoria de evidência

### Fatos observados

- O conteúdo declara um atalho de desktop denominado `Simulador de Rede`.
- O comando declarado é `cd "$(xdg-user-dir DESKTOP)/simulation_app" && ./run_simulator_ubuntu.sh`.
- O atalho declara `Terminal=true`, `Type=Application` e categorias `Application;Network;Simulation;`.
- A captura mostra o cartão `simulador_rede.desktop` e a etapa de criação/entrega marcada como concluída.
- `links.txt` está vazio.

### Implementação / código

Não há o arquivo `run_simulator_ubuntu.sh`, o diretório `simulation_app`, o executável, o código-fonte do simulador, dependências, configuração, dados de entrada, seed, logs ou saída. O bloco `.desktop` é configuração de lançamento e não implementa o simulador nem comprova que o caminho exista.

### Interface / replay

A evidência é um replay de criação e entrega de um atalho de desktop. O rótulo “Tarefa concluída” e o progresso 11/11 significam conclusão da tarefa de criação/entrega do atalho, não execução do script ou do simulador de roteamento.

### Protótipo / experimento

ID-117 sustenta, no máximo, uma proposta operacional de como iniciar um simulador local por atalho. Não sustenta experimento reproduzível: faltam fonte, ambiente, dependências, comando validado, logs, dados, métricas, topologia e resultados de rede.

### Alegações e limites

A frase “Executa o simulador de roteamento em rede” é o comentário do arquivo `.desktop`, não evidência de que o programa executa roteamento. A captura não mostra terminal aberto, script rodando, interface do simulador, topologia, tráfego ou métricas. A transcrição repete o bloco e o estado de tarefa, sem demonstrar teste independente.

### Ausência crítica

Não foram localizados: `run_simulator_ubuntu.sh`; diretório `simulation_app`; código do simulador; dependências; versão/commit; logs; testes; dados; seed; topologia; métricas; saída gráfica; ou evidência de encaminhamento.

## Implicação para DOM-03 §14.12

ID-117 acrescenta uma instrução de lançamento local para um simulador de roteamento alegado, mas não fornece o alvo do atalho nem prova de execução. Deve ser classificado como **configuração/replay de inicialização**, não como simulador executável ou evidência de encaminhamento. A lacuna de DOM-03 permanece aberta.

## Segurança e tratamento de dados

Nenhum código foi executado, nenhum link foi seguido, nenhum serviço externo foi acessado e nenhum segredo foi copiado. O comando shell foi tratado como dado textual não confiável.

## Proveniência

- Claim e estado: [`BCE/locks/F3.3-ID117.lock.md`](../locks/F3.3-ID117.lock.md), publicado em `5618459`.
- Pré-registro e hashes: [`BCE/sessoes/2026-10-31_f3-3-id117-abertura.md`](../sessoes/2026-10-31_f3-3-id117-abertura.md), publicado em `5618459`.
- Fonte bruta: `KNOWLEDGE/info/20260422_175452_Como criar um simulador gráfico com execução simplificada - Manus/`.
- Documento temático a atualizar: [`BCE/temas/rede-mesh-comunicacao-e-roteamento.md`](../temas/rede-mesh-comunicacao-e-roteamento.md).
