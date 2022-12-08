import os
from pathlib import Path
from dotenv import load_dotenv
from redis_om import get_redis_connection


load_dotenv(
    dotenv_path=Path(Path(__file__).resolve().parent.parent / '.env')
)


redis = get_redis_connection(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASSWORD'),
    decode_responses=True,
)
