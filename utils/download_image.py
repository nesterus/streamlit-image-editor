from PIL import Image


def download_image(state, block):
    tmp_path = './tmp/processed.png'
    img = Image.fromarray(state['image'])
    img.save(tmp_path)

    with open(tmp_path, 'rb') as file:
        btn = block.download_button(
            label='Download the processed image',
            data=file,
            file_name="processed.png",
            mime='image/png')
