# Documentação da Descoberta de Vizinhos

Este diretório contém a documentação detalhada sobre os mecanismos e estratégias para a descoberta de vizinhos na rede MeshWave. A capacidade de identificar e localizar dispositivos próximos é fundamental para o estabelecimento e manutenção da conectividade mesh.

## 1. Visão Geral da Descoberta de Vizinhos

A descoberta de vizinhos é o processo pelo qual um dispositivo MeshWave identifica outros dispositivos MeshWave em sua proximidade física ou lógica. Este processo é contínuo e dinâmico, adaptando-se às mudanças na topologia da rede e na disponibilidade dos dispositivos.

### 1.1. Importância na Rede Mesh

*   **Formação da Rede:** Permite que novos dispositivos se juntem à rede e que dispositivos existentes encontrem novos caminhos.
*   **Roteamento:** Fornece informações essenciais para os algoritmos de roteamento determinarem os melhores caminhos para a entrega de mensagens.
*   **Resiliência:** Ajuda a rede a se adaptar a falhas de nós, permitindo a descoberta de rotas alternativas.

## 2. Tecnologias de Descoberta

O Projeto MeshWave emprega uma combinação de tecnologias para otimizar a descoberta de vizinhos, considerando diferentes cenários e requisitos de energia.

### 2.1. Wi-Fi Direct (P2P)

*   **Mecanismo:** Utiliza o serviço `WifiP2pManager.discoverPeers()` para escanear e anunciar a presença de dispositivos Wi-Fi Direct. Permite a descoberta de dispositivos que não estão conectados a um ponto de acesso tradicional.
*   **Vantagens:** Alta velocidade de descoberta, ideal para cenários de alta densidade de dispositivos.
*   **Desafios:** Consumo de energia relativamente alto, pode ser impactado por interferências.

### 2.2. Bluetooth Low Energy (BLE)

*   **Mecanismo:** Dispositivos anunciam sua presença (advertising) e outros dispositivos escaneiam por esses anúncios. Pode ser usado para descoberta de proximidade e identificação de dispositivos de baixo consumo.
*   **Vantagens:** Baixo consumo de energia, ideal para dispositivos IoT e cenários de longa duração de bateria.
*   **Desafios:** Menor alcance e throughput em comparação com Wi-Fi Direct.

### 2.3. Outras Abordagens (Futuras)

*   **Descoberta Baseada em GPS/Localização:** Utilização de coordenadas geográficas para auxiliar na descoberta de vizinhos em áreas geográficas maiores.
*   **Descoberta por Ultrassom/Áudio:** Para cenários de proximidade muito curta e ambientes internos.

## 3. Estratégias de Descoberta

*   **Descoberta Ativa:** Dispositivos enviam ativamente pacotes de sondagem para encontrar vizinhos.
*   **Descoberta Passiva:** Dispositivos escutam por anúncios de outros dispositivos.
*   **Descoberta Híbrida:** Combinação de abordagens ativa e passiva para otimizar o desempenho e o consumo de energia.

## 4. Relatórios de Testes e Análise

(Esta seção será preenchida com os resultados dos testes de desempenho da descoberta de vizinhos, incluindo tempo de descoberta, precisão e impacto no consumo de energia.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


