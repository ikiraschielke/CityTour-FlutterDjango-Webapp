FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /city
WORKDIR /city
ADD requirements.txt /city/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /city/