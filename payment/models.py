from enum import Enum
from redis_om import HashModel

from database.database import redis


class OrderStatus(Enum):
    PENDING = 'pending' 
    COMPLETED = 'completed'
    REFUNDED = 'refunded'


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: float
    status: OrderStatus

    class Meta:
        database = redis
