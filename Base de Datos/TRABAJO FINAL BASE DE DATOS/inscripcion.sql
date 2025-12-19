-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:44:28
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
-- Estructura de tabla para la tabla `inscripcion`
--

CREATE TABLE `inscripcion` (
  `id_inscripcion` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inscripcion`
--

INSERT INTO `inscripcion` (`id_inscripcion`, `id_estudiante`, `id_curso`, `fecha`) VALUES
(1, 1, 1, '2025-01-05'),
(2, 2, 1, '2025-01-05'),
(3, 3, 3, '2025-01-06'),
(4, 1, 1, '2025-01-05'),
(5, 2, 1, '2025-01-05'),
(6, 3, 3, '2025-01-06'),
(7, 1, 1, '2025-01-05'),
(8, 2, 1, '2025-01-05'),
(9, 3, 3, '2025-01-06'),
(10, 1, 1, '2025-01-05'),
(11, 2, 1, '2025-01-05'),
(12, 3, 3, '2025-01-06'),
(13, 1, 1, '2025-01-05'),
(14, 2, 1, '2025-01-05'),
(15, 3, 3, '2025-01-06'),
(16, 1, 1, '2025-01-05'),
(17, 2, 1, '2025-01-05'),
(18, 3, 3, '2025-01-06'),
(19, 1, 1, '2025-01-05'),
(20, 2, 1, '2025-01-05'),
(21, 3, 3, '2025-01-06'),
(22, 1, 1, '2025-01-05'),
(23, 2, 1, '2025-01-05'),
(24, 3, 3, '2025-01-06'),
(25, 1, 1, '2025-01-05'),
(26, 2, 1, '2025-01-05'),
(27, 3, 3, '2025-01-06'),
(28, 1, 1, '2025-01-05'),
(29, 2, 1, '2025-01-05'),
(30, 3, 3, '2025-01-06'),
(31, 1, 1, '2025-01-05'),
(32, 2, 1, '2025-01-05'),
(33, 3, 3, '2025-01-06'),
(34, 1, 1, '2025-01-05'),
(35, 2, 1, '2025-01-05'),
(36, 3, 3, '2025-01-06'),
(37, 1, 1, '2025-01-05'),
(38, 2, 1, '2025-01-05'),
(39, 3, 3, '2025-01-06'),
(40, 1, 1, '2025-01-05'),
(41, 2, 1, '2025-01-05'),
(42, 3, 3, '2025-01-06'),
(43, 1, 1, '2025-01-05'),
(44, 2, 1, '2025-01-05'),
(45, 3, 3, '2025-01-06'),
(46, 1, 1, '2025-01-05'),
(47, 2, 1, '2025-01-05'),
(48, 3, 3, '2025-01-06'),
(49, 1, 1, '2025-01-05'),
(50, 2, 1, '2025-01-05'),
(51, 3, 3, '2025-01-06'),
(52, 1, 1, '2025-01-05'),
(53, 2, 1, '2025-01-05'),
(54, 3, 3, '2025-01-06');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD PRIMARY KEY (`id_inscripcion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  MODIFY `id_inscripcion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
