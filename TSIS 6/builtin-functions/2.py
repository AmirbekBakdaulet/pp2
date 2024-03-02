def sum(x):
    up=0
    low=0
    for i in x:
        if i.isupper():
            up=up+1
        elif i.islower():
            low=low+1
    print(f"the number of upper case latters: {up}")
    print(f"the number of lower case latters: {low}")
x=input("the string:")
sum(x)