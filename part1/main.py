import redis
from redis_cache import RedisCache

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisCache(redis_client=client)


@cache.cache(ttl=120)
def find_divisors(num: int):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    print(find_divisors(10651060))
