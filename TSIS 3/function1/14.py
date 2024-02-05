import histogram
nums=input()
list=[]
for i in nums.split():
    list.append(int(i))
histogram.hist(list)
 