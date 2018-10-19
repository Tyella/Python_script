import uuid

class Generation:
    def __init__(self):
        self.num=0
        self.listid=[]

    def generate_uuid(self,num):
        for i in range(int(num)):
            self.listid.append(uuid.uuid1())

    def get_uuid(self):
        return self.listid

if __name__=='__main__':
    Gencode=Generation()
    Gencode.generate_uuid(200)
    keys=Gencode.get_uuid()

    fileKeys=open('/home/Tyella/文档/uuid.txt','w')
    for k in keys:
        fileKeys.write(str(k)+'\n')
    fileKeys.close()

