import os
def de(path):
    if os.path.exists(path):
        print("path exists")
        file_del=input("file_to_delete is:")
        os.remove(file_del)
    else:
        print("path does not exist")
path=input("the path:")
de(path)


