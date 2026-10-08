# Índice de imagens e diagramas — Lote 003 (F1.4)

## Escopo e método

Catálogo dos arquivos de imagem presentes nos **19 conjuntos** listados em `BCE/fontes/CLASSIFICACAO_LOTE_003.md`. A varredura localizou **35 imagens**, totalizando **3.604.072 bytes**, sem mover, renomear, sobrescrever ou apagar fontes brutas. Os caminhos abaixo são relativos à raiz do repositório e podem ser reconstruídos como `KNOWLEDGE/<diretório do conjunto>/<arquivo>`.

Para cada arquivo foram registrados: nome/caminho, extensão do nome, formato detectado pelo decodificador, bytes, dimensões, SHA-256 dos bytes originais e pHash perceptual de 64 bits (`ImageHash.phash`, hash_size=8). As descrições são observações visuais e/ou sínteses do registro F1.3; não constituem validação dos fatos narrados nas capturas. **OCR automático não foi executado**; reconhecimento textual e origem/licença dos anexos ficam não confirmados quando não são demonstráveis no próprio arquivo.

## Resultado de integridade e comparação

- 35/35 imagens foram abertas e tiveram metadados calculados; extensões internas encontradas: 26 PNG, 8 JPEG e 1 WebP.
- **Duplicatas exatas:** nenhuma entre os 35 arquivos (zero pares com SHA-256 idêntico).
- O filtro exploratório pHash com distância de Hamming `≤ 4` sinalizou 12 pares de capturas `FULL.png`. A semelhança decorre do enquadramento/interface compartilhada; as capturas representam episódios e conteúdos distintos. **Nenhum desses pares foi classificado como duplicata visual.** pHash é triagem, não prova de identidade.
- Os 8 casos de extensão divergente são: L003-03 `img_001.jpg`, `img_003.jpg`, `img_005.jpg`, `img_007.jpg`, `img_011.jpg`, `img_013.jpg` (formato interno PNG); L003-05 `img_000.jpg` (WebP); L003-14 `img_000.jpg` (PNG). Os demais `.jpg` são JPEG e os `.png` são PNG.
- Proveniência: a localização em `KNOWLEDGE/` e a associação ao conjunto estão confirmadas. A origem externa/autoria/licença das imagens incorporadas não está confirmada, exceto que L003-05 `img_000.jpg` é uma captura de página GitHub. Isso não confirma direitos de reutilização. OCR: não executado.

## Catálogo por conjunto

### L003-01 — Android / Gradle

Diretório-fonte: `KNOWLEDGE/andressa/20260422_162449_Desenvolvimento do Aplicativo MeshWave para Android - Manus/`
Vínculo textual: conversa sobre erro de versão de bytecode/Gradle; a captura mostra instruções de `JAVA_HOME`, limpeza e tentativa de build, não um build bem-sucedido.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 133391 | 1006×781 | `eb94c7e16e90973fec7301accd7fb8369366da43aa8dd4d9035d40f32de0ac11` | `ef3449954b954995` | Captura da conversa de troubleshooting de Gradle/Java; evidencia o histórico de tentativa, não o resultado final. |

### L003-02 — ChromaDB / TLS

Diretório-fonte: `KNOWLEDGE/andressa/20260422_161744_Title unclear without content - Manus/`
Vínculo textual: erros TLS/API e estado parcial; a imagem não fornece configuração técnica suficiente para determinar causa-raiz.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 155784 | 1006×781 | `833ece44d950b31a671a85ad335a6dc6a743f6f859da12be7b7dc7624dad8c1e` | `ef34c9944b954b15` | Captura da falha TLS/tarefa em espera, com progresso 4/6; não prova conexão ou vetorização. |

### L003-03 — Sofia API e imagens clínicas externas ao produto

