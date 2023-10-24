from hw7.files_module import create_file

def extensions(ext: list, num: int):
    for i in ext:
        create_file(i, num_files = num )
