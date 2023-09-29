import string
import random

def gen_names(name_file: str):
    names = []
    vowels = "aeiou"
    while len(names) < random.randint(3,10):
        res = "".join(random.sample(string.ascii_letters, random.randint(4,7))).capitalize()
        if len(set(res) & set(vowels)) > 0: #если в результате есть хоть 1 главсная, то добадяем его 
            names.append(res)
    with open(name_file, "a", encoding = "utf-8") as file:
        file.writelines('\n'.join(names))
