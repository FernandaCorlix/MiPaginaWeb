-- Create the volleyball database
CREATE DATABASE volleyball;

-- Switch to the volleyball database
USE volleyball;

-- Create the Equipo table
CREATE TABLE Equipo (
  EquipoID INT PRIMARY KEY,
  nombreEquipo VARCHAR(100)
);

-- Create the jugadores table
CREATE TABLE jugadores (
  id INT PRIMARY KEY,
  NombreUsuario VARCHAR(100),
  contrasenia VARCHAR(50),
  sexo BOOLEAN,
  esAdmin BOOLEAN,
  EquipoID INT,
  FOREIGN KEY (EquipoID) REFERENCES Equipo(EquipoID)
);

