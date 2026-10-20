# Classificação curatorial F3.1 — DOM-01 — E004/L001-04

## Proveniência e escopo

- **Unidade:** F3.1 — consolidação do domínio prioritário 1, DOM-01/P0; auditoria direta do contato E004/L001-04.
- **Fonte física:** `KNOWLEDGE/info/20260422_165745_ARC - Autenticação Recessiva Contextual com inferência Bayesiana - Manus/`.
- **Pré-registro:** `BCE/sessoes/2026-10-19_f3-1-dom01-e004-abertura.md`, publicado em `22c83ac` antes da revisão semântica.
- **Conferência de continuidade:** o controle mestre foi alinhado ao pré-registro em `4a5668c` antes da inspeção da imagem e do fechamento desta unidade.
- **Inventário físico:** quatro arquivos, 1.183.268 bytes. Os hashes SHA-256 pós-leitura coincidem com o pré-registro (4/4).

| Arquivo | Bytes | SHA-256 | Observação de leitura |
|---|---:|---|---|
| `FULL.png` | 151.382 | `743c6746c8c801233efbe0318bdc81b8dfef63aa4789b5c41cf3526b136bef7c` | Captura de interface/replay, 1280×845; apresenta um resumo textual de integração e trecho de código, não uma execução observada. |
| `code_blocks.txt` | 61.167 | `a1e8735be33ba238e5f34eadce6c64f806202e983d57d3076fefa334820d645e` | Blocos extraídos e repetidos; inclui código Kotlin de simulação e trechos de integração incompletos. Não executado. |
| `content.txt` | 970.674 | `a5b077d33db705a975c69752f2096b12a332e5f40edfcd739f3a05bb9855daa6` | Transcrição extensa e repetitiva, com proposta de sincronização, ARC/Bayes, simulador web e integração Android. Revisada em cópia temporária redigida. |
| `links.txt` | 45 | `15486eb5a8cfe2febfe9d85822add82c3734070b862fd34413aefc74da4bba64` | Duas referências URL; uma classificada como `localhost` e outra como host nomeado. Valores omitidos; nenhum destino seguido. |

Não há outros anexos visuais neste diretório. As cópias de revisão foram temporárias, com valores sensíveis e URLs redigidos; nenhuma cópia foi incluída no repositório e `KNOWLEDGE/` permaneceu intacto.

## Achados classificados

### Fatos observados nos artefatos

1. `content.txt` tem 25.038 linhas, das quais 19.139 não vazias. Após redação e comparação literal linha a linha, restam 1.346 linhas não vazias distintas; 17.793 linhas não vazias repetem conteúdo já visto. `code_blocks.txt` tem 1.609 linhas, 1.286 não vazias, 487 distintas após a mesma comparação e 799 repetições não vazias. Essas são métricas de repetição textual, não contagem de afirmações independentes ou de conteúdo tecnicamente validado.
2. A transcrição descreve `ResilientValue<T>` com variantes `Real` e `Placeholder`, aplicada a `SyncResult.averageLatencyMs`. O caminho proposto mantém um valor substituto explícito em caso de sincronização instável e evita tratá-lo como medição real no cálculo bayesiano.
3. O exemplo de sincronização usa pacotes, tempos simulados, jitter e uma latência aproximada. O módulo Bayesiano emprega priors por estado de sincronização, valores fixos de likelihood e um limiar de decisão. A fonte não fornece dados de calibração, justificativa dos parâmetros ou resultados de teste reproduzíveis.
4. O ARC transcrito usa um desafio com índice, comprimento e timestamp, deriva um segmento a partir de hashes e compara a resposta com o segmento esperado. O exemplo também registra segmentos e inclui literais com aparência de segredo/identificador em atribuições de demonstração. Os valores foram redigidos e não são reproduzidos nesta classificação; não é possível determinar apenas pelo corpus se algum valor foi usado fora da simulação.
5. A fonte propõe um simulador local com servidor Kotlin/Ktor, WebSocket, jitter/latência e interface HTML/CSS/JavaScript/Vue. O texto oferece trechos e instruções para gerar um projeto Ktor inicial; não inclui um projeto completo com dependências e build reproduzível. A parte de frontend contém estrutura e funções omitidas ou marcadas como a implementar.
6. A fonte também propõe integração Android por módulos de biblioteca (`sync`, `arc`, `bayesian`), um `MeshPeerConnectionManager`, sockets, coroutines, ViewModel/LiveData e serialização JSON. Os trechos de conexão, serialização e desserialização incluem stubs/omissões; não há aplicativo Android ou pacote `.aar` neste conjunto.
7. `FULL.png` mostra uma página de conversa/interface intitulada “ARC - Autenticação Recessiva Contextual com inferência Bayesiana”, com resumo de integração modular e um trecho de UI/ViewModel. O cartão de conclusão/reprodução da tarefa é parte da interface; a captura não mostra uma aplicação rodando, build, teste ou comunicação real entre dispositivos.
8. `links.txt` contém duas referências; a classificação redigida identificou uma referência a host local (`localhost`) e outra a host nomeado. Nenhuma foi aberta, chamada ou validada, e não se conclui que um serviço esteja disponível.

