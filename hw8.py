# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории.
#  Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
import os 
import json
import csv
import pickle 

def walk_dir(path: str = os.getcwd()):
    dirs = []
    files = []
    files_res = {}
    dirs_res = {}

    for item in os.walk(path):
        for dir in item[1]:
            path = os.path.join(item[0], dir)
            dirs.append( path)
            for file in item[2]:
                file_path = os.path.join(item[0], file)
                files.append(file_path)

    for file in files:
        files_res[file] = (os.path.isfile(file), os.path.getsize(file))
    for dir in dirs:
        dirs_res[dir] = (os.path.isdir(dir), dir_size(dir))
    
    with open("res.json", "w", encoding = "utf-8") as f:
        json.dump(files_res, f, indent = 4, ensure_ascii = False)
        json.dump(dirs_res, f, indent = 4, ensure_ascii = False)
    
    with open("res.csv", "w", newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=["file", "type", "size"],
                    dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(files_res)
        csv_write.writerows(dirs_res)

    with open("res.pickle", "wb") as f:
        pickle.dump(files_res, f)
        pickle.dump(dirs_res, f)
   



def dir_size(path: str):
    size = 0
    for item in os.walk(path):
        for file in item[2]:
            size += os.path.getsize(file)
    return size


# walk_dir(r"C:\Users\User\Desktop\hw1\hw6")