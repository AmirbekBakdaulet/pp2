def filter(numbers):
    if numbers==1:
        return True
    else:
        for i in range(2,numbers):
            if numbers % i == 0:
                return False
            else:
                return True   
    
numbers=input()
thelist=numbers.split()
for i in range(0, len(thelist)):
    if filter(int(thelist[i])) == True:
        print(thelist[i])     

