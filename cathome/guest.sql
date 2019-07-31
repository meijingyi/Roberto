/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:44
*/

SET FOREIGN_KEY_CHECKS=0;

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
  `birthday` date DEFAULT NULL,
  `job` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `wechat` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `guest_phone` int(255) DEFAULT NULL,
  `graduate_school` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `major` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `reference` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `refer_phone` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `apply_status` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`guest_id`),
  KEY `gender_code` (`gender`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of guest
-- ----------------------------
INSERT INTO `guest` VALUES ('1', 'mei', 'mei', '1', 'mei', '1998-01-12', '程序员', '123', '151', 'ECNU', 'CS', null, null, '0');
