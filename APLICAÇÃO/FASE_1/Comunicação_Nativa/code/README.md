
# Código e Algoritmos da Comunicação Nativa

Este diretório é destinado a armazenar o código-fonte, diagramas e algoritmos relacionados à comunicação nativa do Projeto MeshWave.

## Conteúdo Esperado:

*   **Código-fonte:** Implementações de APIs de comunicação (Wi-Fi Direct, Bluetooth Low Energy).
*   **Diagramas:** Diagramas de sequência de comunicação, fluxos de dados.
*   **Algoritmos:** Algoritmos para descoberta de dispositivos, emparelhamento e troca de dados.




## Exemplos de Código para Comunicação Nativa

Este diretório contém exemplos de código para a implementação de funcionalidades de comunicação nativa em Android, utilizando Wi-Fi Direct e Bluetooth Low Energy (BLE).

### 1. Exemplo de Descoberta de Peers (Wi-Fi Direct - Java/Kotlin)

Este snippet demonstra como iniciar a descoberta de peers Wi-Fi Direct em um `Activity` ou `Fragment` Android.

```java
// Em sua Activity ou Fragment

import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pManager.Channel;
import android.net.wifi.p2p.WifiP2pManager.ActionListener;
import android.content.Context;
import android.widget.Toast;
import android.util.Log;

public class WifiDirectDiscovery {

    private WifiP2pManager manager;
    private Channel channel;
    private Context context;

    private static final String TAG = "WifiDirectDiscovery";

    public WifiDirectDiscovery(Context context) {
        this.context = context;
        manager = (WifiP2pManager) context.getSystemService(Context.WIFI_P2P_SERVICE);
        channel = manager.initialize(context, context.getMainLooper(), null);
    }

    public void discoverPeers() {
        if (manager == null || channel == null) {
            Log.e(TAG, "WifiP2pManager or Channel not initialized.");
            Toast.makeText(context, "Wi-Fi Direct não disponível.", Toast.LENGTH_SHORT).show();
            return;
        }

        manager.discoverPeers(channel, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Descoberta de peers iniciada com sucesso.");
                Toast.makeText(context, "Descoberta iniciada", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reasonCode) {
                String reason;
                switch (reasonCode) {
                    case WifiP2pManager.P2P_UNSUPPORTED:
                        reason = "P2P não suportado no dispositivo.";
                        break;
                    case WifiP2pManager.ERROR:
                        reason = "Erro interno do framework.";
                        break;
                    case WifiP2pManager.BUSY:
                        reason = "Framework ocupado, tente novamente.";
                        break;
                    default:
                        reason = "Erro desconhecido: " + reasonCode;
                        break;
                }
                Log.e(TAG, "Falha ao iniciar descoberta de peers: " + reason);
                Toast.makeText(context, "Falha na descoberta: " + reason, Toast.LENGTH_SHORT).show();
            }
        });
    }

    // Métodos para parar descoberta, conectar, etc., seriam adicionados aqui.
}
```

### 2. Exemplo de Conexão P2P (Wi-Fi Direct - Java/Kotlin)

Este snippet mostra como iniciar uma conexão com um dispositivo Wi-Fi Direct descoberto.

```java
// Em sua Activity ou Fragment, após descobrir um dispositivo (WifiP2pDevice device)

import android.net.wifi.p2p.WifiP2pConfig;
import android.net.wifi.p2p.WifiP2pDevice;
import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pManager.ActionListener;
import android.net.wifi.p2p.WifiP2pManager.Channel;
import android.content.Context;
import android.widget.Toast;
import android.util.Log;

public class WifiDirectConnection {

    private WifiP2pManager manager;
    private Channel channel;
    private Context context;

    private static final String TAG = "WifiDirectConnection";

    public WifiDirectConnection(Context context, WifiP2pManager manager, Channel channel) {
        this.context = context;
        this.manager = manager;
        this.channel = channel;
    }

    public void connectToPeer(WifiP2pDevice device) {
        if (manager == null || channel == null || device == null) {
            Log.e(TAG, "Manager, Channel ou Device não inicializados.");
            Toast.makeText(context, "Erro na conexão P2P.", Toast.LENGTH_SHORT).show();
            return;
        }

        WifiP2pConfig config = new WifiP2pConfig();
        config.deviceAddress = device.deviceAddress;

        manager.connect(channel, config, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Iniciação da conexão P2P bem-sucedida para: " + device.deviceName);
                Toast.makeText(context, "Conectando a " + device.deviceName, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reason) {
                String reasonStr;
                switch (reason) {
                    case WifiP2pManager.P2P_UNSUPPORTED:
                        reasonStr = "P2P não suportado.";
                        break;
                    case WifiP2pManager.ERROR:
                        reasonStr = "Erro interno.";
                        break;
                    case WifiP2pManager.BUSY:
                        reasonStr = "Ocupado.";
                        break;
                    default:
                        reasonStr = "Erro desconhecido: " + reason;
                        break;
                }
                Log.e(TAG, "Falha na iniciação da conexão P2P: " + reasonStr);
                Toast.makeText(context, "Falha na conexão: " + reasonStr, Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


