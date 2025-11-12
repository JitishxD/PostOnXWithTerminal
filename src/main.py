import tweepy
from datetime import datetime
from utils import pick_latest_image
from config import load_env_variables
import os
import sys

print("🚀 Starting the Auto Post Challenge Status Script...\n")

# Load and validate environment variables
api_key, api_secret, access_token, access_secret = load_env_variables()

try:
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )
except Exception as e:
    print(f"❌ Error: Failed to initialize Twitter client: {e}")
    input("\nPress ENTER to exit...")
    sys.exit(1)

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
try:
    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_secret)
    api = tweepy.API(auth)
except Exception as e:
    print(f"❌ Error: Failed to authenticate for media upload: {e}")
    input("\nPress ENTER to exit...")
    sys.exit(1)

# upload image
try:
    image_path = pick_latest_image()
    if not image_path:
        print("❌ Error: No image found")
        input("\nPress ENTER to exit...")
        sys.exit(1)

    if not os.path.exists(image_path):
        print(f"❌ Error: Image file not found: {image_path}")
        input("\nPress ENTER to exit...")
        sys.exit(1)

    media = api.media_upload(image_path)
    print(f"✅ Image uploaded successfully: {image_path}")
    print(f"Media ID: {media.media_id}")
except tweepy.TweepyException as e:
    print(f"❌ Error: Failed to upload image: {e}")
    input("\nPress ENTER to exit...")
    sys.exit(1)

# post with image
try:
    response = client.create_tweet(text=post, media_ids=[media.media_id])
    print("✅ Tweet posted successfully!")
    input("\nPress ENTER to exit...")
except tweepy.TweepyException as e:
    print(f"❌ Error: Failed to post tweet: {e}")
    input("\nPress ENTER to exit...")
    sys.exit(1)
