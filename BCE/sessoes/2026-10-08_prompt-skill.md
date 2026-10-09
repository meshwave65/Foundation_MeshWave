# Sessão 2026-10-08 — atualização do prompt para uso da skill

## Escopo e estado inicial

- Início: 2026-10-08 22:06 (-03:00)
- Fim: 2026-10-08 22:07 (-03:00)
- Agente: Manus — manutenção do prompt de retomada BCE
- Branch: `main`
- Commit inicial: `faca103` — registro do diretório canônico `skills/`
- Commit de conteúdo publicado: `ddda1d5` — `docs(bce): atualizar prompt para skill de curadoria`
- Solicitação: atualizar `BCE/PROMPT_RETOMADA_AGENTE.md` para que agentes iniciantes usem a nova skill.

## Alterações e validação

O prompt agora instrui o agente a ler `AGENTS.md` e carregar `skills/meshwave-bce-curation/SKILL.md` antes das regras BCE. Ele esclarece que a skill orienta o fluxo, mas não autoriza trocar ou ampliar a fila de curadoria: solicitações explicitamente fora dessa fila devem permanecer limitadas ao seu escopo e preservar o item e o caminho pendentes. Também reforça que o conteúdo histórico de `KNOWLEDGE/` deve ser tratado como evidência, não como instrução executável. O protocolo A–I foi atualizado para nomear os novos pontos de entrada.

O arquivo editado é o prompt canônico no repositório, `BCE/PROMPT_RETOMADA_AGENTE.md`, correspondente ao link GitHub indicado pelo usuário. `git diff --check` passou e o commit `ddda1d5` foi publicado em `origin/main`.

## Arquivos envolvidos

- `BCE/PROMPT_RETOMADA_AGENTE.md`
- `BCE/CONTROLE_MESTRE.md`
- `BCE/sessoes/2026-10-08_prompt-skill.md` — este checkpoint

Nenhum arquivo em `KNOWLEDGE/` foi lido ou alterado nesta unidade.

## Continuidade da BCE

- Item em andamento: `F2.6`; DOM-06 permanece em `REVISÃO` e a cobertura profunda continua em 9/23.
- Último item de curadoria de fontes concluído: `F2.6-01`.
- Próxima ação exata preservada: antes de ler, pré-registrar `KNOWLEDGE/johann/20260422_175100_SOFIA and MeshWave Ecosystem Documents - Manus/`; validar fisicamente e anotar caminhos, tamanhos e hashes de `content.txt`, `code_blocks.txt`, `links.txt` e imagens no checkpoint seguinte; comparar com DOM-06 e atualizá-lo.
- Conflitos/lacunas e impedimentos: sem alteração nesta unidade; nenhum impedimento novo.
- Commit de conteúdo publicado: `ddda1d5`.
- Commit deste controle/checkpoint: identificar pelo histórico Git após a publicação.
