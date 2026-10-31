# Classificação de fonte — F3.3/ID-120

## Metadados

| Campo | Valor |
|---|---|
| Contato | `F3.3/ID-120` |
| Fonte física | `KNOWLEDGE/info/20260422_175707_É possível criar um app para simuladores_ - Manus/` |
| Tema relacionado | DOM-03 — rede mesh, comunicação e roteamento; relação operacional com frontend/PWA e simuladores |
| Data/hora da auditoria | `2026-10-28 23:31 (-03:00)` |
| Claim | `BCE/locks/F3.3-ID120.lock.md`, publicado em `4de1c3e` |
| Pré-registro | `BCE/sessoes/2026-10-28_f3-3-id120-abertura.md`, publicado em `4de1c3e` |
| Skill | `meshwave-bce-curation`; versão/commit conforme checkout vigente no início da sessão |
| Estado | Classificação concluída; replay de diagnóstico de PWA Vite/Vue com tela branca persistente, sem projeto ou build auditável |
| Hashes pós-leitura | 5/5 correspondem ao pré-registro; artefatos brutos preservados |

## Síntese

ID-120 registra a pergunta “É possível criar um app para simuladores?” e uma tarefa de diagnóstico de um frontend PWA em Vite + Vue. A transcrição afirma que a configuração de hosts permitidos foi ajustada para liberar validação por link público e que o backend estaria disponível em outro endpoint. Porém, quando o usuário tenta acessar o aplicativo no iPhone, a tela permanece branca. O replay registra várias tentativas de corrigir um componente Vue, reiniciar o frontend, investigar logs e preparar um build de produção, mas termina aguardando nova validação do usuário.

`FULL.png` mostra a interface Manus com orientações para testar em outro navegador/dispositivo, abrir o console do Safari, verificar logs detalhados e preparar um build de produção; o estado da tarefa está em “Entregar para validação do usuário”, 9/9, com reprodução concluída. `img_000.jpg` mostra um iPhone exibindo uma página completamente branca em um endereço `manus.computer`. `code_blocks.txt` contém somente saída do servidor Vite informando que a versão 6.3.5 iniciou na porta 5173. Não há código Vue, configuração de host, logs de erro, build de produção, backend, contrato de API, commit ou teste de simulador.

## Artefatos e integridade

| Artefato | Bytes | SHA-256 | Observação da auditoria |
|---|---:|---|---|
| `content.txt` | 89.877 | `aec36cac41f2470a7a4a3e9d0e7566afc6f5fb97d785aea5c2de07c0bfbbd125` | Transcrição repetitiva de diagnóstico de PWA; registra host allowlist, Vite/Vue, tela branca persistente, tentativas de correção e validação pendente. |
| `code_blocks.txt` | 226 | `0164719a266db8f35ee19590d3ce1accb0b15659e70f1bdb84824fed2ef3bdbd` | Apenas separador e saída do Vite; não contém código de aplicação. |
| `links.txt` | 117 | `0d411f2a06f369889129bbae0635df52ff2b0d390f80596578897e984d79f52e` | Dois endereços locais/encaminhados: frontend na porta 5173 e backend na porta 8000; não seguidos. |
| `FULL.png` | 185.957 | `4af7e459184f914981204c38cdb1ce517a4145376ec66083815cd3950ef0598c` | Captura 1280×845 px com diagnóstico de tela branca, sugestões de console/logs/build e entrega pendente ao usuário. |
| `img_000.jpg` | 139.287 | `b71c7068188b88d62c980ed2f52aa5619d41ec5872e152bea552b8cebed7f4a7` | Imagem 750×1334 px, conteúdo detectado como PNG apesar da extensão `.jpg`; iPhone com página branca em endereço `manus.computer`. |

Os cinco hashes foram recalculados antes e depois da leitura e correspondem ao pré-registro. Nenhum arquivo em `KNOWLEDGE/` foi alterado.

## Achados por categoria de evidência

### Fatos observados

