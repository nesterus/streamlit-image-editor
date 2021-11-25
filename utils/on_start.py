from utils import read_json
import os, shutil


def on_start(state):
    general_config = read_json('./configs/general.json')

    if general_config['clear_image']:
        state['image'] = None

    if general_config['clear_config_on_start']:
        for filename in os.listdir(general_config['tmp_file']):
            file_path = os.path.join(general_config['tmp_file'], filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    return state
