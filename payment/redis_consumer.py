import time
import logging.config

from database.database import redis
from database.enums import StreamGroup, StreamKey

from .models import Order, OrderStatus
from .logs.log_settings import LOGGING


logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

group = StreamGroup.PAYMENT.value
stream_key = StreamKey.ORDER_REFUNDED.value

try:
    redis.xgroup_destroy(name=stream_key, groupname=group)
except Exception as err:
    logger.info(str(err))
finally:
    try:
        redis.xgroup_create(name=stream_key, groupname=group)
    except Exception as err:
        logger.info(str(err))


while True:
    try:
        data = redis.xreadgroup(
            groupname=group, consumername=stream_key, streams={stream_key: '>'}
        )
        if data:
            for d in data:
                order_id = d[1][0][1]['pk']
                order: Order = Order.get(order_id)
                order.status = OrderStatus.REFUNDED.value
                order.save()
    except Exception as err:
        logger.info(str(err))

    time.sleep(1)
