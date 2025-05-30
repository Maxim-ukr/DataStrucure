
class Node:
    # майбутні покупці
    def __init__(self, data):
        self.data = data # імя покупця
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """
    # майбутні черги

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None
        self.nodcount = 0

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.nodcount += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.nodcount += 1

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.nodcount += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.nodcount += 1

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.nodcount -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.nodcount -= 1

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.nodcount -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.nodcount -= 1

        return data

    #
# Використовуючи класи з практичної реалізуйте клас Shop з
# трьома чергами до кас. Кожна черга реалізується через
# двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги
# номер idx
#  serve_buyer(idx) – обслуговує покупця з черги
# idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить
# в чергу з номером idx
#  display_info() – виводить на екран 3 черги

class Shop:
    def __init__(self):
        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()


    def add_buyer(self, name, idx):
        # – додає покупця в кінець черги номер idx
        if idx == 1:
            self.queue1.push_end(name)
        elif idx == 2:
            self.queue2.push_end(name)
        elif idx == 3:
            self.queue3.push_end(name)
        else:
            print("Невірний номер черги.")

    def serve_buyer(self, idx):
        # – обслуговує покупця з черги idx(вивести повідомлення та видалити покупця з черги)
        # Якщо черга стала порожньою, то викликати _reorder(idx)
        if idx == 1:
            name = self.queue1.pop_start()
            print(f"Покупець {name} з черги 1 обслужений.")

            if self.queue1.head is None:
                self._reorder(1)

        elif idx == 2:
            name = self.queue2.pop_start()
            print(f"Покупець {name} з черги 2 обслужений.")

            if self.queue2.head is None:
                self._reorder(2)

        elif idx == 3:
            name = self.queue3.pop_start()
            print(f"Покупець {name} з черги 3 обслужений.")

            if self.queue3.head is None:
                self._reorder(3)

        else:
            print("Невірний номер черги.")

    def _reorder(self, idx):
        if idx == 1:
            if self.queue2.nodcount >= self.queue3.nodcount:
                custumer = self.queue2.pop_end()
                self.queue1.push_start(custumer)
            else:
                custumer = self.queue3.pop_end()
                self.queue1.push_start(custumer)

        elif idx == 2:
            if self.queue1.nodcount >= self.queue3.nodcount:
                custumer = self.queue1.pop_end()
                self.queue2.push_start(custumer)
            else:
                custumer = self.queue3.pop_end()
                self.queue2.push_start(custumer)

        else:
            if self.queue1.nodcount >= self.queue2.nodcount:
                custumer = self.queue1.pop_end()
                self.queue3.push_start(custumer)
            else:
                custumer = self.queue2.pop_end()
                self.queue3.push_start(custumer)


    def display_info(self):
        # – виводить на екран 3 черги
        print(f'Черга 1: {self.queue1}')
        print(f'Черга 2: {self.queue2}')
        print(f'Черга 3: {self.queue3}')

    # Приклад використання
shop = Shop()
shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)
print("Черги:")
shop.display_info()
shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)
print("Після обслуговування покупців:")
shop.display_info()
shop.serve_buyer(1)
print("Покупці перейшли до вільної каси:")
shop.display_info()