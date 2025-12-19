-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:43:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `academia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `id_curso` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `curso`
--

INSERT INTO `curso` (`id_curso`, `nombre`, `descripcion`, `id_profesor`) VALUES
(1, 'Programación I', 'Curso base de programación', 1),
(2, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(3, 'Administración I', 'Introducción a la administración', 3),
(4, 'Programación I', 'Curso base de programación', 1),
(5, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(6, 'Administración I', 'Introducción a la administración', 3),
(7, 'Programación I', 'Curso base de programación', 1),
(8, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(9, 'Administración I', 'Introducción a la administración', 3),
(10, 'Programación I', 'Curso base de programación', 1),
(11, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(12, 'Administración I', 'Introducción a la administración', 3),
(13, 'Programación I', 'Curso base de programación', 1),
(14, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(15, 'Administración I', 'Introducción a la administración', 3),
(16, 'Programación I', 'Curso base de programación', 1),
(17, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(18, 'Administración I', 'Introducción a la administración', 3),
(19, 'Programación I', 'Curso base de programación', 1),
(20, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(21, 'Administración I', 'Introducción a la administración', 3),
(22, 'Programación I', 'Curso base de programación', 1),
(23, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(24, 'Administración I', 'Introducción a la administración', 3),
(25, 'Programación I', 'Curso base de programación', 1),
(26, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(27, 'Administración I', 'Introducción a la administración', 3),
(28, 'Programación I', 'Curso base de programación', 1),
(29, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(30, 'Administración I', 'Introducción a la administración', 3),
(31, 'Programación I', 'Curso base de programación', 1),
(32, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(33, 'Administración I', 'Introducción a la administración', 3),
(34, 'Programación I', 'Curso base de programación', 1),
(35, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(36, 'Administración I', 'Introducción a la administración', 3),
(37, 'Programación I', 'Curso base de programación', 1),
(38, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(39, 'Administración I', 'Introducción a la administración', 3),
(40, 'Programación I', 'Curso base de programación', 1),
(41, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(42, 'Administración I', 'Introducción a la administración', 3),
(43, 'Programación I', 'Curso base de programación', 1),
(44, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(45, 'Administración I', 'Introducción a la administración', 3),
(46, 'Programación I', 'Curso base de programación', 1),
(47, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(48, 'Administración I', 'Introducción a la administración', 3),
(49, 'Programación I', 'Curso base de programación', 1),
(50, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(51, 'Administración I', 'Introducción a la administración', 3),
(52, 'Programación I', 'Curso base de programación', 1),
(53, 'Contabilidad I', 'Fundamentos de contabilidad', 2),
(54, 'Administración I', 'Introducción a la administración', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`id_curso`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `curso`
--
ALTER TABLE `curso`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
