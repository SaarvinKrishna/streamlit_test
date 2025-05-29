import streamlit as st
import requests

# Set the app title
st.title('Currency Converter (MYR Based)')

# Welcome message
st.write('Selamat Datang to my Streamlit app!')

# User input for custom message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Fetch currency rates
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Currency selection dropdown
    currency_options = sorted(rates.keys())
    target_currency = st.selectbox('Select target currency:', currency_options)

    # Amount input
    amount_myr = st.number_input('Enter amount in MYR:', min_value=0.0, value=1.0, step=0.1)

    # Conversion calculation
    converted_amount = amount_myr * rates.get(target_currency, 0)
    st.write(f"{amount_myr:.2f} MYR = {converted_amount:.2f} {target_currency}")

    # Show full JSON response (optional)
    with st.expander("Show full API response"):
        st.json(data)

else:
    st.error(f"API call failed with status code: {response.status_code}")


