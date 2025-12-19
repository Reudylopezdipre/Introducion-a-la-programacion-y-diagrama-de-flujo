-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 22:44:17
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
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id_estudiante` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `id_departamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id_estudiante`, `nombre`, `apellido`, `fecha_nacimiento`, `id_departamento`) VALUES
(1, 'Ana', 'García', '2005-01-12', 1),
(2, 'Luis', 'Martínez', '2004-04-20', 1),
(3, 'María', 'Torres', '2003-09-15', 3),
(4, 'Ana', 'García', '2005-01-12', 1),
(5, 'Luis', 'Martínez', '2004-04-20', 1),
(6, 'María', 'Torres', '2003-09-15', 3),
(7, 'Ana', 'García', '2005-01-12', 1),
(8, 'Luis', 'Martínez', '2004-04-20', 1),
(9, 'María', 'Torres', '2003-09-15', 3),
(10, 'Ana', 'García', '2005-01-12', 1),
(11, 'Luis', 'Martínez', '2004-04-20', 1),
(12, 'María', 'Torres', '2003-09-15', 3),
(13, 'Ana', 'García', '2005-01-12', 1),
(14, 'Luis', 'Martínez', '2004-04-20', 1),
(15, 'María', 'Torres', '2003-09-15', 3),
(16, 'Ana', 'García', '2005-01-12', 1),
(17, 'Luis', 'Martínez', '2004-04-20', 1),
(18, 'María', 'Torres', '2003-09-15', 3),
(19, 'Ana', 'García', '2005-01-12', 1),
(20, 'Luis', 'Martínez', '2004-04-20', 1),
(21, 'María', 'Torres', '2003-09-15', 3),
(22, 'Ana', 'García', '2005-01-12', 1),
(23, 'Luis', 'Martínez', '2004-04-20', 1),
(24, 'María', 'Torres', '2003-09-15', 3),
(25, 'Ana', 'García', '2005-01-12', 1),
(26, 'Luis', 'Martínez', '2004-04-20', 1),
(27, 'María', 'Torres', '2003-09-15', 3),
(28, 'Ana', 'García', '2005-01-12', 1),
(29, 'Luis', 'Martínez', '2004-04-20', 1),
(30, 'María', 'Torres', '2003-09-15', 3),
(31, 'Ana', 'García', '2005-01-12', 1),
(32, 'Luis', 'Martínez', '2004-04-20', 1),
(33, 'María', 'Torres', '2003-09-15', 3),
(34, 'Ana', 'García', '2005-01-12', 1),
(35, 'Luis', 'Martínez', '2004-04-20', 1),
(36, 'María', 'Torres', '2003-09-15', 3),
(37, 'Ana', 'García', '2005-01-12', 1),
(38, 'Luis', 'Martínez', '2004-04-20', 1),
(39, 'María', 'Torres', '2003-09-15', 3),
(40, 'Ana', 'García', '2005-01-12', 1),
(41, 'Luis', 'Martínez', '2004-04-20', 1),
(42, 'María', 'Torres', '2003-09-15', 3),
(43, 'Ana', 'García', '2005-01-12', 1),
(44, 'Luis', 'Martínez', '2004-04-20', 1),
(45, 'María', 'Torres', '2003-09-15', 3),
(46, 'Ana', 'García', '2005-01-12', 1),
(47, 'Luis', 'Martínez', '2004-04-20', 1),
(48, 'María', 'Torres', '2003-09-15', 3),
(49, 'Ana', 'García', '2005-01-12', 1),
(50, 'Luis', 'Martínez', '2004-04-20', 1),
(51, 'María', 'Torres', '2003-09-15', 3),
(52, 'Ana', 'García', '2005-01-12', 1),
(53, 'Luis', 'Martínez', '2004-04-20', 1),
(54, 'María', 'Torres', '2003-09-15', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
