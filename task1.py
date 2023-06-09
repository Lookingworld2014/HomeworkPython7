# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

'''
words = input("Введите стишок: ").split() # разбиваем стихотворение на слова
syllables = [] # список для хранения количества слогов в каждой фразе

for word in words:
    syllables.append(word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')) # считаем количество гласных букв в слове и добавляем в список

if len(set(syllables)) == 1: # проверяем, все ли элементы списка равны между собой
    print("Парам пам-пам")
else:
    print("Пам парам")
    '''

shoutout = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def Rhythm(shoutout):
    print(shoutout)
    shoutout = shoutout.split()
    print(shoutout)
    list_1 = []

    for word in shoutout:
        sum_gl = 0
        for i in word:
            if i in 'ауоыиэяюёе':
                sum_gl += 1
        list_1.append(sum_gl)
        print(list_1)
    return len(list_1) == list_1.count(list_1[0])

if Rhythm(shoutout):
    print('Парам пам-пам')
else:
    print('Пам парам')