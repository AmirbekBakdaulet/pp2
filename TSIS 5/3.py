import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.finditer(r'[а-я]+_+[а-я]*', text)
for i in x:
    print(i.group())