# Використовуючи бінарні дерева, організуйте роботу
# автопарку, де зберігаються автомобілі, відсортовані за
# маркою
# Клас Car
# Атрибути:
#  brand – модель автомобіля
#  model – марка автомобіля
#  year – рік випуску
from re import search

from bintrees import AVLTree

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


# Клас CarPark
# Атрибути:
#  cars – дерево з автомобілями
# Методи:
#  add(car) – добавити автомобіль
#  remove(model) – видалити автомобіль
#  search(model) – пошук автомобіля за маркою, якщо є
# то повертає машину інакше None
#  __len__() – кількість автомобілів
#  sell_car(client, model) – продати автомобіль клієнту,
# якщо така марка присутня
class CarPark:
    def __init__(self):
        self.cars = AVLTree()

    def __len__(self):
        return len(self.cars)

    def add(self, car):
        self.cars.insert(key=car.model,value=car)

    def search(self, model):
        if model in self.cars:
            return self.cars[model]
        else:
            return None

    def remove(self, model):
        if self.search(model) != None:
            self.cars.remove(model)
        else:
            print(f'Автомобіля моделі {model} немає в гаражі, тому видалити його неможливо.')


    def sell_car(self, client, model):
        car_for_sell = self.search(model)
        if car_for_sell != None:
            self.remove(model)
            print(f"Клієнту {client} продано автомобіль {car_for_sell.brand}, {car_for_sell.model}, {car_for_sell.year}.")
        else:
            print(f'Автомобіля моделі {model} немає в гаражі, тому його продати неможливо.')


car1 = Car('WV','Golf',2012)
car2 = Car('Deawoo','Lanos',2016)
car3 = Car('Renault','Megan',2024)
car4 = Car('Toyota','Corolla',2012)
car5 = Car('Volvo','V60',2020)

car_garage = CarPark()

car_garage.add(car1)
car_garage.add(car2)
car_garage.add(car3)
car_garage.add(car4)
car_garage.add(car5)
print(f"Авто в гаражі: {len(car_garage)}")

car_garage.remove('Lanoss')
print(f"Авто в гаражі: {len(car_garage)}")
car_garage.sell_car("Ivan",'Lanos')
print(f"Авто в гаражі: {len(car_garage)}")

