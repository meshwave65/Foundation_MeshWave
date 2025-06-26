

## Exemplos de Código e Algoritmos para Energia Adaptativa

Este diretório contém exemplos de código e pseudocódigo para a implementação de mecanismos de energia adaptativa no Projeto MeshWave, focando na otimização do consumo de energia.

### 1. Pseudocódigo para Modo Híbrido BLE/Wi-Fi Direct

Este algoritmo demonstra como um dispositivo pode alternar entre BLE (para baixo consumo) e Wi-Fi Direct (para alto throughput) com base na necessidade de dados.

```pseudocode
FUNCTION manage_power_mode(data_volume_needed):
    IF data_volume_needed == LOW:
        IF current_mode == WIFI_DIRECT:
            switch_to_ble_mode()
            log("Alternando para BLE para economia de energia.")
        END IF
    ELSE IF data_volume_needed == HIGH:
        IF current_mode == BLE:
            switch_to_wifi_direct_mode()
            log("Alternando para Wi-Fi Direct para alta transferência de dados.")
        END IF
    END IF
END FUNCTION

FUNCTION switch_to_ble_mode():
    // Desativar Wi-Fi Direct (se ativo)
    // Ativar BLE para descoberta e comunicação de baixo volume
    SET current_mode = BLE
END FUNCTION

FUNCTION switch_to_wifi_direct_mode():
    // Desativar BLE (se ativo)
    // Ativar Wi-Fi Direct para comunicação de alto volume
    SET current_mode = WIFI_DIRECT
END FUNCTION

// Exemplo de uso:
// Quando uma pequena mensagem de controle precisa ser enviada:
// manage_power_mode(LOW)
// send_ble_message()

// Quando um arquivo grande precisa ser transferido:
// manage_power_mode(HIGH)
// send_wifi_direct_file()
```

### 2. Pseudocódigo para Ciclos de Trabalho (Duty Cycling)

Este algoritmo ilustra como um dispositivo pode entrar em um estado de baixo consumo (dormir) e acordar periodicamente para verificar mensagens ou realizar tarefas.

```pseudocode
FUNCTION start_duty_cycling(sleep_interval_ms, active_interval_ms):
    WHILE TRUE:
        // Estado Ativo
        SET device_state = ACTIVE
        log("Dispositivo ativo. Verificando mensagens e realizando tarefas.")
        perform_active_tasks()
        WAIT(active_interval_ms)

        // Estado Dormindo
        SET device_state = SLEEPING
        log("Dispositivo dormindo para economizar energia.")
        enter_low_power_mode()
        WAIT(sleep_interval_ms)
    END WHILE
END FUNCTION

FUNCTION perform_active_tasks():
    // Verificar novas mensagens
    // Processar dados pendentes
    // Enviar beacons de presença
END FUNCTION

FUNCTION enter_low_power_mode():
    // Desativar módulos de rádio não essenciais
    // Reduzir frequência da CPU
    // Entrar em modo de suspensão
END FUNCTION

// Exemplo de uso:
// start_duty_cycling(5000, 500) // Dorme por 5s, ativo por 0.5s
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


