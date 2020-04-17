import xlsxwriter

# 建立文件
workbook = xlsxwriter.Workbook('hello.xlsx')
# 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误
worksheet = workbook.add_worksheet()
# 向A1写入
worksheet.write('A1', 'Hello world')
# 向第二行第二例写入Excel
worksheet.write(1, 1, 'Excel')
workbook.close()
