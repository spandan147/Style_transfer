import streamlit as st
from PIL import Image
from preprocess import view_image
from predict import transfer
import cv2
import base64

# Update the title of the Streamlit app
st.set_page_config(page_title="Glorifying Monuments in India", layout='wide')
st.title("Glorifying Monuments in India")

# # Show a modal dialog
# if st.button('Open Dialog'):
#     st.markdown(
#         """
#         <div style='position:fixed;left:0px;top:0px;width:100%;height:100%;background-color:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;z-axis:100;'>
#         <div style='background-color:#ffffff;padding:20px;width:300px;'>
#         <h2 style='text-align:center;'>Dialog Title</h2>
#         <p style='text-align:center;'>Dialog Content</p>
#         <p style='text-align:center;'>
#         <button onclick='document.getElementById("dialog").style.display="none";'>Close</button>
#         </p>
#         </div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# Content Image
st.subheader("Upload images here:")


@st.cache_data()
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

content_image = st.file_uploader(
    "Upload Images", type=["png", "jpg", "jpeg"], key='content_image')

if content_image is not None:
    file_details = {"filename": content_image.name, "filetype": content_image.type,
                    "filesize": content_image.size}
    st.write(file_details)
    st.image(view_image(content_image), width=400)

# Style Image
st.subheader("Style Image")

style_Image = st.file_uploader(
    "Upload Images", type=["png", "jpg", "jpeg"], key='style_image')

if style_Image is not None:
    file_details = {"filename": style_Image.name, "filetype": style_Image.type,
                    "filesize": style_Image.size}
    st.write(file_details)
    st.image(view_image(style_Image), width=400)

# Stylize Button
clicked = st.button('Stylize')

if clicked:
    if style_Image is not None and content_image is not None:
        output_image = transfer(content_image, style_Image)
        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=400)
    elif style_Image is None:
        st.write('Please Upload Style Image')
    elif content_image is None:
        st.write('Please Upload Content Image')
    elif style_Image is None and content_image is None:
        st.write('Please Upload Style and Content Image')