import re
text = str(input())
words = re.split(r'[,.]',text)
for word in words:
    print(word)
