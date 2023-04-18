import tensorflow as tf
from PIL import Image
import numpy as np
import streamlit as st

@st.cache_data()
def load_image(upload_img):
    img = Image.open(upload_img).convert('RGB')
    img = np.asarray(img)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

@st.cache_data()
def view_image(image_file):
    img = Image.open(image_file)
    return img

@st.cache_data()
def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return Image.fromarray(tensor)
