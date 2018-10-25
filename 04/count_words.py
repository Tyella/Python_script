import re
from collections import Counter

def cal(filename='ddd.txt'):
    with open(filename,'r') as f:
        data=f.read()
    data=data.lower()
    datalist = re.split(r'[\s\n]+', data)
    return Counter(datalist).most_common()

if __name__ == '__main__':
    dic = cal()
    for i  in range(len(dic)):
        print('%15s  ---->   %3s' % (dic[i][0],dic[i][1]))
