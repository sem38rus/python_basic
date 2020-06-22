# Задание 1
my_list = [-21, False, 24, 'This is String', True, 3.1415923, [2, 34,-23, "This is string"]]
for i in my_list:
    print(f"{i} is {type(i)}")

#Задание 2
elements = int(input("Какое количество элементов будет в списке? : "))
my_list = []
i = 0
while i < elements:
    my_list.append(input("Введите значение списка: "))
    i += 1

for x in range(int(len(my_list) / 2)):
    el = 0
    my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
    el += 2
print(my_list)

#Задание 3

season_list = ["зима", "весна", "лето", "осень"]
season_dict ={1: "зима", 2: "весна", 3: "лето", 4: "осень"}
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print(f"Сезон по списку, {season_list[0]}")
    print(f"Сезон по словарю, {season_dict.get(1)}")
elif month == 3 or month == 4 or month == 5:
    print(f"Сезон по списку, {season_list[1]}")
    print(f"Сезон по словарю, {season_dict.get(2)}")
elif month == 6 or month == 7 or month == 8:
    print(f"Сезон по списку, {season_list[2]}")
    print(f"Сезон по словарю, {season_dict.get(3)}")
elif month == 9 or month == 10 or month == 11:
    print(f"Сезон по списку, {season_list[3]}")
    print(f"Сезон по словарю, {season_dict.get(4)}")
else:
    print("Месяцев всего 12!")

#Задание 4

my_str = input("Введите строку: ")
split_str = my_str.split(' ')
for i, el in enumerate(split_str, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}.  {el}")


