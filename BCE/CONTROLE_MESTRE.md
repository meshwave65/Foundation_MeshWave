# BCE MeshWave — Controle Mestre de Continuidade

> **Documento operacional.** Atualizar este arquivo em todo checkpoint relevante e fazer commit imediatamente. Um agente que retome a tarefa deve conseguir continuar sem ler o histórico do chat.

## Estado atual

| Campo | Valor |
|---|---|
| Status global | `EM_ANDAMENTO — FASE 0: fundação operacional` |
| Última atualização | 2026-10-08 |
| Último commit confirmado | `4a0b1e3` — `docs(bce): registrar decisoes curatoriais iniciais` |
| Branch de trabalho | `main` |
| Último item concluído | `F0.4` — registro inicial de decisões curatoriais |
| Item em andamento | `F0.5` — inventário técnico de `KNOWLEDGE` |
| Próximo item | `F0.6` — criar template de documento de tema |
| Impedimento atual | Nenhum para leitura/escrita GitHub; curadoria de conteúdo ainda não iniciada |
| Responsável pela sessão | Agente BCE MeshWave |

## Como retomar em cinco minutos

1. `git checkout main && git pull --ff-only`;
2. ler `BCE/ORIENTACAO_AGENTES.md`;
3. ler esta tabela e localizar o primeiro item `EM_ANDAMENTO` ou `PENDENTE` com maior prioridade;
4. verificar `git log --oneline -10` e confirmar o último commit publicado;
5. ler o checkpoint mais recente em `BCE/sessoes/`;
6. executar apenas o próximo passo descrito no item;
7. atualizar esta tabela antes de encerrar;
8. fazer commit e push separados para cada unidade lógica.

## Regras de status

- `PENDENTE`: ainda não iniciado.
- `EM_ANDAMENTO`: o próximo agente deve continuar este item.
- `BLOQUEADO`: existe dependência explícita registrada na coluna de impedimento.
- `CONCLUÍDO`: evidências, fontes, documentos, referências, commit e próximo passo foram registrados.
- `REVISÃO`: existe uma versão utilizável, mas requer conferência contra fontes novas ou conflitantes.

## Backlog operacional

### Fase 0 — Fundação da BCE

| ID | Prioridade | Entrega | Status | Evidência/commit | Próxima ação exata |
|---|---:|---|---|---|---|
| F0.1 | P0 | Orientação de agentes | CONCLUÍDO | `1402184` | Nenhuma |
| F0.2 | P0 | Controle mestre | CONCLUÍDO | `2e6a935` | Atualizado por este checkpoint |
| F0.3 | P0 | Índice curatorial inicial | CONCLUÍDO | `849a31b` | Revisar após inventário de conteúdo |
| F0.4 | P0 | Registro de decisões | CONCLUÍDO | `4a0b1e3` | Registrar decisões técnicas nos documentos de tema |
| F0.5 | P0 | Inventário técnico de `KNOWLEDGE` | EM_ANDAMENTO | levantamento preliminar | Gerar contagens, grupos, hashes e lista de fontes |
| F0.6 | P1 | Modelo/template de documento de tema | PENDENTE | — | Criar template reutilizável em `BCE/temas/_TEMPLATE.md` |
| F0.7 | P1 | Primeiro checkpoint de sessão | PENDENTE | — | Registrar a sessão após concluir F0.1–F0.6 |

### Fase 1 — Inventário e classificação das fontes

| ID | Entrega | Status | Dependência |
|---|---|---|---|
| F1.1 | Catálogo de todos os conjuntos de extração | PENDENTE | F0.5 |
| F1.2 | Classificação por conta, tema e tipo de artefato | PENDENTE | F1.1 |
| F1.3 | Detecção de títulos genéricos, duplicatas e fontes vazias | PENDENTE | F1.1 |
| F1.4 | Catálogo de imagens e relação com textos | PENDENTE | F1.1 |
| F1.5 | Catálogo de códigos e evidências de implementação | PENDENTE | F1.1 |
| F1.6 | Mapa de links e referências externas | PENDENTE | F1.1 |
| F1.7 | Relatório de lacunas e qualidade das fontes | PENDENTE | F1.2–F1.6 |

### Fase 2 — Mapa curatorial e documentos de domínio

