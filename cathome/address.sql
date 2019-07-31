/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : cathome

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-09 20:18:00
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
