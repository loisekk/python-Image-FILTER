import streamlit as st
from PIL import Image, ImageFilter


st.title("Image Filter Application")

file = st.file_uploader("Select Image", type=["png", "jpg", "jpeg"])

if file:
    option = st.selectbox(
        label = "Select Filter option",
        options = ["Real", "GrayScale", "Blur", "Emboss"]
    )

    img = Image.open(file)
    if option == "GrayScale":
        img = img.convert("L")
    if option == "Blur":
        img = img.filter(ImageFilter.BLUR)
    if option == "Emboss":
        img = img.filter(ImageFilter.EMBOSS)
    
    st.image(img)

    file.seek(0)
    img.save(file, format ='PNG')

    st.download_button("Download Image", data=file, file_name="filtered_image.png", mime="image/png")