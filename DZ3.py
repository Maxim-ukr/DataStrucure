# Використовуючи черги з пріоритетом створіть програму
# для симуляції роботи аеропорту. Кожен пасажир має пройти
# через 3 етапи: реєстрація, контроль безпеки, посадка.
# Відповідно аеропорт складається з 3-ох зон, кожна з яких має
# свою чергу. Коли Пасажир пройшов одну зону, то переходить
# в наступну.
# Пасажири з вищим пріоритетом обслуговуються першими

# Клас Zone – зона
# Атрибути:
#  name – назва(реєстрація, контроль безпеки або посадка)
#  passengers – черга пасажирів
# Методи:
#  add(passenger) – додає пацієнта в чергу з пріоритетом
#  serve_passenger() – обслуговуємо наступного пасажира
# та повертає його

# Клас Airport – аеропорт
# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3
# зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги
# реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги
# контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та
# переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній
# зоні та скільки успішно все пройшли
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет

from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage):
        self.name = name
        self.priority = priority
        self.baggage = baggage



class Zone:
    # Методи:
    #  add(passenger) – додає пацієнта в чергу з пріоритетом
    #  serve_passenger() – обслуговуємо наступного пасажира
    # та повертає його
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add_passanger(self, passenger):
        priority = passenger.priority

        pair = (priority, passenger)

        self.passengers.put(pair)

    def serve_passenger(self):
        priority, passenger = self.passengers.get()
        return passenger


# -__________DZ
# Створіть дочірні класи від Zone та перевизначте метод
# serve_passenger() щоб він повертав пару: пасажир та True/False
# в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету(у багажі)
#  безпека – відсутність небезпечних предметів у багажі:
# ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger

class ZoneR(Zone):
     def serve_passenger(self):
        priority, passenger = self.passengers.get()
        if "ticket" in passenger.baggage:
            return passenger, True
        else:
            return passenger, False


class ZoneC(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            if ("weapon" in passenger.baggage) or ("knife" in passenger.baggage):
                return passenger, True
            else:
                return passenger, False
        return None, True


class ZoneB(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            return passenger, True
        return None, False


    #


# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3
# зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги
# реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги
# контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та
# переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній
# зоні та скільки успішно все пройшли
class Airport:
    def __init__(self):
        self.zones = {"Registration": ZoneR("Реєстрація"),
                      "Control": ZoneC("Контроль"),
                      "Board": ZoneB("Посадка")}
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passanger(passenger)

    def serve_registration(self):
        pas, bool = self.zones["Registration"].serve_passenger()
        # перевірка чи відповідає пасажир умові переходу в іншу зону
        if bool:
            self.zones["Control"].add_passanger(pas)
            print(f"{pas.name} пройшов в зону контролю безпеки.")
        else:
            print(f"{pas.name} не має квитка.")

    def serve_security_control(self):
        pas, bool = self.zones["Control"].serve_passenger()
        if (pas != None) and not bool:
            self.zones["Board"].add_passanger(pas)
            print(f"{pas.name} пройшов в зону посадки.")
        elif pas != None:
        # else:
            print(f"{pas.name} має в багажі заборонені предмети.")

    def serve_boarding(self):
        pas, bool = self.zones["Board"].serve_passenger()
        if bool:
            self.passengers.append(pas)

    def show_statistics(self):
        print(len(self.passengers))
        for p in self.passengers:
            print(f"В літаку пасажир - {p.name}")


# # Тестування
airport = Airport()

passengers = [
    Passenger("Олег", 3, ["weapon", "clothes"]),
    Passenger("Анна", 5, ["ticket", "knife"]),
    Passenger("Марія", 4, ["clothes"]),  # немає квитка
    Passenger("Сергій", 2, ["ticket", "book"]),
    Passenger("Ігор", 1, ["ticket", "clothes"]),
]

for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_registration()
airport.serve_registration()
airport.serve_registration()

airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()

airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()

airport.show_statistics()
