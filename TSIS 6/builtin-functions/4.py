import time
def calc(n, miliseconds):
    time.sleep(miliseconds/1000)
    print(f"Square root of {n} after {miliseconds} miliseconds is {n ** 0.5}")
n=int(input("the number:"))
mili=int(input("the milisecond:"))
calc(n,mili)
