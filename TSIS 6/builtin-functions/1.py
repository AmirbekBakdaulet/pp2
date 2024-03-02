def multp(x):
    product=1
    for i in x:
        product=int(i)*product
    print(product)
s=input("list:")
thelist=list(s.split())
multp(thelist)