# Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по
#  величине элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. Последняя строка
# содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

size = int(input("Введите количество чисел в списке: "))
sequense = [i+1 for i in range(size)]
print(sequense)
number = int(input("Введите число: "))
min = sequense[0]
for i in sequense:
    if number == i:
        min = i
        break
    elif abs(number - i) < abs(number - min):
        min = i
print(f"Самое близкое к числу {number} число {min}")