### Propostas, alegações e interpretação

- A distinção explícita entre valor real e placeholder é uma decisão de design registrada na interação e um contrato de dados proposto. Ela pode reduzir confusão entre ausência e medição, mas não comprova resiliência operacional nem segurança por si só.
- O texto chama partes do código de “completas e funcionais” e apresenta a integração do simulador/app como executável. Essa é uma alegação no replay; não está acompanhada de diretório de projeto, build, dependências fixadas, testes, logs, commit de implementação ou resultado reproduzível.
- O simulador web e a integração Android devem ser classificados como **proposta/roteiro de implementação com trechos parciais**, não protótipo comprovado. A tela `FULL.png` é captura de conversa, não captura do simulador em runtime.
- O limiar, os priors, as verossimilhanças, o estimador de latência e o tratamento de estados ausentes permanecem parâmetros de exemplo. Não há evidência de calibração, avaliação estatística, modelo de ameaça ou validação criptográfica.
- A transcrição não estabelece protocolo interoperável, contrato de mensagens, frescor/nonce formal, proteção contra replay, armazenamento/rotação de segredos ou segurança do canal. Os limites técnicos registrados anteriormente em DOM-05 permanecem aplicáveis.

## Limites, conflitos e segurança

- A fonte mistura trechos de código, explicação conversacional, repetição de replay e plano de produto. Repetições não constituem confirmações independentes.
- Os blocos Kotlin dependem de tipos e ambiente não fornecidos como projeto compilável; faltam artefatos para verificar compilação, testes, funcionamento ou integração ao MeshWave.
- O roteiro Ktor/Vue é parcial e orienta a criação de um projeto-base externo; a porção JavaScript é principalmente estrutura/placeholder. A integração Android também deixa partes essenciais sem implementação. Não copiar os exemplos para produção sem revisão de segurança e engenharia.
- Literais com aparência de segredo/identificador foram encontrados em exemplos da transcrição e redigidos nas cópias temporárias. Nenhum valor foi copiado para a BCE, terminal de entrega ou mensagens. Como não é possível confirmar se algum literal é real ou ainda utilizado, recomenda-se ao responsável rotacioná-lo caso corresponda a uma credencial ativa.
- Os destinos de `links.txt` não foram seguidos. O endereço local não comprova que exista um serviço, e o host nomeado não foi validado.
- Os quatro hashes pós-leitura coincidem com o pré-registro. Nenhum código foi executado, nenhuma API foi chamada e nenhum arquivo bruto foi alterado.

## Relação com classificações e documentos temáticos

- A classificação inicial `BCE/fontes/CLASSIFICACAO_LOTE_001.md`, entrada L004, identifica corretamente `ResilientValue`, sincronização e inferência bayesiana como design/código transcrito, com confiança maior para a intenção do que para implementação e parâmetros.
- `BCE/temas/arc-autenticacao-contextual-e-bayes.md` (DOM-05) já descreve o fluxo ARC/Bayes e seus riscos. E004 acrescenta a auditoria direta dos quatro artefatos, o roteiro de simulador Ktor/Vue, a proposta de integração Android e a presença de literais sensíveis redigidos; não altera o estado de implementação, calibração ou validação.
- `BCE/temas/visao-geral-ecossistema-meshwave.md` (DOM-01) pode usar E004 como evidência de uma proposta de módulo ARC/Bayes e de planos de integração, sem inferir que esses módulos estejam implantados no ecossistema.
- Não se registra decisão técnica nova em `BCE/REGISTRO_DECISOES.md`: esta unidade classifica evidência e não aprova protocolo, parâmetros ou integração.

## Destino curatorial

1. Atualizar DOM-01 para v0.3.3 e DOM-05 para v0.1.1, mantendo ambos em `REVISÃO` e citando a classificação e o pré-registro.
2. Atualizar o índice curatorial e publicar um checkpoint de fechamento E004, registrando hashes 4/4, repetição, links não seguidos e tratamento de material sensível.
3. Manter a conclusão limitada: **proposta transcrita e trechos de código, sem implementação, compilação, teste ou execução confirmada**.
4. Próximo contato de DOM-01: E005/L001-06, `KNOWLEDGE/johann/20260422_174331_Conhecimento sobre Meshwave, Sofia e módulos ARC-Bayes_ - Manus/`. Antes de qualquer leitura, pré-registrar os arquivos físicos e seus hashes em checkpoint versionado.
