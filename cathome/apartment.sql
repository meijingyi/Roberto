/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : roberto

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:35:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for apartment
-- ----------------------------
DROP TABLE IF EXISTS `apartment`;
CREATE TABLE `apartment` (
  `apt_id` int(11) NOT NULL AUTO_INCREMENT,
  `building_id` int(11) DEFAULT NULL,
  `type_id` int(255) DEFAULT NULL,
  `apt_name` varchar(255) DEFAULT NULL,
  `bathroom_count` int(10) DEFAULT NULL,
  `bedroom_count` int(10) DEFAULT NULL,
  `room_area` int(3) DEFAULT NULL,
  `transport` varchar(255) DEFAULT NULL,
  `max_people_number` int(2) DEFAULT NULL,
  `pic_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`apt_id`),
  KEY `building_id` (`building_id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `apartment_ibfk_1` FOREIGN KEY (`building_id`) REFERENCES `building` (`building_id`),
  CONSTRAINT `apartment_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `apt_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apartment
-- ----------------------------
INSERT INTO `apartment` VALUES ('1', '1', '2', '温馨小屋', '2', '3', '100', '靠近地铁三号线', '3', '/static/img/bg-img/47.jpg');
INSERT INTO `apartment` VALUES ('2', '2', '1', '豪华套房', '3', '5', '150', '靠近地铁一号线', '5', 'img/46.jpg/');
INSERT INTO `apartment` VALUES ('3', '3', '9', '奋斗者家园', '1', '2', '80', '靠近公交960，距离地铁较远', '3', 'img/45.jpg');
