import streamlit as st
from PIL import Image
from preprocess import view_image
from predict import transfer
import cv2
import base64

# Update the title of the Streamlit app
st.set_page_config(page_title="Glorifying Monuments in India", layout='wide')
st.title("Glorifying Monuments in India")

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

content_image_placeholder = st.empty()
content_image = content_image_placeholder.file_uploader(
    "Upload Images", type=["png", "jpg", "jpeg"], key='content_image')
# content_image = st.file_uploader(
#     "Upload Images", type=["png", "jpg", "jpeg"], key='content_image')

if content_image is not None:
    # file_details = {"filename": content_image.name, "filetype": content_image.type,
    #                 "filesize": content_image.size}
    # st.write(file_details)
    st.image(view_image(content_image), width=200)

# Style Image
st.subheader("Style Image")

# style_Image = st.file_uploader(
#     "Upload Images", type=["png", "jpg", "jpeg"], key='style_image')
style_Image_placeholder = st.empty()
style_Image = style_Image_placeholder.file_uploader(
    "Upload Images", type=["png", "jpg", "jpeg"], key='style_image')

if style_Image is not None:
    # file_details = {"filename": style_Image.name, "filetype": style_Image.type,
    #                 "filesize": style_Image.size}
    # st.write(file_details)
    st.image(view_image(style_Image), width=200)

# Stylize Button
clicked = st.button('Stylize')

if clicked:
    if style_Image is not None and content_image is not None:
        output_image = transfer(content_image, style_Image)
        st.write('### Output image:')
        image = Image.open(output_image)

        # Load the output image on a new page using an expander or sidebar
        with st.expander("Output Image", expanded=True):
            st.image(image, width=400, use_column_width=True)

        # # Remove uploaded images from display
        # content_image = None
        # style_Image = None

        # Remove uploaded images from display and clear the placeholders
        content_image_placeholder = st.empty()
        style_Image_placeholder = st.empty()

        # Refresh Button
        if st.button('Refresh', key='refresh_button'):
            st.caching.clear_cache()
    # if style_Image is not None and content_image is not None:
    #     output_image = transfer(content_image, style_Image)
    #     st.write('### Output image:')
    #     image = Image.open(output_image)
    #     st.image(image, width=400)

    #     # Remove uploaded images from display
    #     content_image = None
    #     style_Image = None

    #     # Refresh Button
    #     if st.button('Refresh', key='refresh_button'):
    #         st.caching.clear_cache()

    elif style_Image is None:
        st.write('Please Upload Style Image')
    elif content_image is None:
        st.write('Please Upload Content Image')
    elif style_Image is None and content_image is None:
        st.write('Please Upload Style and Content Image')

# Refresh Button
if st.button('Refresh'):
    st.caching.clear_cache()
    # Add code to reset any states or variables if necessary