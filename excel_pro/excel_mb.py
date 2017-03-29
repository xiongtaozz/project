# coding:utf-8
import os
import xlrd
import xlwt
from xlutils.copy import copy

all_xls = os.listdir(u'学生数据')
list_all = []
for xls_a in range(0, len(all_xls)):
    data = xlrd.open_workbook('学生数据/'.decode('utf-8')+all_xls[xls_a])
    table = data.sheets()[0]
    nrows = table.nrows
    for m in range(1, nrows):
        try:
            if int(table.cell(m, 8).value) == 1:
                list_all.append(table.row_values(m))
        except Exception as e:
            print e

r_xls = xlrd.open_workbook(u'学生数据/合计数据.xls')
r_sheet = r_xls.sheet_by_index(0)
r_rows = r_sheet.nrows
w_xls = copy(r_xls)
sheet_write = w_xls.get_sheet(0)
for i in range(0, len(list_all)):
    for x in range(0, len(list_all[i])):
        sheet_write.write(r_rows, x, list_all[i][x])
w_xls.save('学生数据/合计数据.xls'.decode('utf-8'))