import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional but recommended)
load_dotenv()

# Twitter API Keys
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

#Instagram Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Media directory (ensure it exists)
MEDIA_DIR = "media"
os.makedirs(MEDIA_DIR, exist_ok=True)
