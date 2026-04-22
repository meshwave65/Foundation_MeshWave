

## Exemplos de Código para Descoberta de Vizinhos

Este diretório contém exemplos de código para a implementação de mecanismos de descoberta de vizinhos no Projeto MeshWave, utilizando as APIs de Wi-Fi Direct e Bluetooth Low Energy (BLE) do Android.

### 1. Exemplo de Iniciação de Descoberta Wi-Fi Direct (Java/Kotlin)

Este snippet demonstra como iniciar a descoberta de peers Wi-Fi Direct. É crucial ter as permissões de localização (`ACCESS_FINE_LOCATION`) concedidas para que a descoberta funcione corretamente no Android 10+.

```java
// Em sua Activity ou Serviço

import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pManager.Channel;
import android.net.wifi.p2p.WifiP2pManager.ActionListener;
import android.content.Context;
import android.util.Log;
import android.widget.Toast;

public class WifiDirectPeerDiscovery {

    private WifiP2pManager manager;
    private Channel channel;
    private Context context;

    private static final String TAG = "WifiDirectPeerDiscovery";

    public WifiDirectPeerDiscovery(Context context, WifiP2pManager manager, Channel channel) {
        this.context = context;
        this.manager = manager;
        this.channel = channel;
    }

    public void startDiscovery() {
        if (manager == null || channel == null) {
            Log.e(TAG, "WifiP2pManager ou Channel não inicializados.");
            Toast.makeText(context, "Erro: Wi-Fi Direct não disponível.", Toast.LENGTH_SHORT).show();
            return;
        }

        manager.discoverPeers(channel, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Descoberta de peers Wi-Fi Direct iniciada com sucesso.");
                Toast.makeText(context, "Descoberta Wi-Fi Direct iniciada", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reasonCode) {
                String reason;
                switch (reasonCode) {
                    case WifiP2pManager.P2P_UNSUPPORTED:
                        reason = "P2P não suportado neste dispositivo.";
                        break;
                    case WifiP2pManager.ERROR:
                        reason = "Erro interno do framework Wi-Fi Direct.";
                        break;
                    case WifiP2pManager.BUSY:
                        reason = "Framework Wi-Fi Direct ocupado, tente novamente.";
                        break;
                    default:
                        reason = "Erro desconhecido: " + reasonCode;
                        break;
                }
                Log.e(TAG, "Falha ao iniciar descoberta de peers Wi-Fi Direct: " + reason);
                Toast.makeText(context, "Falha na descoberta Wi-Fi Direct: " + reason, Toast.LENGTH_SHORT).show();
            }
        });
    }

    public void stopDiscovery() {
        if (manager == null || channel == null) return;
        manager.stopPeerDiscovery(channel, new ActionListener() {
            @Override
            public void onSuccess() {
                Log.d(TAG, "Descoberta de peers Wi-Fi Direct parada com sucesso.");
                Toast.makeText(context, "Descoberta Wi-Fi Direct parada", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(int reasonCode) {
                Log.e(TAG, "Falha ao parar descoberta de peers Wi-Fi Direct: " + reasonCode);
            }
        });
    }
}
```

### 2. Exemplo de Escaneamento BLE para Descoberta (Java/Kotlin)

Este snippet demonstra como iniciar um escaneamento BLE para descobrir dispositivos próximos. Requer permissões de localização e Bluetooth.

```java
// Em sua Activity ou Serviço

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothManager;
import android.bluetooth.le.BluetoothLeScanner;
import android.bluetooth.le.ScanCallback;
import android.bluetooth.le.ScanResult;
import android.bluetooth.le.ScanSettings;
import android.content.Context;
import android.content.pm.PackageManager;
import android.os.Handler;
import android.util.Log;
import android.widget.Toast;

import java.util.List;

public class BlePeerDiscovery {

    private BluetoothLeScanner bluetoothLeScanner;
    private BluetoothAdapter bluetoothAdapter;
    private Handler handler = new Handler();
    private boolean scanning;
    private static final long SCAN_PERIOD = 10000; // Scaneia por 10 segundos

    private static final String TAG = "BlePeerDiscovery";

    public BlePeerDiscovery(Context context) {
        if (!context.getPackageManager().hasSystemFeature(PackageManager.FEATURE_BLUETOOTH_LE)) {
            Toast.makeText(context, "BLE não suportado neste dispositivo.", Toast.LENGTH_SHORT).show();
            return;
        }

        final BluetoothManager bluetoothManager = (BluetoothManager) context.getSystemService(Context.BLUETOOTH_SERVICE);
        bluetoothAdapter = bluetoothManager.getAdapter();

        if (bluetoothAdapter == null || !bluetoothAdapter.isEnabled()) {
            Toast.makeText(context, "Bluetooth desativado ou não disponível.", Toast.LENGTH_SHORT).show();
            // Aqui você pode solicitar ao usuário para ativar o Bluetooth
            return;
        }
        bluetoothLeScanner = bluetoothAdapter.getBluetoothLeScanner();
    }

    public void startScan() {
        if (bluetoothLeScanner == null) return;
        if (!scanning) {
            // Para o escaneamento após um período definido
            handler.postDelayed(() -> {
                scanning = false;
                bluetoothLeScanner.stopScan(leScanCallback);
                Log.d(TAG, "Escaneamento BLE parado.");
                Toast.makeText(context, "Escaneamento BLE parado.", Toast.LENGTH_SHORT).show();
            }, SCAN_PERIOD);

            scanning = true;
            ScanSettings settings = new ScanSettings.Builder()
                    .setScanMode(ScanSettings.SCAN_MODE_LOW_LATENCY)
                    .build();
            bluetoothLeScanner.startScan(null, settings, leScanCallback);
            Log.d(TAG, "Escaneamento BLE iniciado.");
            Toast.makeText(context, "Escaneamento BLE iniciado.", Toast.LENGTH_SHORT).show();
        } else {
            Log.d(TAG, "Escaneamento BLE já em andamento.");
        }
    }

    public void stopScan() {
        if (bluetoothLeScanner == null) return;
        if (scanning) {
            scanning = false;
            bluetoothLeScanner.stopScan(leScanCallback);
            handler.removeCallbacksAndMessages(null); // Remove callbacks
            Log.d(TAG, "Escaneamento BLE parado manualmente.");
            Toast.makeText(context, "Escaneamento BLE parado manualmente.", Toast.LENGTH_SHORT).show();
        }
    }

    private ScanCallback leScanCallback = new ScanCallback() {
        @Override
        public void onScanResult(int callbackType, ScanResult result) {
            super.onScanResult(callbackType, result);
            // Processa o resultado do escaneamento
            Log.d(TAG, "Dispositivo BLE encontrado: " + result.getDevice().getName() + " (" + result.getDevice().getAddress() + ")");
            // Aqui você pode filtrar por dispositivos MeshWave específicos
        }

        @Override
        public void onBatchScanResults(List<ScanResult> results) {
            super.onBatchScanResults(results);
            for (ScanResult result : results) {
                Log.d(TAG, "Batch Scan Result: " + result.getDevice().getName());
            }
        }

        @Override
        public void onScanFailed(int errorCode) {
            super.onScanFailed(errorCode);
            Log.e(TAG, "Escaneamento BLE falhou com erro: " + errorCode);
            Toast.makeText(context, "Escaneamento BLE falhou: " + errorCode, Toast.LENGTH_SHORT).show();
        }
    };
}
```

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


