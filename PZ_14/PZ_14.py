# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать количество полученных элементов.
import re

file = open('Dostoevsky.txt', 'r', encoding='utf-8')
content = file.read()

pattern = r'\b((?:18)[0-9]{2}–(?:18)[0-9]{2}|(?:18)[0-9]{2}\s)\b'
matches = re.findall(pattern, content)

count = len(matches)

print(f"Количество лет деятельности писателя: {matches}, всего {count}")
