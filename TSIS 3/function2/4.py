from data import movies
def func(thelist):
    sum=0
    for i in thelist:
        for k in movies:
            if k["name"] == i:
                sum=k["imdb"]+sum
    print(sum / len(thelist))
n=int(input())
thelist=[]
for i in range(n):
    thelist.append(input())
func(thelist)