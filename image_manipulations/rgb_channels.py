import numpy
from utils import *


def rgb_channels(state,block):
    img = state['image']
    default = 126
    r = block.slider('Red',value = default, min_value = 0,max_value = 255)
    g = block.slider('Green', value=default, min_value=0, max_value=255)
    b = block.slider('Blue', value= default, min_value=0, max_value=255)
    #img[img[:,:,1]<((r - default)<0)] = img[img[:,:,0]]=10
   # r = r-default
    #img[::, 0] += (r - default)5
    #img[:, :, 0] = img[:, :, 0] +  (r - default)
    #img[:, :, 0]= numpy.clip(img[:,:,0], 0, 255)
    img[:, :, 1] += abs(r - default)
    img[:, :, 1] += abs( g - default)
    img[:, :, 2] += abs( b - default)


#sdfsdfsdf
    state['image'] = img