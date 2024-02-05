from itertools import permutations
def permut(s):
    perms=permutations(s)
    for i in perms:
        print(" ".join(i))
s=input("enter string:")
l=s.split()
permut(l)



      

    

