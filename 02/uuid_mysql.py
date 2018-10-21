import uuid
import pymysql

class Generation:
    def __init__(self):
        self.num=0
        self.listid=[]

    def generate_code(self,num):
        for i in range(num):
            self.listid.append(uuid.uuid1())

    def get_code(self):
        return self.listid

if __name__=='__main__':
    Gencode=Generation()
    Gencode.generate_code(200)
    keys=Gencode.get_code()

    conn=pymysql.connect(
        host='localhost',
        port=int('3306'),
        user='root',
        passwd='admin',
        db='uuid'
    )
    cursor=conn.cursor()
    for code_num in keys:
        sql='insert into code(code_num) values (\'{}\')'.format(code_num)
        cursor.execute(sql)
    conn.commit()
    conn.close()

