# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :

# coding=utf-8
import sys
import xlrd

data = xlrd.open_workbook('output.xls')
table= data.sheet_by_name(u'导出工作表')
nrows_num = table.nrows
ncols_num = table.ncols
res = []
fileName='盾安控股集团有限公司.docx'
for i in range(1,nrows_num):
    aa=str(table.cell(i,0).value).decode("unicode_escape").encode("utf8")
    if aa in fileName:
        print 'yicunzai'
    else:
        i=i+1

# for i in range(nrows_num):
#         print str(table.row_values(i)).decode("unicode_escape").encode("utf8")

