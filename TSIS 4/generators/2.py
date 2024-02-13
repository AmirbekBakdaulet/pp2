def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n=int(input())
thelist=[]
for i in even(n):
      thelist.append(str(i))
s=""
s=", ".join(thelist)
print(s)