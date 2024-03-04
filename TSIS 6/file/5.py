def w(file, thelist):
    f=open(file, 'w')
    f.write(str(thelist))
file=input("file:")
s=input("list:")
thelist=list(s.split())
w(file,thelist)