import tweepy
import os
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Add scripts directory to Python path
from read_quotes import get_random_quote

# Load .env file (only needed for local testing)
if os.path.exists(".env"):
    load_dotenv()

# Twitter API Keys (Get from GitHub Secrets or .env file)
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Log file to keep track of posted tweets
LOG_FILE = "posted_tweets.log"

def has_already_tweeted(quote):
    """Check if the quote was already posted before."""
    if not os.path.exists(LOG_FILE):
        return False

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        posted_quotes = file.read().splitlines()

    return quote in posted_quotes

def log_tweet(quote):
    """Log the posted tweet to avoid duplication."""
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(quote + "\n")

def post_tweet():
    """Post a random movie quote on Twitter."""
    quote = get_random_quote()
    
    if quote is None:
        print("No quote found. Skipping tweet.")
        return

    if has_already_tweeted(quote):
        print("Quote already tweeted. Trying again...")
        post_tweet()  # Pick another quote if it's already posted
        return

    try:
        api.update_status(quote)
        print(f"✅ Successfully tweeted: {quote}")

        # Log the posted tweet
        log_tweet(quote)

    except tweepy.TweepyException as e:
        print(f"❌ Twitter API Error: {e}")

# Run the bot
if __name__ == "__main__":
    post_tweet()
