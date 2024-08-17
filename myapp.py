
import yfinance as yf
import streamlit as st
st.set_page_config(layout="wide")
st.write("""
# Simple Stock Price data visualisation

## the stock closing price Tesla!

""")


#define the ticker symbol
tickerSymbol = 'TSLA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)

st.write("""
         ## the stock and volume of Tesla!

""")
st.line_chart(tickerDf.Volume)

st.markdown("![gifs](https://media.giphy.com/media/AcfTF7tyikWyroP0x7/giphy.gif?cid=790b7611jd44ansz29oq8whryr08t7p1efqbb54ebshrqs1w&ep=v1_gifs_search&rid=giphy.gif&ct=g)")
