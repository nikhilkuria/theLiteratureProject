import logging
from engine import redis_engine

logger = logging.getLogger(__name__)

URL_PREFIX = 'url'
NAME_TAGS_PREFIX = "tags"
TAGS_NAME_PREFIX = "tags.name"


SPACE_PLACEHOLDER = "."

def store_literature(name: str, url: str, tags: list):
    logger.debug(f"Storing literature name:{name} url:{url} tags:{tags}")

    # Store the url
    url_key = _get_url_key(name)
    redis_engine.set_key(key=url_key, value=url)

    # Store name -> tags
    tag_name = _get_tags_key(name)
    for tag in tags:
        redis_engine.add_key_to_set(key=tag_name, value=tag)

    # Store tags -> name
    for tag in tags:
        tag_to_name_key = _get_tags_to_name_key(tag)
        redis_engine.add_key_to_set(key=tag_to_name_key, value=name)

def _get_url_key(name: str):
    return _add_prefix(URL_PREFIX, _sanitise_space(name))

def _get_tags_key(name: str):
    return _add_prefix(NAME_TAGS_PREFIX, _sanitise_space(name))

def _get_tags_to_name_key(name: str):
    return _add_prefix(TAGS_NAME_PREFIX, _sanitise_space(name))

def _add_prefix(prefix: str, name: str):
    return f"{prefix}:{name}"

def _sanitise_space(name: str):
    return name.replace(" ", SPACE_PLACEHOLDER)