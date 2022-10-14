from openpyxl import Workbook
from openpyxl.worksheet.table import  Table, TableStyleInfo

'''
写excel
'''
workbook = Workbook()
sheet = workbook.active

data = [[1001, '白元芳', '男', '13232323232'],
        [1002, '白洁', '女', '13030303030']
        ]
sheet.append(['学号', '姓名', '性别', '电话'])
for row in data:
    sheet.append(row)
tab = Table(displayName='table1', ref='A1:E5')
tab.tableStyleInfo = TableStyleInfo(name='TableStyleMedium9', showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./res/study.xlsx')