-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2014 at 11:21 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `lectio`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE IF NOT EXISTS `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `length` int(11) NOT NULL,
  `isbn` int(11) NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `title`, `length`, `isbn`, `photo`) VALUES
(1, 'Звіяні вітром', 100000, 2147483647, 'gone-with-the-wind.jpg'),
(2, 'Великі сподівання', 10000, 2147483647, 'big-hopes.jpg'),
(3, 'Євгеній Онєгін', 5000, 2147483647, 'eugene-onegin.jpg'),
(4, 'Ідіот', 15000, 2147483647, 'idiot.jpg'),
(5, 'Червоне і Чорне', 3000, 2147483647, 'red-black.jpg'),
(6, 'Гордість і упередженість', 50000, 123456, 'pride-prejudice.jpg'),
(7, 'Джейн Ейр', 5220000, 123456, 'jane-air.jpg'),
(8, 'Ті, що співають у терні', 89666, 123456, 'mccalow.jpg'),
(9, 'Я, робот', 852147, 45625, 'i-robot.jpg'),
(10, 'Кульбабове вино', 1, 1, 'dandelione-wine.jpg'),
(11, 'Марсіанські хроніки', 1, 1, 'martian-cronicles.jpg'),
(12, '1984', 1, 1, '1984.jpg'),
(13, 'Гарі Потер', 1, 1, 'harry-potter.jpg'),
(14, 'Основа', 1, 1, 'foundation.jpg'),
(15, 'Охорона! Охорона!', 1, 1, 'guard.jpg'),
(16, 'Сага про відьмака', 1, 1, 'vedmak.jpg'),
(17, 'Тканина космосу: Простір, час і текстура реальності', 1, 1, 'space.jpg'),
(18, 'Атлант розправив плечі', 1, 1, 'atlant.jpg'),
(19, 'Космос: Еволюція Всесвіту, життя і цивілізації', 1, 1, 'space-sagan.jpg'),
(20, 'Світ у горіховій скарлупці', 0, 0, 'hokking.jpg'),
(21, 'Кінець нескінченності', 1, 1, 'end_of_eternity.jpg'),
(22, 'Евгений Онегин', 1, 1, 'onegin.jpg'),
(23, 'Ловець у житі', 1, 1, 'catcher-in-the-rye.jpg'),
(24, 'Портрет Доріана Грея', 1, 1, 'portret-doriana-greya4.jpg'),
(29, 'Майстер і Маргарита', 1, 1, 'master-i-margarita.jpg'),
(30, 'Гранатовий браслет', 1, 1, 'bracelete.jpg'),
(31, 'Зима тривоги нашої', 1, 1, 'zima-trevogi-nashey.jpg'),
(32, 'Брудними руками', 1, 1, 'dirty-hands.jpg'),
(33, 'На західному фронті без змін', 1, 1, 'west-front.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `books_users`
--

CREATE TABLE IF NOT EXISTS `books_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `bookmarked_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `books_users`
--

INSERT INTO `books_users` (`id`, `user_id`, `bookmarked_id`, `date`) VALUES
(18, 1, 2, '2014-06-09 11:35:34'),
(24, 1, 3, '2014-06-09 12:25:38'),
(27, 2, 3, '2014-06-10 17:42:36'),
(28, 2, 5, '2014-06-10 17:42:37'),
(29, 2, 4, '2014-06-10 17:42:38'),
(31, 1, 7, '2014-06-10 21:18:48'),
(32, 1, 11, '2014-06-10 21:18:49'),
(33, 1, 23, '2014-06-10 21:19:20');

-- --------------------------------------------------------

--
-- Table structure for table `devices`
--

CREATE TABLE IF NOT EXISTS `devices` (
  `device_id` int(11) NOT NULL AUTO_INCREMENT,
  `unique_id` varchar(100) NOT NULL,
  PRIMARY KEY (`device_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `devices`
--

