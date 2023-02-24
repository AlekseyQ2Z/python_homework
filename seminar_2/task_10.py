"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint

number_coins = int(input("Введите количество монет: "))
eagle_coins = 0
tails_coins = 0
for i in range(number_coins):
    flag = bool(randint(0,1))
    if flag:
        eagle_coins += 1
    else:
        tails_coins += 1
if eagle_coins > tails_coins:
    print(f"Выпало: орлов {eagle_coins}, решек {tails_coins}. Надо перевернуть {tails_coins} решек.")
else:
    print(f"Выпало: орлов {eagle_coins}, решек {tails_coins}. Надо перевернуть {eagle_coins} орлов.")
