# Escopo físico — F2.4 Identidade, identificação de equipamento e DIDs

## Regra de processamento

Este arquivo fecha o lote antes da leitura profunda. Para cada caminho serão lidos `content.txt`, `code_blocks.txt`, `links.txt` e todas as imagens associadas. Título, classificação e presença de cartão não equivalem a implementação, adoção ou conformidade com DID.

## Fontes do lote

1. `KNOWLEDGE/info/20260422_174130_Definição do identificador único do equipamento na rede - Manus`
2. `KNOWLEDGE/info/20260422_173855_Identificador Único do Equipamento na Rede - Manus`
3. `KNOWLEDGE/omaci2008/20260422_173034_Melhor forma de criar DIDs para rede mesh global - Manus`
4. `KNOWLEDGE/info/20260422_164535_DNA do Hardware_ Identidade Resiliente com ARC_PGC - Manus`
5. `KNOWLEDGE/omaci2008/20260422_172158_Imagem para Identidade Auto-Soberana e Verificação - Manus`
6. `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus`
7. `KNOWLEDGE/info/20260422_172056_Análise e continuidade sobre dispositivos Android antigos - Manus`

## Justificativa de inclusão

O lote combina as duas fontes classificadas como definição espacial/CPA/CLA, a proposta de formato DID/GeoID, a fonte de identidade resiliente/DNA do hardware, a evidência visual de identidade soberana, a fonte de mesmo título que a classificação marcou como predominantemente operacional e a fonte Android que pode afetar a disponibilidade de identificadores de dispositivo e compatibilidade.

## Exclusões nesta unidade

- ARC, PGC e inferência bayesiana serão apenas referenciados quando forem dependências da identidade; a especificação de autenticação ficará em DOM-05.
- Roteamento, CLA como mecanismo de rede e Geohash como índice de localização serão relacionados a DOM-03, sem reabrir sua síntese salvo conflito de identidade.
- Fontes de Sofia, persistência, patentes e APIs entram em outros domínios, salvo evidência direta de DID, equipamento ou credencial.

## Resultado esperado

Produzir ou atualizar `BCE/temas/identidade-dids-e-identificador-de-equipamento.md` com terminologia, modelos de identidade, formato(s) proposto(s), relação pessoa–dispositivo–nó, ciclo de vida, privacidade, conflitos, evidências, lacunas e próximo passo. Manter `REVISÃO` se não houver esquema aprovado, implementação ou teste verificável.
