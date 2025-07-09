

## Imagens e Ilustrações das Aplicações Otimizadas

Este diretório contém imagens e diagramas que visualizam os conceitos e a funcionalidade das aplicações otimizadas para o Projeto MeshWave, ilustrando como elas aproveitam a arquitetura da rede mesh.

### 1. Diagrama de Comunicação P2P Direta

Este diagrama ilustra como uma aplicação otimizada pode estabelecer uma comunicação direta ponto a ponto entre dois nós vizinhos na rede mesh, sem passar por um servidor central.

```mermaid
graph TD
    A[Aplicação A (Nó 1)] --> B(Nó 1)
    B -- Conexão Direta Mesh --> C(Nó 2)
    C --> D[Aplicação B (Nó 2)]

    subgraph Rede MeshWave
        B
        C
    end

    Note over B,C: Comunicação Local e Eficiente
```

### 2. Fluxo de Processamento Cooperativo em Aplicações

Este fluxograma demonstra como uma aplicação pode delegar uma tarefa de processamento para outro nó na rede mesh que tenha recursos ociosos, otimizando o desempenho geral.

```mermaid
flowchart TD
    A[Aplicação (Nó X)] --> B{Tarefa de Processamento}
    B --> C{Nó Ocioso Disponível?}
    C -- Sim --> D[Enviar Tarefa para Nó Ocioso]
    D --> E[Nó Ocioso Processa Tarefa]
    E --> F[Nó Ocioso Retorna Resultado]
    F --> A
    C -- Não --> G[Processar Tarefa Localmente]
    G --> A
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


