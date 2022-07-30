# Setup Kafka, Schema registry with Authentication with Sample Schemas Environment
Setup a development environment with Kafka, Schema registry with Authentication and adding a sample data to it using Docker

You can use this project to easily setup a development environment including **Kafka**, **Schema registry** with **Authentication** with adding some **sample schemas** into schema registry.

## Run
To run the project, make sure you have `docker` and `docker-compose` installed, then run:
```
docker-compose up
```

and that's it. To test everything is set up correctly, you can get schemas from Schema Registry like this:

```
curl -X GET --user farbod:test_secret -i http://localhost:8082/subjects/
```
```
curl -X GET --user farbod:test_secret -i http://localhost:8082/subjects/complex-nested/versions/1
```

Also for connecting to Kafka in python, you can use this template:

```
import kafka

consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=['localhost:9092'])

print(consumer.topics())
```

## Schema Registry Users
To change/add the authorized users, change them in `conf/schema-registry/login.properties` and also in `docker-compose.yml`; Then run:
```
docker-compose build
docker-compose up
```

## Schema Registry Sample Schemas
To change/add schemas that are added into Schema Registry when project sets up, change them in `insert_schema.py` file and then run:
```
docker-compose build
docker-compose up
```