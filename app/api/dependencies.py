from redis import Redis

from redisdb.config import RedisSettings

redis_settings = RedisSettings()


async def get_redis_client():
    return Redis(
        host=redis_settings.host, port=redis_settings.port, db=redis_settings.db
    )
