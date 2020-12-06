FROM python:3.6-slim

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python","openstackclustermonitoring/manage.py","runserver","0.0.0.0:80"]
