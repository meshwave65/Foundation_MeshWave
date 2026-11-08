# Checkpoint — Módulo conceitual de aferição de serviços

**Data:** 2026-11-08  
**Repositório:** `meshwave65/Foundation_MeshWave`  
**Branch publicada:** `main`  
**Commit-base reconciliado:** `7e8b3864414f2ce8810dcea5ca67d2036bf65b8e`  
**Tipo de trabalho:** atualização documental lateral, fora da fila de leitura de fontes brutas

## Objetivo

Persistir a definição do responsável para um módulo conceitual de aferição opcional de serviços, qualidade e privacidade por adesão, com ligação ao roadmap geral MeshWave e à PoUW/UMS.

## Definições registradas

- Aferição individual é opcional; o cliente decide se deseja monitoramento da operação.
- A aferição pode ser contínua ou amostral e combinar telemetria, sondagens independentes, evidências de usuários, registros verificáveis, indicadores de qualidade/disponibilidade, regras de falha/degradação/recuperação e contestação.
- A MeshWave pode fornecer o serviço ou homologar aferidores terceiros.
- Protocolos e métodos devem ser abertos e verificáveis para que empresas possam examinar e concordar com critérios.
- Propõe-se uma comissão permanente com representantes das empresas para revisar a correção dos métodos e indicadores.
- Sem adesão ao monitoramento individual, não há redução do preço contratado por aferição individual; telemetria individual identificável não deve ser persistida e não pode ser recuperada. A observabilidade sistêmica permanece, com proteção contra reidentificação.
- Com adesão, a aferição individual e eventuais ajustes devem seguir os critérios previamente acordados.
- A aferição pode ser atividade elegível a PoUW/UMS, mas critérios formais de reconhecimento e remuneração estão pendentes.
- O efeito sistêmico pretendido inclui maior incentivo reputacional/econômico à entrega conforme o contratado, sem tornar aferição universal.

## Artefatos publicados

- `BCE/temas/afericao-servicos-qualidade-e-privacidade.md` — módulo DOM-23.
- `BCE/INDICE_CURATORIAL.md` — DOM-23 indexado.
- `BCE/temas/economia-ums-mwn-pouw-liquidez-distribuida.md` — ligação ao modelo PoUW/UMS.
- `BCE/temas/arquitetura-geral-e-implantacao.md` — módulo inserido como proposta conceitual de roadmap, sem fase ou prazo.
- `BCE/REGISTRO_DECISOES.md` — DEC-BCE-010, decisão de registrar o conceito (não de afirmar implementação).

## Commits

- Documento DOM-23: `7b45a387a7729690ab33d8b7970474cfa5dfb42a`
- Índice DOM-23: `910909405f4c26de1270f5840383d98bb7ea8ce1`
- Economia PoUW/UMS: `bd026b1b1c588f0cfd9b41a641818407d03d3ea4`
- Arquitetura/roadmap: `f8fbd4d8b0431c51fd883dd829143d1b207015b5`
- Registro de decisões DEC-BCE-010: `61a24848e60111845a44e25bebaeae223e75429c`

## Limites e continuidade

Nenhuma fonte bruta em `KNOWLEDGE/` foi aberta, alterada ou processada. Nenhum código foi implementado. Protocolo, métricas, critérios de homologação, comissão, contratos, governança, LGPD e técnica de descarte/anti-reidentificação permanecem para especificação e validação.

A fila e a próxima ação da `MISSION_0011` / F3.3 permanecem inalteradas: reconciliar fila e locks antes de selecionar outro contato elegível. Este trabalho não reivindica, não fecha e não modifica os locks daquela missão.
