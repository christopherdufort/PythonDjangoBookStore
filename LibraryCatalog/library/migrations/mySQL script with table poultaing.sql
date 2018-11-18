use soen341;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

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
  `ASIN` int(10) NOT NULL,
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

show engines;
show tables;

select * from book;

/*
Populate Tables
*/

-- book
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  1', 'Book Author  1', 'Soft Cover', 100, 'Clearing House', 'English', 1023456789, 1023456789100);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  2', 'Book Author  2', 'Soft Cover', 129, 'Clearing House', 'English', 1322222111, 220888877889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  3', 'Book Author  3', 'Soft Cover', 158, 'Clearing House', 'English', 899988989, 997998911011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  4', 'Book Author  4', 'Soft Cover', 187, 'Clearing House', 'English', 9098909911, 881892190089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  5', 'Book Author  5', 'Soft Cover', 216, 'Clearing House', 'English', 792081189, 207326818811);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  6', 'Book Author  6', 'Soft Cover', 245, 'Clearing House', 'English', 8416037711, 595355062289);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  7', 'Book Author  7', 'Soft Cover', 274, 'Clearing House', 'English', 3187733389, 770151166611);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  8', 'Book Author  8', 'Soft Cover', 303, 'Clearing House', 'English', 5585605511, 554965494489);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  9', 'Book Author  9', 'Soft Cover', 332, 'Clearing House', 'English', 2974945589, 491583954411);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  10', 'Book Author  10', 'Soft Cover', 361, 'Clearing House', 'English', 4519613311, 956811486689);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  11', 'Book Author  11', 'Soft Cover', 390, 'Clearing House', 'English', 7441717789, 164337182211);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  12', 'Book Author  12', 'Soft Cover', 419, 'Clearing House', 'English', 6730061111, 999381038889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  13', 'Book Author  13', 'Soft Cover', 448, 'Clearing House', 'English', 6276049989, 598722850011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  14', 'Book Author  14', 'Soft Cover', 477, 'Clearing House', 'English', 1328948911, 893562151089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  15', 'Book Author  15', 'Soft Cover', 506, 'Clearing House', 'English', 1565942189, 592652957811);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  16', 'Book Author  16', 'Soft Cover', 535, 'Clearing House', 'English', 5028276711, 822642823289);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  17', 'Book Author  17', 'Soft Cover', 564, 'Clearing House', 'English', 7799394389, 931639505611);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  18', 'Book Author  18', 'Soft Cover', 593, 'Clearing House', 'English', 2140044511, 2311055489);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  19', 'Book Author  19', 'Soft Cover', 622, 'Clearing House', 'English', 1864406589, 438794493411);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  20', 'Book Author  20', 'Soft Cover', 651, 'Clearing House', 'English', 4576252311, 620654847689);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  21', 'Book Author  21', 'Soft Cover', 680, 'Clearing House', 'English', 3048978789, 894829921211);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  22', 'Book Author  22', 'Soft Cover', 709, 'Clearing House', 'English', 1848900111, 888162199889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  23', 'Book Author  23', 'Soft Cover', 738, 'Clearing House', 'English', 3041110989, 108057789011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  24', 'Book Author  24', 'Soft Cover', 767, 'Clearing House', 'English', 1069987911, 997721112089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Book Title  25', 'Book Author  25', 'Soft Cover', 796, 'Clearing House', 'English', 5928803189, 874390096811);
SELECT * FROM book;

