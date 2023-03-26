import streamlit as st
from PIL import Image
from preprocess import view_image
from predict import transfer
import cv2

st.title('Glorifying Monuments in Odisha')

st.subheader("Content Image")
content_image = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], key='content_image')

if content_image is not None:
    file_details = {"filename": content_image.name, "filetype": content_image.type,
                    "filesize": content_image.size}
    st.write(file_details)
    st.image(view_image(content_image), width=400)
bg = PhotoImage(file = "download.png")
st.subheader("Style Image")
style_Image = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], key='style_image')

if style_Image is not None:
    file_details = {"filename": style_Image.name, "filetype": style_Image.type,
                    "filesize": style_Image.size}
    st.write(file_details)
    st.image(view_image(style_Image), width=400)

clicked = st.button('Stylize')

if clicked:
    if style_Image is not None and content_image is not None:
        output_image = transfer(content_image, style_Image)
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    else:
        st.write('Please Upload files properly')
