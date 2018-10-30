import requests
from bs4 import BeautifulSoup

url='http://tieba.baidu.com/p/2166231880'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
s_images = soup.findAll('img', class_='BDE_Image')

i = 1
for s_image in s_images:
    img_url = s_image['src']
    img_content = requests.get(img_url).content
    file_name = str(i)+'.jpg'
    #文件路径不能是root权限下的，否则文件无法保存
    with open('/home/Tyella/图片/杉本有美/'+file_name,'wb') as f:
        f.write(img_content)
    i+=1
