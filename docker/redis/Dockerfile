FROM redis/redis-stack:latest

COPY ./docker/redis/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

CMD [ "/start" ]
