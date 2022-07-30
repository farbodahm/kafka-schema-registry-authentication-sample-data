FROM python:3.8

WORKDIR /app

COPY . /app
RUN pip install python-schema-registry-client

CMD ["python", "insert_schema.py"]