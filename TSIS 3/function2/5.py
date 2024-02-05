from data import movies
def func(category):
    sum=0
    count=0
    for i in movies:
        if i["category"]==category:
            sum+=i["imdb"]
            count+=1
    print(sum/ count)
func(input())