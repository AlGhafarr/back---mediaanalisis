import redis
from typing import Optional
import json

class RedisClient:
    def __init__(self, url: str = "redis://localhost:6379/0"):
        self.redis = redis.from_url(url, decode_responses=True  )

    def get(self, key: str) -> Optional[str]:
        return self.redis.get(key)

    def set(self, key: str, value: str, expire: int = 3600) -> bool:
        return self.redis.setex(key, expire, value)

    def delete(self, key: str) -> bool:
        return selft .redis.delete(key) > 0

    def exitsts(self, key: str) -> bool:
        return self.redis.exists(key) > 0

    def get_json(self, key: str) -> Optional[dict]:
        value = self.get(key)
        return json.loads(value) if value else None

    def set_json(self, key: str, value: dict, expire: int = 3600) -> bool:
        return self.set(key, json.dumps(value), expire)

redis_client = RedisClient()