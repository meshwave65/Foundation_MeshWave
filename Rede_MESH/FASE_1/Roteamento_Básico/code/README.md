

## Exemplos de Código e Algoritmos para Roteamento Básico

Este diretório contém exemplos de código e pseudocódigo para a implementação de mecanismos de roteamento básico na rede MeshWave. O foco está em demonstrar como os nós podem encaminhar mensagens para seus destinos.

### 1. Pseudocódigo para Roteamento por Inundação (Flooding)

Este algoritmo simples garante que uma mensagem eventualmente chegue ao seu destino, retransmitindo-a para todos os vizinhos, exceto o remetente original.

```pseudocode
FUNCTION handle_received_message(message, source_node):
    IF message.destination == THIS_NODE.id:
        process_message(message)
    ELSE IF message.id NOT IN processed_messages_cache:
        add_to_processed_messages_cache(message.id)
        FOR EACH neighbor IN THIS_NODE.neighbors:
            IF neighbor != source_node:
                send_message(message, neighbor)
    END IF
END FUNCTION

FUNCTION send_message(message, target_node):
    // Lógica para enviar a mensagem para o nó vizinho
    // (e.g., via socket TCP/IP sobre Wi-Fi Direct)
END FUNCTION
```

### 2. Pseudocódigo para Roteamento Simples Baseado em Próximo Salto

Este algoritmo representa uma forma mais controlada de roteamento, onde cada nó decide o próximo salto com base em uma tabela de roteamento local ou conhecimento direto do destinatário.

```pseudocode
FUNCTION handle_received_message(message, source_node):
    IF message.destination == THIS_NODE.id:
        process_message(message)
    ELSE:
        next_hop = lookup_next_hop(message.destination)
        IF next_hop IS NOT NULL:
            send_message(message, next_hop)
        ELSE:
            log_error("Destino inalcançável ou rota desconhecida para " + message.destination)
            // Opcional: Retornar mensagem de erro ao remetente
        END IF
    END IF
END FUNCTION

FUNCTION lookup_next_hop(destination_id):
    // Simula uma tabela de roteamento ou lógica de decisão
    // No protótipo, pode ser uma regra simples: se destino é Z, próximo salto é Y.
    IF destination_id == "NODE_Z" AND THIS_NODE.id == "NODE_X":
        RETURN "NODE_Y"
    ELSE IF destination_id == "NODE_Z" AND THIS_NODE.id == "NODE_Y":
        RETURN "NODE_Z" // Conexão direta
    // ... outras regras
    RETURN NULL // Rota não encontrada
END FUNCTION

FUNCTION send_message(message, target_node):
    // Lógica para enviar a mensagem para o nó vizinho
    // (e.g., via socket TCP/IP sobre Wi-Fi Direct)
END FUNCTION
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


