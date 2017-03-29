/*
Navicat MySQL Data Transfer

Source Server         : 192.168.1.103_3306
Source Server Version : 50547
Source Host           : 192.168.1.103:3306
Source Database       : real_time_pm

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2016-08-26 01:30:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for real_time_pm
-- ----------------------------
DROP TABLE IF EXISTS `real_time_pm`;
CREATE TABLE `real_time_pm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_time` datetime NOT NULL COMMENT '运行时间',
  `real_time` datetime NOT NULL COMMENT '实时数据的时间',
  `city` varchar(255) NOT NULL COMMENT '城市',
  `monitor_station` varchar(255) NOT NULL COMMENT '监测站点',
  `AQI` int(255) DEFAULT NULL,
  `lev` varchar(255) DEFAULT NULL COMMENT '空气质量指数级别',
  `top_pm` varchar(255) DEFAULT NULL COMMENT '首要污染物',
  `pm25` varchar(200) DEFAULT NULL,
  `pm10` varchar(255) DEFAULT NULL,
  `CO` varchar(255) DEFAULT NULL,
  `NO2` varchar(255) DEFAULT NULL,
  `O3_1h` varchar(255) DEFAULT NULL COMMENT 'O3一小时平均',
  `O3_8h` varchar(255) DEFAULT NULL COMMENT 'O3八小时平均',
  `SO2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
