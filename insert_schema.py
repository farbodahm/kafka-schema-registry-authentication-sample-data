from time import sleep
from schema_registry.client import SchemaRegistryClient, schema
import os

SCHEMA_REGISTRY_HOST_NAME = os.environ.get('SCHEMA_REGISTRY_HOST_NAME')
SCHEMA_REGISTRY_PORT = os.environ.get('SCHEMA_REGISTRY_PORT')
SCHEMA_REGISTRY_USERNAME = os.environ.get('SCHEMA_REGISTRY_USERNAME')
SCHEMA_REGISTRY_PASSWORD = os.environ.get('SCHEMA_REGISTRY_PASSWORD')

URL = f'http://{SCHEMA_REGISTRY_USERNAME}:{SCHEMA_REGISTRY_PASSWORD}@{SCHEMA_REGISTRY_HOST_NAME}:{SCHEMA_REGISTRY_PORT}'
print(URL)

client = SchemaRegistryClient(URL)

schemas = [
    {
        "type": "record",
        "namespace": "com.kubertenes",
        "name": "AvroDeployment",
        "fields": [
            {"name": "image", "type": "string"},
            {"name": "replicas", "type": "int"},
            {"name": "port", "type": "int"},
        ],
    },
    {
        "type": "record",
        "name": "trip_record",
        "namespace": "com.landoop.transportation.nyc.trip.yellow",
        "doc": "Schema for yellow taxi trip records from NYC TLC data. [http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml]",
        "fields": [
            {
                "name": "VendorID",
                "type": "int",
                "doc": "A code indicating the TPEP provider that provided the record. 1: Creative Mobile Technologies, LLC 2: VeriFone Inc."
            },
            {
                "name": "tpep_pickup_datetime",
                "type": "string",
                "doc": "The date and time when the meter was engaged."
            },
            {
                "name": "tpep_dropoff_datetime",
                "type": "string",
                "doc": "The date and time when the meter was disengaged."
            },
            {
                "name": "passenger_count",
                "type": "int",
                "doc": "The number of passengers in the vehicle. This is a driver-entered value."
            },
            {
                "name": "trip_distance",
                "type": "double",
                "doc": "The elapsed trip distance in miles reported by the taximeter."
            },
            {
                "name": "pickup_longitude",
                "type": "double",
                "doc": "Longitude where the meter was engaged."
            },
            {
                "name": "pickup_latitude",
                "type": "double",
                "doc": "Latitude where the meter was engaged."
            },
            {
                "name": "RateCodeID",
                "type": "int",
                "doc": "The final rate code in effect at the end of the trip. 1: Standard rate, 2:JFK, 3:Newark, 4:Nassau or Westchester, 5:Negotiated fare, 6:Group ride"
            },
            {
                "name": "store_and_fwd_flag",
                "type": "string",
                "doc": "This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y: store and forward trip N: not a store and forward trip"
            },
            {
                "name": "dropoff_longitude",
                "type": "double",
                "doc": "Longitude where the meter was disengaged."
            },
            {
                "name": "dropoff_latitude",
                "type": "double",
                "doc": "Latitude where the meter was disengaged."
            },
            {
                "name": "payment_type",
                "type": "int",
                "doc": "A numeric code signifying how the passenger paid for the trip. 1: Credit card 2: Cash 3: No charge 4: Dispute 5: Unknown 6: Voided trip"
            },
            {
                "name": "fare_amount",
                "type": "double",
                "doc": "The time-and-distance fare calculated by the meter."
            },
            {
                "name": "extra",
                "type": "double",
                "doc": "Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges."
            },
            {
                "name": "mta_tax",
                "type": "double",
                "doc": "$0.50 MTA tax that is automatically triggered based on the metered rate in use."
            },
            {
                "name": "improvement_surcharge",
                "type": "double",
                "doc": "$0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015."
            },
            {
                "name": "tip_amount",
                "type": "double",
                "doc": "Tip amount – This field is automatically populated for credit card tips. Cash tips are not included."
            },
            {
                "name": "tolls_amount",
                "type": "double",
                "doc": "Total amount of all tolls paid in trip."
            },
            {
                "name": "total_amount",
                "type": "double",
                "doc": "The total amount charged to passengers. Does not include cash tips."
            }
        ]
    },
    {
        "type": "record",
        "name": "milanoRecord",
        "namespace": "com.landoop.telecom.telecomitalia.grid",
        "doc": "Schema for Grid for Telecommunications Data from Telecom Italia.",
        "fields": [
            {
                "name": "SquareId",
                "type": "int",
                "doc": " The id of the square that is part of the Milano GRID"
            },
            {
                "name": "Polygon",
                "type": {
                    "type": "array",
                    "items": {
                        "type": "record",
                        "name": "coordinates",
                        "fields": [
                            {
                                "name": "longitude",
                                "type": "double"
                            },
                            {
                                "name": "latitude",
                                "type": "double"
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        "type": "record",
        "name": "smsCallInternet",
        "namespace": "com.landoop.telecom.telecomitalia.telecommunications",
        "doc": "Schema for Telecommunications Data from Telecom Italia.",
        "fields": [
            {
                "name": "SquareId",
                "type": "int",
                "doc": " The id of the square that is part of the Milano GRID"
            },
            {
                "name": "TimeInterval",
                "type": "long",
                "doc": "The beginning of the time interval expressed as the number of millisecond elapsed from the Unix Epoch on January 1st, 1970 at UTC. The end of the time interval can be obtained by adding 600000 milliseconds (10 minutes) to this value."
            },
            {
                "name": "CountryCode",
                "type": "int",
                "doc": "The phone country code of a nation. Depending on the measured activity this value assumes different meanings that are explained later."
            },
            {
                "name": "SmsInActivity",
                "type": [
                    "null",
                    "double"
                ],
                "doc": "The activity in terms of received SMS inside the Square id, during the Time interval and sent from the nation identified by the Country code."
            },
            {
                "name": "SmsOutActivity",
                "type": [
                    "null",
                    "double"
                ],
                "doc": "The activity in terms of sent SMS inside the Square id, during the Time interval and received by the nation identified by the Country code."
            },
            {
                "name": "CallInActivity",
                "type": [
                    "null",
                    "double"
                ],
                "doc": "The activity in terms of received calls inside the Square id, during the Time interval and issued from the nation identified by the Country code."
            },
            {
                "name": "CallOutActivity",
                "type": [
                    "null",
                    "double"
                ],
                "doc": "The activity in terms of issued calls inside the Square id, during the Time interval and received by the nation identified by the Country code."
            },
            {
                "name": "InternetTrafficActivity",
                "type": [
                    "null",
                    "double"
                ],
                "doc": "The activity in terms of performed internet traffic inside the Square id, during the Time interval and by the nation of the users performing the connection identified by the Country code."
            }
        ]
    },
    {
        "namespace": "my.com.ns",
        "name": "myrecord",
        "type":  "record",
        "fields": [
            {"name": "uid", "type": "int"},
            {"name": "somefield", "type": "string"},
            {"name": "options", "type": {
                "type": "array",
                "items": {
                    "type": "record",
                    "name": "lvl2_record",
                    "fields": [
                        {"name": "item1_lvl2", "type": "string"},
                        {"name": "item2_lvl2", "type": {
                            "type": "array",
                            "items": {
                                "type": "record",
                                "name": "lvl3_record",
                                "fields": [
                                    {"name": "item1_lvl3", "type": "string"},
                                    {"name": "item2_lvl3", "type": "string"}
                                ]
                            }
                        }}
                    ]
                }
            }}
        ]
    }
]

subjects = [
    'test-deployment',
    'nyc_yellow_taxi_trip_data-value',
    'telecom_italia_grid-value',
    'telecom_italia_data-value',
    'complex-nested'
]

# Wait to make sure Kafka and Schema Registry are ready
sleep(60)
for _schema, subject in zip(schemas, subjects):
    avro_schema = schema.AvroSchema(_schema)
    schema_id = client.register(subject, avro_schema)
    print(f'{subject}: {str(schema_id)}')
