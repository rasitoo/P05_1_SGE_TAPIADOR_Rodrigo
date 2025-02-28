FROM python:3.12.9-slim

WORKDIR /apipython

COPY .env /apipython/.env
COPY requirements.txt /apipython/requirements.txt
COPY ./app /apipython/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
