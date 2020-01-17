FROM python:3.8
ADD . /urlshortener
WORKDIR /urlshortener
RUN pip install -r requirements.txt