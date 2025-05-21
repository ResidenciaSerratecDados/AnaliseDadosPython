-- TABLE
CREATE TABLE aluno(
  matricula VARCHAR(10) PRIMARY KEY,
  nome VARCHAR(50),
  idade INT,
  rua VARCHAR(10),
  CEP VARCHAR(9)
);
CREATE TABLE demo (ID integer primary key, Name varchar(20), Hint text );
CREATE TABLE professor(
  CPF VARCHAR(14) PRIMARY KEY,
  nome VARCHAR(60),
  disciplina VARCHAR(20),
  email VARCHAR(60),
  telefone VARCHAR(15),
  salario INT,
  idade INT
);
CREATE TABLE venda (
  id INT PRIMARY KEY,
  produto VARCHAR(50),
  quantidade INT,
  preco DECIMAL(10,2),
  total DECIMAL(10,2) GENERATED ALWAYS AS (quantidade * preco) STORED
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
