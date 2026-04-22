# Documentação da Energia Adaptativa

Este diretório contém a documentação detalhada sobre as estratégias e mecanismos de energia adaptativa no Projeto MeshWave. O objetivo é otimizar o consumo de energia dos dispositivos na rede mesh, prolongando a vida útil da bateria e garantindo a sustentabilidade da rede.

## 1. Visão Geral da Energia Adaptativa

A energia adaptativa refere-se à capacidade dos dispositivos MeshWave de ajustar dinamicamente seu consumo de energia com base em fatores como a carga de trabalho da rede, a disponibilidade de energia, o papel do dispositivo na rede e as condições ambientais. Isso é crucial para redes mesh que operam em ambientes com recursos limitados ou que dependem de baterias.

### 1.1. Importância na Rede Mesh

*   **Sustentabilidade:** Prolonga a vida útil da rede, reduzindo a necessidade de substituição ou recarga frequente de baterias.
*   **Eficiência:** Garante que os recursos de energia sejam utilizados de forma otimizada, evitando desperdício.
*   **Resiliência:** Permite que os nós permaneçam ativos por mais tempo, contribuindo para a estabilidade e conectividade da rede.

## 2. Estratégias de Otimização de Energia

O Projeto MeshWave emprega diversas estratégias para alcançar a energia adaptativa:

### 2.1. Modo Híbrido (BLE/Wi-Fi Direct)

*   **Mecanismo:** Utiliza BLE para descoberta de dispositivos e comunicação de baixo volume de dados quando o consumo de energia é crítico, e alterna para Wi-Fi Direct para transferência de dados de alta velocidade quando necessário. Isso permite que os dispositivos permaneçam em um estado de baixo consumo a maior parte do tempo.
*   **Vantagens:** Combina a eficiência energética do BLE com o alto throughput do Wi-Fi Direct.

### 2.2. Ciclos de Trabalho (Duty Cycling)

*   **Mecanismo:** Dispositivos alternam entre estados de atividade (ligado) e inatividade (dormindo) em intervalos programados. Durante o estado de inatividade, o consumo de energia é minimizado.
*   **Vantagens:** Redução significativa do consumo de energia para dispositivos que não precisam estar constantemente ativos.
*   **Desafios:** Necessidade de sincronização entre os nós para garantir que as mensagens não sejam perdidas durante os períodos de inatividade.

### 2.3. Gerenciamento de Potência de Transmissão

*   **Mecanismo:** Ajusta dinamicamente a potência de transmissão do rádio com base na distância e na qualidade do link com os vizinhos. Transmitir com potência excessiva consome energia desnecessariamente.
*   **Vantagens:** Otimiza o alcance e o consumo de energia, reduzindo interferências.

## 3. Monitoramento e Análise de Energia

(Esta seção será preenchida com detalhes sobre como o consumo de energia é monitorado nos dispositivos MeshWave e como os dados são analisados para refinar as estratégias de energia adaptativa.)

## 4. Relatórios de Testes e Validação

(Esta seção conterá os resultados dos testes de campo e simulações que validam a eficácia das estratégias de energia adaptativa na prolongação da vida útil da bateria e na manutenção do desempenho da rede.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


