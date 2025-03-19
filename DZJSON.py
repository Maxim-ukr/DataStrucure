# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями
import json
import random
from random import randint


def choice():
    print("""    __________________________
    - 1. ГРАТИ               -
    - 2. Вивести результат   -
    - 3. Зберегти дані       -
    - 4. Завантажити дані    -
    - 5. ЗАКІНЧИТИ           -
    __________________________
    """)

def game():
    comp_number = randint(1,100)
    sproba = 0

    while True:
        user_n = int(input(f"Ваша спроба №{sproba+1}. Введіть число від 1 до 100:"))

        if sproba < 4:
            if user_n == comp_number:
                score['user'] += 1
                print(f"""Ви вгадали. Компьюте загадава число {comp_number}. Раунд завершено.""")
                print_result()
                break

            elif user_n > comp_number:
                sproba += 1
                print("Меньше.")


            elif user_n < comp_number:
                sproba += 1
                print("Більше.")

        else:
            score['comp'] += 1
            print(f"Ви НЕ вгадали. Компьюте загадава число {comp_number}. Раунд завершено.")
            print_result()
            break

def print_result():
    print(f"Рахунок (Ви:Компютер) {score['user']}:{score['comp']}")

def save_data():
    with open("users.json", "w") as file:
        json.dump(score, file)
        print("Дані збережені.")

def load_data():
    with open("users.json", "r") as file:
        score = json.load(file)
        print("Дані завантажено.")
        return score


score = {'user': 0, 'comp': 0}

while True:

    choice()

    user_choice = input("Зробіть свій вибір: ")

    if user_choice == "5":
        break
    elif user_choice == "1":
        game()
    elif user_choice == "2":
        print_result()
    elif user_choice == "3":
        save_data()
    elif user_choice == "4":
        score = load_data()
    else:
        print("Невідома команда.")