Diretório-fonte: `KNOWLEDGE/andressa/20260422_161931_Como acessar e concluir missões na API Sofia - Manus/`
Vínculo textual: a transcrição descreve início de capítulo/apresentação sobre arritmias cardíacas, pesquisa de imagens e interrupção por créditos. As imagens abaixo se relacionam ao conteúdo médico narrado, não ao produto MeshWave. Fonte, licença, uso final em apresentação e validação clínica não confirmados.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 162953 | 1006×781 | `099103d0106c596ed08d68667614ab74ef24880008aee13fe4245bb1d87ec8da` | `bf346f346994c8c1` | Captura da missão/capítulo 9, pesquisa visual e falta de créditos; não comprova deck final. |
| `img_000.jpg` | `.jpg` / JPEG | 156844 | 1280×720 | `93f708502a244eda65a4d11a4db50dcf131944fba067166a276dd53aceb82830` | `92d13f19e46e1d43` | Banner médico com retrato de profissional, material/equipamento de procedimento e título “Tratamentos”. |
| `img_001.jpg` | `.jpg` / PNG | 488 | 32×32 | `c837d6cd4f6b7873cd9357a97476546fee48d4b0118d25f855b9dffe7f7dd663` | `cc00b3008c00e600` | Ícone de reprodução do YouTube, miniatura de interface; não é conteúdo clínico substantivo. A extensão diverge do formato interno. |
| `img_002.jpg` | `.jpg` / JPEG | 35716 | 410×1024 | `31fee2ccad2af92513933c1ffa28263bf86bc835a9d6efb1c4be639ad8982ae8` | `ca4341a535bc4bfa` | Infográfico vertical “Arritmias cardíacas”, com definição, riscos, sintomas e prevenção; texto pequeno não foi submetido a OCR. |
| `img_003.jpg` | `.jpg` / PNG | 1865 | 32×32 | `cdf61be732917a95c8fb10d753cde9eea564fdb2cc86a5e3974e88c1b2c37532` | `875c68a7347a61e5` | Miniatura de retrato/avatar; baixa resolução e conteúdo textual não legível. Extensão divergente. |
| `img_004.jpg` | `.jpg` / JPEG | 53864 | 640×480 | `5aa4c548ea05838008e86cf3b572e870270c2aada57d975a978fed278febc3b8` | `de2aa853c186b5b5` | Ilustração anatômica de coração e cateter, com setas de trajeto/procedimento; relacionada a ablação cardíaca. |
| `img_005.jpg` | `.jpg` / PNG | 306 | 32×32 | `4a5adf519a08d5910e14f44e61dc4384213cb503e5ffa5362f26ba2ec71330b6` | `bcb6c3483cb7e248` | Miniatura gráfica rosa muito pequena, possivelmente marca/elemento de origem web; identificação e procedência não confirmadas. Extensão divergente. |
| `img_006.jpg` | `.jpg` / JPEG | 70456 | 801×801 | `cf06d8da5a047646dd435dc477f6454f10498fe81e8d018cb0ce3fb802983e93` | `f809931f46624abf` | Ilustração de ablação de arritmia em coração, com cateter e marcação de foco; inclui identificação profissional impressa na imagem, não validada. |
| `img_007.jpg` | `.jpg` / PNG | 373 | 32×25 | `1e70fc677859d444d8a6959aeb61858656ac76ebc9f5dda2b6e8dae48959cf49` | `c4f559d3644e6651` | Miniatura de ícone verde/amarelado em baixa resolução; associação exata não confirmada. Extensão divergente. |
| `img_008.jpg` | `.jpg` / JPEG | 40562 | 600×400 | `2d25b26c19e3bec0cb858128b68a7a1066605087957a0e49e02af76dadbe2257` | `b93a87c20dc3ce9c` | Fotografia de procedimento hospitalar com profissional manipulando cateter junto ao paciente; não comprova uso em apresentação. |
| `img_009.jpg` | `.jpg` / JPEG | 725 | 32×32 | `71220bbe06c7169b6046241bcaba1bdd328dd9549dca615b0fc00fded0fef4de` | `be12d1e9c582c54f` | Miniatura com letras/elemento vermelho, baixa resolução; possível logomarca, sem atribuição confirmada. |
| `img_010.jpg` | `.jpg` / JPEG | 113397 | 400×320 | `27dd461a70a14122464130e4bd3052081451eb95a3ce7e339524baf1d47c851f` | `bba9c62f92c2c349` | Ilustração de desfibrilador cardioversor implantável (DCI) e eletrodo no coração, com legenda explicativa em português. |
| `img_011.jpg` | `.jpg` / PNG | 556 | 32×32 | `99941eb11b0eb99bbc35ebca0989093aef0f1abcafb6f7f30a9efc888d872611` | `e796b1790e069a39` | Miniatura de logotipo azul/verde, ilegível para atribuição segura; extensão divergente. |
| `img_012.jpg` | `.jpg` / JPEG | 18952 | 300×300 | `bf087780329cf64536b21b48135ba1b8a29ef08332fc037cae2b209fb4b9ccd7` | `bec2e1acca331d91` | Ilustração de gerador de DCI implantado no tórax, com eletrodos conectados ao coração e rótulos em português. |
| `img_013.jpg` | `.jpg` / PNG | 2092 | 32×32 | `6b838f95147d0c4f28eef3883f50ddeb77ef118b507c2309a4a3b585a98b8145` | `e1ffcc0f20274783` | Miniatura escura/colorida de baixa resolução; conteúdo e relação clínica específica não confirmados. Extensão divergente. |

