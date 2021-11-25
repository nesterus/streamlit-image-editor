from utils import *


def adjust_hsv(state, block):
    DEFAULT_HUE = .5

    hsv_img = rgb2hsv(state['image'])

    h = block.slider('Hue', min_value=0., max_value=1., value=DEFAULT_HUE)
    hsv_img[:, :, 0] += (h - DEFAULT_HUE) % 1.

    # TODO: adjust saturation and brightness

    state['image'] = hsv2rgb(hsv_img)
