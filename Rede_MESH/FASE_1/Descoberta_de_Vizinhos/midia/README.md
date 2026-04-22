

## Imagens e Ilustrações da Descoberta de Vizinhos

Este diretório contém imagens e diagramas que visualizam os processos e conceitos relacionados à descoberta de vizinhos na rede MeshWave, utilizando Wi-Fi Direct e BLE.

### 1. Fluxo de Descoberta de Peers Wi-Fi Direct

Este diagrama ilustra os passos envolvidos na descoberta de peers usando Wi-Fi Direct, desde o início da sondagem até a identificação de dispositivos disponíveis.

```mermaid
flowchart TD
    A[Dispositivo Inicia discoverPeers()] --> B{Gerenciador Wi-Fi Direct}
    B --> C[Sonda a Rede]
    C --> D{Outros Dispositivos Respondem}
    D --> E[onPeersAvailable() Callback]
    E --> F[Lista de Peers Disponíveis]
    F --> G[Aplicativo Processa Lista]
```

### 2. Cenário de Descoberta Híbrida (Wi-Fi Direct e BLE)

Este diagrama conceitual mostra como Wi-Fi Direct e BLE podem ser usados em conjunto para uma estratégia de descoberta de vizinhos mais eficiente e com menor consumo de energia.

```mermaid
graph TD
    subgraph Dispositivo MeshWave
        A[Módulo de Descoberta]
    end

    subgraph Tecnologias
        B[Wi-Fi Direct]
        C[Bluetooth Low Energy (BLE)]
    end

    subgraph Rede
        D[Outros Dispositivos MeshWave]
    end

    A -- Inicia --> B
    A -- Inicia --> C
    B -- Descobre --> D
    C -- Descobre --> D
    D -- Anuncia Presença --> B
    D -- Anuncia Presença --> C
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


