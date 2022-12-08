import time
import logging.config

from database.database import redis
from database.enums import StreamGroup, StreamKey
from .models import Product

from inventory.logs.log_settings import LOGGING

logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

group = StreamGroup.INVENTORY.value
stream_key = StreamKey.ORDER_CREATED.value



while True:
    try:
        data = redis.xreadgroup(
            groupname=group, consumername=stream_key, streams={stream_key: '>'}
        )

        if data:
            for d in data:
                order = d[1][0][1]
                try:
                    product: Product = Product.get(order['product_id'])
                    product.quantity -= float(order['quantity'])
                    if product.quantity < 0:
                        raise ValueError(
                            f'In stack not availible {order["quantity"]} product/s'
                        )
                    product.save()
                except Exception as err:
                    logger.info(str(err))
                    
                    redis.xadd(
                        name=StreamKey.ORDER_REFUNDED.value,
                        fields=order,
                        id='*',
                    )

    except Exception as err:
        logger.info(str(err))

    time.sleep(1)
