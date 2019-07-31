/*
Navicat MySQL Data Transfer

Source Server         : focus1
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : roberto4

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-15 17:22:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for agent
-- ----------------------------
DROP TABLE IF EXISTS `agent`;
CREATE TABLE `agent` (
  `agent_id` int(11) DEFAULT NULL,
  `agent_username` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `agent_pw` varchar(255) DEFAULT NULL,
  `agent_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `agent_phone` varchar(255) DEFAULT NULL,
  `agent_company` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `agent_wechat` varchar(255) DEFAULT NULL,
  KEY `agent_id` (`agent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of agent
-- ----------------------------
INSERT INTO `agent` VALUES ('1', 'tianzhiguo', 'tianzhiguo', '田志国', '18798234456', '紫梧桐(上海)公寓管理有限公司', 'tianzhiguo187');
