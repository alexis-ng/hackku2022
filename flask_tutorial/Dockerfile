FROM python:3.9

RUN pip install Flask gunicorn
RUN pip3 install twilio

COPY src/ /app
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind $PORT --workers 1 --threads 8 app:app