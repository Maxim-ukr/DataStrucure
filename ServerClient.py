# Сервер, підключає клієнтів та відповідає
# на їхні запити

# import socket
#
#
# server = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
#                        socket.SOCK_STREAM # протокол передачі(TCP)
#                        )
#
# # вказуємо де знаходиться сервер
# server.bind(('127.0.0.1', 8080))
#
# # очікуємо підключення клієнтів
# server.listen(1) # чекаємо на одного клієнта
#
# print('Чекаємо на підключення...')
#
# # клієнт заходить з певної адреси на сервер
# client, adress = server.accept()
#
# print(f'Підключився клієнт з адреси {adress}')
#
# # якщо клієнтів 2
# # client1, adress1 = server.accept()
# # client2, adress2 = server.accept()
#
# # спілкування з клієнтом
# while True:
#     # отримуєсо дані від клієнта
#     # повідомлення максиму 1024 байта
#     message = client.recv(1024)
#
#     message_str = message.decode()
#
#     # чи зупиняти з'єднання з клієнтом
#     if message_str == '':
#         break
#
#     # відповідь сервера
#     print(f'Клієнт: {message_str}')
#
#     response = input("Ваша відповідь: ")
#     response_bytes = response.encode()
#
#     # надсилаємо відповідь
#     # надсилаємо те саме повідомлення
#     client.send(response_bytes)
#
# # розриваємо зв'язок з клієнтом
# client.close()
# server.close()


#------------------------------------------------------
# повідомлення не str
#
# import socket
# import json
#
#
# server = socket.socket(socket.AF_INET, # спосіб передачі даних(Інтернет)
#                        socket.SOCK_STREAM # протокол передачі(TCP)
#                        )
#
# # вказуємо де знаходиться сервер
# server.bind(('127.0.0.1', 8080))
#
# # очікуємо підключення клієнтів
# server.listen(1) # чекаємо на одного клієнта
#
# print('Чекаємо на підключення...')
#
# # клієнт заходить з певної адреси на сервер
# client, adress = server.accept()
#
# print(f'Підключився клієнт з адреси {adress}')
#
# # якщо клієнтів 2
# # client1, adress1 = server.accept()
# # client2, adress2 = server.accept()
#
# # спілкування з клієнтом
# while True:
#     # отримуєсо дані від клієнта
#     # повідомлення максиму 1024 байта
#     data = client.recv(1024)
#
#     # декодування
#     data = data.decode()
#     data = json.loads(data)
#
#     user_name = data['user_name']
#     message_str = data['message']
#
#     # чи зупиняти з'єднання з клієнтом
#     if message_str == '':
#         break
#
#     # відповідь сервера
#     print(f'{user_name}: {message_str}')
#
#     response = input("Ваша відповідь: ")
#     response_bytes = response.encode()
#
#     # надсилаємо відповідь
#     # надсилаємо те саме повідомлення
#     client.send(response_bytes)
#
# # розриваємо зв'язок з клієнтом
# client.close()
# server.close()

# __________________________________________________________________
# Завдання 1
# Напишіть клієнт-серверний додаток для отримання
# прогнозу погоди.
# Клієнт: надсилає назву міста
# Сервер: отримує прогноз погоди з json файлу та надсилає
# результат клієнту. Якщо такого міста немає, то надсилає
# повідомлення «Невідоме місто»

import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8080))

server.listen(1)

client, adr = server.accept()

with open("NF.json", "r") as file:
    whether = json.load(file)

while True:

    message = client.recv(1024)
    message_str = message.decode()


    if message_str in whether:
        resp_str = f"В місті {message_str} температура {whether[message_str]}"
        resp_byte = resp_str.encode()

        client.send(resp_byte)

    else:
        resp_str = f"Місто {message_str} невідоме."
        resp_byte = resp_str.encode()

        client.send(resp_byte)

client.close()
server.close()

# Завдання 2
# Напишіть клієнт-серверний додаток для спілкування між
# двома людьми:
# Клієнт: на початку програми вводить своє ім’я, далі
# запускається основний цикл, де отримуються та надсилаються
# повідомлення
# Сервер: підключає двох клієнтів, далі запускає основний
# цикл де спочатку отримує повідомлення від клієнта №1 та
# надсилає клієнту №2, а потім навпаки
# Завдання 3
# Додайте до попереднього завдання потоки, щоб клієнти
# могли спілкуватись не обов’язково по черзі. Для цього
# Практичне завдання
# напишіть функції
# Клієнт:
#  receive_message(client) – отримує повідомлення від сервера
# та виводить на екран. Має використовуватись цикл while
# Основна програма:
#  підключитись до сервера
#  створити потік з функцією receive_message
#  запустити потік
#  попросити користувача ввести ім’я
#  створити цикл в якому користувач вводить повідомлення та
# надсилає на сервер
# Сервер
#  send_message(from_client, to_client)
# o from_client – клієнт від якого отримуємо
# повідомлення
# o to_client – клієнт якому надсилаємо повідомлення
# У функції має використовуватись цикл while
# Основна програма:
#  створити сервер
#  підключити двох клієнтів
#  створити 2 потоки з функцією send_message
#  запустити поток