**Diagrama1: Diagrama de Arquitetura da Aplicação** 

  

*Contextualização*: O diagrama de arquitetura apresentado foi desenvolvido para ilustrar a estrutura técnica da aplicação destinada à gestão de vendas e estoque para pequenos empreendedores. Este diagrama detalha os principais componentes do sistema, incluindo a camada de apresentação (*front-end*), construída com **React.js**; a camada de lógica de negócios (*back-end*), implementada em **Django** (Python); e a camada de persistência de dados, gerenciada pelo banco de dados **PostgreSQL**. 

  

Durante as fases de planejamento e design, o diagrama foi utilizado como uma ferramenta fundamental para orientar as decisões técnicas e garantir que a aplicação fosse desenvolvida com foco em escalabilidade, segurança e facilidade de manutenção. Por exemplo, o diagrama destaca a separação entre as camadas de apresentação e de lógica de negócios, assegurando que atualizações na interface do usuário possam ser realizadas independentemente da lógica subjacente do sistema. 

  

**Componentes Detalhados no Diagrama:** 

1. **Camada de Apresentação (Front-End):** 

   - **Framework:** React.js 

   - **Componentes:** Formulários de cadastro de produtos, interface para registro de vendas, painel de controle de estoque. 

   - **Integração:** Comunicação com a API RESTful para troca de dados com o back-end. 

  

2. **Camada de Lógica de Negócios (Back-End):** 

   - **Framework:** Django 

   - **Funções Principais:** Processamento de pedidos, cálculo de estoque em tempo real, geração automática de relatórios financeiros. 

   - **Autenticação:** Implementação de sistema de login baseado em tokens JWT. 

  

3. **Camada de Persistência de Dados (Banco de Dados):** 

   - **Sistema Gerenciador de Banco de Dados:** PostgreSQL 

   - **Entidades:** Tabelas de produtos, vendas, usuários e logs de atividades. 

   - **Relacionamentos:** Definição de chaves estrangeiras para assegurar a integridade referencial entre as tabelas de vendas e estoque. 
