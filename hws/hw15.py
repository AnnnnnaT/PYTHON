# Напишите код, который запускается из командной строки и получает на 
# вход путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога, 
# ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
from collections import namedtuple
import os 
import  argparse

my_format = ("{levelname} - {asctime}")
logging.basicConfig(filename='hws\files.log', filemode='a', encoding='UTF-8',
level=logging.INFO, style='{', format=my_format)
logger = logging.getLogger(__name__)

Result = namedtuple("Result", ["имя", "расширение", "родительский каталог"], defaults=[None, None, None])

def walk_dir(path: str = os.getcwd()):
    items = []
    path = os.path.abspath(path)
    parent = path.rstrip('/').rsplit('/', 1)[1]
    try:
        for item in os.listdir(path):
            name, ext = None, None
            item: str = item.rsplit('/',1)[1]
            if item.rfind('.') != -1 and not item.startswith('.'):
                name, ext = item.rsplit('.', 1)
            else:
               name = item
            items.append(Result(name, ext, parent))
        logger.info()
    except Exception as e:
       logger.error(msg=f'{e.__class__.name__}: {e}')
    return items                     

def parse_ars():
    parser = argparse.ArgumentParser(description="directory content information")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='input directiry path: ')
    args = parser.parse_args()
    return args.p

def main():
    for item in parse_ars():
        for elem in (walk_dir(item)):
            print(repr(elem))

if __name__ == '__main__':
    main()



