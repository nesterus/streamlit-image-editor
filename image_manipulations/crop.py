from PIL import Image
from utils import *

'''def crop(state, block):
    w = block.slider('width', min = 0)
    h = block.slider('hight', min = 0)
    img = state['image']
    start = tuple(map(lambda a, da: a//2-da//2, img.shape, 10))
    end = tuple(map(operator.add, start, (0,5)))
    slices = tuple(map(slice, start, end))
    state['image'] = img[slices]
'''

def crop(state,block):
    img = state['image']
    maximaly = img.shape[0]
    maximalx = img.shape[1]
    cropx = block.slider('width',min_value=maximalx//6, max_value=maximalx,value=maximalx//2)
    cropy = block.slider('hight',min_value=maximaly//6, max_value=maximaly,value=maximaly//2)
    y,x = maximaly, maximalx
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    state['image'] = img[starty:starty+cropy,startx:startx+cropx]