# Biblioteca

📚 SGB - Sistema de Gerenciamento de Biblioteca O SGB é uma solução de software para terminal focada na automação dos processos fundamentais de uma biblioteca acadêmica. O projeto integra uma interface em camadas com um banco de dados relacional para gerenciar o ciclo de vida de empréstimos e a situação financeira dos usuários.

🎯 Objetivo do Projeto Desenvolver uma ferramenta robusta que simule o fluxo real de uma biblioteca, garantindo a integridade dos dados através de relacionamentos SQL e oferecendo uma experiência de uso fluida para o aluno.

🛠️ Pilares Técnicos

Gestão de Dados (SQL) O sistema utiliza um modelo relacional composto por três entidades principais que garantem a organização da informação:
Alunos: Controle de credenciais e integridade do saldo devedor.

Acervo: Catálogo dinâmico com atualização de status em tempo real.

Movimentações: Registro histórico de empréstimos com vínculos de Chave Estrangeira (Foreign Keys) e deleção em cascata.

Lógica de Negócio (Python) A inteligência do software foi construída utilizando conceitos avançados de programação:
Modularização: Divisão de responsabilidades em funções específicas para login, consultas e transações financeiras.

Segurança e Robustez: Implementação de tratamento de exceções (Try/Except) para prevenir interrupções por entradas de dados inválidas.

Processamento Financeiro: Aplicação da biblioteca math para cálculos precisos de multas e arredondamentos conforme regras de negócio.

Automação de Protocolos: Uso da biblioteca random para geração de comprovantes únicos de atendimento.

Interface Humanizada Apesar de ser uma aplicação baseada em console, o sistema prioriza a clareza na comunicação, utilizando uma linguagem natural nas interações e menus intuitivos para facilitar a navegação do usuário.
💻 Tecnologias Utilizadas Linguagem Principal: Python 3.10+

Banco de Dados: SQLite / MySQL

Bibliotecas Adicionais: math (Cálculos), random (Protocolos), sqlite3 (Conectividade)
