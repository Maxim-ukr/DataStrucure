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
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/academy"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# вивести назви доступних таблиць
# for table_name in metadata.tables:
#     print(table_name)

# ____________________________________
# ■ створювати звіти:
# ▷ вивести інформацію про всі навчальні групи,
def groups_info():
    # запит
    query = f"""
        SELECT GROUPS.NAME, GROUPS.YEAR, GROUPS.RATING, DEPARTMENTS.NAME
        FROM GROUPS
        JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENTID
        """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    print(f"GROUPS.NAME,\t GROUPS.YEAR,\t GROUPS.RATING,\t DEPARTMENT.NAME")

    for row in rows:
        for value in row:
            print(f'\t{value}', end='\t\t')
        print()


# ▷ вивести інформацію про всіх викладачів,
def teachers_info():
    # запит
    query = f"""
        SELECT SURNAME, NAME, POSITION, ISPROFESSOR, SALARY, PREMIUM, EMPLOYMENTDATE
        FROM TEACHERS
        """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    print(f"SURNAME,\t NAME,\t\t POSITION,\t ISPROFESSOR,\t SALARY,\t PREMIUM,\t EMPLOYMENTDATE")

    for row in rows:
        for value in row:
            print(f'{value}', end='\t\t')
        print()

# ▷ вивести назви усіх кафедр,
def departments_name():
    query = f"""
            SELECT NAME
            FROM DEPARTMENTS
            """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    print(f"DEPARTMENT NAME")

    for row in rows:
        for value in row:
            print(f'{value}', end='\t\t')
        print()

# ▷ вивести імена та прізвища викладачів, які читають
# лекції в конкретній групі,
def show_groups():

    # запит
    query = f"""
    SELECT NAME 
    FROM GROUPS 
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


def name_teacher_ongroup():
    show_groups()
    groups_name = input("відділенні ")

    query = f"""
        SELECT TEACHERS.SURNAME, TEACHERS.NAME
        FROM GROUPSELECTURES
	    JOIN GROUPS ON GROUPS.ID = GROUPSELECTURES.GROUPEID
	    JOIN LECTURES ON LECTURES.ID = GROUPSELECTURES.LECTUREID
	    JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHERID
    WHERE GROUPS.NAME = '{groups_name}'
    """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    print(f"TEACHERS.SURNAME, TEACHERS.NAME")

    for row in rows:
        for value in row:
            print(f'{value}', end='\t\t')
        print()


# ▷ вивести назви кафедр і груп, які до них відносяться,
def dep_group():
    query = f"""
            SELECT GROUPS.NAME, DEPARTMENTS.NAME
            FROM GROUPS
            JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENTID
            """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    print(f"GROUPS.NAME,\t DEPARTMENT.NAME")

    for row in rows:
        for value in row:
            print(f'\t{value}', end='\t\t')
        print()


# ▷ відобразити кафедру з максимальною кількістю груп,
# ▷ відобразити кафедру з мінімальною кількістю груп,
# ▷ вивести назви предметів, які викладає конкретний
# викладач,
# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна,
# ▷ вивести назви груп, що належать до конкретного
# факультету,
# ▷ вивести назви предметів та повні імена викладачів,
# які читають найбільшу кількість лекцій з них,
# ▷ вивести назву предмету, за яким читається найменше лекцій,
# ▷ вивести назву предмету, за яким читається найбільше лекцій;



while True:
    print("1 - вивести інформацію про всі навчальні групи")
    print("2 - вивести інформацію про всіх викладачів")
    print("3 - вивести назви усіх кафедр")
    print("4 - вивести імена та прізвища викладачів, які читають лекції в конкретній групі")
    print("5 - вивести назви кафедр і груп, які до них відносяться")

    command = input('Введіть номер команди: ')

    if command == '1':
        groups_info()
    elif command == '2':
        teachers_info()
    elif command == '3':
        departments_name()
    elif command == '4':
        name_teacher_ongroup()
    elif command == '5':
        dep_group()
    else:
        print('невірна команда')