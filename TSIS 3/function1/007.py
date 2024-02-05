def agent(thelist):
    zero=False
    seczero=False
    for i in thelist:
        if i==0 and zero==True:
            seczero=True
        elif i==0 and zero==False:
            zero=True
        elif i==7:
            if seczero==True:
                return True
            else:
                zero==False
    return False      
nums=input()
thelist=[]
for i in nums.split():
    thelist.append(int(i))
if agent(thelist)==True:
    print(True)
else:
    print(False)