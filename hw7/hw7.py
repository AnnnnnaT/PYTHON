# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

EXTENSIONS = {
    'videos': ['.mp4',  '.mov'],   
    'texts': ['.txt', '.doc', '.pdf'],
    'images': ['.jpg', '.png']
}

def sort_files(dir):
    for type_ in EXTENSIONS.keys():
        os.makedirs(type_)
    dir_files = os.listdir(dir)
    for item in dir_files:
        ext = '.' + item.split('.')[1]
        for key, value in EXTENSIONS.items():
            if ext in value:
                shutil.move(os.path.join(dir, item), os.path.join(key, item))


#  Напишите функцию группового переименования файлов.
#  Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

def rename(org_name: str, wished_name: str, num_files: int, ext: str, fin_ext: str, org_size: list):
    names = []
    count = 1
    n1 = org_name.replace(ext, "")
    n2 = n1[int(org_size[0]): int(org_size[1])]
    if wished_name:
        res = n2 + wished_name
    else:
        res = n2    
    for _ in range(num_files):
        names.append(res)
    for i in  range(len(names)):
        names[i] = names[i] + str(0)*(num_files-1) + str(count) 
        count+=1
        names[i] += "." + fin_ext
    return names

# print(rename("filefilefilefileextension.py", "anna", 10, "py", "txt", [3,6]))
