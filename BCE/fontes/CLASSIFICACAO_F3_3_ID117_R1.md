# Reauditoria de fonte — F3.3/ID-117-R1

## Metadados

| Campo | Valor |
|---|---|
| Unidade | `F3.3/ID-117-R1` |
| Contato relacionado | `F3.3/ID-117` |
| Origem declarada | Código recuperado do computador local e enviado pelo usuário como `pasted_content.txt` |
| Cópia versionada | `BCE/fontes/anexos/F3.3-ID117-R1/pasted_content.txt` |
| Tamanho | 4.838 bytes; 140 linhas |
| SHA-256 | `78006cf128e751eb3a7617d58fd36977ec8214b0e11ff9618771c1bf9f996fd9` |
| Claim | `BCE/locks/F3.3-ID117-R1.lock.md`, publicado em `ab0791a` |
| Pré-registro | `BCE/sessoes/2026-10-31_f3-3-id117-r1-abertura.md`, publicado em `ab0791a` |
| Estado | Reauditoria concluída; launcher Bash recuperado, sem o projeto do simulador ou resultado de execução |

## Achado novo

O anexo é um script Bash de 140 linhas que implementa o launcher apontado pelo atalho `.desktop` auditado no ID-117. Ele deriva sua própria pasta por `BASH_SOURCE`, exige que o diretório contenha `requirements.txt` e `src/`, cria ou reutiliza um ambiente virtual `venv`, verifica `python3` e `pip`, instala `requirements.txt`, define `src/main.py` como aplicação Flask e usa `127.0.0.1:5000` como URL local.

O script também verifica a porta 5000 com `netstat`, tenta abrir o navegador com `xdg-open`, `gnome-open` ou Firefox, inicia `python3 src/main.py` com `nohup`, redireciona a saída para `flask_server.log`, aguarda cinco segundos e verifica se o processo ainda existe. Isso materializa a lógica do launcher e explica quais artefatos o projeto esperado deveria conter.

## O que a evidência sustenta

O anexo sustenta que existe uma versão textual de um launcher Bash para um simulador/aplicação Flask local. Ele conecta o atalho `.desktop` ao esperado `simulation_app/run_simulator_ubuntu.sh` e especifica um fluxo operacional plausível: validar estrutura, preparar ambiente Python, instalar dependências, iniciar `src/main.py` e abrir `http://127.0.0.1:5000`.

A evidência **não** sustenta que o launcher tenha sido executado, que o diretório exista, que `requirements.txt` ou `src/main.py` estejam disponíveis, que as dependências instalem, que o Flask inicie, que a porta responda, que o simulador implemente roteamento ou que existam gráficos/resultados. Não há logs, código Flask, código do simulador, `requirements.txt`, saída de execução, versão, commit, dados, topologia ou teste.

A linha `pip install -r requirements.txt`, os comandos `nohup`, `netstat`, `ps` e `xdg-open` foram tratados como dados textuais não confiáveis. Nenhum foi executado. Também não houve acesso ao computador local ou ao endereço `127.0.0.1` do usuário.

## Reclassificação curatorial

A classificação anterior do ID-117 permanece correta para os quatro artefatos originais: eles continham apenas o atalho e o replay, sem o script. Com a evidência adicional, o contato passa de **configuração/replay de inicialização sem launcher recuperado** para **launcher Bash recuperado, parcialmente especificado, sem aplicação ou execução verificável**.

A lacuna DOM-03 §14.12 permanece aberta. O launcher fornece uma ponte operacional entre o atalho e uma aplicação Flask esperada, mas não demonstra o simulador, o algoritmo de roteamento, encaminhamento, métricas ou funcionamento.

## Proveniência e integridade

A cópia versionada foi criada sem alteração a partir de `/home/ubuntu/upload/pasted_content.txt`. O SHA-256 foi conferido no arquivo recebido e na cópia do repositório: `78006cf128e751eb3a7617d58fd36977ec8214b0e11ff9618771c1bf9f996fd9`. O anexo foi recebido como script Bash UTF-8; nenhum código foi executado.
