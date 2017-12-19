# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :

# coding=utf-8
import sys
import xlrd

data = xlrd.open_workbook('output.xls')

table = data.sheets()[0]
table2= data.sheet_by_name(u'导出工作表')

nrows_num = table.nrows

ncols_num = table.ncols

aa= table2.nrows

res = []
aa=table.cell(1,0).value
print aa
# for i in range(nrows_num):
#         print str(table.row_values(i)).decode("unicode_escape").encode("utf8")

