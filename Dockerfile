FROM python:3.7.2

RUN mkdir -p /home/Project

WORKDIR /home/Project

COPY requirements.txt /home/Project

RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/Project
