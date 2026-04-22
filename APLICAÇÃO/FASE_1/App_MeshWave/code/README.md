
# Código e Algoritmos do App MeshWave

Este diretório é destinado a armazenar o código-fonte, diagramas de fluxo, algoritmos e outros artefatos de desenvolvimento do aplicativo MeshWave.

## Conteúdo Esperado:

*   **Código-fonte:** Implementações em linguagens como Java/Kotlin (para Android) ou Swift/Objective-C (para iOS), ou frameworks cross-platform como React Native/Flutter.
*   **Diagramas:** Diagramas de classe, sequência, componentes, etc.
*   **Algoritmos:** Descrições e implementações de algoritmos chave para funcionalidades como descoberta de peers, roteamento de mensagens, etc.




## Estrutura de Código Proposta para o Protótipo (React Native)

Considerando a discussão anterior sobre o desenvolvimento cross-platform com React Native, a estrutura de código inicial para o protótipo do aplicativo MeshWave pode ser organizada da seguinte forma:

```
AppMeshWave/
├── App.js                  # Componente raiz da aplicação
├── index.js                # Ponto de entrada da aplicação
├── src/
│   ├── components/         # Componentes reutilizáveis da UI
│   │   ├── MessageInput.js
│   │   └── MessageBubble.js
│   ├── screens/            # Telas principais da aplicação
│   │   ├── ChatScreen.js
│   │   └── HomeScreen.js
│   ├── navigation/         # Configuração de navegação (React Navigation)
│   │   └── AppNavigator.js
│   ├── services/           # Lógica de negócio e comunicação com a rede MeshWave
│   │   ├── WifiDirectService.js  # Gerenciamento de Wi-Fi Direct
│   │   ├── P2PService.js         # Comunicação P2P (sockets)
│   │   └── MessageService.js     # Lógica de envio/recebimento de mensagens
│   ├── utils/              # Funções utilitárias
│   │   └── Permissions.js      # Tratamento de permissões
│   └── assets/             # Imagens, ícones, etc.
├── package.json            # Dependências e scripts do projeto
├── babel.config.js
├── metro.config.js
└── README.md               # Este arquivo
```

### Exemplo de Código (src/screens/ChatScreen.js)

Este é um exemplo simplificado de como a tela de chat pode ser estruturada, focando na interface e na integração com um serviço de mensagens.

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet, KeyboardAvoidingView, Platform } from 'react-native';
import MessageBubble from '../components/MessageBubble';
import MessageService from '../services/MessageService';

const ChatScreen = ({ route }) => {
  const { recipientId } = route.params; // ID do destinatário da conversa
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');

  useEffect(() => {
    // Simula o carregamento de mensagens históricas ou inicia a escuta
    // Em um app real, aqui seria a lógica para carregar mensagens do histórico
    // e configurar listeners para novas mensagens.
    MessageService.onReceiveMessage((msg) => {
      setMessages((prevMessages) => [...prevMessages, msg]);
    });

    return () => {
      // Limpeza de listeners ao desmontar o componente
      MessageService.offReceiveMessage();
    };
  }, []);

  const handleSendMessage = () => {
    if (inputText.trim()) {
      const newMessage = {
        id: messages.length.toString(), // ID temporário
        sender: 'Me', // Substituir pelo ID do usuário atual
        recipient: recipientId,
        text: inputText.trim(),
        timestamp: new Date().toISOString(),
        isMine: true,
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
      MessageService.sendMessage(recipientId, inputText.trim());
      setInputText('');
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      keyboardVerticalOffset={Platform.OS === 'ios' ? 60 : 0}
    >
      <FlatList
        data={messages}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <MessageBubble message={item.text} isMine={item.isMine} sender={item.sender} />
        )}
        contentContainerStyle={styles.messageList}
      />
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Digite sua mensagem..."
          value={inputText}
          onChangeText={setInputText}
          multiline
        />
        <Button title="Enviar" onPress={handleSendMessage} />
      </View>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f0',
  },
  messageList: {
    paddingVertical: 10,
    paddingHorizontal: 5,
  },
  inputContainer: {
    flexDirection: 'row',
    padding: 10,
    borderTopWidth: 1,
    borderTopColor: '#ccc',
    backgroundColor: '#fff',
    alignItems: 'center',
  },
  input: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 20,
    paddingHorizontal: 15,
    paddingVertical: 8,
    marginRight: 10,
    maxHeight: 100, // Limita a altura do input multiline
  },
});

export default ChatScreen;
```

### Exemplo de Código (src/services/MessageService.js)

Este serviço abstrato simula a lógica de envio e recebimento de mensagens, que seria integrada com os módulos de comunicação P2P e TCP/IP.

```javascript
// src/services/MessageService.js

const MessageService = {
  _onReceiveCallback: null,

  // Simula o envio de uma mensagem pela rede MeshWave
  sendMessage: (recipientId, messageText) => {
    console.log(`[MessageService] Enviando para ${recipientId}: ${messageText}`);
    // Aqui a lógica real de comunicação P2P/TCP seria implementada.
    // Por exemplo, chamar WifiDirectService para encontrar o peer
    // e P2PService para enviar os dados.

    // Simulação de recebimento para teste local
    setTimeout(() => {
      const receivedMsg = {
        id: Math.random().toString(),
        sender: recipientId,
        recipient: 'Me',
        text: `Echo: ${messageText}`,
        timestamp: new Date().toISOString(),
        isMine: false,
      };
      if (MessageService._onReceiveCallback) {
        MessageService._onReceiveCallback(receivedMsg);
      }
    }, 1000);
  },

  // Registra um callback para quando uma mensagem for recebida
  onReceiveMessage: (callback) => {
    MessageService._onReceiveCallback = callback;
  },

  // Remove o callback de recebimento
  offReceiveMessage: () => {
    MessageService._onReceiveCallback = null;
  },

  // Simula o recebimento de uma mensagem externa (chamado por módulos de rede)
  simulateExternalReceive: (messageData) => {
    if (MessageService._onReceiveCallback) {
      MessageService._onReceiveCallback(messageData);
    }
  },
};

export default MessageService;
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


