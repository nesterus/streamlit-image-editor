import cv2
from matplotlib import pyplot as plt


def colors_hist(img):
    color = ('b', 'g', 'r')
    fig, ax = plt.subplots()
    ax.set_title('RGB')
    ax.set_xticks([])
    ax.set_yticks([])

    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax.plot(histr, color=col)

    return fig
