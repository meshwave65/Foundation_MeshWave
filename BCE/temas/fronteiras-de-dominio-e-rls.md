# Fronteiras de domínio, projetos compartilhados e RLS

## Metadados

| Campo | Valor |
|---|---|
| Tipo | Decisão técnica/documental |
| Domínios relacionados | MeshWave, SOFIA/Sofia Control Panel, projetos e módulos compartilhados |
| Status | ADOTADA como regra de escopo |
| Data do registro | 2026-11-13 |
| Proveniência | Orientação do responsável, reconciliada com a auditoria operacional Sofia #14 e a separação documental do Foundation_MeshWave |

## Decisão

As tabelas existentes no banco Supabase não devem ser consideradas automaticamente pertencentes ao Sofia Control Panel ou ao núcleo operacional MeshWave apenas por estarem no mesmo projeto Supabase.

Parte das tabelas públicas pertence a outros módulos, protótipos, integrações, projetos legados ou domínios compartilhados. A ausência de Row Level Security (RLS) nessas tabelas, isoladamente, **não deve ser classificada como falha de segurança do SCP** nem motivar a aplicação indiscriminada de RLS.

Qualquer avaliação de RLS deve começar pela identificação do proprietário funcional, do consumidor, do caminho de acesso e do contrato de segurança de cada tabela. A decisão de habilitar RLS pertence ao domínio responsável e exige políticas compatíveis com os clientes existentes; habilitar RLS sem esse mapeamento pode quebrar integrações legítimas.

## Fronteiras de responsabilidade

### Foundation_MeshWave

O Foundation_MeshWave é o repositório curatorial e arquitetural do ecossistema. Ele registra conceitos, decisões, fronteiras de domínio, proveniência e limitações. Não deve transformar uma observação operacional isolada em regra global de segurança sem identificar o domínio responsável.

### Sofia / Sofia Control Panel

O schema `sofia` possui modelo operacional próprio, com identidade local (`sofia.users`) e tabelas de missões, tarefas, agentes e mensagens. As políticas de acesso e o Realtime do messenger Sofia devem ser avaliados especificamente para essas tabelas e para os clientes do SCP.

### Outros módulos e projetos

Tabelas em `public` podem servir a MeshWave, UMS/MWN, MeshWalker, integrações, protótipos, legados ou outros projetos. Relações, RLS, triggers e políticas dessas tabelas não devem ser alteradas em nome do SCP sem confirmação explícita do domínio proprietário.

## Regra operacional para auditorias futuras

1. Identificar o domínio funcional e o proprietário da tabela.
2. Separar ausência de RLS de defeitos de integridade referencial, FKs, dados órfãos ou falhas de fluxo.
3. Não inferir que uma tabela pública é tabela do SCP.
4. Não habilitar, remover ou modificar RLS de tabelas de outros domínios sem autorização específica e plano de compatibilidade/rollback.
5. Registrar achados de RLS do SCP separadamente dos achados de outros projetos.
6. Tratar este documento como classificação de escopo; a política efetiva de cada domínio continua dependente de sua arquitetura e dos seus consumidores autorizados.

## Relação com a auditoria Sofia #14

A auditoria de integridade referencial concentrou-se em FKs, identidade, indicação, aquisições, wallets, créditos, bônus, ledger e no modelo próprio do schema `sofia`. Ela não estabeleceu uma obrigação de habilitar RLS em todas as tabelas públicas do banco.

Os achados sobre `public` devem permanecer classificados conforme seu domínio: MeshWave/UMS, legado, integração ou outro projeto. Eles não devem ser reclassificados como falha de segurança do SCP apenas por aparecerem no mesmo catálogo Supabase.

## Limitações e proveniência

Este registro documenta a orientação de escopo fornecida pelo responsável e a reconcilia com a arquitetura documental existente. O Foundation não contém, neste momento, um inventário autoritativo completo que atribua cada tabela Supabase a um proprietário de projeto. Esse inventário pode ser criado posteriormente como trabalho separado, sem alterar dados, RLS ou integrações.
