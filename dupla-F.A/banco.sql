CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- Tabela Aluno
CREATE TABLE IF NOT EXISTS aluno (
    ra INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    saldo_devedor DECIMAL(10,2) NOT NULL DEFAULT 0.00
); 

-- Tabela Livros
CREATE TABLE IF NOT EXISTS livros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    area VARCHAR(50) NOT NULL,
    situacao ENUM('Disponivel', 'Emprestado') NOT NULL DEFAULT 'Disponivel'
);

-- Tabela Emprestimo
CREATE TABLE IF NOT EXISTS emprestimo (
    id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    ra_aluno INT NOT NULL,
    id_livro INT NOT NULL,
    FOREIGN KEY (ra_aluno) REFERENCES aluno (ra) ON DELETE CASCADE,
    FOREIGN KEY (id_livro) REFERENCES livros (id) ON DELETE CASCADE
);

-- Inserindo dados de exemplo corretamente (Omitindo o RA/ID para o AUTO_INCREMENT agir)
INSERT INTO aluno (nome, senha, saldo_devedor) VALUES 
('Ana Silva', 'senha123', 0.00),
('Carlos Souza', 'python20', 15.50),
('Beatriz Costa', 'livrosbr', 0.00),
('Daniel Oliveira', '123456', 4.00),
('Elena Martins', 'elena_m', 0.00);

INSERT INTO livros (titulo, autor, area, situacao) VALUES 
('Python Fluente', 'Luciano Ramalho', 'Tecnologia', 'Disponivel'),
('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 'Emprestado'),
('Código Limpo', 'Robert C. Martin', 'Tecnologia', 'Disponivel'),
('Dom Casmurro', 'Machado de Assis', 'Literatura', 'Disponivel'),
('Entendendo Algoritmos', 'Aditya Bhargava', 'Tecnologia', 'Emprestado');

-- Inserindo empréstimos baseados nos IDs gerados acima
INSERT INTO emprestimo (ra_aluno, id_livro) VALUES (1, 2), (3, 5);

-- Verificando os dados
SELECT * FROM aluno;
SELECT * FROM livros;
SELECT * FROM emprestimo;