### L003-04 — Sofia API / listagem de tarefas

Diretório-fonte: `KNOWLEDGE/dinecy/20260422_171255_Diretrizes para execução da tarefa no Sofia API - Manus/`
Vínculo textual: falha relatada em `/tasks/next` e retorno à listagem; a imagem não valida contrato nem resposta da API.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 146016 | 1280×845 | `2d46b945f8a261e10bfa8fe0995a3d53c62bdacbb0c913d61eb53a19fe854c0a` | `fd164d9661964596` | Captura do erro no endpoint e cartão/listagem de relatório; conteúdo do relatório não está anexado/validado. |

### L003-05 — Persistência e handoff

Diretório-fonte: `KNOWLEDGE/dinelson/20260422_154208_Sistema de Persistência e Sincronização para Agentes Manus - Manus/`
Vínculo textual: discussão de persistência/transferência entre agentes. O anexo adicional é uma captura de repositório visual, não prova de integração ou sincronização.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 152347 | 1280×845 | `6991e2ac0cfbbd2d80ae02f87195e584b6aea65ee5cc4c22a4ebd46be25f034b` | `ed964d166d964196` | Captura de solicitação de envio de documentos/espera e interrupção por créditos; sem evidência de persistência implementada. |
| `img_000.jpg` | `.jpg` / WebP | 115382 | 894×768 | `c9807111e42f3dfacd49657958eb3645529d44bc6bd43d75e17f95a249840cf8` | `8d60747e3a327a6a` | Captura de página pública GitHub `meshwave65/MeshWave-Roadmap-Images`, com listagem de diagramas/imagens conceituais. A página não valida arquitetura ou implementação; extensão divergente. |

### L003-06 — Sofia API / upload de artefatos

Diretório-fonte: `KNOWLEDGE/filipe/20260422_164903_Instruções para a missão via Sofia API - Manus/`
Vínculo textual: erros 502/404 em tentativas de upload e rótulo visual de tarefa concluída; imagem registra a contradição, não o sucesso.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 181878 | 1280×845 | `c543e384cacfcd8369504e28283c760f842ac46e453aba004fe78764711d2a1e` | `fd164d164d966196` | Captura de erros 502/404 junto a “Tarefa concluída”; não há recibo de upload nem artefato recuperável. |

### L003-07 — Aplicativo Android / interface

Diretório-fonte: `KNOWLEDGE/filipe/20260422_165238_Criar interface para projeto no Android Studio - Manus/`
Vínculo textual: histórico de decisões e erros de interface/conectividade; captura é transcrição da conversa, não screenshot do aplicativo.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 158460 | 1280×845 | `69356d4d8c602ab82ae5bfdf1bcaf5276d6d9154c40b6af43e00eb81adf03e53` | `e934c5966d964596` | Captura de transcrição sobre UI/Wi‑Fi Direct/identidade; não demonstra app, APK ou teste em dispositivos. |

### L003-08 — Continuidade Android/Bluetooth

Diretório-fonte: `KNOWLEDGE/info/20260422_170852_Prosseguimento no Projeto Android Bluetooth - Manus/`
Vínculo textual: alteração de layout relatada e build/hardware pendentes.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 122159 | 1280×845 | `2fd12ba75f3a64a3bdd9565ca6c8f86293413159f0b7d7c7901b6296614dfd64` | `fd164d9641926d36` | Captura de transferência/relatório e status 3/3; não mostra dispositivo, APK ou comunicação Bluetooth. |

### L003-09 — Compatibilidade Android antigo

Diretório-fonte: `KNOWLEDGE/info/20260422_172056_Análise e continuidade sobre dispositivos Android antigos - Manus/`
Vínculo textual: recomendação registrada de considerar Android 8.0; os documentos-base e testes são lacuna.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 172566 | 1280×845 | `00e1d2296347c3bc9c88a20b945db60c7198927dce47b0ad2b2ba3eb74bbea7c` | `fd1641166d964d96` | Captura do resumo sobre suporte Android 8.0 e argumentos de alcance; não prova suporte implementado. |

