-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 19:25:52
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
-- Base de datos: `ventas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `precio`) VALUES
(1, 'Laptop Lenovo', 45000.00),
(2, 'Mouse Logitech', 1500.00),
(3, 'Monitor LG 24\"', 12000.00),
(4, 'Laptop Lenovo', 45000.00),
(5, 'Mouse Logitech', 1500.00),
(6, 'Monitor LG 24\"', 12000.00),
(7, 'Laptop Lenovo', 45000.00),
(8, 'Mouse Logitech', 1500.00),
(9, 'Monitor LG 24\"', 12000.00),
(10, 'Laptop Lenovo', 45000.00),
(11, 'Mouse Logitech', 1500.00),
(12, 'Monitor LG 24\"', 12000.00),
(13, 'Laptop Lenovo', 45000.00),
(14, 'Mouse Logitech', 1500.00),
(15, 'Monitor LG 24\"', 12000.00),
(16, 'Laptop Lenovo', 45000.00),
(17, 'Mouse Logitech', 1500.00),
(18, 'Monitor LG 24\"', 12000.00),
(19, 'Laptop Lenovo', 45000.00),
(20, 'Mouse Logitech', 1500.00),
(21, 'Monitor LG 24\"', 12000.00),
(22, 'Laptop Lenovo', 45000.00),
(23, 'Mouse Logitech', 1500.00),
(24, 'Monitor LG 24\"', 12000.00),
(25, 'Laptop Lenovo', 45000.00),
(26, 'Mouse Logitech', 1500.00),
(27, 'Monitor LG 24\"', 12000.00),
(28, 'Laptop Lenovo', 45000.00),
(29, 'Mouse Logitech', 1500.00),
(30, 'Monitor LG 24\"', 12000.00),
(31, 'Laptop Lenovo', 45000.00),
(32, 'Mouse Logitech', 1500.00),
(33, 'Monitor LG 24\"', 12000.00),
(34, 'Laptop Lenovo', 45000.00),
(35, 'Mouse Logitech', 1500.00),
(36, 'Monitor LG 24\"', 12000.00),
(37, 'Laptop Lenovo', 45000.00),
(38, 'Mouse Logitech', 1500.00),
(39, 'Monitor LG 24\"', 12000.00),
(40, 'Laptop Lenovo', 45000.00),
(41, 'Mouse Logitech', 1500.00),
(42, 'Monitor LG 24\"', 12000.00);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
