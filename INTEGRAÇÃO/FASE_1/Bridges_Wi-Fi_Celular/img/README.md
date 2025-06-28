

## Imagens e Ilustrações das Bridges Wi-Fi/Celular

Este diretório contém imagens e diagramas que visualizam os conceitos e a arquitetura das bridges que conectam a rede MeshWave a redes Wi-Fi tradicionais e redes celulares.

### 1. Diagrama Conceitual de uma Bridge Wi-Fi

Este diagrama ilustra como um dispositivo MeshWave pode atuar como uma bridge, conectando a rede mesh local a uma rede Wi-Fi externa e, consequentemente, à internet.

```mermaid
graph TD
    subgraph Rede MeshWave
        A[Dispositivo MeshWave 1]
        B[Dispositivo MeshWave 2]
        C[Dispositivo MeshWave (Bridge)]
        A --- C
        B --- C
    end

    subgraph Rede Wi-Fi Externa
        D[Roteador Wi-Fi]
        E[Internet]
        D --- E
    end

    C -- Conexão Wi-Fi --> D
```

### 2. Diagrama Conceitual de uma Bridge Celular

Este diagrama mostra como um dispositivo MeshWave com conectividade celular pode servir como um gateway, permitindo que a rede mesh acesse a internet através da rede móvel.

```mermaid
graph TD
    subgraph Rede MeshWave
        A[Dispositivo MeshWave 1]
        B[Dispositivo MeshWave 2]
        C[Dispositivo MeshWave (Bridge Celular)]
        A --- C
        B --- C
    end

    subgraph Rede Celular
        D[Torre de Celular]
        E[Internet]
        D --- E
    end

    C -- Conexão Celular --> D
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


