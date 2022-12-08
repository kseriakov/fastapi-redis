from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from utils.redis_utils import get_all_objects, get_object
from .models import Product


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/products')
def all():
    return get_all_objects(Product)


@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_product(new_product: Product):
    return new_product.save()


@app.get('/products/{pk}')
def get_product(pk: str):
    product = get_object(Product, pk)
    return product


@app.delete('/products/{pk}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(pk: str):
    get_object(Product, pk).delete(pk)
