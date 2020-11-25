seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
месяц = int(input("Введите число месяца >>>"))
if месяц == 1 or месяц == 12 or месяц == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif месяц == 3 or месяц == 4 or месяц == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif месяц == 6 or месяц == 7 or месяц == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif месяц == 9 or месяц == 10 or месяц == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("нет такого месяца")
