# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

# ИсхоAных четных элементов:

l = ['-99 6 12 -36 20 45 100 -15']
f1 = open('data_1.txt', 'w')
f1.writelines(l)
f1.close

f2 = open('data_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(l)
f2.close

f1 = open('data_1.txt')
all = f1.read()
all = all.split()
for i in range(len(all)):
    all[i] = int(all[i])

even = ''
l_even = []
sum_all = sum(all)
for i in all:
    if i > 0 and i % 2 == 0:
        even += str(i) + ' '
        l_even.append(i)
aver_all = sum_all/len(all)
sum_even = sum(l_even)
aver_even = sum_even/len(l_even)

f2 = open('data_2.txt', 'a', encoding='UTF-8')
f2.writelines('\nКоличество элементов: ' + str(len(all)) + '\nСреднее арифметическое элементов: ' + str(aver_all) + '\nПоложительные четные элементы: ' + str(even) + 
              '\nСумма положительных четных элементов: ' + str(sum_even) + '\nСреднее арифметическое положительных четных элементов: ' + str(aver_even)) 