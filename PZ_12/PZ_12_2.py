# Составьте генератор (yield), который преобразует все буквенные символы в строчные.
string = input('Введите строку для то, чтобы все буквы в ней были в нижнем регистре: ')

def to_lower(string):
    for i in string:
        if i.isalpha():
            yield i.lower()
        else:
            yield i


for i in to_lower(string):
    print(i, end = '')
print()