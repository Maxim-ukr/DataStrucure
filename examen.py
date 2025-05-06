# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
# num1 = int(input("Введіть перше число:"))
# num2 = int(input("Введіть друге число:"))
#
# suma = 0
#
# if num1 < num2:
#     for i in range(num1, num2+1):
#         suma += i
#         print(suma)
#
# elif num2 < num1:
#     for i in range(num2, num1+1):
#         suma += i
# else:
#     print(f"{num1} дорівнює {num2}")
#
# print(f"Сума діапазону чисел {num1} та {num2} дорівнює {suma}.")
# from DZJSON import choice

# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.
# suma = 0
#
# for i in range(1, 100+1):
#     if i % 2 == 0:
#         suma += i
#
# print(f"Сума парних чисел в діапазоні від 1 до 100 дорівнює {suma}.")

# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.
# text = input("Введіть текст: ")
#
# for symbol in text:
#     print(symbol)


# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.
# from random import randint
#
# numbs = []
#
# count = randint(1,20)
# print(count)
#
# for i in range(1, count):
#     numb = randint(1,10)
#     numbs.append(numb)
#
# new_numbs = []
#
# for n in numbs:
#     if n %2 == 0:
#         new_numbs.append(n)
#
# print(numbs)
# print(new_numbs)

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.
# def upper_line(lines):
#     new_lines = []
#
#     for line in lines:
#         if line[0].isupper():
#             new_lines.append(line)
#
#     return new_lines
#
# lines = []
#
# while True:
#     line = input("Введіть строку (або натисніть єнтер для кінця): ")
#
#     if line == '':
#         break
#     else:
#         lines.append(line)
#
# res_lines = upper_line(lines)
#
# print(res_lines)

# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
# def python_in_line(lines):
#     new_lines = []
#
#     for line in lines:
#         if 'Python' in line:
#             new_lines.append(line)
#
#     return new_lines
#
# lines = []
#
# while True:
#     line = input("Введіть строку (або натисніть єнтер для кінця): ")
#
#     if line == '':
#         break
#     else:
#         lines.append(line)
#
# res_lines = python_in_line(lines)
#
# print(res_lines)


# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.



# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).
#
#
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
class WebSite():
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.page_list = []

    def add_page(self, page):
        if not page in self.page_list:
            self.page_list.append(page)
        else:
            print("Ви вдруге хочете добавити цю сторінку. Операція НЕ виконана.")

    def del_page(self, page_inx):
        if page in self.page_list:
            self.page_list.pop(page_inx)
        else:
            print("Такої сторінки немає. Операція НЕ виконана.")

    def showinfo(self):
        print(f"Сайт - {self.name}, адреса - {self.url}, сторінки: ")
        for page in self.page_list:
            print(page.info())



# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
class WebPage():
    def __init__(self, name, text, date):
        self.name = name
        self.text = text
        self.date = date

    def info(self):
        print(f"{self.name} - {self.text} - {self.date}")



# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
while True:
    print('________________________________________')
    print('1. Створити сайт.')
    print('2. Додати до сайта сторінку.')
    print('3. Видалити сторінку з сайта. ')
    print('4. Переглянути інформацію про сайт.')
    print('5. Завершити роботу.')
    print('________________________________________')

    choice = input("Введіть номер дії: ")

    if choice == '1':
        name = input("Введіть назву сайта: ")
        url = input("Введіть адресу сайта: ")

        if name != '' and url != '':
            site = WebSite(name, url)
        else:
            print('Ви введи невірні дані для створення сайту.')

    elif choice == '2':
        if site is not None: # так не працює - треба переробити в трай-ексепт.
              name = input("Введіть назву сторінки: ")
              text = input("Введіть зміст сторінки: ")
              date = input("Введіть дату публікації: ")
              if name != '' and text != '' and date != '':
                  page = WebPage(name, text, date)

                  site.add_page(page)

              else:
                  print('Ви введи невірні дані для створення сторінки.')
        else:
            print("Ви ще не створили сайт.")

    elif choice == '3':
        if site is not None:# так не працює - треба переробити в трай-ексепт.
            print("Всі сторінки сайту. Введіть індекс сторінки.")
            i = 0

            for page in site.page_list:
                print(f"{i} - {page.info()}")
                i += 1

            page_choice = int(input("Введіть індекс сторінки: "))

            if page_choice in range(0, i):
                site.del_page(page_choice)

            else:
                print('Ви введи невірні дані для створення сторінки.')
        else:
            print("Ви ще не створили сайт.")

    elif choice == '4':
        if site is not None:# так не працює - треба переробити в трай-ексепт.
            site.showinfo()
        else:
            print("Ви ще не створили сайт.")

    elif choice == '5':
        break
    else:
        print("Ви введи невідому команду.")

# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті.