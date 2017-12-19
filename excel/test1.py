# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :

import xlrd
#import chardet
data = xlrd.open_workbook("output.xls")
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
#print chardet.detect(str(table.row_values(i)))
        print str(table.row_values(i)).decode("unicode_escape").encode("utf8")