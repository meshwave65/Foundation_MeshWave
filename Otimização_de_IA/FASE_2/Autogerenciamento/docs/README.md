# Documentação do Autogerenciamento

Este diretório contém a documentação detalhada sobre os mecanismos de autogerenciamento na rede MeshWave. O autogerenciamento permite que a rede se organize, configure e otimize de forma autônoma, sem intervenção manual.

## 1. Visão Geral do Autogerenciamento

O autogerenciamento é a capacidade da rede MeshWave de se adaptar dinamicamente a mudanças na topologia, carga de trabalho e disponibilidade de recursos. Isso é alcançado através da eleição de líderes de célula, atribuição de papéis e reconfiguração automática.

### 1.1. Importância na Rede Mesh

*   **Escalabilidade:** Facilita o crescimento da rede, pois novos nós podem se integrar e assumir papéis de forma autônoma.
*   **Resiliência:** Permite que a rede se recupere de falhas de nós, elegendo novos líderes e reconfigurando rotas.
*   **Eficiência:** Otimiza o uso de recursos, atribuindo papéis com base na capacidade de cada nó.

## 2. Células MeshWave

A rede MeshWave é organizada em células, que são grupos de dispositivos geograficamente próximos. Cada célula é gerenciada por um dispositivo líder, eleito com base em sua capacidade.

### 2.1. Formação de Células

*   **Mecanismo:** Dispositivos descobrem seus vizinhos e formam grupos com base na proximidade e na qualidade do link.
*   **Vantagens:** Reduz a complexidade do gerenciamento da rede, dividindo-a em unidades menores e mais gerenciáveis.

### 2.2. Eleição de Líder de Célula (Group Owner)

*   **Mecanismo:** Os dispositivos em uma célula elegem um líder (Group Owner) com base em critérios como capacidade de processamento (CPU), memória (RAM), armazenamento e conectividade.
*   **Vantagens:** Garante que o nó mais capaz gerencie a célula, otimizando o desempenho e a estabilidade.

## 3. Atribuição de Papéis

O líder da célula atribui papéis aos outros dispositivos na célula, com base em suas capacidades e na necessidade da rede.

*   **Gateway:** Dispositivo com acesso à internet, responsável por conectar a célula à rede externa.
*   **Repetidor:** Dispositivo que encaminha pacotes entre outros nós, estendendo o alcance da rede.
*   **Nó Final:** Dispositivo que apenas envia e recebe dados, sem participar ativamente do roteamento.

## 4. Relatórios de Testes e Análise

(Esta seção será preenchida com os resultados dos testes de desempenho do autogerenciamento, incluindo tempo de eleição de líder, estabilidade da célula e eficiência da atribuição de papéis.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


