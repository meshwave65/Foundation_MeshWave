

## Imagens e Ilustrações da Redundância

Este diretório contém imagens e diagramas que visualizam os conceitos e a implementação de mecanismos de redundância no Projeto MeshWave, ilustrando como a alta disponibilidade e a resiliência são alcançadas.

### 1. Diagrama de Replicação de Dados

Este diagrama ilustra como um item de dado é replicado para múltiplos nós na rede mesh, garantindo que, mesmo que um nó falhe, o dado ainda esteja disponível em outras réplicas.

```mermaid
graph TD
    A[Dado Original] --> B(Nó de Origem)
    B --> C[Replicação para Nó 1]
    B --> D[Replicação para Nó 2]
    B --> E[Replicação para Nó 3]

    C -- Disponível --> F(Nó 1)
    D -- Disponível --> G(Nó 2)
    E -- Disponível --> H(Nó 3)

    subgraph Rede Mesh
        F
        G
        H
    end
```

### 2. Fluxo de Roteamento com Caminhos Alternativos

Este fluxograma demonstra como o sistema de roteamento do MeshWave pode usar caminhos alternativos para entregar mensagens, garantindo a comunicação mesmo em caso de falha de um caminho primário.

```mermaid
flowchart TD
    A[Mensagem para Destino] --> B{Caminho Primário Ativo?}
    B -- Sim --> C[Enviar via Caminho Primário]
    B -- Não --> D{Caminho Secundário Ativo?}
    D -- Sim --> E[Enviar via Caminho Secundário]
    D -- Não --> F[Falha na Entrega / Notificar]
    C --> G[Mensagem Entregue]
    E --> G
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


