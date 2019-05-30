# 作者：wjq
# 创建时间: 2019/5/15  
# 文件: test.py   
# 软件名称: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook("2222结果.xlsx")
worksheet = workbook.add_worksheet('巡检结果')
headings = ['主机名称', 'ip地址', '内存占用']
worksheet.write_row('A1', headings)

data = [
    ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

# input()
worksheet.write_column('A2', data[0])

workbook.close()