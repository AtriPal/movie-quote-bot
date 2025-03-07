# 📢 Twitter Auto Bot

### A Python bot that automatically tweets a random movie quote every 8 hours using GitHub Actions and Twitter API.


## 🛠️ Features

✅ Tweets a random movie quote from data/movie_quotes.csv

✅ Uses GitHub Actions to run automatically every 8 hours

✅ Supports manual workflow runs

✅ Built with Python and Tweepy


## 🚀 Setup Instructions

1️⃣ Fork & Clone the Repository

git clone https://github.com/YOUR_USERNAME/movie-quote-bot.git
cd movie-quote-bot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Twitter API Keys

Get your API keys from developer.twitter.com and set them in GitHub Secrets:


`API_KEY`

`API_SECRET_KEY`

`ACCESS_TOKEN`

`ACCESS_TOKEN_SECRET`

### 🤖 How It Works

1️⃣ scripts/read_quotes.py → Reads a random quote from movie_quotes.csv.

2️⃣ scripts/post_tweet.py → Posts the quote using Twitter API.

3️⃣ GitHub Actions (.github/workflows/tweet.yml) runs the bot every 8 hours.


### 📝 Running Locally

You can test the bot locally by running:


python scripts/post_tweet.py

### ⚙️ Automating with GitHub Actions

GitHub Actions will automatically run every 8 hours.


✅ To run it manually:

1️⃣ Go to GitHub → Actions

2️⃣ Select Movie Quote Twitter Bot

3️⃣ Click Run Workflow

#### 📌 Notes

🔹 Ensure your Twitter API has posting access (Twitter Basic Access doesn’t allow tweets).

🔹 Check GitHub Secrets if authentication fails.

🔹 Modify tweet.yml if you want a different schedule.


#### 📜 License

This project is open-source and free to use.
