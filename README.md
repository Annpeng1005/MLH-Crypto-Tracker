# MLH Crypto Tracker

AI-powered cryptocurrency monitoring system that detects market drops, retrieves related news, and generates contextual Slack alerts using Gemini AI.

---

## Purpose

MLH Crypto Tracker monitors live cryptocurrency prices, detects significant 24-hour market drops, retrieves related news, and uses Gemini AI to generate professional Slack-style alerts.

Instead of only reporting that a coin dropped, the system attempts to explain *why* by combining market data with real-time news context.

The goal is to transform raw market data into useful insights for a trading or operations team.

---

## System Architecture

![System Diagram](images/system_architecture.png)

This project combines several services and processing components:

- `CoinGecko API`
    - Retrieves live cryptocurrency prices and 24-hour percentage changes

- `Drop Detection Logic`
    - Applies business rules and checks alert thresholds

- `CryptoCompare API`
    - Retrieves related crypto news headlines

- `Gemini AI`
    - Uses Retrieval-Augmented Generation (RAG) to generate contextual summaries

- `Slack Webhook`
    - Sends AI-generated notifications

- `market_alerts.txt`
    - Stores local outputs

---

## Workflow

1. Run the application:

```bash
python main.py
```

2. Retrieve live crypto prices from CoinGecko

3. Detect whether any coin exceeds the alert threshold

4. Retrieve related news headlines

5. Pass market + news context to Gemini AI

6. Generate AI-powered alerts

7. Save output and send Slack notifications

---

## Project Structure

`main.py`

Controls and orchestrates the full application workflow.

`crypto_client.py`

Handles API requests to CoinGecko, CryptoCompare, and Slack.

`ai_agent.py`

Builds prompts and communicates with Gemini AI.

`utils.py`

Contains helper functions, filtering logic, and reusable business rules.

`market_alerts.txt`

Stores generated alerts or stable market output.

`requirements.txt`

Lists required project dependencies.

---

## Packages Installed

```bash
requests
google-genai
python-dotenv
slack-sdk
```

---

## Setup

Install required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_key

CRYPTO_API_KEY=your_key

SLACK_WEBHOOK_URL=your_webhook_url
```

---

## Run Project

```bash
python main.py
```

---

## Example Output

Stable market:

```text
Market is stable today.
```

AI-generated alert:

```text
🚨 Bitcoin dropped 6.2% today.

Recent headlines suggest increased volatility and uncertainty surrounding regulatory developments.
```

Slack:

```text
[Slack notification sent successfully]
```

---

## Prompt Engineering

Gemini receives structured market and news context.

Example:

```text
Act as a financial analyst.

Coin: Bitcoin

24-hour drop: -6.2%

Price: $64,500

Recent headlines:

- ETF uncertainty increases volatility
- Bitcoin selloff continues
- Market sentiment weakens

Write a concise Slack alert explaining possible reasons for the movement.
```

Providing retrieved news context reduces hallucination and improves response quality.

---

## Defensive Programming

Since external APIs may fail or return incomplete data, defensive checks were added throughout the application.

Examples include:

- Verifying `response.status_code == 200`
- Checking whether JSON keys exist
- Handling empty responses
- Skipping failed requests
- Preventing invalid API calls

This prevents a single failure from crashing the full workflow.

---

## Future Roadmap

Potential Phase 2 improvements:

- SQLite database integration
- ETL pipelines for historical storage
- Scheduled cloud deployment
- Personalized alert preferences
- User authentication
- Discord and email support
- Dashboard analytics

---

## Concepts Used

- APIs
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Webhooks
- Defensive Programming
- Modular Project Structure
- Event Detection
- Data Pipelines




