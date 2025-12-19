USE academia;

INSERT INTO departamento (nombre) VALUES
('Informática'),
('Contabilidad'),
('Administración'),
('Electrónica');

INSERT INTO profesor (nombre, apellido, id_departamento) VALUES
('Juan', 'López', 1),
('María', 'Pérez', 2),
('Carlos', 'Ramírez', 3);

INSERT INTO estudiante (nombre, apellido, fecha_nacimiento, id_departamento) VALUES
('Ana', 'García', '2005-01-12', 1),
('Luis', 'Martínez', '2004-04-20', 1),
('María', 'Torres', '2003-09-15', 3);

INSERT INTO curso (nombre, descripcion, id_profesor) VALUES
('Programación I', 'Curso base de programación', 1),
('Contabilidad I', 'Fundamentos de contabilidad', 2),
('Administración I', 'Introducción a la administración', 3);

INSERT INTO clase (id_curso, fecha, aula) VALUES
(1, '2025-01-10', 'A1'),
(1, '2025-01-17', 'A1'),
(2, '2025-01-11', 'B2');

INSERT INTO inscripcion (id_estudiante, id_curso, fecha) VALUES
(1, 1, '2025-01-05'),
(2, 1, '2025-01-05'),
(3, 3, '2025-01-06');

INSERT INTO calificacion (id_estudiante, id_curso, calificacion, fecha) VALUES
(1, 1, 95, '2025-02-01'),
(2, 1, 88, '2025-02-01'),
(3, 3, 92, '2025-02-01');
SELECT * FROM estudiante;
SELECT nombre, apellido FROM estudiante;
SELECT nombre, apellido 
FROM estudiante
WHERE id_departamento = 1;
SELECT * 
FROM estudiante
ORDER BY fecha_nacimiento ASC;
SELECT COUNT(*) AS total_estudiantes FROM estudiante;
SELECT * FROM estudiante WHERE apellido = 'García';
SELECT * FROM estudiante WHERE nombre LIKE 'A%';
SELECT e.nombre, e.apellido, d.nombre AS departamento
FROM estudiante e
INNER JOIN departamento d ON e.id_departamento = d.id_departamento;
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificacion c
INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante;
SELECT d.nombre, COUNT(e.id_estudiante) AS total
FROM departamento d
LEFT JOIN estudiante e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento;
SELECT p.nombre AS profesor, c.nombre AS curso
FROM curso c
INNER JOIN profesor p ON c.id_profesor = p.id_profesor;
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificacion c
INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante
HAVING promedio > 90;
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificacion c
INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante
ORDER BY promedio DESC
LIMIT 5;
SELECT d.nombre, COUNT(e.id_estudiante) AS total
FROM departamento d
LEFT JOIN estudiante e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento;
INSERT INTO departamento (nombre) VALUES
('Informática'),
('Contabilidad'),
('Administración'),
('Electrónica');
CREATE TABLE departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
DROP TABLE departamento;

CREATE TABLE departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
INSERT INTO departamento (nombre) VALUES
('Informática'),
('Contabilidad'),
('Administración'),
('Electrónica');
INSERT INTO departamento (nombre) VALUES
('Informática'),
('Contabilidad'),
('Administración'),
('Electrónica');
