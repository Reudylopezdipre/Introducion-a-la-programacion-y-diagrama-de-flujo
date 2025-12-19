-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2025 a las 19:25:24
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
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre`, `telefono`, `correo`) VALUES
(1, 'Ana Pérez', '829-555-1234', 'ana@gmail.com'),
(2, 'Carlos Méndez', '809-444-9988', 'carlos@gmail.com'),
(3, 'María López', '849-777-6622', 'maria@hotmail.com'),
(4, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(5, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(6, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(7, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(8, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(9, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(10, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(11, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(12, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(13, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(14, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(15, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(16, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(17, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(18, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(19, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(20, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(21, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(22, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(23, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(24, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(25, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(26, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(27, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(28, 'Radhames Mercedes', '829-998-7864', 'mradhames23@gmail.com'),
(29, 'Sofia Lopez', '809-777-8989', 'sofia@gmail.com'),
(30, 'Anabel Prez', '849-777-6622', 'anabel@hotmail.com'),
(31, 'Ana Pérez', '829-555-1234', 'ana@gmail.com'),
(32, 'Carlos Méndez', '809-444-9988', 'carlos@gmail.com'),
(33, 'María López', '849-777-6622', 'maria@hotmail.com'),
(34, 'Ana Pérez', '829-555-1234', 'ana@gmail.com'),
(35, 'Carlos Méndez', '809-444-9988', 'carlos@gmail.com'),
(36, 'María López', '849-777-6622', 'maria@hotmail.com'),
(37, 'Ana Pérez', '829-555-1234', 'ana@gmail.com'),
(38, 'Carlos Méndez', '809-444-9988', 'carlos@gmail.com'),
(39, 'María López', '849-777-6622', 'maria@hotmail.com'),
(40, 'Ana Pérez', '829-555-1234', 'ana@gmail.com'),
(41, 'Carlos Méndez', '809-444-9988', 'carlos@gmail.com'),
(42, 'María López', '849-777-6622', 'maria@hotmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
