from typing import TypeVar
from fastapi import HTTPException, status
from redis_om import HashModel


T = TypeVar('T', bound=HashModel)


def get_object(model: T, pk):
    try:
        return model.get(pk)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{str(model).split(".")[-1][:-2]} with id {pk} does not exists',
        )


def get_all_objects(model: T):
    return [get_object(model, pk) for pk in model.all_pks()]
