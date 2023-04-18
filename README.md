**Stock News Alert**
Stock News Alert is a Python program that uses the Alpha Vantage API and the News API to get the latest stock prices and news articles related to a particular company. 
If the difference in stock prices between two consecutive days is greater than 1%, the program sends an SMS alert to a specified phone number using the Twilio API.

**Requirements**
Python 3.6+
Alpha Vantage API key
News API key
Twilio API key and phone number

**Installation**
To get started, clone this repository to your local machine:

_git clone https://github.com/yourusername/stock-news-alert.git_

Then, install the required packages using pip:

_pip install -r requirements.txt_

**Usage**
To run the program, execute the main.py file:

_python main.py_

The program will prompt you to enter your Twilio phone number, the phone number you want to send the alerts to, and your API keys for Alpha Vantage, News API, and Twilio.

If the difference in stock prices between two consecutive days is greater than 1%, the program will retrieve the top news articles related to the specified company and send an SMS alert for each of the top three news articles.

**Configuration**
To configure the program, create a .env file in the root directory of the project and add your API keys and phone numbers:

_ALPHAVANTAGE_API_KEY=<your alphavantage api key>_
_NEWSAPI_API_KEY=<your newsapi api key>_
_TWILIO_ACCOUNT_SID=<your twilio account sid>_
_TWILIO_AUTH_TOKEN=<your twilio auth token>_
_TO_NUMBER=<phone number to send the alerts to>_

**Contributing**
Contributions are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository.


