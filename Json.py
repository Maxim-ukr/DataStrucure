#data = 'Hello, world'


# with open('data.txt', 'w') as file:
#     file.write(data)
#     #print(data, file=file)

# with open('data.txt', 'r') as file:
#     data = file.read()
#
#
# print(type(data))
# print(data)

# import json


# data = {'number': 24}
# data = [1, 2, 'hello']
# bytes = json.dumps(data)  # переводить дані у серію байтів(серіалізація)
# print(type(bytes))
# print(bytes)
#
# new_data = json.loads(bytes)  # переводить байти назад в об'єкт(десеріалізація)
# print(type(new_data))
# print(new_data)

# файли

# зберегти дані у файл json
# data = {"number": 25, "text": "Hello"}
#
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
# # завантажити дані з файли
# with open('data.json', 'r') as file:
#     new_data = json.load(file)
#
# print(new_data)


# Користувач водить текстові повідомлення, зберегти
# їх у список і у файл. За потреба заіантажити історію спілкування

# завантажити історію
# with open("history.json", 'r') as file:
#     history = json.load(file)
#
# # головний цикл
# while True:
#     text = input("Введіть повідомлення: ")
#
#     if text == "":  # якщо порожньо, то кінець програми
#         # перед завершенням зберегти історію
#         with open("history.json", 'w') as file:
#             json.dump(history, file)
#         break
#
#     elif text == "show": # показати історію
#         print("History")
#         for message in history:
#             print(f"\t {message}")
#
#     else:
#         # просто повідомлення добавити в історію
#         history.append(text)


# збереждення об'єктів класів
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def celebrate_birthday(self):
#         print(f"{self.name} святкує день народження")
#         self.age += 1
#
#     def state_dict(self): # словник з атрибутами
#         data = {
#             'name': self.name,
#             'age': self.age
#         }
#
#         return data
#
#     def load(self, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#
#         self.name = data['name']
#         self.age = data['age']
#
#
# person = Person('', '')
# person.load('data.json')
# person.celebrate_birthday()

# person = Person("John", 30)
# person.celebrate_birthday()
# person.celebrate_birthday()
#
# with open('data.json', 'w') as file:
#     json.dump(person.state_dict(), file) # збереження словника з атрибутами
#
#
# # завантаження даних
# with open('data.json', 'r') as file:
#     data = json.load(file)
#
# new_person = Person(data['name'], data['age'])

# _________________________________________________________________________________________________

# Завдання 1
# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.
import json

def load_from_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def save_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def add_user(users):
    login = input("Введіть логін: ")
    pasw = input("Введіть пароль: ")
    users[login] = pasw

def del_user(users):
    login = input("Введіть логін користувача, якого треба видалити: ")
    users.pop(login)

def change_pasw(users):
    login = input("Введіть логін для якого треба змінити пароль: ")
    if login in users:
        pasw = input("Введіть новий пароль: ")
        users[login] = pasw
    else:
        print(f"Невірний логін.")

def login(users):
    login = input("Введіть логін: ")
    pasw = input("Введіть пароль: ")

    if login in users:
        if users[login] == pasw:
            print("Ви в системі")
        else:
            print('Невірний пароль.')
    else:
        print(f"Невірний логін.")


users = {}
filename = 'users.json'

while True:
    print("""Можливі дії: 
           1. Завантажити данні.
           2. Зберегти данні.
           3. Додати нового користувача.
           4. Видалити користувача.
           5. Зміна паролю.
           6. Вхід у систему.
           0. Закінчити.""")
    choice = input("Введіть дію: ")

    if choice == "0":
        break
    elif choice == "1":
        users = load_from_file(filename)
    elif choice == "2":
        save_to_file(filename, users)
    elif choice == "3":
        add_user(users)
    elif choice == "4":
        del_user(users)
    elif choice == "5":
        change_pasw(users)
    elif choice == "6":
        login(users)
    else:
        print("невідома команда.")


# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)
# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background_color,