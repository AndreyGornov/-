# name = 'Vanya'
# second_name: str = 'Elena'
#
#
# def repeater(s: str, n: int) -> str:
#     return s * n

# f = open('123.txt', 'x')  # создание нового файла и работа с ним
# f.write('Hello world')
# f.close()


# f = open('12.txt', 'a')  # дописывание к файлу
# f.write(str(5 * 2))
# f.close()

# import time
# class MyContextManager:
#     def __enter__(self):
#         self.t = time.time()
#         print('entered')
#         return self
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.e = time.time()
#         print('exited')
#
#     def __float__(self):
#         return float(self.e - self.t)
#
#
#
# with MyContextManager() as mcm:
#     print('AAA')
#     print('bbb')
#
# print(float(mcm))

# написать контекстный менеджер для управления отступами
# при входе в блок with количество отступов (табуляций) увеличивается на 1
# запись ведётся в файл

# class ContextManager:
#     level = 0
#     def __init__(self, filename: str):
#         self.filename = filename
#
#     def __enter__(self):
#         ContextManager.level += 1
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         ContextManager.level -= 1
#
#     def write(self, text: str):
#         with open(self.filename, "a") as f:
#             f.write(f"{'':>{ContextManager}}{text}\n")


# import time
# def countdown(n):
#     while n > 0:
#         print('T-minus ', n)
#         n -= 1
#         time.sleep(5)
#
# from threading import Thread
# t = Thread(target=countdown, args=(10, ), daemon=True) # Вынесение в отдельный поток вызов класса
# print('hello')
# t.start()








