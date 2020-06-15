"""homeworks"""
# Задание 1:

var1 = int(input("Введите число : "))
var2 = str(input("Напишите что-нибудь : "))
print(var1)
print(var2)

# # Задание 2:

time = int(input("Введите время в секундах : "))
h = time // 3600
m = (time - h * 3600) // 60
s = time - (h * 3600 + m * 60)
print(f"Время в формате чч:мм:сс   {h} : {m} : {s}")

# Задание 3:

n = int(input("Введите число : "))
print(n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))

# Задание 4:

n = int(input("Введите число : "))
m = n % 10
n = n // 10
while n > 0:
    if n % 10  > m:
        m = n % 10
    n = n // 10
print(m)

# Задание 5:
revenue = float(input("Введите выручку фирмы : "))
costs = float(input("Введите издержки фирмы : "))
if revenue > costs:
    print(f"Фирма работает в плюс, рентабельность выручки составила: {revenue / costs : .2f}")
    worker = int(input("Введите колличество сотрудников : "))
    print(f"Прибыль в расчете на одного сотрудника равна: {revenue / worker: .2f}")
elif revenue == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


# Задание 6:

a = int(input("Введите результат первого дня : "))
b = int(input("Введите какой нужен результат : "))
s = a
d = 1
while s <= b:
    d = d + 1
    s = 1.1 * s
print(d)