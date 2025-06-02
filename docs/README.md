# 🐱 Cat Facts Twitter Bot

Visit https://x.com/Cat_Facts_Bot to see the bot live!

The **Cat Facts Twitter Bot** is an automated Python application that fetches random cat facts and posts them to Twitter. It leverages the Twitter API v2 for tweet management and is designed for deployment on cloud platforms like Google Cloud Functions.

## 📦 Features

* Creates random cat facts utilizing Gemini API
* Posts cat facts to a specified Twitter account using the Twitter API v2.
* Supports scheduling for regular tweeting intervals through github workflow.

## 🚀 Getting Started

### Prerequisites

* Python 3.9 or higher
* Twitter Developer Account with elevated access
* Twitter API credentials:
  * API Key
  * API Secret Key
  * Access Token
  * Access Token Secret
  * Gemini API Key

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DavJHKim/Cat-Facts-Twitter-Bot.git
   cd Cat-Facts-Twitter-Bot
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:** Create a `.env` file in the root directory and add your Twitter API credentials:

   ```env
   API_KEY=your_api_key
   API_SECRET_KEY=your_api_secret_key
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   GEMINI_API_KEY=your_access_token_secret
   ```

### Running the Bot Locally

To test the bot locally, run:

```bash
python main.py
```

This will fetch a random cat fact and post it to your configured Twitter account and deploy the tweets every 24 hours through a github workflow

## ☁️ Deployment on Google Cloud Functions

## 🛠️ Project Structure

```
Cat-Facts-Twitter-Bot/
├── .github/                  # GitHub Actions 
│   └── run-twitter-bot.yml   # GitHub Workflow action
├── Media/                    # Media assets
├── config/                   # Configuration files
│   └── config.py             # Config script
├── docs/                     # Documentation
├── src/                      # Source code
│   └── gemini.py             # Gemini API script
│   └── twitter_bot.py        # Twitter API script
├── main.py                   # Main application script
├── .gitignore                # Git ignore file
├── .env                      # .env file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any inquiries or feedback, please open an issue on the [GitHub repository](https://github.com/DavJHKim/Cat-Facts-Twitter-Bot/issues).
