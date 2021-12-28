import streamlit as st
import pandas as pd





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
    
    st.image("chart.png",caption="Crypto Currency Market Cap",width=400)

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
    col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
    col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
    col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
    col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
    col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
    col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
    col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )

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

