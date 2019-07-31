/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for building
-- ----------------------------
DROP TABLE IF EXISTS `building`;
CREATE TABLE `building` (
  `building_id` int(11) NOT NULL,
  `building_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `address_id` int(11) DEFAULT NULL,
  `building_manager` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `building_phone` int(20) DEFAULT NULL,
  `other_details` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`building_id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `building_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `address` (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of building
-- ----------------------------
INSERT INTO `building` VALUES ('1', '龙盘山庄', '2', '李一', '123', '123123123');
INSERT INTO `building` VALUES ('2', '明珠小区', '3', '王二', '123', '456456456');
INSERT INTO `building` VALUES ('3', '华师二村', '3', '赵三', '123', '786785685');
