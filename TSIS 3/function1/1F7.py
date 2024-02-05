def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
            break
    return False
nums=input()
thelist=[]
for i in nums.split():
    n=int(i)
    thelist.append(n)
result=has_33(thelist)
print(result)
