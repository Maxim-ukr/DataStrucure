from sqlalchemy import create_engine, MetaData, insert, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

# завантажуємо логін та пароль
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# підключаємось до бд itstep
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/hospital"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# вивести назви доступних таблиць
# for table_name in metadata.tables:
#     print(table_name)


# print(metadata.tables)

# Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних. При спробі
# оновлення усіх рядків в одній таблиці надайте запит на
# підтвердження користувачеві. Оновлювати усі рядки
# можна лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних. При спробі видалити
# усі рядки в одній таблиці потрібно видавати користувачу
# запит на підтвердження. Видаляти усі рядки, можна тільки
# після підтвердження користувачем.

def get_table():
    print('Виберіть таблицю з бази')

    for table_name in metadata.tables:
        print(f'\t{table_name}')

    user_table_name = input('Ваша відповідь: ')

    return user_table_name

def insert_row():
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # список з даними рядка
    values = []

    # список з назвами стовпців
    column_names = []

    for column in table.columns:
        # пропускаємо стовпчик id
        if column.name == 'id':
            continue

        value = input(f'{column.name} = ')

        values.append(value)
        column_names.append(column.name)

    # назви стовпців без лапок
    new_column_names = tuple(column_names)
    new_column_names = str(new_column_names)
    new_column_names = new_column_names.replace('\'', '')

    # запит по добавлянню рядка

    query = f"""
    INSERT INTO {table_name}
    {new_column_names}
    VALUES {tuple(values)}
    """

    # print(query)

    # виконати запит та обробити помилки
    try:
        query = text(query)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def insert_row2():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # словник: ключ - назва стовпця, значення - те що ввів користувач
    values = {}


    for column in table.columns:
        # пропускаємо стовпчик id
        if column.name == 'id':
            continue

        value = input(f'{column.name} = ')

        values[column.name] = value

    # добавляємо рядок
    query = insert(table).values(values)

    try:
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def update_row():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # показати таблицю
    show_table(table_name)

    id = int(input('Виберіть id рядка: '))

    print('Виберіть назву стовпчика')
    for column in table.columns:
        print(f"\t{column.name}")

    column_name = input('Ваша відповідь: ')
    value = input('Ведіть нове значення: ')

    # запит для зміни рядка
    query = f"""
    UPDATE {table_name}
    SET {column_name} = '{value}'
    WHERE id = {id}
    """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def show_table(table_name):
    table = metadata.tables[table_name]

    query = f"""
    SELECT *
    FROM {table_name}
    """

    query = text(query)
    rows = session.execute(query)
    rows = rows.fetchall()

    # вивід назв стовпчиків
    for column in table.columns:
        print(column.name, end='\t\t')
    print()

    for row in rows:
        for value in row:
            print(value, end='\t\t')
        print()

def delete_row():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # показати таблицю
    show_table(table_name)

    id = int(input('Виберіть id рядка: '))

    # запит для видалення рядка
    query = f"""
    DELETE
    FROM {table_name}
    WHERE id = {id}
    """

    # query = delete(table).where(table.c.id == id) - другий варіант (через делете)


    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

def  surname_spec():

    # запит для видалення рядка
    query = f"""
    SELECT DOCTORS.SURNAME, SPECIALIZATIONS.NAME
    FROM DOCTORSPECIALISATION
	JOIN DOCTORS ON DOCTORS.ID = DOCTORSPECIALISATION.DOCTORID
	JOIN SPECIALIZATIONS ON SPECIALIZATIONS.ID = DOCTORSPECIALISATION.SPECIALISATIONID
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)



while True:
    print("1 - вставити рядок в таблицю")
    print("2 - змінити рядок в таблиці")
    print("3 - Видалити рядок в таблиці")
    print("4 -  Вивести прізвища лікарів та їх спеціалізації")

    command = input('Введіть номер команди: ')

    if command == '1':
        insert_row2()
    elif command == '2':
        update_row()
    elif command == '3':
        delete_row()
    elif command == '4':
        surname_spec()
    else:
        print('невірна команда')