/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : roberto11

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-17 15:57:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `address_id` int(11) NOT NULL,
  `address_name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `distinct_id` int(11) unsigned zerofill NOT NULL,
  `province_id` int(11) unsigned zerofill NOT NULL,
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
  `agent_id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_username` varchar(255) NOT NULL,
  `agent_pw` varchar(255) NOT NULL,
  `agent_name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `agent_phone` varchar(255) NOT NULL,
  `agent_company` varchar(255) CHARACTER SET utf8 NOT NULL,
  `agent_wechat` varchar(255) DEFAULT NULL,
  KEY `agent_id` (`agent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of agent
-- ----------------------------
INSERT INTO `agent` VALUES ('1', 'tianzhiguo', 'tianzhiguo', '田志国', '18798234456', '紫梧桐(上海)公寓管理有限公司', 'tianzhiguo187');
INSERT INTO `agent` VALUES ('2', 'agent1', '123456', '李四', '15154111656', '盛大地产', 'lisi123');

-- ----------------------------
-- Table structure for apartment
-- ----------------------------
DROP TABLE IF EXISTS `apartment`;
CREATE TABLE `apartment` (
  `apt_id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `building_id` int(11) NOT NULL,
  `apt_name` varchar(255) NOT NULL,
  `bathroom_count` int(10) NOT NULL,
  `bedroom_count` int(10) NOT NULL,
  `room_area` int(3) NOT NULL,
  `transport` varchar(255) NOT NULL,
  `max_people_number` int(2) NOT NULL,
  `pic_url` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `direction` varchar(255) NOT NULL,
  PRIMARY KEY (`apt_id`),
  KEY `building_id` (`building_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `apartment_ibfk_3` FOREIGN KEY (`agent_id`) REFERENCES `agent` (`agent_id`),
  CONSTRAINT `apartment_ibfk_4` FOREIGN KEY (`building_id`) REFERENCES `building` (`building_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apartment
-- ----------------------------
INSERT INTO `apartment` VALUES ('1', '1', '1', '温馨小屋', '2', '3', '100', '靠近地铁三号线', '3', '/static/img/bg-img/47.jpg', '3200.00', '朝南');
INSERT INTO `apartment` VALUES ('2', '1', '2', '豪华套房', '3', '5', '150', '靠近地铁一号线', '5', '/static/img/bg-img/46.jpg/', '5000.00', '朝南');
INSERT INTO `apartment` VALUES ('3', '1', '3', '奋斗者家园', '1', '2', '80', '靠近公交960，距离地铁较远', '3', '/static/img/bg-img/45.jpg', '1500.00', '朝南');

-- ----------------------------
-- Table structure for booking
-- ----------------------------
DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `apt_id` int(11) NOT NULL,
  `guest_id` int(11) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `submit_time` date DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `status_id` (`status_id`),
  KEY `guest_id` (`guest_id`),
  KEY `apt_id` (`apt_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`guest_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`apt_id`) REFERENCES `apartment` (`apt_id`),
  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `booking_status` (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of booking
-- ----------------------------
INSERT INTO `booking` VALUES ('1', '1', '2', '1', '2019-06-15');
INSERT INTO `booking` VALUES ('2', '1', '2', '0', '2019-06-15');
INSERT INTO `booking` VALUES ('3', '1', '2', '0', '2019-06-15');
INSERT INTO `booking` VALUES ('4', '1', '2', '0', '2019-06-15');
INSERT INTO `booking` VALUES ('5', '2', '2', '0', '2019-06-17');
INSERT INTO `booking` VALUES ('6', '2', '2', '0', '2019-06-17');

-- ----------------------------
-- Table structure for booking_status
-- ----------------------------
DROP TABLE IF EXISTS `booking_status`;
CREATE TABLE `booking_status` (
  `status_id` int(11) NOT NULL,
  `status_discribe` varchar(255) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of booking_status
-- ----------------------------
INSERT INTO `booking_status` VALUES ('0', '未完成');
INSERT INTO `booking_status` VALUES ('1', '已完成');

-- ----------------------------
-- Table structure for building
-- ----------------------------
DROP TABLE IF EXISTS `building`;
CREATE TABLE `building` (
  `building_id` int(11) NOT NULL AUTO_INCREMENT,
  `building_name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `address_id` int(11) NOT NULL,
  `building_manager` varchar(255) CHARACTER SET utf8 NOT NULL,
  `building_phone` varchar(20) NOT NULL,
  `other_details` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`building_id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `building_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `address` (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of building
-- ----------------------------
INSERT INTO `building` VALUES ('1', '龙盘山庄', '2', '李五', '123', '123123123');
INSERT INTO `building` VALUES ('2', '明珠小区', '3', '王二', '123', '456456456');
INSERT INTO `building` VALUES ('3', '华师二村', '3', '赵三', '123', '786785685');
INSERT INTO `building` VALUES ('4', '田楼', '2', '韦正', '110', '无');

-- ----------------------------
-- Table structure for guest
-- ----------------------------
DROP TABLE IF EXISTS `guest`;
CREATE TABLE `guest` (
  `guest_id` int(11) NOT NULL AUTO_INCREMENT,
  `guest_username` varchar(255) CHARACTER SET utf8 NOT NULL,
  `guest_pw` varchar(255) CHARACTER SET utf8 NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8 NOT NULL,
  `guest_name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `job` varchar(255) CHARACTER SET utf8 NOT NULL,
  `wechat` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `guest_phone` varchar(255) NOT NULL,
  `graduate_school` varchar(255) CHARACTER SET utf8 NOT NULL,
  `major` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `feature` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `apply_status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`guest_id`),
  KEY `gender_code` (`gender`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of guest
-- ----------------------------
INSERT INTO `guest` VALUES ('1', 'mei', 'mei', '1', 'mei', '程序员', '123', '151', 'ECNU', 'CS', null, '1');
INSERT INTO `guest` VALUES ('2', 'localhost', '123456', '1', '李四', '程序员', 'lisi1998', '15154111656', '华东师范大学', '计算机', '读书 时尚 ', '0');

-- ----------------------------
-- View structure for apartment_details
-- ----------------------------
DROP VIEW IF EXISTS `apartment_details`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `apartment_details` AS select `apartment`.`apt_id` AS `apt_id`,`apartment`.`bathroom_count` AS `bathroom_count`,`apartment`.`bedroom_count` AS `bedroom_count`,`apartment`.`room_area` AS `room_area`,`apartment`.`transport` AS `transport`,`apartment`.`max_people_number` AS `max_people_number`,`building`.`building_name` AS `building_name`,`a`.`address_name` AS `district`,`b`.`address_name` AS `city`,`apartment`.`price` AS `price`,`c`.`address_name` AS `province`,`apartment`.`apt_name` AS `apt_name`,`apartment`.`pic_url` AS `pic_url`,`building`.`building_manager` AS `building_manager`,`building`.`building_phone` AS `building_phone`,`building`.`other_details` AS `other_details`,`apartment`.`direction` AS `direction`,`agent`.`agent_name` AS `agent_name`,`agent`.`agent_company` AS `agent_company`,`agent`.`agent_phone` AS `agent_phone`,`agent`.`agent_username` AS `agent_username` from (((((`apartment` join `building` on((`apartment`.`building_id` = `building`.`building_id`))) join `address` `a` on((`building`.`address_id` = `a`.`address_id`))) join `address` `b` on((`b`.`address_id` = `a`.`distinct_id`))) join `address` `c` on((`b`.`province_id` = `c`.`address_id`))) join `agent` on((`apartment`.`agent_id` = `agent`.`agent_id`))) ;

-- ----------------------------
-- View structure for order_detail
-- ----------------------------
DROP VIEW IF EXISTS `order_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `order_detail` AS select `booking`.`guest_id` AS `guest_id`,`booking`.`apt_id` AS `apt_id`,`booking`.`booking_id` AS `booking_id`,`booking`.`submit_time` AS `submit_time`,`booking_status`.`status_discribe` AS `status_discribe`,`apartment_details`.`bathroom_count` AS `bathroom_count`,`apartment_details`.`bedroom_count` AS `bedroom_count`,`apartment_details`.`room_area` AS `room_area`,`apartment_details`.`transport` AS `transport`,`apartment_details`.`max_people_number` AS `max_people_number`,`apartment_details`.`building_name` AS `building_name`,`apartment_details`.`district` AS `district`,`apartment_details`.`city` AS `city`,`apartment_details`.`price` AS `price`,`apartment_details`.`province` AS `province`,`apartment_details`.`apt_name` AS `apt_name`,`apartment_details`.`pic_url` AS `pic_url`,`apartment_details`.`building_manager` AS `building_manager`,`apartment_details`.`building_phone` AS `building_phone`,`apartment_details`.`other_details` AS `other_details`,`apartment_details`.`direction` AS `direction`,`apartment_details`.`agent_name` AS `agent_name`,`apartment_details`.`agent_company` AS `agent_company`,`apartment_details`.`agent_phone` AS `agent_phone`,`apartment_details`.`agent_username` AS `agent_username`,`guest`.`guest_username` AS `guest_username`,`guest`.`gender` AS `gender`,`guest`.`guest_name` AS `guest_name`,`guest`.`job` AS `job`,`guest`.`wechat` AS `wechat`,`guest`.`guest_phone` AS `guest_phone`,`guest`.`graduate_school` AS `graduate_school`,`guest`.`major` AS `major`,`guest`.`feature` AS `feature`,`guest`.`apply_status` AS `apply_status` from (((`booking` join `booking_status` on((`booking`.`status_id` = `booking_status`.`status_id`))) join `apartment_details` on((`booking`.`apt_id` = `apartment_details`.`apt_id`))) join `guest` on((`booking`.`guest_id` = `guest`.`guest_id`))) ;
DROP TRIGGER IF EXISTS `123`;
DELIMITER ;;
CREATE TRIGGER `123` BEFORE INSERT ON `apartment` FOR EACH ROW update apartment set max_people_number = max_people_number -1 where apt_id = new.apt_id
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `book`;
DELIMITER ;;
CREATE TRIGGER `book` AFTER INSERT ON `booking` FOR EACH ROW update apartment set max_people_number = max_people_number -1 where apt_id = new.apt_id
;;
DELIMITER ;
