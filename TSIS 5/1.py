import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.finditer(r'\w*а+б*\w*', text)
for i in x:
    print(i.group())
