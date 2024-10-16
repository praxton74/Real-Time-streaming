from confluent_kafka import Consumer

def main():
    consumer_config={
        "bootstrap.servers": "localhost:9092",
        "group.id": "my-group",
        "auto.offset.reset": "earliest",
    }
    consumer=Consumer(consumer_config)
    topic="social_media_stream"
    consumer.subscribe([topic])
    try:
        while True:
            message=consumer.poll(1.0)

            if message is None:
                continue
            if message.error():
                print(f"Consumer error: {message.error()}")
                continue

            data=message.value().decode("utf-8")
            print(f"Received message: {data}")
            
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__=="__main__":
    main()
