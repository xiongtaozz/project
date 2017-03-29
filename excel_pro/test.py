# coding:utf-8
import os
import xlrd
from xlutils.copy import copy
one_any_list = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
r_xls = xlrd.open_workbook(u'学生数据/合计数据.xlsx')
r_sheet = r_xls.sheet_by_index(0)
rows = r_sheet.nrows
w_xls = copy(r_xls)
sheet_write = w_xls.get_sheet(0)
for i in range(0, len(one_any_list)):
    for x in range(0, len(one_any_list[i])):
        sheet_write.write(rows, i, one_any_list[i][x])
w_xls.save(u'学生数据/合计数据.xlsx')
