def c(file):
    d=0
    f = open(file, "r")
    for i in f:
        d=d+1
    print(d)
file=input("file:")
c(file)