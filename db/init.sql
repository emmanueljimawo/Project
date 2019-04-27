-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: feature_request
-- ------------------------------------------------------
-- Server version	5.7.24
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) NOT NULL,
  `description` text NOT NULL,
  `client` varchar(12) NOT NULL,
  `client_priority` int(11) NOT NULL,
  `target_date` date NOT NULL,
  `product_area` varchar(12) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (1,'Test request','This is a test request','Client B',1,'2019-04-27','Billing',1),(2,'Test request','This is a test request','Client C',2,'2019-04-27','Billing',1),(3,'Test request','This is a test request','Client A',3,'2019-04-27','Billing',1),(4,'Test request','This is a test request','Client A',4,'2019-04-27','Billing',1),(5,'Test request','This is a test request','Client B',5,'2019-04-27','Billing',1),(6,'Test request','This is a test request','Client B',6,'2019-04-27','Billing',1),(7,'Test request','This is a test request','Client C',1,'2019-04-27','Billing',1),(8,'Test request','This is a test request','Client C',1,'2019-04-27','Billing',1),(9,'Test request','This is a test request','Client B',2,'2019-04-27','Billing',1),(10,'Test request','This is a test request','Client A',2,'2019-04-27','Billing',1),(11,'Test request','This is a test request','Client C',3,'2019-04-27','Billing',1),(12,'Test request','This is a test request','Client C',3,'2019-04-27','Billing',1),(13,'Test request','This is a test request','Client B',1,'2019-04-27','Billing',1),(14,'Test request','This is a test request','Client A',2,'2019-04-27','Billing',2),(15,'Test request','This is a test request','Client A',1,'2019-04-27','Billing',2);
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin@iws.com','$2b$12$TyMwBTL9Y9m5ZUrjf9TR4eIf7zDrl6t0qHzUfVmC8EyamaPcQpYe2'),(2,'stevejobs','stevejobs@iws.com','$2b$12$03VPWYqcOLeaQHt9u.GrHOcIPJaMccD/BpYj1.DTKQFhUedK.Ucam'),(3,'elonmusk','elonmusk@iws.com','$2b$12$npC6serwKY6Pd0K6Rcdehu4zcFlcGRII6ovcwS.QBE6O5efpAN8L.');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
