/*
Navicat MySQL Data Transfer

Source Server         : aliyun-mysql
Source Server Version : 50546
Source Host           : 123.57.61.63:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50546
File Encoding         : 65001

Date: 2016-06-28 22:05:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for stu
-- ----------------------------
DROP TABLE IF EXISTS `stu`;
CREATE TABLE `stu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stu
-- ----------------------------
INSERT INTO `stu` VALUES ('1', 'zhangsan', '20');
INSERT INTO `stu` VALUES ('2', 'lisi', '21');
INSERT INTO `stu` VALUES ('3', 'xiaoming', '18');
