import tweepy
from dotenv import load_dotenv
from datetime import datetime
import os

# Load .env variables!
load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# POST CONTENT
day_number = int(input("Enter the day number: "))
total_days = 160

problem_name = input("Enter problem name: ")
tc = input("Enter time complexity: ").strip()
sc = input("Enter space complexity: ").strip()

today = datetime.now()
formatted_day = today.strftime("%B %d, %Y")
print(formatted_day)
days_left = total_days - day_number

# The POST
post = f"""
📅 {formatted_day}

Day {day_number}/{total_days} ✅✨ | #GFG160 Challenge 💻🔥
📌 QOTD: {problem_name}
🔹 TC: O({tc}) SC: O({sc})
⏳ {days_left} days to go... 🚀

GFG profile: https://www.geeksforgeeks.org/user/jitishxdd/
@geeksforgeeks

#GeekStreak2025 #GeeksforGeeks #DSA #ChallengeAccepted #cpp
"""

# Auth for media upload (needed for images)
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# upload image
image_path = input("Enter path to image: ").strip()
media = api.media_upload(image_path)

# post with image
client.create_tweet(text=post, media_ids=[media.media_id])
print("posted ✅")
