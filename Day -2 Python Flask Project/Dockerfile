FROM python:3.14.0a7-slim

WORKDIR /flaskapp

COPY app.py requirements.txt /flaskapp/

RUN pip install flask

CMD ["python", "app.py"]