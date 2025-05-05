from src.twitter_bot import tweet
from src.gemini import gemini_generate_tweet

def twitter_script():
    # Select a random prompt

    # Generate tweet
    tweet_text = gemini_generate_tweet("In a tweet format, Generate a creative tweet about a cat fact")

    # Post to Twitter
    tweet(tweet_text)


# Main function
def main():
    """Main function to run the Twitter bot."""
    print("🚀 Starting Twitter Bot...")

    twitter_script()

    print("✅ Twitter Bot execution completed.")

if __name__ == "__main__":
    main()