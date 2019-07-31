/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for booking_status
-- ----------------------------
DROP TABLE IF EXISTS `booking_status`;
CREATE TABLE `booking_status` (
  `status_id` int(11) NOT NULL,
  `status_discribe` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`status_id`),
  CONSTRAINT `booking_status_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `booking` (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of booking_status
-- ----------------------------
