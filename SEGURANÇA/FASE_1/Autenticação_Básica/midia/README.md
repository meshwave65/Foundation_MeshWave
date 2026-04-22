

## Imagens e Ilustrações da Autenticação Básica

Este diretório contém imagens e diagramas que visualizam os conceitos e o fluxo da autenticação básica no Projeto MeshWave, ilustrando como a identidade de usuários e dispositivos é verificada.

### 1. Fluxo de Autenticação de Usuário (Credenciais)

Este diagrama ilustra o processo de autenticação de um usuário ou dispositivo usando credenciais (nome de usuário e senha) e a verificação contra um banco de dados seguro.

```mermaid
sequenceDiagram
    participant Usuário/Dispositivo
    participant Aplicação/Serviço
    participant Banco_de_Dados_Credenciais

    Usuário/Dispositivo->>Aplicação/Serviço: 1. Enviar Credenciais (Usuário, Senha)
    Aplicação/Serviço->>Banco_de_Dados_Credenciais: 2. Consultar Credenciais (Usuário)
    Banco_de_Dados_Credenciais-->>Aplicação/Serviço: 3. Retornar Hash da Senha e Salt
    Aplicação/Serviço->>Aplicação/Serviço: 4. Hashear Senha Fornecida com Salt
    Aplicação/Serviço->>Aplicação/Serviço: 5. Comparar Hashes
    alt Hashes Coincidem
        Aplicação/Serviço-->>Usuário/Dispositivo: 6. Autenticação Bem-Sucedida
    else Hashes Não Coincidem
        Aplicação/Serviço-->>Usuário/Dispositivo: 6. Autenticação Falhou
    end
```

### 2. Diagrama de Autenticação Baseada em PSK (Chave Pré-Compartilhada)

Este diagrama conceitual mostra como dois dispositivos podem autenticar um ao outro usando uma chave pré-compartilhada (PSK) e um mecanismo de desafio-resposta para provar que ambos conhecem a chave sem revelá-la.

```mermaid
sequenceDiagram
    participant Dispositivo_A
    participant Dispositivo_B

    Dispositivo_A->>Dispositivo_B: 1. Iniciar Autenticação (Enviar Desafio)
    Dispositivo_B->>Dispositivo_B: 2. Calcular Resposta (PSK + Desafio)
    Dispositivo_B->>Dispositivo_A: 3. Enviar Resposta
    Dispositivo_A->>Dispositivo_A: 4. Calcular Resposta Esperada
    alt Respostas Coincidem
        Dispositivo_A->>Dispositivo_B: 5. Autenticação Bem-Sucedida
    else Respostas Não Coincidem
        Dispositivo_A->>Dispositivo_B: 5. Autenticação Falhou
    end
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


