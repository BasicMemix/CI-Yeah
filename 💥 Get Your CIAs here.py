from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Pick you CIAs from here 😙", page_icon="🫡", layout="wide")

img_contact_form3 = Image.open("images/image5.jpg")
img_contact_form4 = Image.open("images/image4.jpg")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form3)
    with text_column:
        st.header("Need reference for your CIA? 😛")
        st.subheader('Koi na, We will help!!😘')
        st.subheader("Just don't forget to put in your creativity and initiative 🤩!!")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form4)
    with text_column:
        st.header("Ab yaha tak aa gaye ho 😬")
        st.subheader("Pick your desired CIA from the link below 💕")
        st.write(
            """ 
            - We hope you must have uploaded your previous sem/current sem CIAs in the google form on the Home page 😺

            - If not, Then please do it so others can also be helped 😻

            - Find the CIA of your choice by using required filters : https://shorturl.at/dmqA9 😽
            - ( Kuch to kaam karle bhai )

            - Enjoy!❤
            """
        )

