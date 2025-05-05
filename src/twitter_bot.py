import tweepy
from config.config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, TWITTER_BEARER_TOKEN

# Authenticate with OAuth 1.0a (required for media uploads)
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

# # Authenticate to Twitter Using Twitter API V2
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN, 
                          consumer_key=TWITTER_API_KEY, 
                          consumer_secret=TWITTER_API_SECRET, 
                          access_token=TWITTER_ACCESS_TOKEN, 
                          access_token_secret=TWITTER_ACCESS_SECRET)

# Function to post a tweet using v2 API
def tweet(text):
    try:
        response = client.create_tweet(text=text)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

def upload_media(file_path):
    try:
        media = api.media_upload(file_path)
        print(f"Media uploaded successfully to Twitter! Media ID: {media.media_id}")
        return media.media_id
    except tweepy.TweepyException as e:
        print(f"Error uploading media to Twitter: {e}")
        return None

# Function to post a tweet with media
def tweet_with_media(text, file_path):
    media_id = upload_media(file_path)
    if media_id:
        try:
            response = client.create_tweet(text=text, media_ids=[media_id])
            print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
        except tweepy.TweepyException as e:
            print(f"Error posting tweet: {e}")
    else:
        print("Tweet not posted due to media upload failure.")

def like_tweet(tweet_id):
    """Like a tweet by ID."""
    try:
        response = client.like(tweet_id)
        print(f"Liked tweet {tweet_id}")
    except tweepy.TweepyException as e:
        print(f"Error liking tweet: {e}")

def retweet_tweet(tweet_id):
    """Retweet a tweet by ID."""
    try:
        response = client.retweet(tweet_id)
        print(f"Retweeted tweet {tweet_id}")
    except tweepy.TweepyException as e:
        print(f"Error retweeting: {e}")

def get_user_tweets(user_id, count=10):
    """Fetch recent tweets of a user."""
    try:
        tweets = client.get_users_tweets(id=user_id, max_results=count)
        for tweet in tweets.data:
            print(f"Tweet ID: {tweet.id}, Text: {tweet.text}")
    except tweepy.TweepyException as e:
        print(f"Error fetching user tweets: {e}")

def get_tweet(tweet_id):
    """Fetch a specific tweet by ID."""
    try:
        tweet = client.get_tweet(id=tweet_id)
        print(f"Tweet ID: {tweet.data['id']}, Text: {tweet.data['text']}")
    except tweepy.TweepyException as e:
        print(f"Error fetching tweet: {e}")
def get_user_tweets(user_id, count=10):
    """Fetch recent tweets of a user."""
    try:
        tweets = client.get_users_tweets(id=user_id, max_results=count)
        for tweet in tweets.data:
            print(f"Tweet ID: {tweet.id}, Text: {tweet.text}")
    except tweepy.TweepyException as e:
        print(f"Error fetching user tweets: {e}")