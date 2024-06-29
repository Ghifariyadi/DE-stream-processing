import logging
from kafka import KafkaProducer
import json
from datetime import datetime
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)
