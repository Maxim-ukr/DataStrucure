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
# # У функції має використовуватись цикл while
# Основна програма:
#  створити сервер
#  підключити двох клієнтів
#  створити 2 потоки з функцією send_message
#  запустити потоки

import socket
import json
import threading

def send_message(from_client, to_client):
    while True:
        message = from_client.recv(1024).decode() # а навіщо закодовувати і відразу розкодовувати? Суто, щоб далі розпарсити джейсоном?
        if message:
            to_client.send(message.encode())

            data = json.loads(message)
            if data['message'] == '':
                break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))

server.listen(2)
client1, addr1 = server.accept()
client2, addr2 = server.accept()

thr_client1 = threading.Thread(target=send_message, args=(client1, client2))
thr_client2 = threading.Thread(target=send_message, args=(client2, client1))

thr_client1.start()
thr_client2.start()

thr_client1.join()
thr_client2.join()

client1.close()
client2.close()
server.close()

# ___________________LAB 3 - Client 1 and Client 2 odnakovi
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
#
# import socket
# import json
# import threading
#
# def receive_message(client):
#     while True:
#         receive = client.recv(1024).decode()
#         data = json.loads(receive)
#
#         print()
#         print(f"{data['name']}: {data['message']}")
#
#         if data['message'] == '':
#              break
#
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 8080))
#
# thr = threading.Thread(target=receive_message, args=(client,))
#
# thr.start()
#
# name = input('Як вас звати? >>> ')
#
# while True:
#     message = input(f'{name}: ')
#     # даний інпут фактично працює не коректно: він чекає на введення інформації і якщо приходить вхідне повідомлення, то
#     # курсор сбрасується на нову строку і виходить відірвано -
#     # ("Іван: Привіт
#     # Сергій:
#     # Іван: Як справи?
#     # Привіт (типу Сергій тільки відповів")
#     # Виправити цей баг в межах термінального спілкування без меню або іншого окремого виклику інпута з одночасним
#     # термінейтом потоку отримання інформації, я не зміг - способу не знайшов.
#
#     data = {'name': name,
#             'message': message}
#     code = json.dumps(data)
#     client.send(code.encode())
#
#     if message == '':
#         break
#
# thr.join()
#
# client.close()
#
