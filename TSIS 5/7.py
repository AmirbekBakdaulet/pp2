import re
f= open("row.txt", "r", encoding="utf8")
text =f.read()
x=re.sub("_([a-z]+)",lambda x: x.group(1).capitalize(), text)
print(x)