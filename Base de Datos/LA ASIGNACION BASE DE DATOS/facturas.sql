-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 19:25:35
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
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `id_factura` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT 1,
  `total` decimal(10,2) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`id_factura`, `id_cliente`, `id_producto`, `cantidad`, `total`, `fecha`) VALUES
(1, 1, 1, 1, 45000.00, '2025-12-07 18:19:24'),
(2, 2, 2, 2, 3000.00, '2025-12-07 18:19:24'),
(3, 3, 1, 1, 45000.00, '2025-12-07 18:19:24'),
(4, 3, 3, 1, 12000.00, '2025-12-07 18:19:24'),
(5, 1, 1, 1, 45000.00, '2025-12-07 18:21:55'),
(6, 2, 2, 2, 3000.00, '2025-12-07 18:21:55'),
(7, 3, 1, 1, 45000.00, '2025-12-07 18:21:55'),
(8, 3, 3, 1, 12000.00, '2025-12-07 18:21:55'),
(9, 1, 1, 1, 45000.00, '2025-12-07 18:21:59'),
(10, 2, 2, 2, 3000.00, '2025-12-07 18:21:59'),
(11, 3, 1, 1, 45000.00, '2025-12-07 18:21:59'),
(12, 3, 3, 1, 12000.00, '2025-12-07 18:21:59'),
(13, 1, 1, 1, 45000.00, '2025-12-07 18:22:01'),
(14, 2, 2, 2, 3000.00, '2025-12-07 18:22:01'),
(15, 3, 1, 1, 45000.00, '2025-12-07 18:22:01'),
(16, 3, 3, 1, 12000.00, '2025-12-07 18:22:01'),
(17, 1, 1, 1, 45000.00, '2025-12-07 18:22:06'),
(18, 2, 2, 2, 3000.00, '2025-12-07 18:22:06'),
(19, 3, 1, 1, 45000.00, '2025-12-07 18:22:06'),
(20, 3, 3, 1, 12000.00, '2025-12-07 18:22:06'),
(21, 1, 1, 1, 45000.00, '2025-12-07 18:22:13'),
(22, 2, 2, 2, 3000.00, '2025-12-07 18:22:13'),
(23, 3, 1, 1, 45000.00, '2025-12-07 18:22:13'),
(24, 3, 3, 1, 12000.00, '2025-12-07 18:22:13'),
(25, 1, 1, 1, 45000.00, '2025-12-07 18:22:14'),
(26, 2, 2, 2, 3000.00, '2025-12-07 18:22:14'),
(27, 3, 1, 1, 45000.00, '2025-12-07 18:22:14'),
(28, 3, 3, 1, 12000.00, '2025-12-07 18:22:14'),
(29, 1, 1, 1, 45000.00, '2025-12-07 18:22:16'),
(30, 2, 2, 2, 3000.00, '2025-12-07 18:22:16'),
(31, 3, 1, 1, 45000.00, '2025-12-07 18:22:16'),
(32, 3, 3, 1, 12000.00, '2025-12-07 18:22:16'),
(33, 1, 1, 1, 45000.00, '2025-12-07 18:22:17'),
(34, 2, 2, 2, 3000.00, '2025-12-07 18:22:17'),
(35, 3, 1, 1, 45000.00, '2025-12-07 18:22:17'),
(36, 3, 3, 1, 12000.00, '2025-12-07 18:22:17'),
(37, 1, 1, 1, 45000.00, '2025-12-07 18:22:35'),
(38, 2, 2, 2, 3000.00, '2025-12-07 18:22:35'),
(39, 3, 1, 1, 45000.00, '2025-12-07 18:22:35'),
(40, 3, 3, 1, 12000.00, '2025-12-07 18:22:35'),
(41, 1, 1, 1, 45000.00, '2025-12-07 18:23:11'),
(42, 2, 2, 2, 3000.00, '2025-12-07 18:23:11'),
(43, 3, 1, 1, 45000.00, '2025-12-07 18:23:11'),
(44, 3, 3, 1, 12000.00, '2025-12-07 18:23:11'),
(45, 1, 1, 1, 45000.00, '2025-12-07 18:23:13'),
(46, 2, 2, 2, 3000.00, '2025-12-07 18:23:13'),
(47, 3, 1, 1, 45000.00, '2025-12-07 18:23:13'),
(48, 3, 3, 1, 12000.00, '2025-12-07 18:23:13'),
(49, 1, 1, 1, 45000.00, '2025-12-07 18:23:14'),
(50, 2, 2, 2, 3000.00, '2025-12-07 18:23:14'),
(51, 3, 1, 1, 45000.00, '2025-12-07 18:23:14'),
(52, 3, 3, 1, 12000.00, '2025-12-07 18:23:14'),
(53, 1, 1, 1, 45000.00, '2025-12-07 18:23:19'),
(54, 2, 2, 2, 3000.00, '2025-12-07 18:23:19'),
(55, 3, 1, 1, 45000.00, '2025-12-07 18:23:19'),
(56, 3, 3, 1, 12000.00, '2025-12-07 18:23:19');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`id_factura`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_producto` (`id_producto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `facturas`
--
ALTER TABLE `facturas`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  ADD CONSTRAINT `facturas_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
