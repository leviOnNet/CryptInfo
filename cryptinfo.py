import streamlit as st
import pandas as pd
from rates import rate
from binance import AsyncClient
from binance.client import Client
import config1
from pandas.core.frame import DataFrame
from datetime import datetime

client = Client(config1.API_KEY, config1.API_SECRET)
symbol_df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')


# Load market data from Binance API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)

options = st.sidebar.selectbox("Choose Dashboard",('Getting Started with Crypto','Prices','graphs','Crypto Wallets and Exchanges','Tokens'))

st.header(options)


if options == 'Getting Started with Crypto':
    
    st.subheader("What is Crypto Currency and why should you care?")
    st.write("Crypto-currency is a  digital currency in which transactions are verified and records maintained by a decentralized system using cryptography, rather than by a centralized authority. It makes use of the blockchain system to create, dispense, log and verify transactions.")
    
    st.image("chart1.png",caption="Crypto Currency Market Cap",width=300)

    st.write("As seen on the image above from coinmarketcap.com, the market cap for crypto-currencies has increased exponentially with Bitcoin Leading the way. with a rise in online payment systems, and web3 around the corner, online ecosystems are growing fast and crypto-currency is the prefered method of payment for many as the market caps prove.")

    st.subheader("Is it too late to get started?")
    st.write("No. it is actually still early days with regards to the full scope of possible implementations of this technology.")

    st.subheader("So, where to start?")
   
    st.write("The answer this really depends on your location/region. some countries are embracing the technology while others are not (Including South Africa), this mostly due the fact that masses are not educated enough on the subject and this creates a huge space for scams, user mistakes or actions which might cause people to loose money.")
    st.write("The main reason I created this app is to keep people informed about crytos and set out safe ways for people to navigate this new and vast field. Check out varified crypto wallets below")
    url_btn = st.button('View Crypto Wallets')
    
    
    if url_btn:
        options ='Crypto Wallets1'

if options == 'Crypto Wallets1':
    link1='[Luno](https://luno.com/)'
    st.markdown(link1,unsafe_allow_html=True)
    link2 = '[Cryto.com](https://crypto.com/)'
    st.markdown(link2,unsafe_allow_html=True)
    link3 = '[Binance](https://binance.com/)'
    st.markdown(link3,unsafe_allow_html=True)

if options == 'graphs':
    col1_selection = st.selectbox('Select Pair', symbol_df.symbol, list(symbol_df.symbol).index('BTCUSDT') )
    col1_df = symbol_df[symbol_df.symbol == col1_selection]
    symbol =pd.DataFrame({"symbol":col1_df["symbol"]},index=None,dtype=str)
    symbol["symbol"] = symbol["symbol"].astype(str)
    for s in symbol["symbol"]:
        

        candlesticks = client.get_historical_klines(s, AsyncClient.KLINE_INTERVAL_6HOUR, "4 day ago UTC")

        processed_candlesticks = []
        processed_time_candlesticks = []
        closes = []

    for data in candlesticks:
            candlestick = { 
                "time": data[0]/1000 , 
                "open": data[1],
                "high": data[2], 
                "low": data[3], 
                "close": float(data[4])*rate
            }


            processed_candlesticks.append(candlestick)
            True_candlestickts = DataFrame(processed_candlesticks)
            processed_time_candlesticks.append(candlestick["time"])
            closes.append(candlestick["close"])
            
            
    timestamps = []
    for i in processed_time_candlesticks:
        timestamp = datetime.fromtimestamp(i)
        timestamps.append(timestamp)
    timestamp_cleaned = []
    for i in timestamps:
        timestamp_clean = i.strftime('%Y-%m-%d %H:%M:%S')
        timestamp_cleaned.append(timestamp_clean)


    Closes_with_date = pd.DataFrame({"Closes":closes,"Time":timestamp_cleaned})
    Closes_with_date = Closes_with_date.set_index('Time')
    st.write(s)
    st.line_chart(Closes_with_date,width=300,height=500,use_container_width=False)
