# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

import threading

# наскільки я зрозумів, враховуючи, що з потока нічого ретьорнути неможна, для виконання цієї задачі необхідно
# створити та в потоці обявити глобальну змінну типу ліст і в нього апендити.
nums = []


def num_input():
    global nums

    while True:
        try:
            num = input('Введіть число: ')
            if num == '':
                break
            num = int(num)
            nums.append(num) # неспрацьовує при помилці перевода в інт, бо виникає помилка - тож все ок
        except Exception as err:
            print(f"Помилка: {err} - {num} не є цифрою.")

def sum_list(nums):
    print(f"Сума складає {sum(nums)}")

def seredne(nums):
    print(f"Середнє дорівнює {sum(nums) / len(nums)}")

num_input()
print(nums)
sum_list(nums)
seredne(nums)
print('Теж саме тільки через потоки')

thr_num_input = threading.Thread(target=num_input)
thr_sum_list = threading.Thread(target=sum_list, args=(nums,))
thr_seredne = threading.Thread(target=seredne, args=(nums,))

thr_num_input.start()
thr_num_input.join()

print(nums)

thr_sum_list.start()
thr_seredne.start()

thr_sum_list.join()
thr_seredne.join()
