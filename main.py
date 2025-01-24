import streamlit as st
import requests
import pandas as pd

# API key setup
API_KEY = "YOUR_API_KEY" 

# Streamlit app title
st.title("Wealthify")

# Input for stock symbol
ticker = st.text_input("Enter a stock ticker (e.g., AAPL):")

if ticker:
    # Fetch stock data from Polygon.io
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        
        # Display data
        if results:
            st.write(f"**Stock Data for {ticker.upper()}:**")
            for item in results:
                st.write(f"Date: {pd.to_datetime(item['t'], unit='ms').date()}")
                st.write(f"Open: ${item['o']}")
                st.write(f"High: ${item['h']}")
                st.write(f"Low: ${item['l']}")
                st.write(f"Close: ${item['c']}")
                st.write(f"Volume: {item['v']}")
        else:
            st.error("No data found for the given ticker.")
    else:
        st.error(f"Error fetching data: {response.status_code}")
