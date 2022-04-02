CREATE DATABASE Sepomex

USE Sepomex

CREATE TABLE Estados (
	id_estado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	d_estado VARCHAR(50),
	c_estado VARCHAR(5)
)

CREATE TABLE Municipios (
	id_municipio INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	d_mnpio VARCHAR(50)
)

CREATE TABLE Colonias (
	id_colonia INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	id_estado INT NOT NULL,
	id_municipio INT NOT NULL,
	d_asenta VARCHAR(50) NOT NULL,
	d_codigo VARCHAR(5),
	FOREIGN KEY (id_estado) REFERENCES Estados(id_estado),
	FOREIGN KEY (id_municipio) REFERENCES Municipios(id_municipio)
)