/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for booking
-- ----------------------------
DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `apt_id` int(11) NOT NULL,
  `guest_id` int(11) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `begin_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `people_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `status_id` (`status_id`),
  KEY `guest_id` (`guest_id`),
  KEY `apt_id` (`apt_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`guest_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`apt_id`) REFERENCES `apartment` (`apt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of booking
-- ----------------------------
