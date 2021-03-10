# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:31:39 2021

@author: Stephen
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key_path = "C:\\sandbox\\alphavantage\\key.txt"

ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
data = ts.get_daily(symbol='EURUSD', outputsize='full')[0]
data.columns = ["open", "high", "low", "close", "volume"]

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "GOOG", "FB"]
close_prices = pd.DataFrame()
for ticker in all_tickers:
    starttime= time.time()
    ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
    data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')[0]
    data.columns = ["open", "high", "low", "close", "volume"] 
    close_prices[ticker] = data["close"]
