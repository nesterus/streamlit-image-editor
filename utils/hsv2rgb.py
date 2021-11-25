from skimage import color
import numpy as np


def hsv2rgb(img):
    return (color.hsv2rgb(img) * 255).astype(np.uint8)
