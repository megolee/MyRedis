import sys
from redis.client import StrictRedis

redis_db_qa2 = [('10.157.26.84', 6379, 0),('10.157.26.85', 6379, 0),('10.157.26.86', 6379, 0), ('10.157.26.87', 6379, 0), ('10.157.26.88', 6379, 0)]

print sys.argv[0]
if sys.argv[1] == 'qa2':
	target_redis = redis_db_qa2
elif  sys.argv[1] == 'stage':
	target_redis = redis_db_qa2
else:
	print 'Bad argument!!!!!!!'
	sys.exit()

smscode = 'SOA:MYACCOUNT:SMSCODE:1001:'+sys.argv[2]
print smscode
	
for i in target_redis:
	myredis = StrictRedis(i[0], i[1], i[2])
	#address = i[0]+':'i[1]
	sms = myredis.get(smscode)
	if not sms:
		myredis.client_kill(address)
		break
	myredis.client_kill(address)

print sms
	
