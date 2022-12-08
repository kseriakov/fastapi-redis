FROM python:3.10.8-alpine3.16

ENV ROOT_FOLDER /var/www/fastapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p ${ROOT_FOLDER}

WORKDIR ${ROOT_FOLDER}

# build-essential - для компиляции приложений
# в apline его нет, эвивалент - build-base
RUN apk upgrade && apk update && \
    apk add build-base  \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./req.txt ./req.txt
RUN pip install -r ./req.txt

COPY ./docker/fastapi/payment/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

CMD [ "/entrypoint" ]