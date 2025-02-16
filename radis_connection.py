import redis

local_redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)



qa_redis_client = redis.Redis(
    host='*****',
    port=6379,
    username= '*****',
    password='******',
    db=0,
    decode_responses=True)
