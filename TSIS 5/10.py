import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.sub("([a-z]*)([A-Z])", r'\1_\2', text)
y=x.lower()
print(y)