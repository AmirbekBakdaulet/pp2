import math
def area(n,s):
    if n>=3:
        print((n * s ** 2) / (4 * math.tan(math.pi / n)))
    else:
        return False
n=int(input("n:"))
s=float(input("s:"))
area(n,s)