"""
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
"""
number = int(input("Введите число: "))
temp = 1
#string = ''                             или можно решить через строку
while temp <= number:
    print(temp, end = " ")
    #string += str(temp) + " "    
    temp *= 2
#print(string)