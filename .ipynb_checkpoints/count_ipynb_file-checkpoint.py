def count_files():
    ls = os.listdir()
    ls_only_py_files = len(list(filter(lambda x : x.endswith(".py"),ls)))
    return(ls_only_py_files)

count_files()