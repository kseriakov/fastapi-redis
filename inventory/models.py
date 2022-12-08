from redis_om import HashModel

from database.database import redis


class Product(HashModel):
    name: str
    price: float
    quantity: float

    class Meta:
        database = redis