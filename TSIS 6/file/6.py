import os
for i in range(65, 91):
    file_name= chr(i)+ '.txt'
    f = open(file_name, "x")
    print("they were created")
