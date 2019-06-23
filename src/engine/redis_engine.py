import logging
import redis

logger = logging.getLogger(__name__)

logger.debug(f"Initialising Redis engine")
redis_store = redis.Redis(host='localhost', port=6379, db=0)

def set_key(key:str, value:str):
    logger.debug(f"Set the value: {value} to the key: {key}")
    redis_store.set(name=key, value=value)

def add_key_to_set(key:str, value:str):
    logger.debug(f"Add value: {value} to the set with key: {key}")
    redis_store.sadd(key, value)

def get_value(key:str):
    logger.debug(f"Fetch value for the key: {key}")
    value = redis_store.get(key)
    return value

def get_values_from_set(key:str):
    logger.debug(f"Fetch value from the set for the key: {key}")
    values = redis_store.smembers(key)
    return values