# coding:utf-8
# 必备,缺省,不定长(元组),字典

# 1 关于函数参数
# def add(*args, **kwargs):
#     pass
#
# add(1, 2, 3, 4, 5, a=1, b=2, c=3)

'''

    markslist: 学生名称(name {str}),学生成绩(mark{int})
    grade:学生等级表
'''


# def get_graded_students(markslist, grade):
#     grade_to_minmax = {}  # 学生成绩等级评判
#     if grade == 'A':
#         pass
#     if grade == 'B':
#         pass
#     if grade == 'C':
#         pass
#     if grade == 'D':
#         pass
#     if grade == 'F':
#         pass
#     for (name,mark) in markslist:
#         pass

class cls_mark(object):

    def __init__(self):
        self.grade_to_minmax= {'A': (80, 100), 'B': (70, 79), 'C': (60, 69), 'D': (50, 59), 'F': (0, 49)}
        self.maxmark_to_grade = {49: 'F', 59: 'D', 69: 'C', 79: 'B', 100: 'A'}
        self.minmark_to_grade = {0: 'F', 50: 'D', 60: 'C', 70: 'B', 80: 'A'}
        self.result = []

    def eq_maxmark(self, mark):
        if (0 <= mark) and (mark <= 49):
            return 'F'
        if (50 <= mark) and (mark <= 59):
            return 'D'
        if (60 <= mark) and (mark <= 69):
            return 'C'
        if (70 <= mark) and (mark <= 79):
            return 'B'
        if(80 <= mark) and (mark <= 100):
            return 'A'

    def get_graded_students(self, markslist, grade):
        max_mark =0
        min_mark =0
        for (name, mark) in markslist:
            if grade == 'A':
                # if mark self.grade_to_minmax[grade]
                if self.eq_maxmark(mark) == grade:
                    max_mark = self.grade_to_minmax[grade][1]
                    min_mark = self.grade_to_minmax[grade][0]
            if grade == 'B':
                # if mark self.grade_to_minmax[grade]
                if self.eq_maxmark(mark) == grade:
                    max_mark = self.grade_to_minmax[grade][1]
                    min_mark = self.grade_to_minmax[grade][0]
            if grade == 'C':
                # if mark self.grade_to_minmax[grade]
                if self.eq_maxmark(mark) == grade:
                    max_mark = self.grade_to_minmax[grade][1]
                    min_mark = self.grade_to_minmax[grade][0]
            if grade == 'D':
                # if mark self.grade_to_minmax[grade]
                if self.eq_maxmark(mark) == grade:
                    max_mark = self.grade_to_minmax[grade][1]
                    min_mark = self.grade_to_minmax[grade][0]
            if grade == 'F':
                # if mark self.grade_to_minmax[grade]
                if self.eq_maxmark(mark) == grade:
                    max_mark = self.grade_to_minmax[grade][1]
                    min_mark = self.grade_to_minmax[grade][0]
            if (min_mark <= mark) and (mark <= max_mark):
                self.result.append((name, self.eq_maxmark(mark)))




