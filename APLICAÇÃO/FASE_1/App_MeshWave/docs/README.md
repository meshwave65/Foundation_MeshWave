# Documentação do App MeshWave

Este diretório contém a documentação detalhada sobre o desenvolvimento e funcionamento do aplicativo MeshWave, um protótipo de comunicação móvel descentralizada, similar a um aplicativo de mensagens como o WhatsApp, mas construído sobre a infraestrutura MeshWave.

## 1. Visão Geral do Aplicativo

O aplicativo MeshWave visa demonstrar a operabilidade e os conceitos de comunicação P2P (Peer-to-Peer) e roteamento em uma rede mesh. Ele permitirá a troca de mensagens de texto e, futuramente, o envio de arquivos entre dispositivos conectados à rede MeshWave, sem depender de uma infraestrutura centralizada tradicional.

### 1.1. Propósito

O principal propósito deste protótipo é validar a viabilidade técnica da comunicação direta entre dispositivos em uma rede mesh, testar a resiliência do roteamento e a capacidade de autogerenciamento da rede. Ele servirá como uma prova de conceito para futuras aplicações descentralizadas.

### 1.2. Funcionalidades Principais (Protótipo Inicial)

*   **Troca de Mensagens:** Envio e recebimento de mensagens de texto entre usuários da rede mesh.
*   **Descoberta de Peers:** Capacidade de identificar outros dispositivos MeshWave disponíveis na proximidade via Wi-Fi Direct.
*   **Conexão P2P:** Estabelecimento de conexões diretas entre dispositivos para comunicação.
*   **Roteamento Básico:** Encaminhamento de mensagens através de nós intermediários quando o destinatário não está em alcance direto.

## 2. Requisitos Funcionais e Não Funcionais

### 2.1. Requisitos Funcionais

*   O aplicativo deve permitir que usuários enviem e recebam mensagens de texto.
*   O aplicativo deve ser capaz de descobrir outros dispositivos MeshWave na rede local.
*   O aplicativo deve permitir a conexão direta com peers descobertos.
*   O aplicativo deve ser capaz de rotear mensagens para destinatários não diretamente conectados.
*   O aplicativo deve exibir um log de eventos para monitoramento da comunicação.

### 2.2. Requisitos Não Funcionais

*   **Desempenho:** A troca de mensagens deve ocorrer com latência aceitável em cenários de rede mesh.
*   **Confiabilidade:** As mensagens devem ser entregues ao destinatário, mesmo com falhas de conexão temporárias (com retransmissão).
*   **Segurança:** Implementação futura de criptografia E2E para mensagens.
*   **Usabilidade:** Interface de usuário intuitiva para envio de mensagens e visualização de logs.
*   **Portabilidade:** Capacidade de ser executado em dispositivos Android (e futuramente iOS).

## 3. Arquitetura Proposta

A arquitetura do aplicativo MeshWave é baseada em um modelo descentralizado, utilizando as capacidades de Wi-Fi Direct para comunicação P2P e sockets TCP/IP para a troca de dados. A lógica de roteamento é distribuída entre os nós da rede.

### 3.1. Componentes Principais

*   **Módulo de Gerenciamento Wi-Fi Direct:** Responsável pela descoberta de peers, conexão e gerenciamento de grupos P2P.
*   **Módulo de Comunicação (Sockets):** Gerencia a abertura e fechamento de sockets para envio e recebimento de dados.
*   **Módulo de Roteamento:** Determina o próximo salto para uma mensagem com base no destinatário e na topologia da rede (simplificado no protótipo).
*   **Interface de Usuário (UI):** Permite ao usuário interagir com o aplicativo, enviar mensagens e visualizar o log.

## 4. Casos de Uso

*   **UC-001: Enviar Mensagem Direta:** Um usuário envia uma mensagem para um peer diretamente conectado.
*   **UC-002: Enviar Mensagem Roteada:** Um usuário envia uma mensagem para um peer não diretamente conectado, que é roteada por um ou mais nós intermediários.
*   **UC-003: Receber Mensagem:** Um usuário recebe uma mensagem de outro peer.
*   **UC-004: Descobrir Peers:** O aplicativo descobre outros dispositivos MeshWave disponíveis na rede.
*   **UC-005: Conectar a Peer:** O aplicativo estabelece uma conexão P2P com um peer descoberto.

## 5. Relatórios de Testes

(Este seção será preenchida com os resultados dos testes de operabilidade e desempenho do protótipo.)

## 6. Observações e Decisões de Design

(Esta seção registrará as decisões importantes tomadas durante o desenvolvimento, como a escolha de tecnologias, padrões de comunicação, e desafios encontrados.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


