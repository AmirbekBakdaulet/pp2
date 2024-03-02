def ispol(x):
    for i in range(len(x)):
        if x[i]==x[len(x)-i-1]:
            return True
        else:
            return False
        
x=input("the string:")
print(ispol(x))