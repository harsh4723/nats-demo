FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn","asgi:asgi","--workers","5","--bind","0.0.0.0:8001","--worker-class","uvicorn.workers.UvicornWorker"]