-- magazine
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  1', 'Readers Digest', 'English', 9012345678, 9012345678912);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  2', 'Readers Digest', 'English', 2222222122, 219989977878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  3', 'Readers Digest', 'English', 9999990078, 989007809922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  4', 'Readers Digest', 'English', 9999017722, 891773182278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  5', 'Readers Digest', 'English', 9902754478, 265545045522);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  6', 'Readers Digest', 'English', 372693322, 268959506678);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  7', 'Readers Digest', 'English', 6896638878, 656991161122);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  8', 'Readers Digest', 'English', 2767248922, 722124951078);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  9', 'Readers Digest', 'English', 3957643278, 760370156722);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  10', 'Readers Digest', 'English', 1806684522, 666645515478);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  11', 'Readers Digest', 'English', 8861767678, 167906032322);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  12', 'Readers Digest', 'English', 7315000122, 492697199878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  13', 'Readers Digest', 'English', 4185012078, 497022787922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  14', 'Readers Digest', 'English', 4316195722, 615256004278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  15', 'Readers Digest', 'English', 7303376478, 330344423522);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  16', 'Readers Digest', 'English', 3034271322, 424097928678);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  17', 'Readers Digest', 'English', 392860878, 285694939122);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  18', 'Readers Digest', 'English', 8893226922, 313798973078);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  19', 'Readers Digest', 'English', 429465278, 946098334722);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  20', 'Readers Digest', 'English', 2517062522, 703735137478);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  21', 'Readers Digest', 'English', 9189189678, 909778610322);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  22', 'Readers Digest', 'English', 9729778122, 968082421878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  23', 'Readers Digest', 'English', 3248034078, 800159765922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  24', 'Readers Digest', 'English', 1555373722, 535816826278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Magazine Title  25', 'Readers Digest', 'English', 3981998478, 195865801522);
SELECT * from magazine;

-- video
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  1', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  2', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  3', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  4', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  5', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  6', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  7', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  8', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  9', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  10', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  11', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  12', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  13', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  14', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  15', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  16', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  17', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  18', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  19', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  20', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  21', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  22', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  23', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  24', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date) VALUES ('Video Title  25', 'Director Dude', 'Soft Cover', 'Producer Girl', 'Hunter S Thompson', 'English', 'French', 'None');
SELECT * FROM video;


-- music
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  1', 'cd', 'Led Zeppelin', 'English', '1990-06-04', 45678910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  2', 'casette', 'Led Zeppelin', 'English', '1990-06-04', 33231090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  3', 'vinyl record', 'Led Zeppelin', 'English', '1990-06-04', 97858910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  4', '8 track', 'Led Zeppelin', 'English', '1990-06-04', 61051090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  5', 'cd', 'Led Zeppelin', 'English', '1990-06-04', 90038910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  6', 'casette', 'Led Zeppelin', 'English', '1990-06-04', 48871090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  7', 'vinyl record', 'Pink Floyd', 'English', '1990-06-04', 22218910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  8', '8 track', 'Pink Floyd', 'English', '1990-06-04', 96691090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  9', 'cd', 'Pink Floyd', 'English', '1990-06-04', 94398910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  10', 'casette', 'Pink Floyd', 'English', '1990-06-04', 4511090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  11', 'vinyl record', 'Pink Floyd', 'English', '1990-06-04', 6578910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  12', '8 track', 'Pink Floyd', 'English', '1990-06-04', 72331090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  13', 'cd', 'Neil Young', 'English', '1990-06-04', 58758910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  14', 'casette', 'Neil Young', 'English', '1990-06-04', 151090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  15', 'vinyl record', 'Neil Young', 'English', '1990-06-04', 50938910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  16', '8 track', 'Neil Young', 'English', '1990-06-04', 87971090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  17', 'cd', 'Neil Young', 'English', '1990-06-04', 83118910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  18', 'casette', 'Neil Young', 'English', '1990-06-04', 35791090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  19', 'vinyl record', 'Metallica', 'English', '1990-06-04', 55298910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  20', '8 track', 'Metallica', 'English', '1990-06-04', 43611090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  21', 'cd', 'Curtis Mayfield', 'English', '1990-06-04', 67478910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  22', 'casette', 'Curtis Mayfield', 'English', '1990-06-04', 11431090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  23', 'vinyl record', 'Buddy Guy', 'English', '1990-06-04', 19658910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  24', '8 track', 'Buddy Guy', 'English', '1990-06-04', 39251090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Album  25', 'cd', 'Buddy Guy', 'English', '1990-06-04', 11838910);

SELECT * from music;

