# Fronteiras de domínio, projetos compartilhados e RLS

## Metadados

| Campo | Valor |
|---|---|
| Tipo | Decisão técnica/documental |
| Domínios relacionados | MeshWave, SOFIA/Sofia Control Panel, projetos e módulos compartilhados |
| Status | ADOTADA como regra de escopo |
| Data do registro | 2026-11-13 |
| Proveniência | Contexto do responsável, reconciliado com a auditoria operacional Sofia #14 e a separação documental do Foundation_MeshWave |

## Decisão

As tabelas existentes no banco Supabase não devem ser consideradas automaticamente pertencentes ao Sofia Control Panel ou ao núcleo operacional MeshWave apenas por estarem no mesmo projeto Supabase.

O histórico correto é que vários projetos foram inicialmente construídos sob a conta `meshwave65`, o que criou uma base compartilhada e uma mistura de estruturas. Posteriormente, foi iniciada uma migração da estrutura MWN para uma nova conta/projeto `mwn`, mas a migração ficou parcial e não foi concluída. Durante esse processo, permaneceram dúvidas e dificuldades principalmente na transferência de `auth.users` e dos usuários associados.

Assim, uma tabela pública pode ser de outro módulo, projeto legado, integração ou domínio compartilhado; mas também pode ser uma estrutura do MWN que ficou no ambiente antigo por causa da migração incompleta. A ausência de Row Level Security (RLS), isoladamente, **não deve ser classificada como falha específica do SCP** nem motivar a aplicação indiscriminada de RLS. Ela também não deve ser presumida como segura: o contexto de conta compartilhada e migração parcial mantém um risco residual de segurança e governança que precisa ser tratado em uma auditoria de separação/migração.

Qualquer avaliação de RLS deve começar pela identificação do proprietário funcional, do consumidor, do caminho de acesso e do contrato de segurança de cada tabela. A decisão de habilitar RLS pertence ao domínio responsável e exige políticas compatíveis com os clientes existentes; habilitar RLS sem esse mapeamento pode quebrar integrações legítimas.

## Fronteiras de responsabilidade

### Foundation_MeshWave

O Foundation_MeshWave é o repositório curatorial e arquitetural do ecossistema. Ele registra conceitos, decisões, fronteiras de domínio, proveniência e limitações. Não deve transformar uma observação operacional isolada em regra global de segurança sem identificar o domínio responsável.

### Sofia / Sofia Control Panel

O schema `sofia` possui modelo operacional próprio, com identidade local (`sofia.users`) e tabelas de missões, tarefas, agentes e mensagens. As políticas de acesso e o Realtime do messenger Sofia devem ser avaliados especificamente para essas tabelas e para os clientes do SCP.

### Outros módulos, projetos e legado de migração

Tabelas em `public` podem servir a MeshWave, UMS/MWN, MeshWalker, integrações, protótipos, legados ou outros projetos. Algumas podem ter permanecido na conta/projeto histórico `meshwave65` por causa da migração parcial para `mwn`. Relações, RLS, triggers e políticas dessas tabelas não devem ser alteradas em nome do SCP sem confirmação explícita do domínio proprietário e do estado de migração.

## Contexto de migração MWN

O uso inicial da conta `meshwave65` como base comum para vários projetos produziu acoplamento operacional e dificuldade para distinguir, no mesmo Supabase, o que pertence ao SCP, ao MeshWave, ao MWN e a estruturas históricas. A tentativa posterior de migrar a estrutura MWN para uma nova conta/projeto `mwn` foi apenas parcialmente concluída.

O ponto mais sensível foi a migração de identidade: usuários de `auth.users`, perfis dependentes, referências UUID, sessões, proprietários funcionais e credenciais não podem ser tratados como simples linhas independentes. A migração parcial pode deixar tabelas, funções, triggers, FKs, RLS e integrações apontando para o projeto antigo ou para identidades que não foram reproduzidas no novo projeto.

Esse histórico explica por que a classificação correta não é “tabelas sem RLS são de outros projetos e, portanto, irrelevantes”. A classificação correta é: **o alerta não é um defeito específico do SCP, mas a separação incompleta de projetos e identidades constitui risco de segurança e governança que requer investigação própria**.

## Regra operacional para auditorias futuras

1. Identificar o domínio funcional e o proprietário da tabela.
2. Separar ausência de RLS de defeitos de integridade referencial, FKs, dados órfãos ou falhas de fluxo.
3. Não inferir que uma tabela pública é tabela do SCP.
4. Não habilitar, remover ou modificar RLS de tabelas de outros domínios sem autorização específica e plano de compatibilidade/rollback.
5. Registrar achados de RLS do SCP separadamente dos achados de outros projetos.
6. Tratar este documento como classificação de escopo; a política efetiva de cada domínio continua dependente de sua arquitetura, dos seus consumidores autorizados e do estado da migração para `mwn`.
7. Separar uma futura auditoria de migração: inventário de projetos, proprietários, tabelas, funções, triggers, extensões, buckets, Auth, perfis e referências cruzadas entre o ambiente histórico e o ambiente `mwn`.

## Relação com a auditoria Sofia #14

A auditoria de integridade referencial concentrou-se em FKs, identidade, indicação, aquisições, wallets, créditos, bônus, ledger e no modelo próprio do schema `sofia`. Ela não estabeleceu uma obrigação de habilitar RLS em todas as tabelas públicas do banco.

Os achados sobre `public` devem permanecer classificados conforme seu domínio e estado de migração: MeshWave/UMS, legado, integração, outro projeto ou estrutura MWN ainda retida no ambiente histórico. Eles não devem ser reclassificados como falha específica de segurança do SCP apenas por aparecerem no mesmo catálogo Supabase; ao mesmo tempo, a conta compartilhada e a migração incompleta devem permanecer registradas como risco sistêmico separado.

## Limitações e proveniência

Este registro documenta o contexto fornecido pelo responsável e o reconcilia com a arquitetura documental existente. O Foundation não contém, neste momento, um inventário autoritativo completo que atribua cada tabela Supabase a um proprietário de projeto nem um mapa completo do que foi ou não migrado para `mwn`. Esse inventário deve ser criado posteriormente como trabalho separado, sem alterar dados, RLS ou integrações durante a investigação.
