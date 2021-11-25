from utils import *
from image_analysis.colors_hist import colors_hist
from image_analysis.hsv_hist import hsv_hist


def display_analysis(state, block):
    # block.write('Original image')
    block.pyplot(render_image(state['original_image']))
    block.write('H:{}, W:{}, C:{}'.format(*state['image'].shape))
    block.write(
        'Min:{}, median:{}, max:{}'.format(round(state['image'].min(), 1), round(state['image'].mean(), 1),
                                           round(state['image'].max(), 1)))
    block.write(state['image'].dtype)
    block.pyplot(colors_hist(state['image']))
    block.pyplot(hsv_hist(state['image']))
