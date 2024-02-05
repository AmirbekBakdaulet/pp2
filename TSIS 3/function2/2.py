from data import movies
def func():
    thelist=[]
    for i in movies:
        if i['imdb']>5.5:
            thelist.append(i)
    print(thelist)
func()