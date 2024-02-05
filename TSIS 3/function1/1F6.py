def reverse(S):
    thelist=S.split()
    thelist.reverse()
    newS=" ".join(thelist)
    print(newS)
reverse(input())