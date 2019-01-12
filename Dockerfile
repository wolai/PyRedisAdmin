FROM python:2.7.10

COPY . /app
WORKDIR /app

CMD ["python", "routes.py"]

