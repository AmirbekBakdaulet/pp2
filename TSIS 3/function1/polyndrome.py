def ispol(s):
    thelist=s.split()
    thelist.reverse()
    reverseS=" ".join(thelist)
    if reverseS==s:
        print(True)
    else:
        print(False)
s=input()
ispol(s)