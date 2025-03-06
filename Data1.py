#
# ==============================================================================структури даних

# нотація O

# n = 10
# a = 2 + 3  # швидкість не залежить від n. O(1)
#
#
# for i in range(n):  # кількість операцій залежить від n. O(n)
#     print(i)
#
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)

# import math
#
# N = 10**12
# print(math.log(N))


# зв'язний список
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # вузол який йде наступним
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
#
# # node1 = Node(4)
# # node2 = Node('abc')
# # node3 = Node(5)
# #
# # node1.next = node2
# # node2.next = node3
# #
# # print(node1)
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None  # перший вузол, поки що список порожній
#
#     def append(self, data):
#         node = Node(data)
#
#         # якщо список пустий
#         if self.head is None:
#             self.head = node
#             return  # кінець
#
#         # знайти останній вузол
#         end = self.head
#
#         while end.next is not None:  # поки можна рухатись далі
#             end = end.next
#
#         end.next = node
#
#     def __str__(self):
#         return str(self.head)
#
#
# class LinkedList1:
#     def __init__(self):
#         self.head = None  # перший вузол, поки що список порожній
#         self.tail = None  # останній вузол, поки що список порожній
#
#     def append(self, data):
#         node = Node(data)
#
#         # якщо список пустий
#         if self.head is None:
#             self.head = node
#             self.tail = node
#             return  # кінець
#
#         # добавити в кінець вузол
#         self.tail.next = node
#         self.tail = node
#
#     def __str__(self):
#         return str(self.head)
#
#
# list1 = LinkedList1()
#
# list1.append(2)
# list1.append(5)
# list1.append(1)
# list1.append(4)
#
# print(list1)


# __________________________________________________________

# Створіть клас однозв’язного списку SinglyLinkedList
# Методи
#  print() – виводить список на екран
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_start() – видалити перший елемент

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __str__(self):
#         return f"{self.head}"
#
#     def push_end(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         self.tail.next = new_node
#         self.tail = new_node
#
#         #  push_start(data) – добавити на початку
#     def push_start(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         new_node.next = self.head
#         self.head = new_node
#
#     def pop_start(self):
#         if self.head is None:
#             raise ValueError('List is empty')
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#             return
#
#         # self.head = self.head.next
#         next_node = self.head.next
#         self.head.next = None
#         self.head = next_node
#
# data = SinglyLinkedList()
#
# data.push_end(1)
# print(data)
# data.push_end(2)
# print(data)
# data.push_end(3)
# data.push_start(5)
# print(data)
# data.push_start(10)
# print(data)
# data.pop_start()
# print(data)

# +++++++++++++++++++++++++++++++++STEKI

# class Shop:
#     def __init__(self):
#         self.queue1 = DoublyLinkedList()
#         self.queue2 = DoublyLinkedList()
#         self.queue3 = DoublyLinkedList()
#
#     def get_queue(self, idx):
#         if idx == 1:
#             return self.queue1
#         elif idx == 2:
#             return self.queue2
#         elif idx == 3:
#             return self.queue3
#
#
#     def add(self, name, idx):
#         queue = self.get_queue(idx)
#         queue.push_end(name)


# list1 = []
# list1[2]  # O(N) -- кількість операцій співрадає(в середньому) з кількітю елементів у списку
# list1[::-1]  # задом наперед O(N)
# list1 += [1, 2, 3]  # O(N)
# list1.append(2)  # O(N)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

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
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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
        else:
            self.tail = self.tail.prev
            self.tail.next = None

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
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def is_empty(self):
        """
        Чи є порожній
        :return: True якщо порожній
        """
        return self.head is None

    def peek(self):
        """
        Повертає останній елемент, не видаляючи його
        :return: останній елемент
        """
        return self.tail.data



# stack = DoubleLinkedList()
# print(stack)
#
# stack.push_end(2)  # добавити до стеку
# print(stack)
#
# stack.push_end(4)
# stack.push_end(1)
# stack.push_end(5)
# print(stack)
#
#
# last_num = stack.pop_end()
# print(f"{last_num=}")
# print(stack)

# є послідовність символів, видалити дублікати,
# які знаходяться пору

# abbbccccaaaabbb -> abcab

# text = "abbbccccaaaabbb"
# stack = DoubleLinkedList()
#
# for char in text:
#     # якщо стек порожній
#     # print(stack)
#     if stack.is_empty():
#         stack.push_end(char)
#         continue  # переходимо до наступної літери

    # last_char = stack.pop_end()  # дістаємо останню
    #
    # if last_char == char:
    #     # вертаємо last_char назад
    #     stack.push_end(last_char)
    # else:
    #     stack.push_end(last_char)
    #     stack.push_end(char)


    # з peek
    # last_char = stack.peek()
    #
    # if last_char != char:
    #     stack.push_end(char)


# перевести стек в str
# new_text = ''
#
# while not stack.is_empty():
#     last_char = stack.pop_end()
#     new_text = last_char + new_text
#
# print(new_text)

# _______________________________

# Завдання 2
# Використовуючи стек створіть клас EnterNumber для
# введення числа в рядку
# Атрибути:
#  digits – стек з введеними цифрами
# Методи:
#  add(digit) – додати нову цифру, вивести помилку якщо
# не цифра
#  undo() – видалити останню цифру
#  get_number() – повернути число
#  clear() – очистити стек

class EnterNumber:
    def __init__(self):
        self.digits = DoubleLinkedList()

    def add_didg(self, digit):
        self.digits.push_end(digit)

    def undo(self):
        self.digits.pop_end()

    def get_number(self):
        num_str = ''

        while not self.digits.is_empty():
            if self.digits.peek().isdigit():
                num_str = self.digits.pop_end() + num_str
            else:
                raise ValueError("In text not only digit. Operation is break.")

        return int(num_str)

    def clear(self):
        self.digits = DoubleLinkedList()



reader = EnterNumber()
dig = input("Enter the digit: ")
reader.add_didg(dig)
dig = input("Enter the digit: ")
reader.add_didg(dig)
dig = input("Enter the digit: ")
reader.add_didg(dig)

reader.clear()

dig = input("Enter the digit: ")
reader.add_didg(dig)


print(reader.get_number())
# print()



