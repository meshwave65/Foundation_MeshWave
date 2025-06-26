

## Exemplos de Código e Algoritmos para Ativação em Duas Etapas

Este diretório contém exemplos de código e pseudocódigo para a implementação do mecanismo de ativação em duas etapas no Projeto MeshWave, focando na interação entre o dispositivo satélite e o dispositivo gestor.

### 1. Pseudocódigo para Dispositivo Satélite (Solicitação de Ingresso)

Este algoritmo descreve o comportamento de um dispositivo que deseja ingressar na rede MeshWave, solicitando acesso e aguardando a confirmação.

```pseudocode
FUNCTION request_network_join(network_id, device_id):
    display_user_prompt("Deseja ingressar na rede " + network_id + "?")
    IF user_confirms():
        send_join_request(network_id, device_id)
        start_timeout_timer(JOIN_REQUEST_TIMEOUT)
        WHILE NOT join_confirmed AND NOT timeout_expired:
            wait_for_confirmation()
        END WHILE

        IF join_confirmed:
            log("Ingresso na rede " + network_id + " confirmado.")
            configure_network_settings()
        ELSE:
            log_error("Falha ao ingressar na rede " + network_id + ": Tempo esgotado ou acesso negado.")
        END IF
    ELSE:
        log("Ingresso na rede " + network_id + " cancelado pelo usuário.")
    END IF
END FUNCTION

FUNCTION send_join_request(network_id, device_id):
    // Enviar mensagem criptografada para o dispositivo gestor
    // contendo network_id e device_id
END FUNCTION

FUNCTION wait_for_confirmation():
    // Escutar por mensagem de confirmação do dispositivo gestor
    // Se receber, SET join_confirmed = TRUE
END FUNCTION

FUNCTION configure_network_settings():
    // Receber e aplicar configurações de rede (IP, rotas, etc.)
END FUNCTION
```

### 2. Pseudocódigo para Dispositivo Gestor (Validação e Confirmação)

Este algoritmo descreve o comportamento de um dispositivo gestor que recebe solicitações de ingresso, valida-as e envia confirmações.

```pseudocode
FUNCTION listen_for_join_requests():
    WHILE TRUE:
        received_request = receive_join_request()
        IF received_request IS NOT NULL:
            device_id = received_request.device_id
            network_id = received_request.network_id

            IF is_device_whitelisted(device_id) OR request_manual_approval(device_id):
                log("Dispositivo " + device_id + " aprovado para ingresso.")
                send_join_confirmation(device_id, network_id, network_settings)
            ELSE:
                log_error("Dispositivo " + device_id + " negado para ingresso.")
                send_join_denial(device_id, network_id)
            END IF
        END IF
    END WHILE
END FUNCTION

FUNCTION is_device_whitelisted(device_id):
    // Verificar se device_id está em uma lista de dispositivos pré-aprovados
    RETURN TRUE_OR_FALSE
END FUNCTION

FUNCTION request_manual_approval(device_id):
    // Exibir solicitação de aprovação em painel administrativo
    // Aguardar decisão do administrador
    RETURN TRUE_OR_FALSE
END FUNCTION

FUNCTION send_join_confirmation(device_id, network_id, settings):
    // Enviar mensagem criptografada para o dispositivo satélite
    // contendo confirmação e configurações de rede
END FUNCTION

FUNCTION send_join_denial(device_id, network_id):
    // Enviar mensagem de negação para o dispositivo satélite
END FUNCTION
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


