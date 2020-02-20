-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: smashcards
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `char_ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `HP` int NOT NULL,
  `ATK` int NOT NULL,
  `DEF` int NOT NULL,
  `SPD` int NOT NULL,
  PRIMARY KEY (`char_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
INSERT INTO `characters` VALUES (1,'Mario',170,60,60,60),(2,'Luigi',170,60,50,70),(3,'Donkey Kong',190,60,80,20),(4,'Link',175,60,70,40),(5,'Samus',185,55,80,30),(6,'Yoshi',185,55,70,40),(7,'Kirby',115,80,50,80),(8,'Fox',130,80,45,95),(9,'Pikachu',140,70,50,90),(10,'Jigglypuff',120,140,20,60),(11,'Captain Falcon',175,40,40,100),(12,'Ness',150,70,70,70),(13,'Peach',150,70,80,60),(14,'Bowser',200,50,90,10),(15,'Dr Mario',170,50,70,60),(16,'Zelda',150,40,60,60),(17,'Sheik',150,80,50,80),(18,'Young Link',145,50,70,50),(19,'Ganondorf',185,100,60,30),(20,'Falco',140,90,50,80),(21,'Pichu',110,120,20,80),(22,'Mewtwo',145,70,60,60),(23,'Ice Climbers',145,60,50,50),(24,'Marth',145,90,40,80),(25,'Roy',145,80,60,60),(26,'Mr. Game & Watch',120,70,40,70);
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `user_ID` int NOT NULL,
  `char_ID1` int NOT NULL,
  `char_ID2` int NOT NULL,
  `char_ID3` int NOT NULL,
  `team_name` varchar(30) NOT NULL,
  KEY `user_ID` (`user_ID`),
  KEY `char_ID1` (`char_ID1`),
  KEY `char_ID2` (`char_ID2`),
  KEY `char_ID3` (`char_ID3`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `users` (`user_ID`),
  CONSTRAINT `teams_ibfk_2` FOREIGN KEY (`char_ID1`) REFERENCES `characters` (`char_ID`),
  CONSTRAINT `teams_ibfk_3` FOREIGN KEY (`char_ID2`) REFERENCES `characters` (`char_ID`),
  CONSTRAINT `teams_ibfk_4` FOREIGN KEY (`char_ID3`) REFERENCES `characters` (`char_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (1,1,1,1,'test name');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_ID` int NOT NULL AUTO_INCREMENT,
  `forename` varchar(30) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`user_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Test','Surname','cooluser7','test@email.com','*****'),(2,'Test2','Surname2','cooluser8','test2@email.com','*********'),(3,'Test3','Surname3','cooluser9','test3@email.com','******************');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-20 14:54:09
