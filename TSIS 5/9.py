import re
f= open("row.txt", "r", encoding="utf8")
text = f.read()
x=re.sub(r"([а-я])*([А-Я])",r'\1 \2', text)
print(x)