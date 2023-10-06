from random import randint, uniform

def fill_file(num: int, name: str):
    with open(name, "a", encoding = "utf-8") as file:
        for _ in range(num):
            file.write(f"{randint(-1000,1000)} | {uniform(-1000,1000)}\n")