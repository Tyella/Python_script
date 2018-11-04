import json
import xlwt

with open('/home/Tyella/文档/student.txt') as f:
    content = f.read()
wb = xlwt.Workbook()
ws = wb.add_sheet('stduent')
json = json.loads(content)
i = 0
for con in json:
    values = json.get(con)
    ws.write(i, 0, con)
    j = 1
    for value in values:
        ws.write(i, j, value)
        j += 1
    i += 1
wb.save('/home/Tyella/文档/stduent.xls')

