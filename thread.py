# ----------------------------ПОТОКИ
# Як було раніше
# def func1():
#     print('Hello from func1')
#
#
# def func2():
#     print('Hello from func2')
#
#
# func1()  # виконується код з func1
# func2()  # чекає поки завершиться попередній код, тоді починає роботу
# func2()
# func1()

# # створення потоків
# import threading
# import time

# def func1():
#     for i in range(1000_000):
#         if i % 100_000 == 0:  # виводити раз на 100_000
#             print('Hello from func1\n', end='')
#
#
# def func2():
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print('Hello from func2\n', end='')
#
#
# # потік для виконання функції func1
# thread1 = threading.Thread(target=func1)
#
# # потік для виконання функції func2
# thread2 = threading.Thread(target=func2)
#
#
# # запускаємо потоки
# thread1.start()
# thread2.start()
#
# print('hello before join')  # може запуститись коли потоки ще працюють
#
# # момент коли потоки закінчили роботу
# thread1.join()
# thread2.join()
#
# print('END')  # запуститься коли потоки закінчили роботу

# функції з параметрами

# def greeting(name, age):
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print(f'Привіт {name}, {age} років\n', end='')
#
#
# def summa(nums):
#     for i in range(1000_000):
#         if i % 100_000 == 0:
#             print(f'Сума чисел {nums} = {sum(nums)}\n', end='')
#
#
# nums = [1, 2, 3, 4]
#
# # thread1 = threading.Thread(target=greeting, args=('John',), kwargs={"age": 35})
# thread1 = threading.Thread(target=greeting, args=('John', 35))
# thread2 = threading.Thread(target=summa, args=(nums,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# спільна ділянка пам'яті

# nums = [1, 2, 3, 4]
# lock = threading.Lock()
#
#
# def append():
#     # дістати nums зі спільної області пам'яті
#     global nums, lock
#
#     for num in range(1000):
#         # працює зі спільною ділянкою пам'яті
#         # інші потоки зупиняються поки цей не завершить роботу
#         lock.acquire()
#
#         nums.append(num)
#
#         lock.release()  # роботу завершено, інші потоки можуть працювати
#
# def remove():
#     global nums, lock
#
#     for _ in range(1000):
#         lock.acquire()
#         nums.pop(0)
#         lock.release()
#
#
# thread1 = threading.Thread(target=append)
# thread2 = threading.Thread(target=remove)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(nums)

# _____________________________________________________________

# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
#Користувач вводить з клавіатури значення у список
# Після чого запускаються два потоки. Перший потік знахо
# дить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

# import threading
#
#
# def find_max(numbers):
#     print(max(numbers))
#
#
# def find_min(numbers):
#     print(min(numbers))
#
#
# def read():
#     numbers = []
#
#     while True:
#         input_number = int(input(" number "))
#
#         if input_number == 0:
#             return numbers
#
#
#         numbers.append(input_number)
#
#
# numbers = read()
#
# maximum = threading.Thread(target=find_max, args=(numbers,))
# minimum = threading.Thread(target=find_min, args=(numbers,))
#
# maximum.start()
# minimum.start()
#
# maximum.join()
# minimum.join()


# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.


# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

import threading
import json

lock = threading.Lock() # створення змінної, яка відповідає за функцію "ЗАМОК" в потоці.

def even(path):
    global lock

    lock.acquire() # відкриття замку в потоці

    with open(path, "r") as file:
        nums = json.load(file)

    lock.release() #закриття замку в потоці

    new_nums = []

    for num in nums:
        if num % 2 == 0:
            new_nums.append(num)

    new_path = path[:-5] + "_even.json"

    with open(new_path, "w") as file:
        json.dump(new_nums, file)


def odd(path):
    global lock

    lock.acquire()

    with open(path, "r") as file:
        nums = json.load(file)

    lock.release()

    new_nums = []

    for num in nums:
        if num % 2 != 0:
            new_nums.append(num)

    new_path = path[:-5] + "_odd.json"

    with open(new_path, "w") as file:
        json.dump(new_nums, file)


path = input("Введіть шлях до файлу: ")

thr_even = threading.Thread(target=even, args=(path,))
thr_odd = threading.Thread(target=odd, args=(path,))

thr_even.start()
thr_odd.start()

thr_even.join()
thr_odd.join()



# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран
#
# import threading
#
#
# def func(user_path, user_word):
#     try:
#         with open(user_path, 'r') as file:
#             words = file.read().lower()
#     except Exception:
#         print('Файлу не існує')
#         return
#
#     word_count = words.count(user_word)
#     print(f"Слово {user_word} зустрічається {word_count} разів")
#
#
# user_path = input('Enter path: ')
# user_word = input('Enter word for search: ').lower()
#
# thread_user = threading.Thread(target=func, args=(user_path, user_word))
# thread_user.start()
# thread_user.join()
