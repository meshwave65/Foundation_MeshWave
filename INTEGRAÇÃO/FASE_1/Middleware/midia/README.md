

## Imagens e Ilustrações do Middleware

Este diretório contém imagens e diagramas que visualizam os conceitos e a arquitetura do middleware do Projeto MeshWave, ilustrando como ele facilita a comunicação e a interação entre os componentes do sistema.

### 1. Diagrama de Arquitetura do Middleware

Este diagrama ilustra a posição do middleware como uma camada intermediária entre as aplicações e a camada de rede, destacando seus principais componentes e suas interações.

```mermaid
graph TD
    subgraph Aplicações
        A[App MeshWave]
        B[Outras Aplicações]
    end

    subgraph Middleware MeshWave
        C[Módulo de Descoberta de Serviços]
        D[Módulo de Mensageria]
        E[Módulo de Segurança]
    end

    subgraph Camada de Rede
        F[Wi-Fi Direct]
        G[BLE]
        H[Módulo de Roteamento]
    end

    A --> C
    A --> D
    B --> C
    B --> D

    C --> F
    C --> G
    D --> H
    E --> H

    H --> F
    H --> G
```

### 2. Fluxo de Comunicação Através do Middleware

Este fluxograma detalha como uma mensagem é processada e encaminhada através das diferentes camadas do middleware, desde a aplicação de origem até a camada de rede.

```mermaid
sequenceDiagram
    participant Aplicação
    participant Middleware
    participant Camada_Rede

    Aplicação->>Middleware: Enviar Mensagem
    Middleware->>Middleware: Processar Mensagem (Adicionar Metadados)
    Middleware->>Camada_Rede: Encaminhar Pacote
    Camada_Rede->>Camada_Rede: Roteamento
    Camada_Rede-->>Middleware: Pacote Recebido
    Middleware-->>Middleware: Desprocessar Mensagem
    Middleware-->>Aplicação: Entregar Mensagem
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


