# Classificação de fonte — F3.3/ID-206

## Metadados

| Campo | Valor |
|---|---|
| Contato | `F3.3/ID-206` |
| Fonte física | `KNOWLEDGE/meshwave65/20260422_Desenvolvimento de simulador - Manus/` |
| Tema relacionado | DOM-03 — rede mesh, comunicação e roteamento; lacuna §14.12 |
| Data/hora da auditoria | `2026-10-28 23:26 (-03:00)` |
| Claim | `BCE/locks/F3.3-ID206.lock.md`, publicado em `a1efa54` |
| Pré-registro | `BCE/sessoes/2026-10-28_f3-3-id206-abertura.md`, publicado em `a1efa54` |
| Skill | `meshwave-bce-curation`; versão/commit conforme checkout vigente no início da sessão |
| Estado | Classificação concluída; interface de simulador demonstrada, mas nenhuma implementação executável ou resultado reproduzível confirmado |
| Hashes pós-leitura | 5/5 correspondem ao pré-registro; artefatos brutos preservados |

## Síntese

ID-206 registra uma tarefa intitulada “Desenvolvimento de simulador” e uma interface de configuração para uma simulação de rede MeshWave. A imagem `img_000.jpg` mostra uma tela com grade de CPAs, usuários e conectividade, parâmetros de simulação e perfis de mobilidade, além do botão “Executar Simulação”. A captura `FULL.png` mostra uma interface Manus Lite com passos de criação de uma aplicação React, leitura de `App`, configuração Vite, tentativa de iniciar/expor um servidor React e interrupção por contexto longo.

O conjunto não contém o projeto React, o código Python anunciado na etapa “Implementação da Geração de Imagens no Simulador Python”, o arquivo `App`, dados, dependências, commit, versão, logs ou saída de execução. O único código recuperável é um fragmento incompleto e repetido de configuração Vite. Os rótulos “Reprodução da tarefa Manus concluída” e “Experimente você mesmo” são estados da interface/reprodução e não comprovam que uma simulação foi executada ou que o roteamento foi implementado.

## Artefatos e integridade

| Artefato | Bytes | SHA-256 | Observação da auditoria |
|---|---:|---|---|
| `content.txt` | 10.927 | `f03068434f639d9e9491029c24cad7bf3276aa54321ac9ac220af0466871f72f` | Transcrição de 605 linhas, fortemente repetitiva; repete rótulos de UI, fragmentos Vite e estados de reprodução. |
| `code_blocks.txt` | 682 | `3a64e3e4b0c15e1dac9c44111b6595fa3e376ead68b612a03e488e2754170e02` | Dois fragmentos quase idênticos de configuração Vite; importação de `defineConfig` e o restante do projeto não aparecem. |
| `links.txt` | 22 | `3794c198c4ad415f025776affe173db4e5a9078d4b01741d24477080aca13f5e` | Contém apenas `https://help.manus.im/`; não seguido. |
| `FULL.png` | 123.518 | `b4eccf72d35824d9ab80848de6b93a7b8b8cf831ebecac41fe89eeafc6873abc` | Captura 1280×845 px de interface Manus Lite, com passos de criação de aplicação React e interrupção por contexto longo. |
| `img_000.jpg` | 84.564 | `3552686377cb1c5555ec73ad0f5f1b9bd67fb53860efe9b3a3136e0213603b46` | Imagem 1024×768 px de formulário visual de parâmetros de simulação; extensão `.jpg`, conteúdo detectado como WebP. |

Os cinco hashes foram recalculados antes e depois da leitura e correspondem ao pré-registro. Nenhum arquivo em `KNOWLEDGE/` foi alterado.

## Achados por categoria de evidência

### Fatos observados

- A transcrição e a captura referem-se a uma tarefa chamada “Desenvolvimento de simulador”.
- `FULL.png` registra a criação/recriação de uma aplicação React, leitura de `App`, alteração do título, criação de interface, inicialização/exposição de servidor React e configuração Vite; a captura termina com a mensagem de que o contexto ficou longo.
- `img_000.jpg` mostra uma interface intitulada “Configure os parâmetros para a simulação da rede MeshWave”. A tela apresenta dimensões X/Y `10`/`10`, total de CPAs `100`, usuários por CPA `1`, raio de conexão `5`, TTL de busca `10`, total de usuários `100`, três etapas, dez tentativas por etapa, perfis de mobilidade `0.58`, `0.3`, `0.1` e `0.02` e total `1.000`. Há um botão “Executar Simulação”.
- A transcrição repete a expressão “Implementação da Geração de Imagens no Simulador Python”, mas não contém o arquivo Python ou um resultado de geração.
- `links.txt` contém somente um endereço de suporte do Manus; nenhum destino foi consultado.

