from binance.client import Client
import binance

#Credential data
"""
Create a Binance API and remember to allow futures trading
"""
api_key = 'YOUR_API_ADDRESS'
api_secret = 'YOUR_API_SECRET'

client = Client(api_key, api_secret)