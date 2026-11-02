# Checkpoint — Governança do mercado MWN e documentação preliminar para investidores

- **Data:** 2026-11-01
- **Repositório:** `meshwave65/Foundation_MeshWave`
- **Branch:** `main`
- **Natureza:** registro documental dos princípios informados pelo responsável; não é auditoria de implementação.

## Contexto

O responsável definiu como objetivo evoluir a plataforma MeshWave, carteira e blockchain MWN para um canal próprio de aquisição e, quando tecnicamente implementado, um mercado funcional de compra e venda que possa coexistir com exchanges externas. A intenção é preparar desde já documentação preliminar de governança e apresentação a investidores.

## Princípio estabelecido

Ordens de compra e venda dos usuários — Meshwalkers — terão prioridade sobre ordens próprias da MeshWave. A organização não deverá priorizar descarregar suas reservas nem priorizar compras institucionais quando houver ordens compatíveis e executáveis de usuários que devam ser atendidas primeiro.

O princípio abrange ordens associadas a Genesis, tesouraria, reservas e demais operações sob controle direto ou indireto da MeshWave. Sua aplicação deve ocorrer no matching engine, com origem das ordens identificável e registros auditáveis; não basta uma promessa na interface ou um procedimento manual.

## Documentos adicionados

1. `BCE/temas/governanca-mercado-mwn-prioridade-meshwalkers.md` — princípio de prioridade e requisitos preliminares para o regulamento operacional.
2. `BCE/temas/documento-base-investidores-mwn.md` — documento-base conceitual com estágio atual, plano por etapas, riscos e limites das afirmações.
3. Atualização de `BCE/temas/economia-ums-mwn-pouw-liquidez-distribuida.md` — referência à governança do mercado e separação entre aquisição primária e negociação secundária.
4. Atualização de `BCE/INDICE_CURATORIAL.md` — inclusão do novo documento temático e materiais de apresentação.
5. Atualização de `BCE/REGISTRO_DECISOES.md` — referência de rastreabilidade documental.
6. Atualização do `README.md` — índice inicial para os documentos fundamentais.

## Métricas iniciais mencionadas

O documento-base registra os números anteriormente fornecidos para o projeto principal — 13 aquisições, 12 compradores, R$ 55,97 e 2.590,60402683 MWN — explicitamente como valores informados e sujeitos a reconciliação com os registros de origem antes de publicação externa. Não são descritos como volume de exchange.

## Limites

- Não foi alterado código da blockchain, carteira, compra ou venda.
- Não se afirma que o mercado secundário já esteja operacional.
- Matching engine, tipos de ordem, preço/tempo, reserva de saldo, liquidação, execução parcial, API, controles de tesouraria e prevenção de conflito permanecem requisitos a especificar e testar.
- A documentação é preliminar; a operação deve passar por avaliação jurídica/regulatória aplicável.
- Nenhuma garantia de listagem, liquidez, valorização ou retorno foi afirmada.

## Próxima etapa documental/técnica

Elaborar o Regulamento Operacional da Exchange MWN e, em paralelo, verificar o código atual da plataforma para mapear o que já existe no ciclo de compra, carteira, transferência e eventual venda entre usuários. A implementação deve respeitar a regra de prioridade dos Meshwalkers desde o primeiro fluxo demonstrável.