### Código / possível implementação

Há **código transcrito parcial**, não implementação verificável do simulador. O fragmento contém `import react from '@vitejs/plugin-react'`, `import tailwindcss from '@tailwindcss/vite'`, `import path from 'path'` e uma configuração `defineConfig` com plugins React/Tailwind e alias `@`. O trecho aparece truncado ou com OCR defeituoso (`om 'vite'`) e não inclui `defineConfig` importado, `package.json`, `src/`, lógica de simulação, geração de imagens, algoritmo de vizinhança/encaminhamento ou qualquer arquivo Python.

### Interface / replay

As imagens demonstram uma interface de configuração e uma sequência de reprodução de tarefa Manus. Elas sustentam que uma tela ou mockup com os parâmetros descritos foi exibida. Não sustentam que o botão foi acionado com sucesso, que os parâmetros foram aplicados, que uma topologia foi criada, que usuários foram conectados, que pacotes foram encaminhados ou que algum resultado foi salvo.

### Protótipo / experimento

O conjunto pode ser classificado como **protótipo visual alegado** de uma interface de simulador. Não há experimento reproduzível: faltam comando, projeto completo, dependências, entradas, seed, saída, logs, teste, versão e ambiente. A frase “Reprodução da tarefa Manus concluída” refere-se à reprodução do fluxo na interface, não ao resultado técnico do simulador.

### Proposta, decisão e hipótese

Os parâmetros exibidos podem representar uma configuração proposta para simulação, mas o pacote não fornece especificação formal, justificativa, modelo de mobilidade, algoritmo de conexão, política de TTL ou decisão aprovada. Não se infere que os valores sejam calibrados, executáveis ou representativos de uma rede real.

### Duplicata / ruído

A transcrição contém repetição extensa da configuração Vite, dos títulos e dos estados de interface. Essas repetições não acrescentam evidência independente. O conteúdo de suporte do Manus é referência declarada e não foi seguido.

### Ausência crítica

Não foram localizados no pacote: código-fonte Python do simulador; projeto React completo; `App`; `package.json`; lockfile; versão/commit; dependências instaláveis; dados de entrada; seed; comando de execução; testes; logs; arquivos de saída; métricas; topologia; protocolo de roteamento; ou evidência de geração de imagem/encaminhamento.

## Implicação para DOM-03 §14.12

ID-206 reforça a existência de uma interface visual de configuração de simulação MeshWave, mas **não resolve** a lacuna sobre onde estão os fontes, versão, testes, dados e logs do simulador nem se há encaminhamento. Deve ser classificado como interface/replay com código transcrito parcial e proposta de protótipo, não como implementação verificável. O tema permanece em `REVISÃO`; a próxima verificação exige localizar um artefato-fonte completo e seus metadados sob novo caminho físico e claim.

## Segurança e tratamento de dados

Nenhum código foi executado, nenhum link foi seguido e nenhum serviço externo foi acessado. Não foram copiados tokens, senhas, chaves ou dados pessoais desnecessários. A classificação foi limitada aos cinco artefatos reivindicados e seus hashes.

## Proveniência

- Claim e estado: [`BCE/locks/F3.3-ID206.lock.md`](../locks/F3.3-ID206.lock.md), publicado em `a1efa54`.
- Pré-registro e hashes: [`BCE/sessoes/2026-10-28_f3-3-id206-abertura.md`](../sessoes/2026-10-28_f3-3-id206-abertura.md), publicado em `a1efa54`.
- Fonte bruta: `KNOWLEDGE/meshwave65/20260422_Desenvolvimento de simulador - Manus/`.
- Documento temático a atualizar: [`BCE/temas/rede-mesh-comunicacao-e-roteamento.md`](../temas/rede-mesh-comunicacao-e-roteamento.md).
