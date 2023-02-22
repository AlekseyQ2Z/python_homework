"""
Найдите сумму цифр трехзначного числа.
"""

count = int(input("Введите трехзначное число: "))
if 99 < count < 1000:
    sum_number = 0
    while count > 0:
        sum_number += count % 10
        count //= 10
    print(f"Сумма цифр этого числа равна: {sum_number}")
else:
    print("Число не трехзначное")