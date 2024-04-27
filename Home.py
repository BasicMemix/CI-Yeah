from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="CI-Yeahhh", page_icon="🫡", layout="wide")
st.sidebar.success("Select the Pages above 👆")

img_contact_form = Image.open("images/image.png")
img_contact_form1 = Image.open("images/image1.png")
img_contact_form2 = Image.open("images/image3.png")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_study = load_lottieurl("https://lottie.host/107488e8-4fe6-4062-9d6a-be0801fa8985/yuSa83b8OU.json")
lottie_work = load_lottieurl("https://lottie.host/c8711280-fd20-42a5-8539-521dc5643cbe/rsxnK2ccg7.json")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.header("Welcome to CI-Yeahhh 😛")
        st.subheader('Got problems with CIAs? Chill out fam, WE HERE!!😘')
        st.title("Communicate with Cry-stites and Get your CIAs done in minutes 🤩!!")
        st.write("Submit your CIA's : https://forms.gle/NoPdZPiJ86eXUNSK8")

with st.container():
    st.write("----------")
    left_column, right_column = st.columns(2)
with left_column:
    st.header("Hum kya karte hai 🧐?")
    st.write(
        """
        Feeling overwhelmed bcoz of deadlines(😭) and unsure where to start? You're not alone!👊 We know juggling
        Classes📚, Activities💃 and a Social Life👩‍❤️‍💋‍👨 can make assignments feel like a mountain⛰ That's where we
        come in!😎 This website is your one-stop place for acing any assignment.
        We offer a variety of resources to help you!🔥
        """
    )
with right_column:
    st_lottie(lottie_study, height=220, key="study")

with st.container():
    st.write("---")
    st.header("HERE'S HOW EVERYTHING WORKS 🫡")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Step 1")
        st.write(
            """ 
            - Upload your CIA's with the required information for others 🤓
            
            - Submit your current sem/previous sem CIAs : https://forms.gle/NoPdZPiJ86eXUNSK8
            - Make sure the drive link should be accessible to everyone 😡
            
            - Co-operate with the above points please 🥹
            """
        )

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form1)
    with text_column:
        st.subheader("Step 2")
        st.write(
                """ 
                - Once you have uploaded all your current sem/previous sem CIAs
                - ( Mandatory hai yr, PLEASE DO IT ) 😺

                - Go to the Short URL link available on the next page in order to access all the CIAs 😻
                
                - Find the CIA of your choice by using required filters 😽
                - ( Kuch to kaam karle bhai )
                
                - Enjoy!❤
                """
            )
        