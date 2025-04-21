# Додайте до програми по роботі з таблицею People
# такий функціонал:
#  добавити нову людину
#  вивести людей, ім’я яких починається на певну літеру
#  вивести людей, які народитись після певної дати
#  вивести скільки людей живе у певній країні


from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json
from datetime import date
from datetime import datetime

with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/people"
engine = create_engine(db_url)

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    birthday = Column(Date)

    def __repr__(self):
        return (f"Name {self.name}, Surname {self.surname}, city {self.city}, country {self.country},"
                f"birthday {self.birthday}")


Session = sessionmaker(engine)
session = Session()

def command1():
    user_input = input("Введіть запит: ")

    query_sql = text(user_input)

    # виконуємо запит
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)


#  добавити нову людину
def command2():
    user_name = input("Введіть імя: ")
    user_surn = input("Введіть прізвище: ")
    user_city = input("Введіть місто: ")
    user_country = input("Введіть країну: ")
    user_input = input("Введіть дату народження (у форматі РРРР-ММ-ДД): ")
    try:
        user_birthday = datetime.strptime(user_input, "%Y-%m-%d").date()
        print("Дата народження:", user_birthday)
    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")

    people = People(name=user_name, surname=user_surn, city=user_city, country=user_country, birthday=user_birthday),
    session.add_all(people)
    session.commit()


#  вивести людей, ім’я яких починається на певну літеру
def command3():
    user_input = input("Введіть літеру, на яку має починатися імя: ")

    query_sql = text(f"SELECT * FROM PEOPLE WHERE NAME LIKE '{user_input}%'")

    # виконуємо запит
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)

#  вивести людей, які народитись після певної дати
def command4():
    user_input = input("Введіть дату народження (у форматі РРРР-ММ-ДД): ")

    try:
        user_birthday = datetime.strptime(user_input, "%Y-%m-%d").date()
        print("Дата народження:", user_birthday)

        # Правильне використання параметра
        query_sql = text("SELECT * FROM PEOPLE WHERE BIRTHDAY > :bday")
        result = session.execute(query_sql, {"bday": user_birthday})

        for row in result:
            print(row)

    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")


#  вивести скільки людей живе у певній країні
def command5():
    user_input = input("Введіть назву країни: ")

    query_sql = text("SELECT COUNT(*) FROM PEOPLE WHERE COUNTRY = :country")

    result = session.execute(query_sql, {"country": user_input})
    count = result.scalar()

    print(f"Кількість людей з країни {user_input}: {count}")


while True:
    print("1 - Виконати запит.")
    print('2 - Добавити нову людину, ')
    print('3 - Вивести людей, ім’я яких починається на певну літеру, ')
    print('4 - вивести людей, які народитись після певної дати, ')
    print('5 - вивести скільки людей живе у певній країні.')

    command = input("Введіть команду: ")

    if command == "1":
        command1()
    elif command == "2":
        command2()
    elif command == "3":
        command3()
    elif command == "4":
        command4()
    elif command == "5":
        command5()

    else:
        break


#

# Завдання 2
# Додайте до першого завдання можливість вносити,
# видаляти, оновлювати дані за допомогою запитів INSERT,
# DELETE, UPDATE. Перед виконанням запиту перевіряйте
# правильність назви таблиці. Також забороніть запит на
# видалення та оновлення усіх рядків (UPDATE та DELETE
# без умов).
# Завдання 3
# Модифікуйте перше завдання так, щоб користувач не
# міг вводити запит, а користувався готовими фільтрами.
# Наприклад: відображення усіх людей, відображення усіх
# людей з одного
# Практичне завдання
# 1
# міста (користувач задає з клавіатури як значення), відображення усіх людей з однієї країни (користувач задає з
# клавіатури як параметр).
# Завдання 4
# Модифікуйте третє завдання, щоб фільтр для показу міг бути комплексним. Наприклад, користувач може
# виставити фільтр на країну та місто, після чого відобразяться люди, для яких спрацює цей комплексний
# фільтр. Підтримайте умову АБО.
# Завдання 5
# Додайте до четвертого завдання можливість вносити,
# видаляти, оновлювати дані через інтерфейс додатка. Користувач не може ввести запит INSERT, UPDATE, DELETE
# безпосередньо.
# Завдання 6
# Додайте до додатку можливість зберігати результати
# роботи фільтрів у файл. Наприклад, результат роботи
# фільтра для відображення усіх людей або результат роботи
# фільтра з відображення людей з одного міста

