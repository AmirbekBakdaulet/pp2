x=input()
t=tuple(x.split(","))
l=[]
for i in t:
   l.append(bool(i.strip()))
bool_t=tuple(l)
if all(t):
   print(True)
else:
   print(False)

