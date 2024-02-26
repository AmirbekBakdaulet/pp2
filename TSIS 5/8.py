import re
f= open("row.txt", "r", encoding="utf8")
text = f.read()
x=re.findall("[а-я]*[А-Я][а-я]*", text)
print(x)