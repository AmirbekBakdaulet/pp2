def unique(list):
    newl=[]
    for i in list:
        if i not in newl:
            newl.append(i)
                
    print(newl) 
nums=input()
list=nums.split()
unique(list)