| ID | Entrega | Status | Dependência |
|---|---|---|---|
| F2.1 | Documento de visão geral do ecossistema MeshWave | PENDENTE | F1.7 |
| F2.2 | Arquitetura geral e implantação | PENDENTE | F1.7 |
| F2.3 | Mesh networking, comunicação e roteamento | PENDENTE | F1.7 |
| F2.4 | Identidade, identificação de equipamento e DIDs | PENDENTE | F1.7 |
| F2.5 | ARC, autenticação contextual e inferência bayesiana | PENDENTE | F1.7 |
| F2.6 | SOFIA, agentes, missões e persistência de conhecimento | PENDENTE | F1.7 |
| F2.7 | Aplicações, simuladores e interfaces | PENDENTE | F1.7 |
| F2.8 | Hardware, dispositivos e infraestrutura | PENDENTE | F1.7 |
| F2.9 | Segurança, privacidade, LGPD e governança | PENDENTE | F1.7 |
| F2.10 | Estratégia, parceiros, patentes e implantação | PENDENTE | F1.7 |
| F2.11 | Desenvolvimento, versionamento e operações | PENDENTE | F1.7 |

### Fase 3 — Curadoria profunda

| ID | Entrega | Status | Dependência |
|---|---|---|---|
| F3.1 | Consolidar fontes do domínio prioritário 1 | PENDENTE | F2 |
| F3.2 | Reconstruir arqueologia das decisões | PENDENTE | F3.1 |
| F3.3 | Validar estado da arte contra código e imagens | PENDENTE | F3.1 |
| F3.4 | Registrar conflitos, descartes e hipóteses | PENDENTE | F3.1 |
| F3.5 | Publicar revisão do domínio | PENDENTE | F3.2–F3.4 |
| F3.6 | Repetir para cada domínio | PENDENTE | F3.5 |

### Fase 4 — Integração e manutenção evolutiva

| ID | Entrega | Status | Dependência |
|---|---|---|---|
| F4.1 | Mapa de relações entre documentos | PENDENTE | F3 |
| F4.2 | Índice navegável e referências cruzadas | PENDENTE | F4.1 |
| F4.3 | Auditoria de cobertura de fontes | PENDENTE | F3–F4 |
| F4.4 | Auditoria de rastreabilidade e conflitos | PENDENTE | F3–F4 |
| F4.5 | Procedimento de atualização contínua | PENDENTE | F4.1–F4.4 |

## Inventário inicial conhecido

Levantamento preliminar do clone em 2026-10-08:

- `KNOWLEDGE/`: aproximadamente **1.364 arquivos**;
- aproximadamente **286 diretórios**;
- aproximadamente **123 MB**;
- **273** conjuntos contendo `content.txt`, `code_blocks.txt` e `links.txt`;
- **273 PNGs** e **268 JPGs**;
- **2 scripts Python** de extração;
- não foram encontrados arquivos chamados `context.txt` ou `link.txt` no levantamento inicial;
- a estrutura observada usa diretórios por conta e nomes de tarefas com timestamp;
- existem fontes potencialmente alheias ao escopo MeshWave, que deverão ser classificadas como fora de escopo, contexto externo ou ruído — nunca apagadas sem decisão registrada.

Esses números são uma fotografia inicial, não um inventário definitivo. F0.5 deve gerar a contagem reproduzível e versionada.

## Protocolo de checkpoint da sessão

Ao iniciar uma sessão, copiar e preencher:

```markdown
### Sessão YYYY-MM-DD — agente/identificador
- Início:
- Commit inicial:
- Item assumido:
- Objetivo desta sessão:
- Fontes previstas:
- Resultado esperado:
```

Ao terminar:

```markdown
- Fim:
- Commit(s) publicados:
- Fontes lidas:
- Arquivos criados/alterados:
- Decisões registradas:
- Conflitos/lacunas:
- Último ponto concluído:
- Próximo passo exato:
- Impedimentos:
```

O checkpoint detalhado deve ser salvo em `BCE/sessoes/AAAA-MM-DD_<identificador>.md` quando a sessão ultrapassar uma alteração simples.

## Critério de passagem entre agentes

O agente atual só deve declarar a tarefa transferível quando:

- o `Estado atual` estiver atualizado;
- houver um único próximo passo inequívoco;
- os commits estiverem publicados;
- fontes parcialmente processadas estiverem marcadas;
- nenhum trabalho não publicado estiver implícito no chat;
- eventuais bloqueios estiverem escritos neste documento.

## Histórico de checkpoints

| Data | Agente | Evento | Commit | Próximo passo |
|---|---|---|---|---|
| 2026-10-08 | Agente BCE MeshWave | Criada orientação operacional | `1402184` | Criar controle mestre |
| 2026-10-08 | Agente BCE MeshWave | Criado controle mestre | `2e6a935` | Criar índice curatorial |
| 2026-10-08 | Agente BCE MeshWave | Criado índice curatorial | `849a31b` | Criar registro de decisões |
| 2026-10-08 | Agente BCE MeshWave | Criado registro de decisões | `4a0b1e3` | Iniciar inventário técnico de `KNOWLEDGE` |
