FROM python:3.7.2

EXPOSE 5000

WORKDIR /Project

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /Project

ENTRYPOINT [ "python" ]

CMD [ "manage.py", "runserver" ]
