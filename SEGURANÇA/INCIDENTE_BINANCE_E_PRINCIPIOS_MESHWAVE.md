# Segurança MeshWave — lições do incidente Binance e princípios de arquitetura

**Registro:** 2026-11-03 | **Status:** documento de referência arquitetural

## Objetivo

Consolidar o aprendizado do incidente reportado envolvendo falsa entrevista, malware, comprometimento de endpoint e abuso de ferramentas internas, relacionando-o à arquitetura MeshWave. Este documento complementa os blueprints dos componentes; não substitui suas especificações nem atesta implementação.

## Princípios arquiteturais registrados

1. **Segregação de ativos:** UMS mantidas em carteiras individuais; não há transferência direta de UMS entre usuários do ecossistema. UMS só são expostas ao mercado após conversão para MWN.
2. **Cadeia de saída:** carteira individual → conversão UMS/MWN → MW-Ex → carteira externa. Cada etapa deve manter sua própria fronteira de autorização; autorizar uma etapa não significa autorizar automaticamente a seguinte.
3. **Autenticação contextual:** segundo fator associado ao dispositivo móvel MeshWalker como parte da autorização de operações sensíveis.
4. **PGC:** camada concebida para autenticidade física/contextual do usuário e de seus equipamentos de acesso. A prova contextual não deve ser descrita como simples fingerprint convencional.
5. **ARC:** vigilância e correlação de eventos e etapas da operação, com decisões explicáveis e rastreáveis.
6. **Isolamento de infraestrutura crítica:** servidores críticos sem acesso à Internet; administração por conexão física autorizada, sem Wi-Fi e por estação que não esteja conectada à Internet.
7. **Limitação de autoridade:** serviços públicos, agentes, interfaces e ferramentas não devem adquirir acesso irrestrito ao plano crítico ou à custódia.
8. **Proporcionalidade:** avaliar ataques pelo caminho completo, barreiras existentes e custo/retorno plausível; não extrapolar de uma hipótese isolada para afirmar comprometimento sistêmico.

## Aplicação ao incidente de referência

A lição relevante é impedir que comprometimento de endpoint ou credencial seja convertido em autoridade sobre ferramentas internas e ativos. Na MeshWave, a defesa conceitual combina compartimentalização de carteiras, conversão obrigatória, MW-Ex, segundo fator, PGC, ARC e isolamento físico. A eficácia depende de preservar essas fronteiras no código, configuração e operação.

## Estado e validação

Os princípios acima refletem as definições arquiteturais fornecidas pelo responsável do projeto. Devem ser validados por inspeção de código, configuração e procedimento operacional antes de serem apresentados como controles efetivamente implementados. Requisitos de validação devem ser mantidos nos blueprints específicos, não presumidos como concluídos.

## Referência de evento

Exame: https://exame.com/future-of-money/binance-diz-que-hackers-usaram-entrevista-de-emprego-falsa-e-ia-em-ataque/  
Complementar com fontes primárias e cobertura independente (Reuters/AP/Chainalysis) antes de publicação externa.
