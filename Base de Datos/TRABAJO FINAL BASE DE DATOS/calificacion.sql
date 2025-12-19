-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:43:30
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
-- Estructura de tabla para la tabla `calificacion`
--

CREATE TABLE `calificacion` (
  `id_calificacion` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `calificacion` decimal(5,2) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificacion`
--

INSERT INTO `calificacion` (`id_calificacion`, `id_estudiante`, `id_curso`, `calificacion`, `fecha`) VALUES
(1, 1, 1, 95.00, '2025-02-01'),
(2, 2, 1, 88.00, '2025-02-01'),
(3, 3, 3, 92.00, '2025-02-01'),
(4, 1, 1, 95.00, '2025-02-01'),
(5, 2, 1, 88.00, '2025-02-01'),
(6, 3, 3, 92.00, '2025-02-01'),
(7, 1, 1, 95.00, '2025-02-01'),
(8, 2, 1, 88.00, '2025-02-01'),
(9, 3, 3, 92.00, '2025-02-01'),
(10, 1, 1, 95.00, '2025-02-01'),
(11, 2, 1, 88.00, '2025-02-01'),
(12, 3, 3, 92.00, '2025-02-01'),
(13, 1, 1, 95.00, '2025-02-01'),
(14, 2, 1, 88.00, '2025-02-01'),
(15, 3, 3, 92.00, '2025-02-01'),
(16, 1, 1, 95.00, '2025-02-01'),
(17, 2, 1, 88.00, '2025-02-01'),
(18, 3, 3, 92.00, '2025-02-01'),
(19, 1, 1, 95.00, '2025-02-01'),
(20, 2, 1, 88.00, '2025-02-01'),
(21, 3, 3, 92.00, '2025-02-01'),
(22, 1, 1, 95.00, '2025-02-01'),
(23, 2, 1, 88.00, '2025-02-01'),
(24, 3, 3, 92.00, '2025-02-01'),
(25, 1, 1, 95.00, '2025-02-01'),
(26, 2, 1, 88.00, '2025-02-01'),
(27, 3, 3, 92.00, '2025-02-01'),
(28, 1, 1, 95.00, '2025-02-01'),
(29, 2, 1, 88.00, '2025-02-01'),
(30, 3, 3, 92.00, '2025-02-01'),
(31, 1, 1, 95.00, '2025-02-01'),
(32, 2, 1, 88.00, '2025-02-01'),
(33, 3, 3, 92.00, '2025-02-01'),
(34, 1, 1, 95.00, '2025-02-01'),
(35, 2, 1, 88.00, '2025-02-01'),
(36, 3, 3, 92.00, '2025-02-01'),
(37, 1, 1, 95.00, '2025-02-01'),
(38, 2, 1, 88.00, '2025-02-01'),
(39, 3, 3, 92.00, '2025-02-01'),
(40, 1, 1, 95.00, '2025-02-01'),
(41, 2, 1, 88.00, '2025-02-01'),
(42, 3, 3, 92.00, '2025-02-01'),
(43, 1, 1, 95.00, '2025-02-01'),
(44, 2, 1, 88.00, '2025-02-01'),
(45, 3, 3, 92.00, '2025-02-01'),
(46, 1, 1, 95.00, '2025-02-01'),
(47, 2, 1, 88.00, '2025-02-01'),
(48, 3, 3, 92.00, '2025-02-01'),
(49, 1, 1, 95.00, '2025-02-01'),
(50, 2, 1, 88.00, '2025-02-01'),
(51, 3, 3, 92.00, '2025-02-01'),
(52, 1, 1, 95.00, '2025-02-01'),
(53, 2, 1, 88.00, '2025-02-01'),
(54, 3, 3, 92.00, '2025-02-01');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `calificacion`
--
ALTER TABLE `calificacion`
  ADD PRIMARY KEY (`id_calificacion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `calificacion`
--
ALTER TABLE `calificacion`
  MODIFY `id_calificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
