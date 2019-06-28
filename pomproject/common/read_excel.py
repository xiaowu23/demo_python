# -*- coding:utf-8
"""
用来测试
"""
import xlrd

# 第1步：打开excel表格
data = xlrd.open_workbook("testdata.xlsx")

# 第2步：打开sheet页
table = data.sheet_by_name(u"登录")

# 第3步：获取行数
nrows = table.nrows
print(nrows)

# 第4步：获取列数
ncols = table.ncols
print(ncols)

# 获取第一行的值
keys = table.row_values(0)
print(keys)

#获取第二列的值
values = table.col_values(1)
print(values)