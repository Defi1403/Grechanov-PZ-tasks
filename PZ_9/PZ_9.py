# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', отражающая продажи продукции по дням в кг.
# Преобразовать информацию из строки в словари, с использованием функции найти минимальные продажи по каждому виду продукции, результаты вывести на экран.
pears = {}
carrots = {}
inf = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
inf = inf.split()

pears['фрукты'] = inf[0]
pears['продажи по дням'] = []
for i in inf[1:6]:
    pears['продажи по дням'].append(int(i))

carrots['овощи'] = inf[6]
carrots['продажи по дням'] = []
for i in inf[7:]:
    carrots['продажи по дням'].append(int(i))

print(f"Минимальные продажи груш: {min(pears['продажи по дням'])} кг")
print(f"Минимальные продажи моркови: {min(carrots['продажи по дням'])} кг")