INSERT INTO `devices` (`device_id`, `unique_id`) VALUES
(1, 'abc-fake');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE IF NOT EXISTS `log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `device_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `progress` decimal(5,2) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=68 ;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`log_id`, `device_id`, `book_id`, `datetime`, `progress`) VALUES
(1, 1, 1, '2014-01-02 20:00:00', '0.00'),
(2, 1, 1, '2014-04-20 20:00:00', '70.00'),
(3, 1, 1, '2014-03-21 20:00:00', '100.00'),
(4, 1, 2, '2014-04-13 20:00:00', '0.00'),
(5, 1, 2, '2014-01-06 20:00:00', '80.00'),
(6, 1, 2, '2014-04-20 20:00:00', '100.00'),
(7, 1, 3, '2014-04-12 20:00:00', '0.00'),
(8, 1, 3, '2014-01-20 20:00:00', '98.00'),
(9, 1, 3, '2014-04-16 20:00:00', '100.00'),
(10, 1, 4, '2014-04-23 20:00:00', '0.00'),
(11, 1, 4, '2014-01-18 20:00:00', '62.00'),
(12, 1, 4, '2014-02-12 20:00:00', '40.00'),
(13, 1, 4, '2014-03-18 20:00:00', '50.00'),
(14, 1, 2, '2014-01-23 20:00:00', '5.00'),
(15, 3, 9, '2014-04-03 20:00:00', '5.00'),
(16, 3, 9, '2014-03-24 20:00:00', '100.00'),
(17, 3, 10, '2013-12-31 20:00:00', '5.00'),
(18, 3, 10, '2014-04-03 20:00:00', '100.00'),
(19, 3, 11, '2014-05-16 20:00:00', '5.00'),
(20, 3, 11, '2014-03-04 20:00:00', '100.00'),
(21, 3, 1, '2014-01-25 20:00:00', '5.00'),
(22, 3, 1, '2014-03-10 20:00:00', '100.00'),
(23, 3, 12, '2014-03-20 20:00:00', '5.00'),
(24, 3, 12, '2014-05-19 20:00:00', '100.00'),
(25, 3, 13, '2014-04-01 20:00:00', '5.00'),
(26, 4, 14, '2014-02-14 20:00:00', '5.00'),
(27, 4, 14, '2014-04-20 20:00:00', '100.00'),
(28, 4, 15, '2014-05-24 20:00:00', '5.00'),
(29, 4, 15, '2014-05-06 20:00:00', '100.00'),
(30, 4, 16, '2014-02-08 20:00:00', '5.00'),
(31, 4, 16, '2014-05-26 20:00:00', '100.00'),
(32, 4, 17, '2014-05-17 20:00:00', '5.00'),
(33, 4, 17, '2014-03-13 20:00:00', '100.00'),
(34, 4, 18, '2014-05-13 20:00:00', '5.00'),
(35, 4, 18, '2014-03-06 20:00:00', '100.00'),
(36, 4, 19, '2014-03-22 20:00:00', '5.00'),
(37, 4, 19, '2014-04-19 20:00:00', '100.00'),
(38, 4, 20, '2014-04-06 20:00:00', '5.00'),
(39, 5, 21, '2014-01-04 20:00:00', '5.00'),
(40, 5, 21, '2014-02-26 20:00:00', '100.00'),
(41, 5, 1, '2014-01-04 20:00:00', '5.00'),
(42, 5, 1, '2014-04-12 20:00:00', '100.00'),
(43, 5, 22, '2014-05-08 20:00:00', '5.00'),
(44, 5, 22, '2014-04-19 20:00:00', '100.00'),
(45, 5, 23, '2014-02-16 20:00:00', '5.00'),
(46, 5, 23, '2014-01-14 20:00:00', '100.00'),
(47, 5, 24, '2014-03-20 20:00:00', '5.00'),
(48, 6, 29, '2014-03-22 20:00:00', '5.00'),
(49, 6, 29, '2014-05-21 20:00:00', '100.00'),
(50, 6, 30, '2014-03-19 20:00:00', '5.00'),
(51, 6, 30, '2014-03-21 20:00:00', '100.00'),
(52, 6, 31, '2014-05-22 20:00:00', '5.00'),
(53, 6, 31, '2014-03-13 20:00:00', '100.00'),
(54, 6, 18, '2014-04-26 20:00:00', '5.00'),
(55, 6, 18, '2014-04-25 20:00:00', '100.00'),
(56, 6, 32, '2014-02-24 20:00:00', '5.00'),
(57, 6, 32, '2014-03-23 20:00:00', '100.00'),
(58, 6, 6, '2014-05-12 20:00:00', '5.00'),
(59, 6, 6, '2014-05-01 20:00:00', '100.00'),
(60, 6, 33, '2014-03-15 20:00:00', '5.00'),
(61, 6, 33, '2014-02-09 20:00:00', '100.00'),
(62, 6, 23, '2014-01-15 20:00:00', '5.00'),
(63, 7, 12, '2014-03-22 20:00:00', '5.00'),
(64, 7, 12, '2014-03-11 20:00:00', '100.00'),
(65, 7, 23, '2014-03-23 20:00:00', '5.00'),
(66, 7, 23, '2014-01-18 20:00:00', '100.00'),
(67, 7, 29, '2014-01-23 20:00:00', '5.00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `device_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(32) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `device_id`, `name`, `photo`, `email`, `password`) VALUES
(1, 1, 'Никита Остер', 'm128.jpg', NULL, 'e10adc3949ba59abbe56e057f20f883e'),
(2, 2, 'Марина Флафьева', 'w128.jpg', NULL, 'e10adc3949ba59abbe56e057f20f883e'),
(3, 3, 'Надя', 'nadya.jpg', NULL, 'ee11cbb19052e40b07aac0ca060c23ee'),
(4, 4, 'Стас', 'stas.jpg', NULL, 'ee11cbb19052e40b07aac0ca060c23ee'),
(5, 5, 'Лера', 'Lera.jpg', lera@gmail.com, 'lera'),
(6, 6, 'Таня', 'tanya.jpg', NULL, 'ee11cbb19052e40b07aac0ca060c23ee'),
(7, 7, 'Рита', 'rita.jpg', NULL, 'ee11cbb19052e40b07aac0ca060c23ee');

-- --------------------------------------------------------

--
-- Table structure for table `users_books_ratings`
--

CREATE TABLE IF NOT EXISTS `users_books_ratings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=33 ;

--
-- Dumping data for table `users_books_ratings`
--

INSERT INTO `users_books_ratings` (`id`, `book_id`, `user_id`, `rating`) VALUES
(1, 1, 1, 0),
(2, 2, 1, 1),
(3, 3, 1, 0),
(4, 9, 3, 1),
(5, 10, 3, 1),
(6, 11, 3, 1),
(7, 1, 3, 1),
(8, 12, 3, 1),
(9, 13, 3, 1),
(10, 14, 4, 1),
(11, 15, 4, 1),
(12, 16, 4, 1),
(13, 17, 4, 1),
(14, 18, 4, 1),
(15, 19, 4, 1),
(16, 20, 4, 1),
(17, 21, 5, 1),
(18, 1, 5, 1),
(19, 22, 5, 1),
(20, 23, 5, 1),
(21, 24, 5, 1),
(22, 29, 6, 1),
(23, 30, 6, 1),
(24, 31, 6, 1),
(25, 18, 6, 1),
(26, 32, 6, 1),
(27, 6, 6, 1),
(28, 33, 6, 1),
(29, 23, 6, 1),
(30, 12, 7, 1),
(31, 23, 7, 1),
(32, 29, 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_users`
--

CREATE TABLE IF NOT EXISTS `users_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `bokmarked_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
