import requests
import os
from datetime import date
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = os.environ.get('ALPHAVANTAGE_API_KEY')
API_KEY_NEWS = os.environ.get('NEWSAPI_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
to_number = os.environ.get('TO_NUMBER')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

d = date.today()  # get current date
day = d.day  # get the day of the month as an integer
day_before = day - 1

parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCK,
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
data = response_stock.json()
closing_price = float(data["Time Series (Daily)"][f"2023-04-{day_before}"]["4. close"])
print(closing_price)

# Get the day before yesterday's closing stock price
day_b_yesterday = day - 2
closing_price_dby = float(data["Time Series (Daily)"][f"2023-04-{day_b_yesterday}"]["4. close"])
print(closing_price_dby)

# Find the positive difference between 1 and 2 but the positive difference is 20.
difference_price = round(abs(closing_price - closing_price_dby), 2)
print(f"The difference in prices is {difference_price}")

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
percentage_difference_in_price = (closing_price * 100) / closing_price_dby
final_percentage_difference_in_price = round(percentage_difference_in_price - 100, 2)
print(f"The percentage difference in prices is {final_percentage_difference_in_price}%")

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
parameters_news = {
    "q": "Tesla",
    "from": f"{day_before}",
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWS,
}

response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
news_articles = response_news.json()
articles = news_articles['articles']

# Use Python slice operator to create a list that contains the first 3 articles. Hint:
if final_percentage_difference_in_price > 1:
    article_list = []
    for article in articles[:3]:
        article_dict = {
            'title': article['title'],
            'description': article['description'],
            'url': article['url']
        }
        article_list.append(article_dict)

# Create a new list of the first 3 article's headline and description using list comprehension.
article_list = [{'title': article['title'], 'description': article['description'], 'url': article['url']}
                for article in articles[:3]]

# Send each article as a separate message via Twilio.
symbol = "🔻"
if final_percentage_difference_in_price > 0:
    symbol = "🔺"
for i in range(0, 3):
    current_article = article_list[i]

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+16204078779',
        body=f'TSLA: {symbol}{final_percentage_difference_in_price}%\n'
             f'Headline:{current_article["title"]}\n'
             f'Brief:{current_article["description"]}\n'
             f'Url:{current_article["url"]}',
        to='+254790758813'
    )
