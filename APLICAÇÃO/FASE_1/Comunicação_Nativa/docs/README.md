# Documentação da Comunicação Nativa

Este diretório contém a documentação detalhada sobre a implementação e funcionamento dos módulos de comunicação nativa do Projeto MeshWave, focando em tecnologias como Wi-Fi Direct e Bluetooth Low Energy (BLE) para comunicação P2P.

## 1. Visão Geral da Comunicação P2P

A comunicação Peer-to-Peer (P2P) é um pilar fundamental do Projeto MeshWave, permitindo que dispositivos se conectem e troquem dados diretamente, sem a necessidade de um servidor central. Isso garante resiliência, escalabilidade e eficiência em ambientes sem infraestrutura de rede tradicional.

### 1.1. Wi-Fi Direct

O Wi-Fi Direct permite que dispositivos com Wi-Fi se conectem diretamente entre si, formando uma rede P2P. É ideal para a descoberta de peers e a transferência de dados em alta velocidade em curtas distâncias.

### 1.2. Bluetooth Low Energy (BLE)

O BLE é otimizado para baixo consumo de energia e é adequado para a descoberta de dispositivos e a troca de pequenas quantidades de dados em cenários onde a eficiência energética é crítica. Pode ser usado em conjunto com o Wi-Fi Direct para um modo híbrido de otimização de energia.

## 2. Especificações de Protocolos de Comunicação

### 2.1. Descoberta de Dispositivos

*   **Wi-Fi Direct:** Utiliza o serviço `WifiP2pManager.discoverPeers()` para encontrar dispositivos próximos.
*   **BLE:** Utiliza o modo de publicidade (advertising) e escaneamento (scanning) para descoberta.

### 2.2. Estabelecimento de Conexão

*   **Wi-Fi Direct:** Conexão estabelecida via `WifiP2pManager.connect()`, formando um grupo P2P com um Group Owner (GO) e clientes.
*   **BLE:** Conexão baseada em GATT (Generic Attribute Profile), onde um dispositivo atua como servidor GATT e outro como cliente.

### 2.3. Troca de Dados

*   **Wi-Fi Direct:** Utiliza sockets TCP/IP sobre a conexão P2P para troca de mensagens e arquivos.
*   **BLE:** Troca de dados via características GATT (leitura, escrita, notificação).

## 3. Relatórios de Testes de Conectividade

(Esta seção será preenchida com os resultados dos testes de conectividade, incluindo latência, throughput e estabilidade das conexões Wi-Fi Direct e BLE.)

## 4. Análise de Desempenho da Comunicação

(Esta seção conterá análises detalhadas sobre o desempenho dos módulos de comunicação, identificando gargalos e oportunidades de otimização.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


