import streamlit as st
import numpy as np
from PIL import Image, ImageFile
import os

from utils import *
from image_analysis import *
from image_manipulations import *

ImageFile.LOAD_TRUNCATED_IMAGES = True

state = {
    'image': None,  # An active image to work with
    'original_image': None  # An active image to work with
}

state = on_start(state)  # Clear previous run data

show_analysis = st.sidebar.checkbox('Show image analysis', value=True)
main_block, analysis_block = None, None

if show_analysis:
    main_block, analysis_block = st.columns([5, 2])
else:
    main_block = st

if state['image'] is None:

    selected_gallery_image_name = st.sidebar.selectbox('Choose image from Gallery',
                                                       [None, *list_files('./data/gallery')])
    if selected_gallery_image_name is not None:
        img = np.array(Image.open(os.path.join('./data/gallery', selected_gallery_image_name)))
        state['image'] = img.copy()
        state['original_image'] = img.copy()

    datafile = st.sidebar.file_uploader("Or upload your file", type=['png'])
    if datafile is not None:
        img = upload_image(datafile)
        state['image'] = img.copy()
        state['original_image'] = img.copy()

# Display an image in the main block
if state['image'] is not None:

    # Image manipulations
    if st.sidebar.checkbox('Adjust HSV', value=True):
        adjust_hsv(state, st.sidebar)
        main_block.info('More info on HSV colorspace: https://ru.wikipedia.org/wiki/HSV_(%D1%86%D0%B2%D0%B5%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C)')

    main_block.pyplot(render_image(state['image']))
    download_image(state, st.sidebar)

    if analysis_block is not None:
        display_analysis(state, analysis_block)
