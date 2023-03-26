import streamlit as st
from PIL import Image
from preprocess import view_image
from predict import transfer
import cv2
import base64

st.title('Glorifying Monuments in Odisha')

st.subheader("Content Image")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('download.png')


content_image = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], key='content_image')

if content_image is not None:
    file_details = {"filename": content_image.name, "filetype": content_image.type,
                    "filesize": content_image.size}
    st.write(file_details)
    st.image(view_image(content_image), width=400)

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
