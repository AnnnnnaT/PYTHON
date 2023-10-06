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
