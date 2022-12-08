import time
from fastapi import FastAPI, HTTPException, Request, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from database.database import redis
from database.enums import StreamKey
from inventory.models import Product
from utils.async_requests import async_get_request
from utils.redis_utils import get_object, get_all_objects
from .models import Order, OrderStatus


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def order_completed(order: Order):
    order.status = OrderStatus.COMPLETED.value
    order.save()

    redis.xadd(
        name=StreamKey.ORDER_CREATED.value,
        fields=order.dict(),
        id='*',
    )


@app.post('/orders', status_code=status.HTTP_201_CREATED)
async def create(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Request does not contain product_id or quantity',
        )

    product: Product = await async_get_request(
        f'http://inventory:8000/products/{product_id}'
    )

    # Проверка, что продукт существует
    get_object(Product, product_id)

    new_order = Order(
        product_id=product_id,
        price=product.get('price'),
        fee=(0.2 * product.get('price')),
        total=(1.2 * product.get('price')),
        quantity=quantity,
        status=OrderStatus.PENDING.value,
    )
    new_order.save()

    background_tasks.add_task(order_completed, new_order)

    return new_order


@app.get('/orders')
def all():
    return get_all_objects(Order)


@app.delete('/orders/delete/all', status_code=status.HTTP_204_NO_CONTENT)
def delete_all():
    orders_ids = Order.all_pks()
    for id in orders_ids:
        Order.delete(id)


@app.get('/orders/{pk}')
def get_order(pk: str):
    order = get_object(Order, pk)
    return order


@app.delete('/orders/{pk}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(pk: str):
    get_object(Order, pk).delete(pk)
