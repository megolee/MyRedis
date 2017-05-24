import sys
from rediscluster.client import StrictRedisCluster

redis_db_qa2 = [{'host':'10.157.26.84', 'port':6379},{'host':'10.157.26.85', 'port':6379},{'host':'10.157.26.86', 'port':6379}, {'host':'10.157.26.87', 'port':6379}, {'host':'10.157.26.88', 'port':6379}]

redis_db_stage = [{'host':'10.157.24.45', 'port':6379},{'host':'10.157.24.46', 'port':6379},{'host':'10.157.24.47', 'port':6379}, {'host':'10.157.24.54', 'port':6379}, {'host':'10.157.24.55', 'port':6379}]

if sys.argv[1] == 'qa2':
	target_redis = redis_db_qa2
elif  sys.argv[1] == 'stage':
	target_redis = redis_db_qa2
else:
	print 'Bad argument!!!!!!!'
	sys.exit(1)

smscode = 'SOA:MYACCOUNT:SMSCODE:1001:'+sys.argv[2]

try:
	redisconn = StrictRedisCluster(startup_nodes=target_redis)
	#print redisconn.mget(smscode)
	sms = redisconn.mget(smscode)
	if sms[0]:
		print "smscode is:", sms
	else:
		print "Cannot find the smscode"
		
except Exception,e:
	print "Connect Redis node error:", e
	sys.exit(1)