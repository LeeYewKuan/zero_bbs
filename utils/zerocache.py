# 从redis包中导入Redis类
from redis import Redis

# 初始化redis实例变量
zero_redis = Redis(host='127.0.0.1', port=6379)


def set(key, value, timeout=60):
    zero_redis.set(key, value, timeout)


def get(key):
    zero_redis.get(key)


def delete(key):
    zero_redis.delete(key)

