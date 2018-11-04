import json
import xlwt

wb=xlwt.Workbook()
ws=wb.add_sheet('number')
with open('/home/Tyella/文档/number.txt')as f:
    content=f.read()
json=json.loads(content)
i=0
for con in json:
    j=0
    for item in con:
        ws.write(i,j,item)
        j+=1
    i+=1
wb.save('/home/Tyella/文档/number.xls')
