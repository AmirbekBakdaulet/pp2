import os
def z(s,c):
    f= open(s,"r")
    x=open(c,"a")
    x.write(f.read())
s=input("source file:")
c=input("new file:")
z(s,c)