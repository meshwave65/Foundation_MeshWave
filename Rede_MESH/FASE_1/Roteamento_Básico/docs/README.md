# Documentação do Roteamento Básico

Este diretório contém a documentação detalhada sobre os princípios e a implementação do roteamento básico na rede MeshWave. O roteamento é essencial para garantir que as mensagens alcancem seus destinos, mesmo que não haja uma conexão direta entre a origem e o destino.

## 1. Visão Geral do Roteamento Básico

No contexto de uma rede mesh descentralizada, o roteamento básico refere-se à capacidade de um nó encaminhar pacotes de dados para outros nós na rede, passo a passo, até que o pacote chegue ao seu destino final. Diferente das redes tradicionais, onde roteadores centrais decidem os caminhos, em uma rede mesh, cada nó pode atuar como um roteador.

### 1.1. Importância na Rede Mesh

*   **Conectividade End-to-End:** Permite a comunicação entre dispositivos que não estão em alcance direto.
*   **Resiliência:** Oferece múltiplos caminhos para a entrega de dados, aumentando a tolerância a falhas.
*   **Escalabilidade:** Permite que a rede cresça adicionando mais nós, que também atuam como roteadores.

## 2. Princípios de Roteamento

O roteamento básico na MeshWave foca em algoritmos simples e eficientes para encaminhamento de pacotes.

### 2.1. Roteamento por Inundação (Flooding)

*   **Mecanismo:** Cada nó que recebe um pacote o retransmite para todos os seus vizinhos, exceto para o nó de onde o pacote foi recebido. Isso garante que o pacote eventualmente alcance o destino, mas pode gerar tráfego excessivo.
*   **Uso:** Ideal para redes pequenas ou para descoberta inicial de rotas, onde a simplicidade e a garantia de entrega são mais importantes que a eficiência de banda.

### 2.2. Roteamento Baseado em Tabela (Table-Driven Routing)

*   **Mecanismo:** Cada nó mantém uma tabela de roteamento que mapeia destinos para o próximo salto. As tabelas são atualizadas periodicamente ou quando há mudanças na topologia.
*   **Uso:** Mais eficiente em termos de banda que o flooding, mas requer mecanismos para manter as tabelas atualizadas.

## 3. Estratégias de Roteamento Básico

*   **Roteamento Hop-by-Hop:** Cada nó decide o próximo salto com base em sua tabela de roteamento local, sem ter conhecimento completo do caminho.
*   **Encaminhamento Simples:** No protótipo inicial, o encaminhamento pode ser baseado em regras pré-definidas ou na identificação do destinatário.

## 4. Relatórios de Testes e Análise

(Esta seção será preenchida com os resultados dos testes de desempenho do roteamento básico, incluindo latência, taxa de entrega de pacotes e consumo de recursos.)

---

**Autor:** Diogenes Duarte Sobral
**Contato:** celular +55 21 972341965, omaci2008@gmail.com


