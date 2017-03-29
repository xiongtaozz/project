/*
Navicat MySQL Data Transfer

Source Server         : Mysql
Source Server Version : 50536
Source Host           : localhost:3306
Source Database       : orm_mysql

Target Server Type    : MYSQL
Target Server Version : 50536
File Encoding         : 65001

Date: 2016-07-27 16:42:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 学生', '7', 'add_student');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 学生', '7', 'change_student');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 学生', '7', 'delete_student');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 老师', '8', 'add_teacher');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 老师', '8', 'change_teacher');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 老师', '8', 'delete_teacher');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 课程', '9', 'add_course');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 课程', '9', 'change_course');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 课程', '9', 'delete_course');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 课程选修', '10', 'add_optionalcourse');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 课程选修', '10', 'change_optionalcourse');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 课程选修', '10', 'delete_optionalcourse');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 成绩', '11', 'add_score');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 成绩', '11', 'change_score');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 成绩', '11', 'delete_score');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$N3h3VISR2YiH$Apd4svKNF3LiyfBYmuy3hVH2ixZU/9vsf15EzwXmNVs=', null, '1', 'admin', '', '', 'admin@qq.com', '1', '1', '2016-04-12 12:56:43');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `demo_course`
-- ----------------------------
DROP TABLE IF EXISTS `demo_course`;
CREATE TABLE `demo_course` (
  `cno` varchar(5) NOT NULL,
  `cname` varchar(20) NOT NULL,
  `tno_id` int(11) NOT NULL,
  PRIMARY KEY (`cno`),
  KEY `demo_course_3e35c197` (`tno_id`),
  CONSTRAINT `demo_course_tno_id_187c4ad0_fk_demo_teacher_id` FOREIGN KEY (`tno_id`) REFERENCES `demo_teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of demo_course
-- ----------------------------
INSERT INTO `demo_course` VALUES ('3-105', '计算机导论', '1');
INSERT INTO `demo_course` VALUES ('3-106', '大学英语', '3');
INSERT INTO `demo_course` VALUES ('3-107', '大学物理', '6');
INSERT INTO `demo_course` VALUES ('3-108', '超级化学', '5');
INSERT INTO `demo_course` VALUES ('3-109', '大学语文', '4');
INSERT INTO `demo_course` VALUES ('3-241', 'PCB印刷', '9');
INSERT INTO `demo_course` VALUES ('3-242', '计算机基础', '10');
INSERT INTO `demo_course` VALUES ('3-243', '音乐', '8');
INSERT INTO `demo_course` VALUES ('3-244', '美术鉴赏', '7');
INSERT INTO `demo_course` VALUES ('3-245', '电子工程课', '2');

-- ----------------------------
-- Table structure for `demo_optionalcourse`
-- ----------------------------
DROP TABLE IF EXISTS `demo_optionalcourse`;
CREATE TABLE `demo_optionalcourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_pub` datetime NOT NULL,
  `cno_id` varchar(5) NOT NULL,
  `sno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demo_optionalcourse_cno_id_52fd8699_fk_demo_course_cno` (`cno_id`),
  KEY `demo_optionalcourse_83fa7413` (`sno_id`),
  CONSTRAINT `demo_optionalcourse_cno_id_52fd8699_fk_demo_course_cno` FOREIGN KEY (`cno_id`) REFERENCES `demo_course` (`cno`),
  CONSTRAINT `demo_optionalcourse_sno_id_56d0c9e9_fk_demo_student_id` FOREIGN KEY (`sno_id`) REFERENCES `demo_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of demo_optionalcourse
-- ----------------------------
INSERT INTO `demo_optionalcourse` VALUES ('1', '2016-04-12 12:56:17', '3-105', '1');
INSERT INTO `demo_optionalcourse` VALUES ('2', '2016-04-12 12:56:17', '3-243', '1');
INSERT INTO `demo_optionalcourse` VALUES ('3', '2016-04-12 12:56:17', '3-106', '1');
INSERT INTO `demo_optionalcourse` VALUES ('4', '2016-04-12 12:56:18', '3-107', '1');
INSERT INTO `demo_optionalcourse` VALUES ('5', '2016-04-12 12:56:18', '3-105', '2');
INSERT INTO `demo_optionalcourse` VALUES ('6', '2016-04-12 12:56:18', '3-105', '3');
INSERT INTO `demo_optionalcourse` VALUES ('7', '2016-04-12 12:56:18', '3-105', '4');
INSERT INTO `demo_optionalcourse` VALUES ('8', '2016-04-12 12:56:18', '3-105', '5');
INSERT INTO `demo_optionalcourse` VALUES ('9', '2016-04-12 12:56:18', '3-105', '6');
INSERT INTO `demo_optionalcourse` VALUES ('10', '2016-04-12 12:56:18', '3-105', '7');
INSERT INTO `demo_optionalcourse` VALUES ('11', '2016-04-12 12:56:18', '3-105', '8');
INSERT INTO `demo_optionalcourse` VALUES ('12', '2016-04-12 12:56:18', '3-105', '9');
INSERT INTO `demo_optionalcourse` VALUES ('13', '2016-04-12 12:56:18', '3-105', '10');

-- ----------------------------
-- Table structure for `demo_score`
-- ----------------------------
DROP TABLE IF EXISTS `demo_score`;
CREATE TABLE `demo_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` decimal(3,1) NOT NULL,
  `cno_id` varchar(5) NOT NULL,
  `sno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demo_score_cno_id_268225cd_fk_demo_course_cno` (`cno_id`),
  KEY `demo_score_83fa7413` (`sno_id`),
  CONSTRAINT `demo_score_cno_id_268225cd_fk_demo_course_cno` FOREIGN KEY (`cno_id`) REFERENCES `demo_course` (`cno`),
  CONSTRAINT `demo_score_sno_id_5fedf9e3_fk_demo_student_id` FOREIGN KEY (`sno_id`) REFERENCES `demo_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of demo_score
-- ----------------------------
INSERT INTO `demo_score` VALUES ('1', '99.0', '3-105', '1');
INSERT INTO `demo_score` VALUES ('2', '75.0', '3-106', '1');
INSERT INTO `demo_score` VALUES ('3', '85.5', '3-245', '1');
INSERT INTO `demo_score` VALUES ('4', '75.0', '3-105', '2');
INSERT INTO `demo_score` VALUES ('5', '85.0', '3-244', '2');
INSERT INTO `demo_score` VALUES ('6', '95.5', '3-243', '2');
INSERT INTO `demo_score` VALUES ('7', '60.5', '3-107', '3');
INSERT INTO `demo_score` VALUES ('8', '65.5', '3-108', '3');
INSERT INTO `demo_score` VALUES ('9', '60.5', '3-109', '3');
INSERT INTO `demo_score` VALUES ('10', '88.5', '3-105', '4');
INSERT INTO `demo_score` VALUES ('11', '90.5', '3-107', '4');
INSERT INTO `demo_score` VALUES ('12', '95.5', '3-109', '4');
INSERT INTO `demo_score` VALUES ('13', '78.0', '3-105', '5');
INSERT INTO `demo_score` VALUES ('14', '66.5', '3-245', '5');
INSERT INTO `demo_score` VALUES ('15', '93.0', '3-108', '5');
INSERT INTO `demo_score` VALUES ('16', '81.0', '3-242', '6');
INSERT INTO `demo_score` VALUES ('17', '77.5', '3-243', '6');
INSERT INTO `demo_score` VALUES ('18', '90.0', '3-241', '6');
INSERT INTO `demo_score` VALUES ('19', '67.0', '3-242', '7');
INSERT INTO `demo_score` VALUES ('20', '83.0', '3-241', '7');
INSERT INTO `demo_score` VALUES ('21', '71.0', '3-245', '7');
INSERT INTO `demo_score` VALUES ('22', '90.0', '3-105', '8');
INSERT INTO `demo_score` VALUES ('23', '96.0', '3-108', '8');
INSERT INTO `demo_score` VALUES ('24', '99.0', '3-106', '8');
INSERT INTO `demo_score` VALUES ('25', '80.0', '3-107', '9');
INSERT INTO `demo_score` VALUES ('26', '70.0', '3-245', '9');
INSERT INTO `demo_score` VALUES ('27', '60.0', '3-244', '9');
INSERT INTO `demo_score` VALUES ('28', '79.0', '3-105', '9');
INSERT INTO `demo_score` VALUES ('29', '66.0', '3-244', '10');
INSERT INTO `demo_score` VALUES ('30', '76.0', '3-106', '10');
INSERT INTO `demo_score` VALUES ('31', '86.0', '3-106', '10');
INSERT INTO `demo_score` VALUES ('32', '95.0', '3-244', '11');
INSERT INTO `demo_score` VALUES ('33', '86.0', '3-107', '11');
INSERT INTO `demo_score` VALUES ('34', '96.0', '3-108', '11');
INSERT INTO `demo_score` VALUES ('35', '76.0', '3-243', '12');
INSERT INTO `demo_score` VALUES ('36', '66.0', '3-241', '12');
INSERT INTO `demo_score` VALUES ('37', '56.0', '3-106', '12');

-- ----------------------------
-- Table structure for `demo_student`
-- ----------------------------
DROP TABLE IF EXISTS `demo_student`;
CREATE TABLE `demo_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) NOT NULL,
  `ssex` varchar(4) NOT NULL,
  `sbirthday` date DEFAULT NULL,
  `classno` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of demo_student
-- ----------------------------
INSERT INTO `demo_student` VALUES ('1', '韩梅梅', '女', '1990-06-11', '95033');
INSERT INTO `demo_student` VALUES ('2', '张全蛋', '男', '1995-08-30', '95034');
INSERT INTO `demo_student` VALUES ('3', '火雷蛋', '男', '1993-10-01', '95035');
INSERT INTO `demo_student` VALUES ('4', '呵呵哒', '女', '1996-01-05', '95033');
INSERT INTO `demo_student` VALUES ('5', '小笼包', '女', '1992-12-12', '95033');
INSERT INTO `demo_student` VALUES ('6', '李狗蛋', '男', '1997-11-11', '95036');
INSERT INTO `demo_student` VALUES ('7', '唐马儒', '男', '1999-05-30', '95035');
INSERT INTO `demo_student` VALUES ('8', '李小花', '女', '1991-11-29', '95033');
INSERT INTO `demo_student` VALUES ('9', '赵铁柱', '男', '1999-09-05', '95034');
INSERT INTO `demo_student` VALUES ('10', '王尼玛', '男', '1979-10-05', '95031');
INSERT INTO `demo_student` VALUES ('11', 'DSB', '男', '1989-10-05', '95031');
INSERT INTO `demo_student` VALUES ('12', '李军', '男', '1988-11-05', '95034');

-- ----------------------------
-- Table structure for `demo_teacher`
-- ----------------------------
DROP TABLE IF EXISTS `demo_teacher`;
CREATE TABLE `demo_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(20) NOT NULL,
  `tsex` varchar(4) NOT NULL,
  `tbirthday` date DEFAULT NULL,
  `depart` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of demo_teacher
-- ----------------------------
INSERT INTO `demo_teacher` VALUES ('1', '王思聪', '男', '1985-11-11', '计算机系');
INSERT INTO `demo_teacher` VALUES ('2', '张旭', '男', '1989-01-11', '电子工程系');
INSERT INTO `demo_teacher` VALUES ('3', '李旭', '女', '1980-12-11', '英语系');
INSERT INTO `demo_teacher` VALUES ('4', '陈旭', '女', '1985-09-25', '中文系');
INSERT INTO `demo_teacher` VALUES ('5', '王旭', '男', '1975-03-13', '化学系');
INSERT INTO `demo_teacher` VALUES ('6', '毛旭', '男', '1979-07-29', '物理系');
INSERT INTO `demo_teacher` VALUES ('7', '方旭', '女', '1988-10-11', '美术系');
INSERT INTO `demo_teacher` VALUES ('8', '桑旭', '男', '1990-06-19', '音乐系');
INSERT INTO `demo_teacher` VALUES ('9', '臧旭', '男', '1988-12-12', '电子工程系');
INSERT INTO `demo_teacher` VALUES ('10', '章旭', '女', '1990-08-08', '计算机系');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'demo', 'course');
INSERT INTO `django_content_type` VALUES ('10', 'demo', 'optionalcourse');
INSERT INTO `django_content_type` VALUES ('11', 'demo', 'score');
INSERT INTO `django_content_type` VALUES ('7', 'demo', 'student');
INSERT INTO `django_content_type` VALUES ('8', 'demo', 'teacher');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-04-12 12:56:06');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-04-12 12:56:09');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-04-12 12:56:09');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2016-04-12 12:56:10');
INSERT INTO `django_migrations` VALUES ('10', 'demo', '0001_initial', '2016-04-12 12:56:14');
INSERT INTO `django_migrations` VALUES ('11', 'sessions', '0001_initial', '2016-04-12 12:56:14');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
