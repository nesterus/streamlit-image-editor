from matplotlib import pyplot as plt


def render_image(img):
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(img)
    return fig