### L003-10 — Exportação de base / identidade mencionada

Diretório-fonte: `KNOWLEDGE/info/20260422_173802_Identificador Único do Equipamento na Rede - Manus/`
Vínculo textual: conteúdo trata sobretudo de exportação/entrega de base; a captura não contém especificação de identificador.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 125333 | 1280×845 | `0d9e7929db0a5000c3c6146eb5bbb91f74e1fc9d0969ee195a2b18a57a0e31a1` | `ed964d9645966534` | Captura de cartão de ZIP de 34,88 MB e link inacessível; não comprova conteúdo, integridade ou download. |

### L003-11 — Sofia API / missão médica

Diretório-fonte: `KNOWLEDGE/iury/20260422_161704_Access Sofia API to Receive and Complete Missions - Manus/`
Vínculo textual: tentativa narrada de consultar/reivindicar missão e criar subtarefa, interrompida; sem prova de estado remoto.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 141395 | 1280×845 | `117df53e945597e38537a174db7614d9f90f60425b959a300f278b34c5757b18` | `fd164d964d924996` | Captura de etapa de missão/subtarefa e créditos esgotados 3/4; não comprova API ou conclusão. |

### L003-12 — Sofia API / relatório de tarefa

Diretório-fonte: `KNOWLEDGE/iury/20260422_161913_Instruções para a Tarefa no Sofia API Oráculo - Manus/`
Vínculo textual: recomendação para banco de dados e relatório `Final_Report_TSK42.md`; arquivo e upload não validados.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 158240 | 1280×845 | `37950aa359055da8e940d5f47ce76b46e296d748ef36d31a626ff0287bf79ce2` | `ed364d964d964d12` | Captura de cartão do relatório e status “Tarefa concluída”; não confirma o arquivo ou persistência pela API. |

### L003-13 — Android / erro de build

Diretório-fonte: `KNOWLEDGE/iury/20260422_162213_Resource Not Found Error in Android Build - Manus/`
Vínculo textual: método `disconnect()` e instruções de limpeza/rebuild discutidas; créditos interrompem a análise.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 162556 | 1280×845 | `71cf5dcc217e0ded9294d0b93bc6edeb50a7128246f64c50ad2fc17839fa0588` | `b9364d966d964196` | Captura de instruções Clean/Make/Assemble e créditos; não mostra build aprovado. |

### L003-14 — Android Studio / falha de compilação

Diretório-fonte: `KNOWLEDGE/iury/20260422_162301_Resource Not Found Error in Android Build Process - Manus/`
Vínculo textual: protótipo Java/XML e Wi‑Fi Direct; a captura adicional exibe erros de símbolos/construtores, sem resultado posterior.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 163599 | 1280×845 | `1665a6390ca9fc48c4b904fdfd1894cdf6265a99c18968845a73fa0b70b4859a` | `fd36419649964d96` | Captura do plano de recuperação/substituição de arquivos; plano não equivale a compilação. |
| `img_000.jpg` | `.jpg` / PNG | 171826 | 1398×664 | `ba95398362cb88c0936c59bd8607c6155601280053eee177f1593f9609c3bd3a` | `f19f438f1d6128e1` | Captura do Android Studio: árvore de projeto e painel de build com erros `cannot find symbol`, construtor/socket; evidência visual do erro narrado, não da correção. Extensão divergente. |

### L003-15 — Identidade / proposta de DID

Diretório-fonte: `KNOWLEDGE/omaci2008/20260422_173034_Melhor forma de criar DIDs para rede mesh global - Manus/`
Vínculo textual: proposta de formato de identificador; a imagem não valida capacidade, base ou aprovação.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 134488 | 1280×845 | `dee71dc200350258be47dda53fe5c97181a85e378b4129737189ca523fbc0d8e` | `bd164d966d166196` | Captura da proposta de campos e números de capacidade para identificador; sem prova de algoritmo, conformidade DID ou adoção. |

### L003-16 — Sofia API / finalização de relatório

Diretório-fonte: `KNOWLEDGE/natalia/20260422_171420_Instruções para Missão via Sofia API Manual - Manus/`
Vínculo textual: falha de finalização e alegação posterior de anexo; o relatório integral e recibo não foram recuperados.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 165439 | 1280×845 | `e477a993b8754f597b8115a4160cd66b5513e404117447b3dbbb57e5e3b4806c` | `fd364d9665964192` | Captura de relatório alegado de 9,95 KB e status “Tarefa concluída”; não confirma persistência/recuperabilidade. |

