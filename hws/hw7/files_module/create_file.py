from random import randbytes, randint, sample
import string


def create_file(extension: str, min_name = 6, max_name = 30, min_byte = 256, \
                 max_byte = 4096, num_files = 42):
    res_name = "".join(sample(string.ascii_letters, randint(min_name, max_name)))
    with open(f'{res_name}.{extension}', "wb") as f:
        for _ in range(num_files):
            f.write(randbytes(randint(min_byte, max_byte)))