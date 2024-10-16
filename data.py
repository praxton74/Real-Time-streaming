from faker import Faker
import random
import time

faker=Faker()

def generate_social_media_post():
    post_id=faker.uuid4()
    user_id=faker.uuid4()
    content=faker.text()
    timestamp=int(time.time())
    return f"{post_id},{user_id},{content},{timestamp}"


def generate_engagement():
    user_id=faker.uuid4()
    action=random.choice(["like", "comment", "share"])
    timestamp=int(time.time())
    return f"{user_id},{action},{timestamp}"


if __name__=="__main__":
    with open("sample_data.txt", "w") as f:
        for _ in range(10):                              # Generate 10 sample posts
            post=generate_social_media_post()
            f.write(post+"\n")
            print(f"Post: {post}")
            time.sleep(1)                                # Simulate a 1-second interval between posts

        for _ in range(20):                              # 20 sample engagements
            engagement=generate_engagement()
            f.write(engagement+"\n")
            print(f"Engagement: {engagement}")
            time.sleep(1)                                
