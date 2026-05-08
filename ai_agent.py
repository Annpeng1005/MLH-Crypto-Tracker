def make_ai_alert(coin_name, change, price, titles, client):

    headline_text = ""
    for title in titles:
        headline_text = headline_text + title + "\n"

    prompt = f"""
  Act as financial analyst,

  coin:{coin_name}
  24-hour change: {change}%
  Current price: ${price}

  Recent news headlines:
  {headline_text}

  Write a professional, urgent 2-sentence Slack alert explaining the price drop using only the news conext above.
  """

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)

    ai_alert = response.text
    return ai_alert
