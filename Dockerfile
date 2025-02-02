FROM python:3.9-alphine3.21

WORKDIR /FAQ_Model

COPY requirement.txt requirement.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000

