from asyncio import current_task


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


class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def do(self):
        """
        Виконує завдання, за потреби розбиває його на підзавдання
        :return: список підзавдань
        """
        if self.subtasks:
            print(f"Виконую завдання: {self.name}. Розбиваю на підзавдання")
        else:
            print(f"Завершено завдання: {self.name}")

        return self.subtasks


class Project:
    ## YOUR CODE
    # Використовуючи стеки, змоделюйте роботу над
    # виконанням проекту. Як відомо складні завдання часто
    # розбивають на під задачі в процесі роботи, і тільки коли всі
    # вони виконані вважається що з основним завданням ви
    # впорались.
    # Створіть клас Project
    # Атрибути:
    #  tasks – стек з завданнями, об’єкти класу Task (початкове
    # завдання передається в init)
    def __init__(self, tasks):
        self.tasks = DoubleLinkedList()
        self.tasks.push_end(tasks)


    # Методи:
    #  do_task() – видалити останнє завдання з стеку та
    # виконати його, якщо для цього потрібно зробити під
    # завдання, то добавити їх у стек
    # Якщо стек порожній то вивести про це повідомлення
    def do_task(self):
        if self.tasks.is_empty():
            print("Немає завдань.")
            return

        # print(self.tasks)
        current_task = self.tasks.pop_end()
        new_task = current_task.do()

        for t in new_task:
            self.tasks.push_end(t)


    #  is_finished() – True якщо завдань не залишилось
    def is_finished(self):
        if self.tasks.is_empty():
            print("Немає невиконаних завдань.") # Виводить повідомлення про кінець.
            # Перевірка кінця в ду_таск - не спрацює, бо спочатку незапуститься цикл Вайл з виконанням цього Ду_таск
        return self.tasks.is_empty()
    #
    # Клас Task(уже реалізований):
    #  do() – виконує завдання(виводить на екран інформацію
    # про це) та повертає список з підзавданням для
    # успішного виконаня



task = Task('Підготовка до зйомок')

task.subtasks = [
    Task('Пошук локацій'),
    Task('Підготовка сценарію'),
    Task('Кастинг акторів')
]

# Підзавдання для "Пошук локацій"
task.subtasks[0].subtasks = [
    Task('Огляд локацій у місті'),
    Task('Огляд локацій за містом'),
    Task('Узгодження місць для зйомок')
]

# Підзавдання для "Підготовка сценарію"
task.subtasks[1].subtasks = [
    Task('Написання основного сценарію'),
    Task('Редагування сценарію'),
    Task('Підготовка сценарних приміток'),
]

# Підзавдання для "Кастинг акторів"
task.subtasks[2].subtasks = [
    Task('Пошук головних акторів'),
    Task('Пошук другорядних акторів'),
    Task('Підготовка контрактів для акторів')
]

# Підзавдання для "Пошук локацій у місті"
task.subtasks[0].subtasks[0].subtasks = [
    Task('Вибір декорацій для зйомок'),
    Task('Узгодження з власниками приміщень')
]

# Підзавдання для "Огляд локацій за містом"
task.subtasks[0].subtasks[1].subtasks = [
    Task('Вибір лісу для сцени битви'),
    Task('Пошук старовинних будівель для сцени'),
]

# Підзавдання для "Написання основного сценарію"
task.subtasks[1].subtasks[0].subtasks = [
    Task('Написання першої частини'),
    Task('Написання другої частини'),
]

# Підзавдання для "Пошук головних акторів"
task.subtasks[2].subtasks[0].subtasks = [
    Task('Пошук актора на роль головного героя'),
    Task('Пошук актриси на роль головної героїні')
]


project = Project(task)


# print(task.do())
# project.do_task()
while not project.is_finished():
    project.do_task()


