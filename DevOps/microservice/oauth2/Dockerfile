FROM python:3.12
LABEL maintainer = "Sarim Ahmed Khan"

WORKDIR /code/

COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-root

CMD ["poetry", "run", "uvicorn", "oauth2.main:app", "--host", "0.0.0.0", "--reload"]