if options == 'Crypto Wallets and Exchanges':
    
    st.write('For beginners, Luno is the simplest exchange in the market. I would suggest using it especially given that the south african gorvenment has banned users from depositing directly into Binance and other Unregulated exchanges. However, there is a workaround, once you have buy crypto in Luno it is easy to transer the funds to other exchanges.')
    st.write("Watch this video on how Luno works")
    link1='[Luno Link](https://luno.com/)'
    st.markdown(link1,unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=t0otWTvgB64')
    st.write('')
    st.write('')
    st.write("Watch this video on how Binance works")
    link3 = '[Binance Link](https://binance.com/)'
    st.markdown(link3,unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=AjIsqkNFx1c')
    st.write('')
    st.write('')
    st.write("Watch this video on how Crypto.com works")
    link2 = '[Cryto.com Link](https://crypto.com/)'
    st.markdown(link2,unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=K8qYdD1sC7w')
    st.write('')
    st.write('')
    st.write("Watch this video on how coinbase works")
    link4 = '[Cryto.com Link](https://coinbase.com/)'
    st.markdown(link4,unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=o9TZCCE6l3E')
    st.write('')
    st.write('')
    st.write('Honourable mention to EasyEquities with thier EC10 package')
    link5 = '[EasyEquities Link](https://www.easyequities.co.za/)'
    st.markdown(link2,unsafe_allow_html=True)

    st.video('https://www.youtube.com/watch?v=0K3AhBGk3mo')

    
if options == 'Prices':
    # Widget (Cryptocurrency selection box)
    col1_selection = st.sidebar.selectbox('Pair 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    col2_selection = st.sidebar.selectbox('Pair 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    col3_selection = st.sidebar.selectbox('Pair 3', df.symbol, list(df.symbol).index('BNBBUSD') )
    col4_selection = st.sidebar.selectbox('Pair 4', df.symbol, list(df.symbol).index('XRPBUSD') )
    col5_selection = st.sidebar.selectbox('Pair 5', df.symbol, list(df.symbol).index('ADABUSD') )
    col6_selection = st.sidebar.selectbox('Pair 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
    col7_selection = st.sidebar.selectbox('Pair 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
    col8_selection = st.sidebar.selectbox('Pair 8', df.symbol, list(df.symbol).index('DOTBUSD') )
    col9_selection = st.sidebar.selectbox('Pair 9', df.symbol, list(df.symbol).index('MATICBUSD') )

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]
    col2_df = df[df.symbol == col2_selection]
    col3_df = df[df.symbol == col3_selection]
    col4_df = df[df.symbol == col4_selection]
    col5_df = df[df.symbol == col5_selection]
    col6_df = df[df.symbol == col6_selection]
    col7_df = df[df.symbol == col7_selection]
    col8_df = df[df.symbol == col8_selection]
    col9_df = df[df.symbol == col9_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)
    col2_price = round_value(col2_df.weightedAvgPrice)
    col3_price = round_value(col3_df.weightedAvgPrice)
    col4_price = round_value(col4_df.weightedAvgPrice)
    col5_price = round_value(col5_df.weightedAvgPrice)
    col6_price = round_value(col6_df.weightedAvgPrice)
    col7_price = round_value(col7_df.weightedAvgPrice)
    col8_price = round_value(col8_df.weightedAvgPrice)
    col9_price = round_value(col9_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    col2_percent = f'{float(col2_df.priceChangePercent)}%'
    col3_percent = f'{float(col3_df.priceChangePercent)}%'
    col4_percent = f'{float(col4_df.priceChangePercent)}%'
    col5_percent = f'{float(col5_df.priceChangePercent)}%'
    col6_percent = f'{float(col6_df.priceChangePercent)}%'
    col7_percent = f'{float(col7_df.priceChangePercent)}%'
    col8_percent = f'{float(col8_df.priceChangePercent)}%'
    col9_percent = f'{float(col9_df.priceChangePercent)}%'

    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    col2.metric(col2_selection, col2_price, col2_percent)
    col3.metric(col3_selection, col3_price, col3_percent)
    col1.metric(col4_selection, col4_price, col4_percent)
    col2.metric(col5_selection, col5_price, col5_percent)
    col3.metric(col6_selection, col6_price, col6_percent)
    col1.metric(col7_selection, col7_price, col7_percent)
    col2.metric(col8_selection, col8_price, col8_percent)
    col3.metric(col9_selection, col9_price, col9_percent)

    st.header('**All Price**')
    st.dataframe(df)

    st.info('Credit: Created by Levi ((https://instagram.com/Levi_eloco))')

    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)

