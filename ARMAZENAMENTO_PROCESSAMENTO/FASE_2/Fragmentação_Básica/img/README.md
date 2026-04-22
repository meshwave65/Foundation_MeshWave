

## Imagens e Ilustrações da Fragmentação Básica

Este diretório contém imagens e diagramas que visualizam os conceitos e o fluxo da fragmentação básica de dados no Projeto MeshWave, ilustrando como os arquivos são divididos em partes menores.

### 1. Diagrama de Fragmentação de Arquivo

Este diagrama ilustra o processo de um arquivo sendo dividido em múltiplos fragmentos de tamanho fixo, cada um com seu próprio identificador e metadados.

```mermaid
graph TD
    A[Arquivo Original] --> B(Módulo de Fragmentação)
    B --> C1[Fragmento 1]
    B --> C2[Fragmento 2]
    B --> C3[Fragmento 3]
    B --> C4[Fragmento N]

    subgraph Fragmentos
        C1
        C2
        C3
        C4
    end

    C1 -- Metadados: ID, Índice, Checksum --> M1[Metadados F1]
    C2 -- Metadados: ID, Índice, Checksum --> M2[Metadados F2]
    C3 -- Metadados: ID, Índice, Checksum --> M3[Metadados F3]
    C4 -- Metadados: ID, Índice, Checksum --> M4[Metadados FN]
```

### 2. Fluxo de Remontagem de Arquivos

Este fluxograma demonstra como os fragmentos são coletados, verificados e concatenados na ordem correta para reconstruir o arquivo original.

```mermaid
flowchart TD
    A[Coletar Fragmentos] --> B{Verificar Checksum?}
    B -- Sim --> C{Checksum Válido?}
    C -- Sim --> D[Ordenar por Índice]
    C -- Não --> E[Erro: Fragmento Corrompido]
    D --> F[Concatenar Fragmentos]
    F --> G[Arquivo Reconstruído]
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


