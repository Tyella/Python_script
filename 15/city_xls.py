import json
import xlwt

wb=xlwt.Workbook()
ws=wb.add_sheet('city')
with open('/home/Tyella/文档/city.txt')as f:
    content=f.read()
json=json.loads(content)
i=0
for con in json:
    ws.write(i, 0, con)
    ws.write(i, 1, json.get(con))
    i+=1
wb.save('/home/Tyella/文档/city.xls')

