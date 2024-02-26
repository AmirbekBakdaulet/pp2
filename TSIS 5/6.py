import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.sub("\s", "|", text)
y=re.sub(",","|",x)
z=re.sub("\.","|",y)
print(z)