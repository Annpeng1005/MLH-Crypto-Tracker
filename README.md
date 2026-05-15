# MLH Crypto Tracker

## Video Script
https://github.com/user-attachments/assets/81d526fd-7989-4587-a408-0d7d75cb3589

## Purpose of the Project

MLH Crypto Tracker is a Python backend project that monitors live cryptocurrency prices, detects major 24-hour drops, retrieves related crypto news, and uses Gemini AI to generate professional Slack-style alerts.

The purpose is to turn raw market data into useful, context-aware insights for a trading or operations team.

---

## Files Included

main.py
Runs the full project workflow.

crypto_client.py
Handles API calls to CoinGecko, CryptoCompare, and Slack.

ai_agent.py
Sends market data and news headlines to Gemini and generates AI-powered alerts.

utils.py
Contains helper logic for filtering coins, checking drops, extracting headlines, and formatting alerts.

market_alerts.txt
Output file containing AI-generated alerts or a stable-market message.

requirements.txt
Lists required Python packages.

README.md
Explains setup, usage, and project purpose.

---

## Packages Installed

This project uses:
requests
google-genai
python-dotenv


## How to Run
pip install -r requirements.txt

Create a .env file:

GEMINI_API_KEY=your_gemini_key
CRYPTO_API_KEY=your_cryptocompare_key
SLACK_WEBHOOK_URL=your_slack_webhook_url

## Run:

python main.py
What to Expect After Running

The program will fetch live crypto prices, check for coins that dropped past the threshold, retrieve related news, generate a Gemini AI alert, send it to Slack, and save the result in market_alerts.txt.

If no coin drops enough, the output will say:

Market is stable today.

## System Design Diagram

<img width="1016" height="1128" alt="image" src="https://github.com/user-attachments/assets/03326d7b-233e-47ae-8f00-86b1aaca2cf3" />




