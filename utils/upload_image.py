import os
from matplotlib import pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image


def upload_image(file):
    with open(os.path.join("./tmp", file.name), "wb") as f:
        f.write(file.getbuffer())

    # return np.array(plt.imread(os.path.join("./tmp", file.name)))
    return np.array(Image.open(os.path.join("./tmp", file.name)))
