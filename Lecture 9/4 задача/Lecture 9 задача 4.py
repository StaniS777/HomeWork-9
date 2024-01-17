import re
with open('text.txt') as e, open('Stop_words.txt') as d:
	text, exceptions = e.read(), d.read().split()
for i in exceptions:
	text = re.sub(i, '*' * len(i), text, flags=re.I)
print(text)