-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: bat-store2
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articulo`
--

DROP TABLE IF EXISTS `articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articulo` (
  `codigo_barras` char(13) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Precio` float NOT NULL,
  `reorden` varchar(45) NOT NULL,
  PRIMARY KEY (`codigo_barras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articulo`
--

LOCK TABLES `articulo` WRITE;
/*!40000 ALTER TABLE `articulo` DISABLE KEYS */;
INSERT INTO `articulo` VALUES ('7501000000001','Leche Entera 1L',25.5,'50'),('7501000000002','Pan Blanco Bimbo',32,'30'),('7501000000003','Jugo Naranja 1.5L',38.75,'25'),('7501000000004','Arroz Grano Largo 1KG',22,'60'),('7501000000005','Frijol Negro 900GR',28.9,'40'),('7501000000006','Aceite Vegetal 900ML',45,'20'),('7501000000007','Pasta Dental 75ML',18.5,'70'),('7501000000008','Jabón de Tocador 150GR',12,'100'),('7501000000009','Refresco Cola 600ML',15,'80'),('7501000000010','Galletas Marías 170GR',10.5,'90'),('7501000000011','Café Tostado 250GR',65,'15'),('7501000000012','Atún en Lata 140GR',20,'35');
/*!40000 ALTER TABLE `articulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caja` (
  `idcaja` int NOT NULL,
  `Empleado_idEmpleado` int NOT NULL,
  `dinero_en_caja` float NOT NULL,
  PRIMARY KEY (`idcaja`),
  KEY `fk_caja_Empleado1_idx` (`Empleado_idEmpleado`),
  CONSTRAINT `fk_caja_Empleado1` FOREIGN KEY (`Empleado_idEmpleado`) REFERENCES `empleado` (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
INSERT INTO `caja` VALUES (101,1,1500.75),(102,3,2300.5),(103,5,890.2);
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_general`
--

DROP TABLE IF EXISTS `cliente_general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente_general` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_general`
--

LOCK TABLES `cliente_general` WRITE;
/*!40000 ALTER TABLE `cliente_general` DISABLE KEYS */;
INSERT INTO `cliente_general` VALUES (1,'Cliente General 2025-05-31');
/*!40000 ALTER TABLE `cliente_general` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_proveedor`
--

DROP TABLE IF EXISTS `detalle_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_proveedor` (
  `Proveedor_idProveedor` int NOT NULL,
  `Cantidad` int NOT NULL,
  `costo_compra` float NOT NULL,
  `fecha_compra` date NOT NULL,
  `Articulo_codigo_barras` char(13) NOT NULL,
  PRIMARY KEY (`Proveedor_idProveedor`),
  KEY `fk_Proveedor_has_Producto_Proveedor1_idx` (`Proveedor_idProveedor`),
  KEY `fk_Detalle proveedor_Articulo1_idx` (`Articulo_codigo_barras`),
  CONSTRAINT `fk_Detalle proveedor_Articulo1` FOREIGN KEY (`Articulo_codigo_barras`) REFERENCES `articulo` (`codigo_barras`),
  CONSTRAINT `fk_Proveedor_has_Producto_Proveedor1` FOREIGN KEY (`Proveedor_idProveedor`) REFERENCES `proveedor` (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_proveedor`
--

LOCK TABLES `detalle_proveedor` WRITE;
/*!40000 ALTER TABLE `detalle_proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta` (
  `Venta_idVenta` int NOT NULL,
  `Articulo_codigo_barras` char(13) NOT NULL,
  PRIMARY KEY (`Venta_idVenta`,`Articulo_codigo_barras`),
  KEY `fk_Venta_has_Articulo_Venta1_idx` (`Venta_idVenta`),
  KEY `fk_Detalle venta_Articulo1_idx` (`Articulo_codigo_barras`),
  CONSTRAINT `fk_Detalle venta_Articulo1` FOREIGN KEY (`Articulo_codigo_barras`) REFERENCES `articulo` (`codigo_barras`),
  CONSTRAINT `fk_Venta_has_Articulo_Venta1` FOREIGN KEY (`Venta_idVenta`) REFERENCES `venta` (`idVenta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_venta`
--

LOCK TABLES `detalle_venta` WRITE;
/*!40000 ALTER TABLE `detalle_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `idEmpleado` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Numero` varchar(45) NOT NULL,
  `Puesto` varchar(45) NOT NULL,
  PRIMARY KEY (`idEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,'Ana García','9611234567','Cajero'),(2,'Luis Pérez','9617654321','Gerente'),(3,'Marta López','9612345678','Cajero'),(4,'Carlos Ruiz','9618765432','Supervisor'),(5,'Sofía Hernández','9613456789','Cajero'),(6,'Diego Díaz','9619876543','Limpieza'),(7,'Elena Castro','9614567890','Cajero'),(8,'Fernando Gómez','9610987654','Seguridad'),(9,'Isabel Ramos','9615678901','Cajero'),(10,'Javier Torres','9611122334','Contador');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metodo_de_pago`
--

DROP TABLE IF EXISTS `metodo_de_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metodo_de_pago` (
  `idMetodo de pago` int NOT NULL,
  `metodo` varchar(45) NOT NULL,
  PRIMARY KEY (`idMetodo de pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metodo_de_pago`
--

LOCK TABLES `metodo_de_pago` WRITE;
/*!40000 ALTER TABLE `metodo_de_pago` DISABLE KEYS */;
INSERT INTO `metodo_de_pago` VALUES (1,'Efectivo'),(2,'Tarjeta de Crédito'),(3,'Tarjeta de Débito'),(4,'Transferencia Bancaria');
/*!40000 ALTER TABLE `metodo_de_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `idProveedor` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Telefono` char(10) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `idVenta` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `total` float NOT NULL,
  `cliente general_idCliente` int NOT NULL,
  `Metodo de pago_idMetodo de pago` int NOT NULL,
  `caja_idcaja` int NOT NULL,
  PRIMARY KEY (`idVenta`),
  KEY `fk_Venta_cliente general1_idx` (`cliente general_idCliente`),
  KEY `fk_Venta_Metodo de pago1_idx` (`Metodo de pago_idMetodo de pago`),
  KEY `fk_Venta_caja1_idx` (`caja_idcaja`),
  CONSTRAINT `fk_Venta_caja1` FOREIGN KEY (`caja_idcaja`) REFERENCES `caja` (`idcaja`),
  CONSTRAINT `fk_Venta_cliente general1` FOREIGN KEY (`cliente general_idCliente`) REFERENCES `cliente_general` (`idCliente`),
  CONSTRAINT `fk_Venta_Metodo de pago1` FOREIGN KEY (`Metodo de pago_idMetodo de pago`) REFERENCES `metodo_de_pago` (`idMetodo de pago`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,'2025-05-31',60.9,1,1,101);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-31 14:28:48
