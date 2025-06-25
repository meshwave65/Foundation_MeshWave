

## Exemplos de Código para Gerenciamento de Conexões

Este diretório contém exemplos de código para a implementação de mecanismos de gerenciamento de conexões no Projeto MeshWave, utilizando as APIs de Wi-Fi Direct do Android.

### 1. Exemplo de Conexão a um Peer Wi-Fi Direct (Java/Kotlin)

Este snippet demonstra como iniciar uma conexão com um dispositivo Wi-Fi Direct descoberto. Ele é uma continuação do exemplo de descoberta de peers.

```java
// Em sua Activity ou Serviço, após ter um WifiP2pDevice 'device' disponível

import android.net.wifi.p2p.WifiP2pConfig;
import android.net.wifi.p2p.WifiP2pDevice;
import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pManager.ActionListener;
import android.net.wifi.p2p.WifiP2pManager.Channel;
import android.content.Context;
import android.util.Log;
import android.widget.Toast;

public class WifiDirectConnectionManager {

    private WifiP2pManager manager;
    private Channel channel;
    private Context context;

    private static final String TAG = "WifiDirectConnMgr";

    public WifiDirectConnectionManager(Context context, WifiP2pManager manager, Channel channel) {
        this.context = context;
        this.manager = manager;
        this.channel = channel;
    }

    public void connectToDevice(WifiP2pDevice device) {
        if (manager == null || channel == null || device == null) {
            Log.e(TAG, "Manager, Channel ou Device não inicializados para conexão.");
            Toast.makeText(context, "Erro: Não foi possível iniciar conexão.", Toast.LENGTH_SHORT).show();
            return;
        }

        WifiP2pConfig config = new WifiP2pConfig();
        config.deviceAddress = device.deviceAddress;
        // config.groupOwnerIntent = 0; // Para fazer este dispositivo menos propenso a ser GO

        manager.connect(channel, config, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Iniciação da conexão P2P bem-sucedida para: " + device.deviceName);
                Toast.makeText(context, "Conectando a " + device.deviceName, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reason) {
                String reasonStr = getFailureReason(reason);
                Log.e(TAG, "Falha na iniciação da conexão P2P: " + reasonStr);
                Toast.makeText(context, "Falha na conexão: " + reasonStr, Toast.LENGTH_SHORT).show();
            }
        });
    }

    public void disconnect() {
        if (manager == null || channel == null) return;

        manager.removeGroup(channel, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Grupo P2P removido com sucesso.");
                Toast.makeText(context, "Desconectado do grupo P2P.", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reason) {
                String reasonStr = getFailureReason(reason);
                Log.e(TAG, "Falha ao remover grupo P2P: " + reasonStr);
                Toast.makeText(context, "Falha ao desconectar: " + reasonStr, Toast.LENGTH_SHORT).show();
            }
        });
    }

    private String getFailureReason(int reasonCode) {
        switch (reasonCode) {
            case WifiP2pManager.P2P_UNSUPPORTED: return "P2P não suportado";
            case WifiP2pManager.ERROR: return "Erro geral";
            case WifiP2pManager.BUSY: return "Framework ocupado";
            default: return "Erro desconhecido (" + reasonCode + ")";
        }
    }
}
```

### 2. Tratamento de Eventos de Conexão (BroadcastReceiver - Java/Kotlin)

Para monitorar o status da conexão Wi-Fi Direct, é necessário registrar um `BroadcastReceiver` que escute as ações de mudança de estado da conexão (`WIFI_P2P_CONNECTION_CHANGED_ACTION`).

```java
// Em seu BroadcastReceiver (ex: WiFiDirectBroadcastReceiver.java)

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.NetworkInfo;
import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pInfo;
import android.util.Log;

public class WiFiDirectConnectionReceiver extends BroadcastReceiver {

    private WifiP2pManager manager;
    private WifiP2pManager.Channel channel;
    private MainActivity activity; // Referência à sua Activity principal

    private static final String TAG = "WiFiDirectConnReceiver";

    public WiFiDirectConnectionReceiver(WifiP2pManager manager, WifiP2pManager.Channel channel, MainActivity activity) {
        this.manager = manager;
        this.channel = channel;
        this.activity = activity;
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();

        if (WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION.equals(action)) {
            if (manager == null) {
                return;
            }

            NetworkInfo networkInfo = intent.getParcelableExtra(WifiP2pManager.EXTRA_NETWORK_INFO);

            if (networkInfo.isConnected()) {
                // Estamos conectados a um peer. Solicitar informações de conexão.
                manager.requestConnectionInfo(channel, new WifiP2pManager.ConnectionInfoListener() {
                    @Override
                    public void onConnectionInfoAvailable(WifiP2pInfo info) {
                        // info.groupFormed indica se um grupo P2P foi formado
                        // info.isGroupOwner indica se este dispositivo é o Group Owner
                        // info.groupOwnerAddress é o endereço IP do Group Owner
                        activity.log("Conexão P2P estabelecida. Group formed: " + info.groupFormed + ", Is GO: " + info.isGroupOwner);
                        // Aqui você pode iniciar threads de comunicação (servidor/cliente)
                    }
                });
            } else {
                // Desconectado
                activity.log("Conexão P2P perdida.");
            }
        }
    }
}
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


