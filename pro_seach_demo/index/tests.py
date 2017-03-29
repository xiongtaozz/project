# from django.test import TestCase
import os
import xlrd
# Create your tests here.

# print os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads'+'/xls/abc.xls')
data = xlrd.open_workbook('D:\parcms\workbase\pro_seach_demo\uploads/xls/abc.csv', encoding_override='utf-8')
print data