FROM python:3.12
LABEL maintainer = "Sarim Ahmed Khan"

WORKDIR /code/

COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-root

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "kafka_messaging.main:app", "--host", "0.0.0.0", "--reload"]