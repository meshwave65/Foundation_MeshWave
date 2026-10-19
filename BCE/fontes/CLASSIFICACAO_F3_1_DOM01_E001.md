# Classificação curatorial F3.1 — DOM-01 — E001/L001-01

## Proveniência

- **Fonte:** `KNOWLEDGE/info/20260422_171119_O que é o projeto Meshwave_ - Manus/`
- **Arquivos:** `content.txt`, `code_blocks.txt`, `links.txt`, `FULL.png`.
- **Inventário:** 4 arquivos; 454.549 bytes.
- **Qualidade textual:** `content.txt` tem 1.993 linhas, 1.734 não vazias e 121 linhas literais distintas; repetição dominante, com blocos de resposta reproduzidos aproximadamente 21 vezes.
- **Código:** `code_blocks.txt` tem 13 linhas/172 bytes e contém somente rótulos/termos (`v0.1.0-alpha`, `v0.2.0-alpha`, `ANDROID_ID`, `Decentralized Identifier`); não é código executável.
- **Links:** `links.txt` tem 863 bytes, com redirecionamentos de grounding não seguidos.
- **Imagem:** `FULL.png`, 1280×845, exibe principalmente a discussão sobre fragilidade do `ANDROID_ID`, reputação, reset, resiliência e proposta de “DNA do Equipamento”; UI/replay, não prova de execução.
- **Hashes pós-leitura:** `FULL.png` `681e5c619adf590d248d4383d048e599efd0dfd36b53ebd25dc9603f81199c36`; `code_blocks.txt` `f5d91389e824b19b6de6650a71de3924d9d7605e04775265c5b7ced99c5bbf70`; `content.txt` `70298fc29e07fc3ab8f2f058e6bf035c9559c66943ad6e083479a52c0699f3d7`; `links.txt` `8088cc16b5643d53eeeef9a9ca72beddf1fc3c73d5a91d65acf1c5e182ca3648`.

## Achados classificados

### Fatos observados no artefato

1. O transcript associa MeshWave a uma rede mesh de comunicação entre dispositivos móveis e descreve o projeto como alternativa à dependência de operadoras.
2. O transcript também lista homônimos/contextos externos — criptomoeda, visualização musical e classe `meshWave` do OpenFOAM — sem validação nesta curadoria.
3. A expressão “autenticação recessiva contextual” é explicitamente tratada como termo não padronizado e interpretado na conversa.
4. A narrativa descreve roteamento dinâmico, inferência Bayesiana, confiança contextual, autenticação contínua/passiva e isolamento de nós anômalos como uma combinação conceitual.
5. A fonte narra uma evolução de roadmap entre autenticação básica, identidade resiliente/SSI, ARC/autenticação adaptativa, governança de identidade e modelos de IA mais avançados.
6. A fonte relata um protótipo `v0.1.0-alpha` associado a `ANDROID_ID` e aponta fragilidade quando o identificador muda; propõe `v0.2.0-alpha`, “DNA do Equipamento” e o paradigma do “Barco de Teseu”.

### Propostas, hipóteses e interpretações

- MeshWave como rede auto-organizável com seleção de caminhos por confiança, eficiência e contexto.
- Inferência Bayesiana para atualizar a confiabilidade de vizinhos e prever congestionamento/offline.
- Autenticação “recessiva” como autenticação passiva, ativada diante de anomalia, ou como confiança herdada de nós confiáveis.
- Identidade multifatorial/probabilística capaz de sobreviver a reset, atualização de sistema, reparo ou troca de aparelho.
- Roadmap com aprendizado federado, IA generativa para simulação de ameaças e governança descentralizada.

Essas formulações são propostas ou interpretações do transcript. Não há código completo, build, teste, protocolo, métrica, threat model ou deployment verificável neste conjunto.

## Conflitos e limites

- O transcript mistura descrição do projeto com resultados de busca e homônimos externos; somente a associação explícita ao corpus MeshWave deve ser usada no DOM-01.
- Rótulos `v0.1.0-alpha`/`v0.2.0-alpha` não estão ligados a commit, tag, release, APK ou changelog verificável.
- `ANDROID_ID`, DID, “DNA do Equipamento” e identidade resiliente aparecem como formulações sucessivas, mas a fonte não estabelece qual é normativa.
- O conteúdo usa linguagem de confirmação e aprovação do assistente, mas isso não é evidência independente de decisão ou implementação.
- Os redirecionamentos de grounding em `links.txt` não foram acessados; não sustentam confirmação externa.

## Destino curatorial

- Atualizar DOM-01 com a auditoria física, repetição, evolução da identidade e separação entre visão, roadmap e estado implementado.
- Manter DOM-01 em `REVISÃO`.
- Próximo contato F3.1: E002/L001-02, após commit desta classificação e da atualização de DOM-01.
