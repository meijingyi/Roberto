/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:17
*/

SET FOREIGN_KEY_CHECKS=0;

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
