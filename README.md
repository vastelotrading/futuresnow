# Newtures
Binance Futures trading bot

Please read comments in `strategy.py` for more information about trading options

Option #1: Scanning all available symbols on Futures Market and place orders when meet conditions

Option #2: Selected symbols only

Requirements:

Python 3.7 or above, Pip

Setup on your local machine:

1.Install all required libraries in `requirements.txt` by run this following command 

`pip install -r requirements.txt`

2.Read instruction comments in `strategy.py` and set your own strategy

3.Run `clock.py`

Note: This is a Heroku bot and use TA-Lib as technical indicators library so you need include TA-Lib buildpack for your Heroku app

`https://elements.heroku.com/buildpacks/numrut/heroku-buildpack-python-talib`

because this library cannot be build through pip alone
