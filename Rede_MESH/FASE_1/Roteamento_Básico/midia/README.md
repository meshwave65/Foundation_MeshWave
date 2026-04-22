

## Imagens e Ilustrações do Roteamento Básico

Este diretório contém imagens e diagramas que visualizam os conceitos e fluxos do roteamento básico na rede MeshWave.

### 1. Diagrama de Roteamento por Inundação (Flooding)

Este diagrama ilustra como uma mensagem se propaga através da rede quando o roteamento por inundação é utilizado. Cada nó retransmite a mensagem para todos os seus vizinhos, exceto o remetente.

```mermaid
graph TD
    A[Nó A] --> B(Nó B)
    A --> C(Nó C)
    B --> D(Nó D)
    C --> D
    B --> E(Nó E)
    D --> F(Nó F)

    subgraph Mensagem de A para F
        A -- Mensagem --> B
        A -- Mensagem --> C
        B -- Mensagem --> D
        B -- Mensagem --> E
        C -- Mensagem --> D
        D -- Mensagem --> F
    end
```

### 2. Exemplo de Roteamento Hop-by-Hop

Este diagrama mostra um caminho de roteamento simples onde cada nó decide o próximo salto com base em informações locais, sem a necessidade de uma visão global da rede.

```mermaid
sequenceDiagram
    participant Origem
    participant Nó1
    participant Nó2
    participant Destino

    Origem->>Nó1: Mensagem para Destino
    Nó1->>Nó2: Mensagem para Destino
    Nó2->>Destino: Mensagem para Destino
    Destino-->>Nó2: ACK
    Nó2-->>Nó1: ACK
    Nó1-->>Origem: ACK
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


