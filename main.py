import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie


st.set_page_config(page_title="For mummy", page_icon=":tada:", layout="wide")

st.subheader('Happy Birthday Mummy! look I made a website!'
             '')
st.title('I love you')
st.write("Thankyou so much for raising me and thinking about my needs and loving me. You are the best mother I love "
         "you the most")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_bfwzjr7h.json")
st_lottie(lottie_hello,
          speed=1,
          loop=True,
          height=360,
          width=360)

lottie_second = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jzmdkj5n.json")
st_lottie(lottie_second,
          speed=1,
          loop=True,
          height=500,
          width=500)

st.title("My E-cards")
st.image("Happy b'day (1).jpg")
st.image("I LOVE U.jpg")

st.title("YOU ARE SPECIAL")
