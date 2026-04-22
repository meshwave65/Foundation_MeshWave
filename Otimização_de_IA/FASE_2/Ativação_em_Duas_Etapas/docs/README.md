# Documentação da Ativação em Duas Etapas

Este diretório contém a documentação detalhada sobre o mecanismo de ativação em duas etapas no Projeto MeshWave. Este processo de segurança visa garantir que apenas dispositivos autorizados possam ingressar na rede mesh, prevenindo acessos indevidos e aumentando a integridade da rede.

## 1. Visão Geral da Ativação em Duas Etapas

A ativação em duas etapas é um protocolo de segurança que exige a confirmação de um dispositivo satélite e a validação por um dispositivo gestor antes que o dispositivo satélite possa se tornar um membro pleno da rede MeshWave. Isso adiciona uma camada extra de segurança, especialmente em ambientes onde a descoberta de dispositivos pode ser aberta.

### 1.1. Importância na Rede Mesh

*   **Segurança:** Previne a inclusão de dispositivos não autorizados na rede, protegendo contra ataques e acesso indevido a dados.
*   **Controle:** Permite que os administradores da rede tenham controle sobre quais dispositivos podem se juntar à rede.
*   **Integridade:** Garante que a rede seja composta apenas por nós confiáveis, mantendo a integridade da comunicação.

## 2. Processo de Ativação

O processo de ativação em duas etapas envolve a interação entre o dispositivo satélite (o novo dispositivo que deseja ingressar) e o dispositivo gestor (um nó já estabelecido na rede, geralmente o líder da célula ou um gateway).

### 2.1. Solicitação de Ingresso (Dispositivo Satélite)

*   O dispositivo satélite, após descobrir a rede MeshWave, envia uma solicitação de ingresso. Esta solicitação pode incluir informações de identificação do dispositivo.
*   O dispositivo satélite exibe uma interface para o usuário confirmar o desejo de ingressar na rede.

### 2.2. Validação (Dispositivo Gestor)

*   O dispositivo gestor recebe a solicitação de ingresso e a apresenta a um administrador (ou a um processo automatizado).
*   A validação pode ocorrer de duas formas:
    *   **Whitelist:** O dispositivo gestor verifica se o ID do dispositivo satélite está em uma lista de dispositivos pré-aprovados.
    *   **Aprovação Manual:** Um administrador aprova manualmente a solicitação através de uma interface de gerenciamento.

### 2.3. Confirmação e Ingresso

*   Após a validação bem-sucedida, o dispositivo gestor envia uma confirmação ao dispositivo satélite.
*   O dispositivo satélite, ao receber a confirmação, completa seu processo de ingresso na rede, obtendo as configurações necessárias e começando a participar da comunicação mesh.

## 3. Mecanismos de Segurança

*   **Criptografia:** A comunicação durante o processo de ativação deve ser criptografada para proteger as informações de identificação e as chaves de rede.
*   **Assinaturas Digitais:** As mensagens de solicitação e confirmação podem ser assinadas digitalmente para garantir a autenticidade.

## 4. Relatórios de Testes e Análise

(Esta seção será preenchida com os resultados dos testes de segurança e usabilidade do processo de ativação em duas etapas, incluindo a eficácia na prevenção de acessos não autorizados.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


