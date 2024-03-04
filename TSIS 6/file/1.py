import os
def sel(path):
    l1=[]
    l2=[]
    l3=[]
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            l1.append(i)
        elif os.path.isfile(os.path.join(path, i)):
            l2.append(i)
    print(l1)
    print(l2)
    print(os.listdir(path))
    
path =  input("path:")
sel(path)
