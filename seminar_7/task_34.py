# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
#  разобраться в его кричалках не настолько просто, насколько легко он их
#  придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
# есть, если число слогов (т.е. число гласных букв) в каждой фразе
#  стихотворения одинаковое. Фраза может состоять из одного слова, если
#  во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
# друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def defines_rhyme(list_1):
    dict_1 = {}
    for word in list_1:
        dict_1[word] = vowel(word)
    print(dict_1)
    first_value = dict_1[next(iter(dict_1))]
    print(first_value)
    for key, value in dict_1.items():
        if value != first_value:
            return 'Пам парам'
    return 'Парам пам-пам'


def vowel(word):
    vowels = 'аеёиоуыэюя'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


poem = list(input('Введите фразу: ').lower().split())
print(defines_rhyme(poem))