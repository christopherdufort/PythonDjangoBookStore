-- MySQL Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `soen341`
--

DROP DATABASE IF EXISTS soen341;
CREATE DATABASE soen341;
USE soen341;

-- --------------------------------------------------------

--
-- Table structure for table `library_user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `library_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `session_expire` date NOT NULL,
  `session_key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `library_book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `format` varchar(255) NOT NULL,
  `pages` int(11) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  `isbn_10` bigint(20) DEFAULT NULL,
  `isbn_13` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `magazine`
--

DROP TABLE IF EXISTS `magazine`;
CREATE TABLE IF NOT EXISTS `magazine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  `isbn_10` bigint(20) NOT NULL,
  `isbn_13` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `music`
--

DROP TABLE IF EXISTS `music`;
CREATE TABLE IF NOT EXISTS `music` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `artist` varchar(255) NOT NULL,
  `label` varchar(255) NOT NULL,
  `release_date` date NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
CREATE TABLE IF NOT EXISTS `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `director` varchar(255) NOT NULL,
  `producers` varchar(500) NOT NULL,
  `actors` varchar(500) NOT NULL,
  `language` varchar(255) NOT NULL,
  `subtitles` varchar(255) NOT NULL,
  `dubbed` varchar(255) NOT NULL,
  `release_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------
COMMIT;
