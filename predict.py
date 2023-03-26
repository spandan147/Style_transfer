from model import model
from preprocess import load_image
import tensorflow as tf
import numpy as np
import cv2
import streamlit as st
from PIL import Image

def transfer(content_image, style_image):
    content_image = load_image(content_image)
    style_image = load_image(style_image)
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.keras.utils.array_to_img(
        stylized_image[0], data_format=None, scale=True, dtype=None
    )
    stylized_image.save('generated_img.jpg')
    return 'generated_img.jpg'

