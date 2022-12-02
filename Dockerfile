# Dockerfile, Image, Container

FROM python:3.10

ADD app.py .

RUN pip install requests

CMD ["python", "./app.py"]