FROM python:3.10-slim-buster

RUN apt update -y && apt install awcli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]