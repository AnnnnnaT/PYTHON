def  zip_func(file_1, file_2):

    with (
        open(file_1, "r", encoding = "utf-8" ) as f1,
        open(file_2, "r", encoding = "utf-8" ) as f2        
    ):
        names = f1.readlines()
        nums = f2.readlines()

    nums = list(map(lambda x: (int(x.strip().split('|')[0]) * float(x.strip().split("|")[1])), nums))
    names = list(map(lambda x: x.strip(), names))
    
    res = list(zip(names, nums))

    with open("result_file.txt", "a", encoding = "utf-8") as f_res:
        for list_ in res:
            if list_[1] < 0:
                f_res.write(f'{list_[0].lower()} - {abs(list_[1])}\n')
            else:
                f_res.write(f"{list_[0].upper()} - {round(list_[1])}\n")