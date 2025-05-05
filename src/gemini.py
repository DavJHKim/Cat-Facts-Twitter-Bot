from config.config import MEDIA_DIR, GEMINI_API_KEY

import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Function to generate a tweet using Gemini
def gemini_generate_tweet(prompt="Generate a creative tweet about AI."):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return None