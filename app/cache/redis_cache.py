import os
import json
import redis
from dotenv import load_dotenv
from app.core.config import settings

load_dotenv()   

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key: str):
    value = redis_client.get(key)
    if value:
        return json.load(value)
    return None

def set_cached_prediction(key : str, value: dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))