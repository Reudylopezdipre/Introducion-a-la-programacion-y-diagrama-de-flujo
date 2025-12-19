-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:43:42
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
-- Estructura de tabla para la tabla `clase`
--

CREATE TABLE `clase` (
  `id_clase` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `aula` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clase`
--

INSERT INTO `clase` (`id_clase`, `id_curso`, `fecha`, `aula`) VALUES
(1, 1, '2025-01-10', 'A1'),
(2, 1, '2025-01-17', 'A1'),
(3, 2, '2025-01-11', 'B2'),
(4, 1, '2025-01-10', 'A1'),
(5, 1, '2025-01-17', 'A1'),
(6, 2, '2025-01-11', 'B2'),
(7, 1, '2025-01-10', 'A1'),
(8, 1, '2025-01-17', 'A1'),
(9, 2, '2025-01-11', 'B2'),
(10, 1, '2025-01-10', 'A1'),
(11, 1, '2025-01-17', 'A1'),
(12, 2, '2025-01-11', 'B2'),
(13, 1, '2025-01-10', 'A1'),
(14, 1, '2025-01-17', 'A1'),
(15, 2, '2025-01-11', 'B2'),
(16, 1, '2025-01-10', 'A1'),
(17, 1, '2025-01-17', 'A1'),
(18, 2, '2025-01-11', 'B2'),
(19, 1, '2025-01-10', 'A1'),
(20, 1, '2025-01-17', 'A1'),
(21, 2, '2025-01-11', 'B2'),
(22, 1, '2025-01-10', 'A1'),
(23, 1, '2025-01-17', 'A1'),
(24, 2, '2025-01-11', 'B2'),
(25, 1, '2025-01-10', 'A1'),
(26, 1, '2025-01-17', 'A1'),
(27, 2, '2025-01-11', 'B2'),
(28, 1, '2025-01-10', 'A1'),
(29, 1, '2025-01-17', 'A1'),
(30, 2, '2025-01-11', 'B2'),
(31, 1, '2025-01-10', 'A1'),
(32, 1, '2025-01-17', 'A1'),
(33, 2, '2025-01-11', 'B2'),
(34, 1, '2025-01-10', 'A1'),
(35, 1, '2025-01-17', 'A1'),
(36, 2, '2025-01-11', 'B2'),
(37, 1, '2025-01-10', 'A1'),
(38, 1, '2025-01-17', 'A1'),
(39, 2, '2025-01-11', 'B2'),
(40, 1, '2025-01-10', 'A1'),
(41, 1, '2025-01-17', 'A1'),
(42, 2, '2025-01-11', 'B2'),
(43, 1, '2025-01-10', 'A1'),
(44, 1, '2025-01-17', 'A1'),
(45, 2, '2025-01-11', 'B2'),
(46, 1, '2025-01-10', 'A1'),
(47, 1, '2025-01-17', 'A1'),
(48, 2, '2025-01-11', 'B2'),
(49, 1, '2025-01-10', 'A1'),
(50, 1, '2025-01-17', 'A1'),
(51, 2, '2025-01-11', 'B2'),
(52, 1, '2025-01-10', 'A1'),
(53, 1, '2025-01-17', 'A1'),
(54, 2, '2025-01-11', 'B2');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clase`
--
ALTER TABLE `clase`
  ADD PRIMARY KEY (`id_clase`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clase`
--
ALTER TABLE `clase`
  MODIFY `id_clase` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
