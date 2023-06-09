-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: hw_5_sql_practice
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `COUNTRY_ID` int NOT NULL AUTO_INCREMENT,
  `COUNTRY_NAME` char(50) NOT NULL,
  `REGION_ID` int NOT NULL,
  PRIMARY KEY (`COUNTRY_ID`),
  KEY `REGION_ID` (`REGION_ID`),
  CONSTRAINT `COUNTRIES_ibfk_1` FOREIGN KEY (`REGION_ID`) REFERENCES `regions` (`REGION_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Ukraine',1);
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `DEPARTMENT_ID` int NOT NULL AUTO_INCREMENT,
  `DEPARTMENT_NAME` char(100) NOT NULL,
  `MANAGER_ID` int DEFAULT NULL,
  `LOCATION_ID` int DEFAULT NULL,
  PRIMARY KEY (`DEPARTMENT_ID`),
  UNIQUE KEY `MANAGER_ID` (`MANAGER_ID`),
  KEY `LOCATION_ID` (`LOCATION_ID`),
  CONSTRAINT `DEPARTMENTS_ibfk_1` FOREIGN KEY (`LOCATION_ID`) REFERENCES `locations` (`LOCATION_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (10,'IT Support',1,1),(20,'Software Development',2,2),(30,'Database Administration',3,3),(40,'Web Development',4,4),(50,'Network Administration',5,5),(60,'Systems Analysis',6,6),(70,'Application Design',7,7),(80,'Software Testing',8,8),(90,'IT Management',9,9);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `EMPLOYEE_ID` int NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` char(20) NOT NULL,
  `LAST_NAME` char(30) NOT NULL,
  `EMAIL` char(50) DEFAULT NULL,
  `PHONE_NUMBER` char(20) DEFAULT NULL,
  `HIRE_DATE` date NOT NULL,
  `JOB_ID` int DEFAULT NULL,
  `SALARY` double(10,2) NOT NULL,
  `COMMISSION_PCT` int DEFAULT NULL,
  `MANAGER_ID` int NOT NULL,
  `DEPARTMENT_ID` int DEFAULT NULL,
  PRIMARY KEY (`EMPLOYEE_ID`),
  KEY `JOB_ID` (`JOB_ID`),
  KEY `DEPARTMENT_ID` (`DEPARTMENT_ID`),
  KEY `MANAGER_ID` (`MANAGER_ID`),
  CONSTRAINT `EMPLOYEES_ibfk_1` FOREIGN KEY (`JOB_ID`) REFERENCES `jobs` (`JOB_ID`),
  CONSTRAINT `EMPLOYEES_ibfk_2` FOREIGN KEY (`DEPARTMENT_ID`) REFERENCES `departments` (`DEPARTMENT_ID`),
  CONSTRAINT `EMPLOYEES_ibfk_3` FOREIGN KEY (`MANAGER_ID`) REFERENCES `departments` (`MANAGER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Roman','Mereniuk','roman@gmail.com','093488754','2007-08-23',3,5000.00,NULL,6,60),(2,'John','Smith','john@gmail.com','0123456789','2007-10-25',4,6000.00,NULL,9,90),(3,'Adam','Brown','adam@gmail.com','0123456780','2007-02-05',9,7000.00,NULL,6,60),(4,'Joe','Hill','joe@gmail.com','0123456781','2007-04-01',8,8000.00,20,3,30);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_history`
--

DROP TABLE IF EXISTS `job_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_history` (
  `EMPLOYEE_ID` int DEFAULT NULL,
  `START_DATE` date NOT NULL,
  `END_DATE` date DEFAULT NULL,
  `JOB_ID` int NOT NULL,
  `DEPARTMENT_ID` int DEFAULT NULL,
  KEY `EMPLOYEE_ID` (`EMPLOYEE_ID`),
  KEY `JOB_ID` (`JOB_ID`),
  KEY `DEPARTMENT_ID` (`DEPARTMENT_ID`),
  CONSTRAINT `JOB_HISTORY_ibfk_1` FOREIGN KEY (`EMPLOYEE_ID`) REFERENCES `employees` (`EMPLOYEE_ID`),
  CONSTRAINT `JOB_HISTORY_ibfk_2` FOREIGN KEY (`JOB_ID`) REFERENCES `jobs` (`JOB_ID`),
  CONSTRAINT `JOB_HISTORY_ibfk_3` FOREIGN KEY (`DEPARTMENT_ID`) REFERENCES `departments` (`DEPARTMENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_history`
--

LOCK TABLES `job_history` WRITE;
/*!40000 ALTER TABLE `job_history` DISABLE KEYS */;
INSERT INTO `job_history` VALUES (1,'2007-08-23',NULL,8,60),(2,'2007-10-25',NULL,1,90),(3,'2007-02-05',NULL,9,60),(4,'2007-04-01',NULL,5,30);
/*!40000 ALTER TABLE `job_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `JOB_ID` int NOT NULL AUTO_INCREMENT,
  `JOB_TITLE` char(255) NOT NULL,
  `MIN_SALARY` float(10,2) NOT NULL,
  `MAX_SALARY` float(10,2) NOT NULL,
  PRIMARY KEY (`JOB_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,'Python Developer',95000.00,150000.00),(2,'Front-end developer',80000.00,120000.00),(3,'DevOps',110000.00,170000.00),(4,'Software Engineer',50000.00,100000.00),(5,'Systems Administrator',40000.00,80000.00),(6,'Network Engineer',31000.00,63200.00),(7,'Web Developer',22000.00,65000.00),(8,'Database Administrator',31000.00,77000.00),(9,'QA Engineer',33000.00,75000.00);
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `LOCATION_ID` int NOT NULL AUTO_INCREMENT,
  `STREET_ADDRESS` char(255) NOT NULL,
  `POSTAL_CODE` char(50) NOT NULL,
  `CITY` char(50) NOT NULL,
  `STATE_PROVINCE` char(50) NOT NULL,
  `COUNTRY_ID` int DEFAULT NULL,
  PRIMARY KEY (`LOCATION_ID`),
  KEY `COUNTRY_ID` (`COUNTRY_ID`),
  CONSTRAINT `LOCATIONS_ibfk_1` FOREIGN KEY (`COUNTRY_ID`) REFERENCES `countries` (`COUNTRY_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Street 1','11111','Kyiv','Kyivska oblast',1),(2,'Street 2','79008','Lviv','Lvivska state',1),(3,'3 Main Street','81048','Odesa','Odeska state',1),(4,'street 4','40568','Kharkiv','Kharkivska state',1),(5,'Street 5','39501','Dnipro','Dnipropetrovska state',1),(6,'street 6','14893','Donetsk','Donetska oblast',1),(7,'Street 7','45682','Vinnytsia','Vinnytska oblast',1),(8,'8 Main Street','00008','Zaporizhia','Zaporizka oblast',1),(9,'9 Main Street','14157','Cherkasy','Cherkaska oblast',1);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regions` (
  `REGION_ID` int NOT NULL AUTO_INCREMENT,
  `REGION_NAME` char(50) NOT NULL,
  PRIMARY KEY (`REGION_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
INSERT INTO `regions` VALUES (1,'Europe'),(2,'Asia'),(3,'Africa'),(4,'Australia'),(5,'North America'),(6,'South America'),(7,'Oceania'),(8,'Antarctica');
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-19 20:24:55
