-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:44:40
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
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `id_profesor` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `id_departamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`id_profesor`, `nombre`, `apellido`, `id_departamento`) VALUES
(1, 'Juan', 'López', 1),
(2, 'María', 'Pérez', 2),
(3, 'Carlos', 'Ramírez', 3),
(4, 'Juan', 'López', 1),
(5, 'María', 'Pérez', 2),
(6, 'Carlos', 'Ramírez', 3),
(7, 'Juan', 'López', 1),
(8, 'María', 'Pérez', 2),
(9, 'Carlos', 'Ramírez', 3),
(10, 'Juan', 'López', 1),
(11, 'María', 'Pérez', 2),
(12, 'Carlos', 'Ramírez', 3),
(13, 'Juan', 'López', 1),
(14, 'María', 'Pérez', 2),
(15, 'Carlos', 'Ramírez', 3),
(16, 'Juan', 'López', 1),
(17, 'María', 'Pérez', 2),
(18, 'Carlos', 'Ramírez', 3),
(19, 'Juan', 'López', 1),
(20, 'María', 'Pérez', 2),
(21, 'Carlos', 'Ramírez', 3),
(22, 'Juan', 'López', 1),
(23, 'María', 'Pérez', 2),
(24, 'Carlos', 'Ramírez', 3),
(25, 'Juan', 'López', 1),
(26, 'María', 'Pérez', 2),
(27, 'Carlos', 'Ramírez', 3),
(28, 'Juan', 'López', 1),
(29, 'María', 'Pérez', 2),
(30, 'Carlos', 'Ramírez', 3),
(31, 'Juan', 'López', 1),
(32, 'María', 'Pérez', 2),
(33, 'Carlos', 'Ramírez', 3),
(34, 'Juan', 'López', 1),
(35, 'María', 'Pérez', 2),
(36, 'Carlos', 'Ramírez', 3),
(37, 'Juan', 'López', 1),
(38, 'María', 'Pérez', 2),
(39, 'Carlos', 'Ramírez', 3),
(40, 'Juan', 'López', 1),
(41, 'María', 'Pérez', 2),
(42, 'Carlos', 'Ramírez', 3),
(43, 'Juan', 'López', 1),
(44, 'María', 'Pérez', 2),
(45, 'Carlos', 'Ramírez', 3),
(46, 'Juan', 'López', 1),
(47, 'María', 'Pérez', 2),
(48, 'Carlos', 'Ramírez', 3),
(49, 'Juan', 'López', 1),
(50, 'María', 'Pérez', 2),
(51, 'Carlos', 'Ramírez', 3),
(52, 'Juan', 'López', 1),
(53, 'María', 'Pérez', 2),
(54, 'Carlos', 'Ramírez', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`id_profesor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `profesor`
--
ALTER TABLE `profesor`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
