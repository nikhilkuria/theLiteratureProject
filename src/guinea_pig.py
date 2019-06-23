import logging
import sys

from service import storage_service
from engine import redis_engine

logger = logging.getLogger()

def _configure_logger():
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(module)s]: %(message)s')
    logging_out = logging.StreamHandler(sys.stdout)
    logging_err = logging.StreamHandler(sys.stderr)
    logging_out.setFormatter(formatter)
    logging_err.setFormatter(formatter)
    logging_out.setLevel(logging.DEBUG)
    logging_err.setLevel(logging.WARNING)

    # root logger, no __name__ as in submodules further down the hierarchy
    global logger
    logger.addHandler(logging_out)
    logger.addHandler(logging_err)
    logger.setLevel(logging.DEBUG)

if __name__=="__main__":
    _configure_logger()
    print("I am a Guinea pig")
    storage_service.store_literature(name="test", url="http://www.google.com", tags=['search_engine', "seo", "minimal"])
    storage_service.store_literature(name="facebook login", url="http://www.facebook.com", tags=['social network', "seo", "minimal"])

    print(redis_engine.get_value('url:test'))

    print(redis_engine.get_values_from_set('tags:test'))
