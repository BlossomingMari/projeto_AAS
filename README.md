# Enunciado do Projeto - 2026/2027

## Sistema de Gestão de uma Loja de Sapatilhas

## 1. Objetivos

Este projeto tem como objetivo desenvolver um sistema distribuído baseado em microserviços para a gestão de uma loja online fictícia de sapatilhas, permitindo gerir um catálogo de modelos, tamanhos e stock, utilizadores, encomendas e pagamentos.

## 2. Descrição

Neste projeto pretende-se o desenvolvimento de um sistema baseado em microserviços para uma loja fictícia especializada na venda de sapatilhas.

O sistema deverá permitir aos clientes consultar o catálogo de sapatilhas, pesquisar modelos, verificar tamanhos e disponibilidade, criar encomendas e acompanhar o estado das suas compras.

Cada modelo poderá estar disponível em vários tamanhos, com quantidades de stock distintas. Por exemplo, um cliente pretende comprar um par de sapatilhas, tamanho 42.

O sistema deve verificar se esse tamanho está disponível, registar a encomenda, processar um pagamento simulado e atualizar o stock após a confirmação do pagamento.

O sistema será dividido em vários microserviços independentes, responsáveis pela gestão do catálogo e stock, utilizadores, encomendas e pagamentos.

Os microserviços deverão comunicar entre si para concluir as operações que dependem de mais de um serviço.

## 3. Componentes mínimos do Projeto

O projeto deve ter pelo menos os seguintes microserviços:

1. **Microserviço de catálogo e stock:** gestão de sapatilhas, marcas, modelos, tamanhos, preços e quantidades disponíveis. Deve permitir consultar os produtos e verificar a disponibilidade por tamanho.
2. **Microserviço de utilizadores:** responsável pelo registo, autenticação e manutenção de contas de clientes.
3. **Microserviço de encomendas:** responsável pela criação e consulta de encomendas, pela identificação dos produtos e tamanhos escolhidos, pela verificação de stock e pela atualização do estado das encomendas.
4. **Microserviço de pagamentos:** responsável pelo processamento simulado de pagamentos e pela comunicação da confirmação do pagamento ao microserviço de encomendas. Não é necessária ligação a serviços bancários reais.

## 4. Tecnologias mínimas

- **Python:** para o desenvolvimento dos microserviços.
- **Docker:** para a containerização dos microserviços.

As ferramentas adicionais necessárias ficam ao critério de cada grupo.

É importante salientar que o foco deste projeto é o desenvolvimento back-end, especificamente a arquitetura distribuída baseada em microserviços. O projeto deve ter interface web, no entanto esta deve ser simples e não deve ser o foco principal do projeto.

## 5. Segurança

Em termos de segurança é necessário implementar autenticação do utilizador.

## 6. Avaliação

Os alunos serão avaliados com base na funcionalidade do sistema e na integração efetiva dos microserviços.

## 7. Entrega do Projeto

O projeto deve ser entregue via e-learning até **10 de janeiro de 2027 às 23h59**.

## 8. Apresentação

Todos os projetos entregues serão sujeitos a uma apresentação. Para esse efeito, cada grupo terá que efetuar uma apresentação do projeto desenvolvido para a turma, de forma a demonstrar que o código entregue foi de facto feito pelo grupo e que a distribuição de trabalho foi equilibrada.

O calendário das apresentações será disponibilizado no e-learning, após o prazo de entrega da implementação do projeto. Cada apresentação tem a duração máxima de 15 minutos e deve, pelo menos, focar os seguintes pontos:

- **Introdução:** apresentação breve do projeto e respetivo objetivo.
- **Estrutura do projeto:** apresentação da arquitetura do sistema.
- **Simulação do sistema:** apresentação de um exemplo do sistema em funcionamento, incluindo todas as funcionalidades implementadas.
- **Conclusões.**

Como auxílio pode desenvolver um PPT (não é obrigatório).
