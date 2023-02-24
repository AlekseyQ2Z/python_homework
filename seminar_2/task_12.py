"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

from math import sqrt

sum_number = int(input("Введите сумму чисел: "))
multiply_number = int(input("Введите произведение чисел: "))
discriminant = sum_number * sum_number - 4 * multiply_number
if discriminant < 0:
    print("Ошибка ввода")
else:
    sqrt_discriminant = int(sqrt(discriminant))
    number_1 = (sum_number + sqrt_discriminant) // 2
    number_2 = sum_number - number_1
    print(f"Петя задумал числа {number_1} и {number_2}")
