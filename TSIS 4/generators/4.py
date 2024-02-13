def squares(a,b):
    for i in range(int(a**0.5), int((b**0.5)+1)):
        yield i*i
a=int(input("a:"))
b=int(input("b:"))
for i in squares(a,b):
    print(i)