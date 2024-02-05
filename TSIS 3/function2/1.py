from data import movies
def func(movie):
    for i in movies:
        if movie==i['name'] and i['imdb']>5.5:
            return True
    return False 
if func(input())==True:
    print(True)
else:
    print(False)