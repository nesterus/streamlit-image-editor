from utils import *


def adjust_hsv(state, block):
    default = .5

    hsv_img = rgb2hsv(state['image'])

    h = block.slider('Hue', min_value=0., max_value=1., value=default)
    hsv_img[:, :, 0] += (h - default) % 1.

    # TODO: adjust saturation and brightness

    s = block.slider('Saturation', min_value=0., max_value=1., value=default)
    hsv_img[:, :, 1] += (s - default) % 1.

    v = block.slider('Value', min_value=0., max_value=1., value=default)
    hsv_img[:, :, 2] += (v - default) % 1.

    state['image'] = hsv2rgb(hsv_img)