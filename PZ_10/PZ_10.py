# Туристичекие агенства предлагают следующие туры. Вояж - Мексика, Канада, Израиль, Италия, США. РейнаТур - Англия, Япония, Канада, ЮАР.
# Радуга - США, Испания, Швеция, Австралия. Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США.

voyaj = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
reinatour = {'Англия', 'Япония', 'Канада', 'ЮАР'}
raduga = {'США', 'Испания', 'Швеция', 'Австралия'}
tours = ('Voyaj', 'ReinaTour', 'Raduga')
canada = {'Канада'}
usa = {'США'}

list_can = []
def chose_can(set, name_set):
    if 'Канада' in set & canada:
        list_can.append(name_set)

chose_can(voyaj, tours[0])
chose_can(reinatour, tours[1])
chose_can(raduga, tours[2])

list_usa = []
def chose_usa(set, name_set):
    if 'США' in set & usa:
        list_usa.append(name_set)

chose_usa(voyaj, tours[0])
chose_usa(reinatour, tours[1])
chose_usa(raduga, tours[2])

print(f'Тур в Канаду можно приобрести в: {list_can}')
print(f'Тур в США можно приобрести в: {list_usa}')