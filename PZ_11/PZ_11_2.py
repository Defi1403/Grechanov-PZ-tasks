# Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей.

low = 0
print()
for i in open('text18-7.txt', encoding='UTF-8'):
    print(i, end = '')
    for j in i:
        j = j.rstrip()
        if j.islower() == True:
            low += 1
print(f'\n\nКоличество букв в нижнем регистре: {low}')

f1 = open('text18-7.txt', encoding='UTF-8')
l = f1.readlines()
l.insert(2, l[-1] + '\n')
del l[-1]
f1.close()

f2 = open('text18-7_1.txt', 'w', encoding='UTF-8')
f2.writelines(l)
f2.close()
