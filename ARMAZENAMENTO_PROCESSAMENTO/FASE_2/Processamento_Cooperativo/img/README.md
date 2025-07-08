

## Imagens e Ilustrações do Processamento Cooperativo

Este diretório contém imagens e diagramas que visualizam os conceitos e o fluxo do processamento cooperativo no Projeto MeshWave, ilustrando como as tarefas são divididas, distribuídas e seus resultados agregados.

### 1. Fluxo de Processamento Distribuído (Conceitual)

Este diagrama ilustra o processo de uma tarefa complexa sendo dividida em subtarefas, distribuída para múltiplos nós para processamento paralelo e, em seguida, os resultados sendo agregados para formar a solução final.

```mermaid
sequenceDiagram
    participant Usuário/Aplicação
    participant Módulo_Processamento
    participant Nó_A
    participant Nó_B
    participant Nó_C

    Usuário/Aplicação->>Módulo_Processamento: 1. Enviar Tarefa Complexa
    Módulo_Processamento->>Módulo_Processamento: 2. Dividir em Subtarefas (ST1, ST2, ST3)

    Módulo_Processamento->>Nó_A: 3. Enviar ST1
    Módulo_Processamento->>Nó_B: 4. Enviar ST2
    Módulo_Processamento->>Nó_C: 5. Enviar ST3

    Nó_A->>Nó_A: 6. Processar ST1
    Nó_B->>Nó_B: 7. Processar ST2
    Nó_C->>Nó_C: 8. Processar ST3

    Nó_A->>Módulo_Processamento: 9. Retornar Resultado ST1
    Nó_B->>Módulo_Processamento: 10. Retornar Resultado ST2
    Nó_C->>Módulo_Processamento: 11. Retornar Resultado ST3

    Módulo_Processamento->>Módulo_Processamento: 12. Agregação de Resultados
    Módulo_Processamento-->>Usuário/Aplicação: 13. Retornar Resultado Final
```

### 2. Diagrama de Seleção de Nó para Subtarefa

Este diagrama conceitual mostra os critérios que podem ser usados para selecionar o nó mais adequado para executar uma subtarefa em um ambiente de processamento cooperativo.

```mermaid
graph TD
    A[Subtarefa Pendente] --> B{Capacidade de CPU/Memória?}
    B -- Sim --> C{Carga Atual do Nó?}
    C -- Baixa --> D{Proximidade (Latência)?}
    D -- Alta --> E[Selecionar Nó]
    D -- Baixa --> E
    C -- Alta --> F[Rejeitar Nó / Tentar Outro]
    B -- Não --> F
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


