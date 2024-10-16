from confluent_kafka import Producer
import time


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(
            f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
        )


def main():
    producer_config = {
        "bootstrap.servers": "localhost:9092",
    }

    producer = Producer(producer_config)

    topic = "social_media_stream"

    with open("sample_data.txt") as f:
        for line in f:
            producer.produce(
                topic, value=line.strip().encode("utf-8"), callback=delivery_report
            )
            time.sleep(1)

    producer.flush()


if __name__ == "__main__":
    main()