### L003-17 — Git / patch e contexto Android

Diretório-fonte: `KNOWLEDGE/natalia/20260422_171728_Erro no Prototipo Android_ Análise dos Arquivos - Manus/`
Vínculo textual: conversa sobre terminal/Git; patch, aplicação, build e teste ausentes.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 134399 | 1280×845 | `6b86d1029efc18b303842f01cbbded568feff93f268150fa88f8037d0df631c9` | `f91649166d964d96` | Captura de instruções Git/créditos/tarefa em espera; não demonstra patch aplicado ou app. |

### L003-18 — Android / fragmento Gradle

Diretório-fonte: `KNOWLEDGE/meshwave65/20260422_Analise do erro com arquivos do projeto Android - Manus/`
Vínculo textual: fragmento de `build.gradle` e versões disputadas; a captura registra incompatibilidade/interrupção, não build bem-sucedido.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 101822 | 1280×845 | `21e677934483f04ec2afe4ebaa5ef1c671c219defa1d1814b6834c298a250706` | `ed166d964d964196` | Captura de trecho de configuração Java 17/Gradle e interrupção; não valida compatibilidade nem compilação. |

### L003-19 — Git / sincronização operacional

Diretório-fonte: `KNOWLEDGE/iury/20260422_161432_Como sincronizar repositório local com GitHub via SSH - Manus/`
Vínculo textual: roteiro de Git/SSH e alegações de push/licença; a captura não confirma o estado remoto atual.

| Arquivo | Extensão / formato detectado | Bytes | Dimensões | SHA-256 | pHash | Descrição e relação com o texto |
|---|---|---:|---|---|---|---|
| `FULL.png` | `.png` / PNG | 147843 | 1280×845 | `51cc66e1e3e1bd18b1fccb7b0d12276940d049df1cc2173a43995e87fca9f461` | `fd96c19669966514` | Captura de roteiro SSH/main/licença e rótulo de tarefa concluída; não comprova push, configuração ou licença publicada. |

## Relação com os domínios e decisões de curadoria

| Conjuntos | Domínio/uso da imagem | Tratamento curatorial |
|---|---|---|
| L003-01, L003-07–09, L003-13–14, L003-17–18 | Android, Gradle, interfaces, compatibilidade e erros | Evidência de histórico, requisitos ou falhas relatadas; não promover a prova de build, APK, hardware ou operação. |
| L003-02, L003-04, L003-06, L003-11–12, L003-16 | Sofia API, tarefas, uploads e relatórios | Capturas de estados/erros e cartões de interface; não validar chamadas, uploads, conclusão ou persistência. |
| L003-05, L003-10, L003-19 | Handoff, exportação e Git operacional | Contexto de processo; não validar arquitetura, integridade de pacote, sincronização ou estado remoto. |
| L003-15 | Identidade/DID | Representação de proposta; não validar especificação, cálculo, governança ou conformidade. |
| L003-03 | Material médico externo | Contexto visual do capítulo médico narrado; fora do núcleo de produto MeshWave e com fonte/licença não confirmadas. |

Não foram alteradas as imagens brutas. Relações temáticas entre os conjuntos não foram convertidas em relações de duplicidade: permanecem as distinções e ressalvas da classificação F1.3.

## Lacunas e próximos usos

1. Investigar fonte, autoria, licença e contexto de captura dos anexos incorporados, sobretudo os 14 arquivos `img_000.jpg`–`img_013.jpg` de L003-03, antes de qualquer reutilização externa.
2. Se houver necessidade de citar texto dentro de capturas, executar OCR como etapa separada e confrontar o resultado com o arquivo original; esta catalogação não afirma OCR.
3. Manter nomes/extensões originais. As divergências PNG/WebP sob `.jpg` estão registradas para rastreabilidade, sem normalização destrutiva.
4. Usar este índice como apoio a F1.5 (código/evidências) e F1.6 (links/fontes externas), sem inferir implementação a partir de capturas.

## Histórico

| Data | Alteração | Commit |
|---|---|---|
| 2026-10-08 | Catálogo de 35 imagens dos 19 conjuntos Lote 003; metadados, SHA-256, pHash, observações e lacunas | ver histórico Git desta alteração |
