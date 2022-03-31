CREATE DATABASE Sepomex

USE Sepomex

CREATE TABLE Estados (
	id_estado INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	d_estado NVARCHAR(50),
	c_estado NVARCHAR(5)
)

CREATE TABLE Municipios (
	id_municipio INT IDENTITY(1,1)NOT NULL PRIMARY KEY ,
	d_mnpio NVARCHAR(50)
)

CREATE TABLE Colonias (
	id_colonia INT IDENTITY(1,1) NOT NULL,
	id_estado INT NOT NULL,
	id_municipio INT NOT NULL,
	d_asenta NVARCHAR(50) NOT NULL,
	d_codigo NVARCHAR(5)
	FOREIGN KEY (id_estado) REFERENCES Estados(id_estado),
	FOREIGN KEY (id_municipio) REFERENCES Municipios(id_municipio)
)