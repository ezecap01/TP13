CREATE DATABASE biblioteca;
USE biblioteca;


CREATE TABLE autores 
(id INT IDENTITY(1,1) PRIMARY KEY,
nombre VARCHAR(100),
nacionalidad VARCHAR(100),
)

CREATE TABLE libros 
(id INT IDENTITY(1,1) PRIMARY KEY,
titulo VARCHAR(100),
genero VARCHAR(50),
año INT,
id_autor INT,
FOREIGN KEY (id_autor) REFERENCES autores(id)
)

INSERT INTO autores (nombre, nacionalidad) VALUES ('Gabriel García Márquez', 'Colombiano');
INSERT INTO libros (titulo, genero, año, id_autor) VALUES ('Cien años de soledad', 'Novela', 1967, 1);

