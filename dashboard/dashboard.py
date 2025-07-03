import streamlit as st
import pandas as pd
from kafka import KafkaConsumer
import json

st.title("📊 Real-Time Retail Dashboard")

# Kafka setup
consumer = KafkaConsumer(
    'retail_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='dashboard-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Display messages as table
data = []

placeholder = st.empty()

while True:
    for message in consumer:
        record = message.value
        data.append(record)
        df = pd.DataFrame(data)
        with placeholder.container():
            st.dataframe(df.tail(10))
