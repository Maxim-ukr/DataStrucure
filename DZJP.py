# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle

def add_artist(artists):
    art = input("Введіть нового артиста: ")
    artists[art] = []

def add_album(artists):
    art = input("Введіть артиста: ")
    if art in artists:
        alb = input("Введіть альбом, який треба додати: ")
        print(type(art))
        artists[art].append(alb)
    else:
        print("В переліку відсутній такий артист.")

def save_jason(artists):
    with open("DZ.jsn", 'w') as file:
        json.dump(artists, file)

def save_pickle(artists):
    with open("DZ.pcl", 'wb') as file:
        pickle.dump(artists, file)

def open_jason():
    with open("DZ.jsn", 'r') as file:
       return json.load(file)

def open_pickle():
    with open("DZ.pcl", 'rb') as file:
        return pickle.load(file)



artists = {}

add_artist(artists)
add_artist(artists)
add_artist(artists)
print(artists)
add_album(artists)
add_album(artists)
print(artists)
save_jason(artists)
save_pickle(artists)
add_artist(artists)
add_album(artists)
print(artists)
artists = open_jason() # перед додаванням функції опен пікл перевірив на опен джейсон
artists = open_pickle()
print(artists)