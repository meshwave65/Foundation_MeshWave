# Registro de Decisões Curatoriais — BCE MeshWave

> Este arquivo registra decisões sobre a própria Base de Conhecimento Evolutivo. Decisões técnicas do MeshWave devem ser registradas nos documentos de seus respectivos temas e referenciadas aqui quando afetarem a arquitetura documental.

## Como usar

Cada decisão recebe um identificador estável. Não apagar decisões antigas: se uma decisão for substituída, criar nova entrada com relação explícita à anterior.

Estados permitidos: `PROPOSTA`, `ADOTADA`, `SUBSTITUÍDA`, `REJEITADA`, `PENDENTE_VALIDACAO`.

## Decisões

### DEC-BCE-001 — Criar uma camada BCE separada das fontes brutas

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** Criar `BCE/` para documentos curados, mantendo `KNOWLEDGE/` como repositório de evidências brutas e históricas.
- **Motivo:** A curadoria precisa evoluir sem destruir a proveniência original; misturar documentos finais e extrações dificultaria auditoria e retomada.
- **Alternativas consideradas:** reescrever diretamente `KNOWLEDGE/`; criar documentos na raiz; usar somente um README.
- **Por que não foram escolhidas:** não preservariam adequadamente a separação entre fonte, interpretação e estado da arte.
- **Impacto:** todo documento curado deve apontar para fontes relativas em `KNOWLEDGE/`.
- **Revisão:** somente se a estrutura do repositório for redesenhada por decisão explícita.

### DEC-BCE-002 — Usar documentos de controle explícitos para continuidade

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** Usar orientação, controle mestre, índice curatorial, registro de decisões e checkpoints de sessão.
- **Motivo:** outro agente precisa continuar sem depender do histórico do chat ou de memória implícita.
- **Alternativas consideradas:** apenas mensagens de commit; apenas issues; apenas um arquivo TODO.
- **Por que não foram escolhidas:** commits não descrevem necessariamente o próximo passo e issues não garantem um estado operacional único dentro do repositório.
- **Impacto:** toda sessão deve atualizar o próximo passo inequívoco.

### DEC-BCE-003 — Fazer commits incrementais por unidade lógica

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** Cada criação, alteração significativa, decisão ou checkpoint deve ter commit pequeno e descritivo, com push imediato.
- **Motivo:** reduzir perda de trabalho, permitir transferência a outro agente e facilitar reversão/auditoria.
- **Alternativas consideradas:** um commit ao fim de cada fase; um commit ao fim de toda a curadoria.
- **Por que não foram escolhidas:** um trabalho monumental poderia ser interrompido e deixaria o estado intermediário invisível.
- **Impacto:** alterações de controle e conteúdo podem gerar commits separados.

### DEC-BCE-004 — Preservar a história arqueológica

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** Todo documento de tema deverá distinguir estado atual, evolução, alternativas, descartes, otimizações, conflitos e lacunas.
- **Motivo:** o objetivo não é apenas documentar o resultado final, mas contar como as ideias chegaram a ele.
- **Alternativas consideradas:** resumir somente a versão mais recente; manter apenas uma linha do tempo superficial.
- **Por que não foram escolhidas:** apagariam decisões intermediárias e dificultariam entender por que uma solução foi adotada.

### DEC-BCE-005 — Não apagar fontes durante a curadoria

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** `KNOWLEDGE/` será tratado como evidência primária; duplicatas, ruídos e fontes externas serão classificados, não eliminados, salvo decisão posterior explicitamente registrada.
- **Motivo:** títulos semelhantes podem conter versões, imagens ou decisões distintas.
- **Impacto:** a limpeza será lógica/documental, não destrutiva.

### DEC-BCE-006 — Classificar domínios antes da leitura profunda

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** iniciar com um índice curatorial baseado no inventário e nos títulos, marcando-o como preliminar, antes de escrever documentos finais.
- **Motivo:** 273 conjuntos de extração e mais de mil arquivos exigem uma ordem de trabalho explícita.
- **Risco aceito:** títulos podem ser genéricos ou enganosos.
- **Mitigação:** revisar a classificação após ler conteúdo, código, links e imagens; registrar fusões/divisões futuras.

### DEC-BCE-007 — Tratar fontes sensíveis sem copiar segredos

- **Data:** 2026-10-08
- **Estado:** ADOTADA
- **Decisão:** não reproduzir tokens, senhas, chaves ou dados pessoais encontrados em históricos; registrar apenas a existência, localização e necessidade de rotação quando relevante.
- **Motivo:** documentos históricos podem conter material operacional sensível.
- **Impacto:** a rastreabilidade deve usar caminho e descrição não sensível.

## Decisões pendentes de validação

### DEC-BCE-008 — Ordem dos domínios prioritários

- **Data:** 2026-10-08
- **Estado:** PENDENTE_VALIDACAO
- **Proposta:** começar por visão geral, arquitetura, rede/roteamento, identidade e ARC/Bayes.
- **Justificativa:** esses temas parecem formar as dependências conceituais dos demais.
- **Validação necessária:** confirmar após o inventário de conteúdo completo e, se necessário, ajustar com base na densidade das fontes.

### DEC-BCE-009 — Granularidade final dos documentos

- **Data:** 2026-10-08
- **Estado:** PENDENTE_VALIDACAO
- **Proposta:** um documento por domínio, com possibilidade de subdividir módulos grandes.
- **Justificativa:** evitar tanto um documento monolítico quanto fragmentação excessiva.
- **Validação necessária:** medir sobreposição, tamanho e coesão após F1.7.

## Histórico de alterações deste registro

| Data | Alteração | Commit |
|---|---|---|
| 2026-10-08 | Registro criado com decisões BCE-001 a BCE-009 | a publicar |
