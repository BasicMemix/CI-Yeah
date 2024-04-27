from PIL import Image
import streamlit as st

img_contact_form5 = Image.open("images/image6.jpg")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form5)
        with text_column:
            st.title("Koi dikkat hai? 😢")
            st.header("Talk to us 🤟")
            st.write("##")
            contact_form = """
            <form action="https://formsubmit.co/singhanadi18@gmail.com" method="POST">
            <input type="text" name="name" PlaceHolder="Your Name" required>
            <input type="email" name="email" PlaceHolder="Your E-Mail" required>
            <textarea name="Message" PlaceHolder="Your Message Here" required></textarea>
            <button type="submit">Send</button>
            </form>
            """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
