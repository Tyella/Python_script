import uuid
import redis

r=redis.StrictRedis(host='localhost',port=6389)
for i in range(200):
    r.set('key_id',str(i),uuid.uuid1())

for i in range(200):
    print(r.get('key_id'+str(i)))
