




import re

text = 'Карта map и объект bitmap - это разные вещи'

match = re.findall(r'\bmap\b', text)
print(match)

text = 'Еда, беду, 55-я победа'
match = re.findall(r'еда', text)
match = re.findall(r'\w', text, re.ASCII)
print(match)

text = "D43F"

match = re.findall(r"\D\d\d\D", text)
print(match)

