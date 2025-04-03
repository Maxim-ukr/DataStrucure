
# ____________________________TEST
import socket
import json
import threading

def receive_message(client):
    while True:
        receive = client.recv(1024).decode()
        data = json.loads(receive)

        print()
        print(f"{data['name']}: {data['message']}")

        if data['message'] == '':
             break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

thr = threading.Thread(target=receive_message, args=(client,))

thr.start()

name = input('Як вас звати? >>> ')

while True:
    message = input(f'{name}: ')
    # даний інпут фактично працює не коректно: він чекає на введення інформації і якщо приходить вхідне повідомлення, то
    # курсор сбрасується на нову строку і виходить відірвано -
    # ("Іван: Привіт
    # Сергій:
    # Іван: Як справи?
    # Привіт (типу Сергій тільки відповів")
    # Виправити цей баг в межах термінального спілкування без меню або іншого окремого виклику інпута з одночасним
    # термінейтом потоку отримання інформації, я не зміг - способу не знайшов.

    data = {'name': name,
            'message': message}
    code = json.dumps(data)
    client.send(code.encode())

    if message == '':
        break

thr.join()

client.close()

