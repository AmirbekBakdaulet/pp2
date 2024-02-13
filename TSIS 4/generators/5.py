def dec(n):
    for i in range(n,-1,-1):
        yield i
n=int(input("n:"))
for i in dec(n):
    print(i)
