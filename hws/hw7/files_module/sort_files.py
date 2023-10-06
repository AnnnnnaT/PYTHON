import os
import shutil

EXTENSIONS = {
    'videos': ['.mp4',  '.mov'],   
    'texts': ['.txt', '.doc', '.pdf'],
    'images': ['.jpg', '.png']
}

def sort_files(dir):
    for ext in EXTENSIONS.keys():
        os.makedirs(ext)
    dir_files = os.listdir(dir)
    for item in dir_files:
        ext = '.' + item.split('.')[1]
        for key, value in EXTENSIONS.items():
            if ext in value:
                shutil.move(os.path.join(dir, item), os.path.join(key, item))


