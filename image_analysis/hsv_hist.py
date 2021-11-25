import cv2
from matplotlib import pyplot as plt


def hsv_hist(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color = ('b', 'g', 'r')
    fig, ax = plt.subplots()
    ax.set_title('HSV')
    ax.set_xticks([])
    ax.set_yticks([])

    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax.plot(histr, color=col)

    return fig
