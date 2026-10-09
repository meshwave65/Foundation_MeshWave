# Skills do projeto

Este diretório é o armazenamento canônico das skills reutilizáveis específicas do repositório `Foundation_MeshWave`. Cada skill deve ter seu próprio subdiretório, contendo um `SKILL.md` com frontmatter YAML (`name` e `description`) e instruções focadas; inclua `scripts/`, `references/` ou `templates/` somente quando forem necessários. Valide skills novas ou alteradas com o validador oficial antes de publicar.

## Catálogo

| Skill | Caminho | Uso |
|---|---|---|
| `meshwave-bce-curation` | [`skills/meshwave-bce-curation/SKILL.md`](meshwave-bce-curation/SKILL.md) | Retomada da BCE, auditoria de fontes, classificação de evidências, atualização de documentos e checkpoints. |

Os agentes encontram a skill de curadoria pela instrução raiz [`AGENTS.md`](../AGENTS.md) e pela orientação da BCE. Mantenha cada skill em apenas uma cópia canônica; não duplique o conteúdo em caminhos de compatibilidade, para evitar divergência.
