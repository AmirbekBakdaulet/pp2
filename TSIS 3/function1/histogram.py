def hist(list):
    for i in list:
        print("*"*i)
nums=input()
list=[]
for i in nums.split():
    list.append(int(i))
hist(list)        