- A tarefa trata de um app para simuladores e identifica o frontend como `Vite + Vue`.
- A transcrição registra ajuste de hosts permitidos, tentativa de liberar acesso público e referência a frontend na porta 5173 e backend na porta 8000.
- O usuário relata “Tela fica em branco” no iPhone; após uma alegada correção de componente e reinício do frontend, a fonte registra que a tela branca persiste.
- A captura `img_000.jpg` mostra uma tela branca no navegador do iPhone, sem interface do simulador, logs ou gráficos.
- `FULL.png` registra recomendações para testar outro navegador/dispositivo, usar o console do Safari, verificar logs detalhados e preparar um build de produção. A etapa final permanece aguardando validação do usuário.
- `code_blocks.txt` mostra somente o servidor Vite 6.3.5 pronto em `localhost:5173` e em um endereço de rede interno; isso é log de inicialização, não código de aplicação nem prova de renderização.

### Implementação / código

Não há código-fonte Vue, componentes, `vite.config`, `package.json`, dependências, configuração de host, backend, endpoint, logs de erro ou build de produção. A saída Vite confirma apenas que algum servidor de desenvolvimento foi iniciado em uma porta, não que o PWA foi compilado corretamente, que as rotas foram carregadas ou que os simuladores puderam ser selecionados/executados.

### Interface / replay

A evidência demonstra um replay de diagnóstico e uma captura de navegador móvel em branco. O estado “Reprodução da tarefa Manus concluída” e o progresso 9/9 referem-se à tarefa de reprodução/entrega, não ao funcionamento do app nem à execução de simuladores.

### Protótipo / experimento

O pacote sustenta uma tentativa de protótipo frontend/PWA e um plano de diagnóstico. Não sustenta experimento reproduzível: faltam código, build, dependências, dispositivo/versão do Safari, console, logs, requests/responses, dados de simulador, comandos, seed e resultados gráficos. A validação foi explicitamente deixada para o usuário.

### Alegações e limites

A transcrição afirma que o host allowlist foi corrigido, que uma causa possível do componente foi corrigida e que o frontend foi reiniciado. Essas são alegações narradas no replay; não existem diff, commit, log detalhado ou artefato que permita confirmá-las. O único resultado diretamente observado é a tela branca no iPhone e a repetição de “Tela fica em branco”.

### Ausência crítica

Não foram localizados: projeto Vue; configuração de hosts; `package.json`; lockfile; componentes; código dos simuladores; backend; API; logs de navegador/servidor; build de produção; versão/commit; teste de seleção/execução; gráficos; resultados ou evidência de roteamento.

## Implicação para DOM-03 §14.12

ID-120 documenta uma camada de frontend/PWA destinada a selecionar e executar simuladores, mas a evidência disponível mostra falha de carregamento em iPhone e validação incompleta. O contato não fornece implementação do simulador, código de roteamento, logs ou resultados. Deve ser classificado como replay de diagnóstico de interface com falha observada, não como simulador executável ou evidência de encaminhamento. A lacuna de DOM-03 permanece aberta.

## Segurança e tratamento de dados

Nenhum código foi executado, nenhum link foi seguido, nenhum serviço externo foi acessado e nenhum segredo foi copiado. Os endereços `manus.computer` foram preservados somente como strings observadas nos artefatos.

## Proveniência

- Claim e estado: [`BCE/locks/F3.3-ID120.lock.md`](../locks/F3.3-ID120.lock.md), publicado em `4de1c3e`.
- Pré-registro e hashes: [`BCE/sessoes/2026-10-28_f3-3-id120-abertura.md`](../sessoes/2026-10-28_f3-3-id120-abertura.md), publicado em `4de1c3e`.
- Fonte bruta: `KNOWLEDGE/info/20260422_175707_É possível criar um app para simuladores_ - Manus/`.
- Documento temático a atualizar: [`BCE/temas/rede-mesh-comunicacao-e-roteamento.md`](../temas/rede-mesh-comunicacao-e-roteamento.md).
