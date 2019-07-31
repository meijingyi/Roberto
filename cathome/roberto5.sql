/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : roberto5

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-15 17:08:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `address_id` int(11) NOT NULL,
  `address_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `distinct_id` int(11) unsigned zerofill DEFAULT NULL,
  `province_id` int(11) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO `address` VALUES ('1', '上海市', '00000000000', '00000000004');
INSERT INTO `address` VALUES ('2', '普陀区', '00000000001', '00000000004');
INSERT INTO `address` VALUES ('3', '徐汇区', '00000000001', '00000000004');
INSERT INTO `address` VALUES ('4', '上海市', '00000000000', '00000000000');
INSERT INTO `address` VALUES ('5', '山东省', '00000000000', '00000000000');
INSERT INTO `address` VALUES ('6', '济南市', '00000000000', '00000000005');
INSERT INTO `address` VALUES ('7', '历下区', '00000000006', '00000000005');

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `username` varchar(255) CHARACTER SET utf8 NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('123', '123');
INSERT INTO `admin` VALUES ('1234', '1234');

-- ----------------------------
-- Table structure for agent
-- ----------------------------
DROP TABLE IF EXISTS `agent`;
CREATE TABLE `agent` (
  `agent_id` int(11) DEFAULT NULL,
  `agent_username` varchar(255) DEFAULT NULL,
  `agent_pw` varchar(255) DEFAULT NULL,
  `agent_name` varchar(255) DEFAULT NULL,
  `agent_phone` varchar(255) DEFAULT NULL,
  `agent_company` varchar(255) DEFAULT NULL,
  `agent_wechat` varchar(255) DEFAULT NULL,
  KEY `agent_id` (`agent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of agent
-- ----------------------------

-- ----------------------------
-- Table structure for apartment
-- ----------------------------
DROP TABLE IF EXISTS `apartment`;
CREATE TABLE `apartment` (
  `apt_id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) DEFAULT NULL,
  `building_id` int(11) DEFAULT NULL,
  `type_id` int(255) DEFAULT NULL,
  `apt_name` varchar(255) DEFAULT NULL,
  `bathroom_count` int(10) DEFAULT NULL,
  `bedroom_count` int(10) DEFAULT NULL,
  `room_area` int(3) DEFAULT NULL,
  `transport` varchar(255) DEFAULT NULL,
  `max_people_number` int(2) DEFAULT NULL,
  `pic_url` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `direction` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`apt_id`),
  KEY `building_id` (`building_id`),
  KEY `type_id` (`type_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `apartment_ibfk_1` FOREIGN KEY (`building_id`) REFERENCES `building` (`building_id`),
  CONSTRAINT `apartment_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `apt_type` (`type_id`),
  CONSTRAINT `apartment_ibfk_3` FOREIGN KEY (`agent_id`) REFERENCES `agent` (`agent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apartment
-- ----------------------------
INSERT INTO `apartment` VALUES ('1', null, '1', '2', '温馨小屋', '2', '3', '100', '靠近地铁三号线', '3', '/static/img/bg-img/47.jpg', '3000.00', null);
INSERT INTO `apartment` VALUES ('2', null, '2', '1', '豪华套房', '3', '5', '150', '靠近地铁一号线', '5', 'img/46.jpg/', '5000.00', null);
INSERT INTO `apartment` VALUES ('3', null, '3', '9', '奋斗者家园', '1', '2', '80', '靠近公交960，距离地铁较远', '3', 'img/45.jpg', '1500.00', null);

-- ----------------------------
-- Table structure for apt_type
-- ----------------------------
DROP TABLE IF EXISTS `apt_type`;
CREATE TABLE `apt_type` (
  `type_id` int(11) NOT NULL,
  `decoration` tinyint(1) DEFAULT NULL,
  `air-conditioner` tinyint(1) DEFAULT NULL,
  `WIFI` tinyint(1) DEFAULT NULL,
  `TV` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of apt_type
-- ----------------------------
INSERT INTO `apt_type` VALUES ('1', '1', '1', '1', '1');
INSERT INTO `apt_type` VALUES ('2', '1', '1', '1', '0');
INSERT INTO `apt_type` VALUES ('3', '1', '1', '0', '1');
INSERT INTO `apt_type` VALUES ('4', '1', '1', '0', '0');
INSERT INTO `apt_type` VALUES ('5', '1', '0', '1', '1');
INSERT INTO `apt_type` VALUES ('6', '1', '0', '1', '0');
INSERT INTO `apt_type` VALUES ('7', '1', '0', '0', '1');
INSERT INTO `apt_type` VALUES ('8', '1', '0', '0', '0');
INSERT INTO `apt_type` VALUES ('9', '0', '1', '1', '1');
INSERT INTO `apt_type` VALUES ('10', '0', '1', '1', '0');
INSERT INTO `apt_type` VALUES ('11', '0', '1', '0', '1');
INSERT INTO `apt_type` VALUES ('12', '0', '1', '0', '0');
INSERT INTO `apt_type` VALUES ('13', '0', '0', '1', '1');
INSERT INTO `apt_type` VALUES ('14', '0', '0', '1', '0');
INSERT INTO `apt_type` VALUES ('15', '0', '0', '0', '1');
INSERT INTO `apt_type` VALUES ('16', '0', '0', '0', '0');

-- ----------------------------
-- Table structure for booking
-- ----------------------------
DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `apt_id` int(11) NOT NULL,
  `guest_id` int(11) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `submit_time` varchar(255) DEFAULT NULL,
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

-- ----------------------------
-- Table structure for guest
-- ----------------------------
DROP TABLE IF EXISTS `guest`;
CREATE TABLE `guest` (
  `guest_id` int(11) NOT NULL AUTO_INCREMENT,
  `guest_username` varchar(255) CHARACTER SET utf8 NOT NULL,
  `guest_pw` varchar(255) CHARACTER SET utf8 NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `guest_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `job` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `wechat` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `guest_phone` varchar(255) DEFAULT NULL,
  `graduate_school` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `major` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `feature` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `apply_status` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`guest_id`),
  KEY `gender_code` (`gender`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of guest
-- ----------------------------
INSERT INTO `guest` VALUES ('1', 'mei', 'mei', '1', 'mei', '程序员', '123', '151', 'ECNU', 'CS', null, '0');
INSERT INTO `guest` VALUES ('2', 'localhost', '123456', '1', '李四', '程序员', 'lisi1998', '15154111656', '华东师范大学', '计算机', '读书 时尚 ', '0');

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL,
  `question_detail` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `answer_detail` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of question
-- ----------------------------
