def count_files():
    import os
    ls = os.listdir()
    ls_only_py_files = len(list(filter(lambda x : x.endswith(".py"),ls)))
    print("number of python files is :",ls_only_py_files)

count_files()