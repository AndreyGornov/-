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

import time
class MyContextManager:
    def __enter__(self):
        self.t = time.time()
        print('entered')
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.e = time.time()
        print('exited')

    def __float__(self):
        return float(self.e - self.t)



with MyContextManager() as mcm:
    print('AAA')

print(float(mcm))

class IndentWriter:
    def __init__(self, file_obj):
        self.file = file_obj
        self.level = 0  # Текущий уровень отступа

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        # Позволяем исключениям, если они возникнут, всплывать дальше
        return False

    def write(self, text):
        # Добавляем табуляции перед строкой и записываем в файл
        indent = "\t" * self.level
        self.file.write(f"{indent}{text}\n")
print()







