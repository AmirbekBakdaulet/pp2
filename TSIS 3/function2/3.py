from data import movies
def func(thecat):
    thelist=[]
    for i in movies:
        if i['category']==thecat:
            thelist.append(i)
    print(thelist)
func(input())