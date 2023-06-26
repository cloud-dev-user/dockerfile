# Dockerfile
FROM python:3.9

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
