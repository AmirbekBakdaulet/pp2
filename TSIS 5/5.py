import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.finditer(r'\w*a.*b$', text)
for i in x:
    print(i.group())