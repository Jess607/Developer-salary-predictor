FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt  /app

RUN pip install -r requirements.txt

COPY model.h5 /app

COPY app.py /app

COPY preprocessing.joblib /app 

COPY templates /app/templates 

COPY static /app/static

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]