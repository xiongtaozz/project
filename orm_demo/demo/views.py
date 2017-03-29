# coding: utf-8
from django.shortcuts import render
from django.db.models import *
from demo.models import *
# import requests

# Create your views here.


def query(request):
    # -- 1、 查询Student表中的所有记录的Sname、Ssex和classno列。
    # SELECT sname,ssex,class FROM student;

    # -- 2、 查询教师所有的单位即不重复的Depart列。
    # SELECT DISTINCT(depart) FROM teacher;

    # -- 3、 查询Student表的所有记录。
    # SELECT * FROM student;

    # -- 4、 查询Score表中成绩在60到80之间的所有记录。
    # SELECT * FROM score WHERE grade BETWEEN 60 AND 80;

    # -- 5、 查询Score表中成绩为85，86或88的记录。
    # SELECT * FROM score WHERE grade IN (85,86,88);

    # -- 6、 查询Student表中“95031”班或性别为“女”的同学记录。
    # SELECT * FROM student WHERE class='95031' OR ssex='女';

    # -- 7、 以Class降序查询Student表的所有记录。
    # SELECT * FROM student ORDER BY class DESC;

    # -- 8、 以Cno升序、grade降序查询Score表的所有记录。
    # SELECT * FROM score ORDER BY cno ASC,grade DESC;

    # -- 9、 查询“95031”班的学生人数。
    # SELECT COUNT(*) AS total_sum FROM student GROUP BY class HAVING class='95031';

    # -- 10、查询Score表中的最高分的学生学号和课程号。
    # SELECT sno,cno FROM score ORDER BY grade DESC LIMIT 1;

    # -- 11、查询‘3-105’号课程的平均分。
    # SELECT ROUND(AVG(grade),2) AS avg_grade FROM score
    # GROUP BY cno HAVING cno='3-105';

    # -- 12、查询Score表中至少有5名学生选修的并以3开头的课程的平均分数。
    # SELECT ROUND(AVG(grade),2) AS avg_grade FROM score
    # GROUP BY cno HAVING COUNT(sno)>=5 AND cno LIKE '3%';

    # # -- 13、查询最低分大于70，最高分小于90的Sno列。
    # SELECT sno FROM score GROUP BY sno HAVING MAX(grade)<90 AND MIN(grade)>70;

    # -- 14、查询所有学生的Sname、Cno和grade列。
    # SELECT s.sname,c.cno,c.grade FROM student AS s
    # JOIN score AS c ON s.sno=c.sno;

    # -- 15、查询所有学生的Sno、Cname和grade列。 # Sno(x)
    # SELECT c.sno,l.cname,c.grade FROM score AS c
    # JOIN lesson AS l ON c.cno=l.cno;

    # -- 16、查询所有学生的Sname、Cname和grade列。
    # SELECT s.sname,l.cname,c.grade FROM student AS s
    # JOIN score AS c ON s.sno=c.sno
    # JOIN lesson AS l ON c.cno=l.cno;

    # 17、查询“95033”班所选课程的平均分。
    # select c.cname,avg(defree)
    # from score sc ,course c,student st
    # where c.cno = sc.cno
    # and  sc.sno = st.sno
    # and st.class='95033'
    # group by sc.cno

    # -- 18、假设使用如下命令建立了一个grade表：
    # CREATE TABLE grade(
    # low DOUBLE(4,1),
    # upp DOUBLE(4,1),
    # rank CHAR(1)
    # );
    # INSERT INTO grade VALUES(90,100,'A'),
    # (80,89,'B'),
    # (70,79,'C'),
    # (60,69,'D'),
    # (0,59,'E');
    # COMMIT;
    #
    # -- 19、查询选修“3-105”课程的成绩高于“9”号同学成绩的所有同学的记录。
    # select * from demo_student where sno in (
    # select sno from
    # demo_score sc
    # where sc.cno_id='3-105'
    # and  sc.grade >(select grade from demo_score
    # where sno_id = 9
    # and cno_id='3-105'))

    # -- 20、查询score中选学一门以上课程的同学中分数为非最高分成绩的记录。
    # select * from demo_score a
    # where sno_id in (select sno_id from demo_score group by sno_id having COUNT(*)>1)
    # and
    # (grade not in (select MAX(grade) from demo_score b where a.cno_id=b.cno_id group by cno_id))

    # -- 21、查询成绩高于学号为“109”、课程号为“3-105”的成绩的所有记录。
    # SELECT * FROM score WHERE grade>
    # (SELECT MAX(grade) FROM score GROUP BY sno HAVING sno=109)
    # AND cno='3-105';
    # -- 22、查询和学号为108的同学同年出生的所有学生的Sno、Sname和Sbirthday列。
    # SELECT sno,sname,sbirthday FROM student WHERE YEAR(sbirthday)=
    # (SELECT YEAR(sbirthday) FROM student WHERE sno=108);
    # -- 23、查询“张旭“教师任课的学生成绩。
    # SELECT grade FROM score AS s
    # JOIN lesson AS l ON s.cno=l.cno
    # JOIN teacher AS t ON l.tno=t.tno
    # WHERE t.tname='张旭';
    # -- 24、查询选修某课程的同学人数多于5人的教师姓名。
    # -- 第一种，子查询方式查询：
    # SELECT tname FROM teacher WHERE tno IN
    # (SELECT tno FROM lesson WHERE cno IN
    # (SELECT cno FROM score GROUP BY cno HAVING COUNT(*)>5));
    # -- 第二种，表连接方式查询：
    # SELECT tname FROM teacher AS t
    # JOIN lesson AS l ON t.tno=l.tno
    # JOIN score AS s ON s.cno=l.cno
    # GROUP BY s.cno HAVING COUNT(s.sno)>5;
    # -- 25、查询95033班和95031班全体学生的记录。
    # SELECT s.sname,c.grade,c.cno FROM score AS c
    # JOIN student AS s ON c.sno=s.sno
    # WHERE s.class IN ('95033','95031');
    # -- 26、查询存在有85分以上成绩的课程Cno.
    # SELECT cno FROM score GROUP BY cno HAVING MAX(grade)>85;
    # -- 27、查询出“计算机系“教师所教课程的成绩表。
    # SELECT c.sno,c.grade,c.cno,l.cname FROM score AS c
    # JOIN lesson AS l ON c.cno=l.cno
    # JOIN teacher AS t ON t.tno=l.tno
    # WHERE t.depart='计算机系';
    # -- 28、查询“计算机系”与“电子工程系“不同职称的教师的Tname和Prof。
    # -- 表结构不正确
    # -- 29、查询选修编号为“3-105“课程且成绩至少高于选修编号为“3-245”的同学的
    # --     Cno、Sno和grade,并按grade从高到低次序排序。
    # -- 没理解题目意思
    # -- 30、查询选修编号为“3-105”且成绩高于选修编号为“3-245”课程的同学的
    # --     Cno、Sno和grade.
    # -- 没理解题目意思
    # -- 31、查询所有教师和同学的name、sex和birthday.
    # SELECT sname AS name,ssex AS sex,sbirthday AS birthday FROM student
    # UNION ALL
    # SELECT tname,tsex,tbirthday FROM teacher;
    # -- 32、查询所有“女”教师和“女”同学的name、sex和birthday.
    # SELECT sname AS name,ssex AS sex,sbirthday AS birthday FROM student WHERE ssex='女'
    # UNION ALL
    # SELECT tname,tsex,tbirthday FROM teacher WHERE tsex='女';
    # -- 33、查询成绩比该课程平均成绩低的同学的成绩表。
    # SELECT grade,sno FROM score GROUP BY cno
    # HAVING grade<AVG(grade);
    # -- 34、查询所有任课教师的Tname和Depart.
    # SELECT tname,depart FROM teacher WHERE tno IN
    # (SELECT tno FROM lesson);
    # -- 35 查询所有未讲课的教师的Tname和Depart.
    # SELECT tname,depart FROM teacher WHERE tno NOT IN
    # (SELECT tno FROM lesson);
    # -- 36、查询至少有2名男生的班号。
    # SELECT class FROM student GROUP BY ssex
    # HAVING COUNT(*)>2 AND ssex='男';
    # -- 37、查询Student表中不姓“王”的同学记录。
    # SELECT * FROM student WHERE SUBSTRING(sname,1,1)!='王';
    # -- 38、查询Student表中每个学生的姓名和年龄。
    # SELECT sname,(YEAR(CURRENT_DATE())-YEAR(sbirthday)) AS age FROM student;
    # -- 39、查询Student表中最大和最小的Sbirthday日期值。
    # SELECT MAX(sbirthday),MIN(sbirthday) FROM student;
    # -- 40、以班号和年龄从大到小的顺序查询Student表中的全部记录。
    # SELECT * FROM student ORDER BY class DESC,sbirthday ASC;
    # -- 41、查询“男”教师及其所上的课程。
    # SELECT l.cname,t.tname FROM lesson AS l
    # JOIN teacher AS t ON l.tno=t.tno
    # WHERE t.tsex='男';
    # -- 42、查询最高分同学的Sno、Cno和grade列。
    # SELECT sno,cno,grade FROM score WHERE grade=
    # (SELECT MAX(grade) FROM score);
    # -- 43、查询和“李军”同性别的所有同学的Sname.
    # SELECT sname FROM student WHERE ssex=
    # (SELECT ssex FROM student WHERE sname='李军');
    # -- 44、查询和“李军”同性别并同班的同学Sname.
    # SELECT sname FROM student WHERE ssex=
    # (SELECT ssex FROM student WHERE sname='李军')
    # AND class=(SELECT class FROM student WHERE sname='李军');
    # -- 45、查询所有选修“计算机导论”课程的“男”同学的成绩表
    # SELECT s.sname,c.cno,l.cname,c.grade FROM student AS s
    # JOIN score AS c ON s.sno=c.sno
    # JOIN lesson AS l ON l.cno=c.cno
    # WHERE l.cname='计算机导论' AND s.ssex='男';
    return render(request, 'query.html', locals())