# a = [1,2,3,4]
# print(id(a))
# a.append(5)
# #a.extend(b) #Все значения из списка a дополняются списком b
# print(id(a))
# b = 2 ** 10000
# print(b)

#
# a =[1,2,3,4]
# b = [5,6,7]
# a.append(b)
# b.append(8)
# print(a) #вывод [1,2,3,4, [5,6,7,8]]

#Множества не могут храниться в множествах
# a = {1,2,3}
# b = {3,4,5}
# print(a | b)

# a = {1,2,3}
# b = [4,5,6]
# c = a | set(b)# ^ симметрическая разность
# print(c)

#Словари
# a = {1: 2, 3: 4}
# print(a)

# дано: текст
#получить: частный словарь символов
# a = input()
# slovar = {}
# asa = set(a)
# for i in asa:
#     slovar[i] = 0
#
# for k in a:
#     slovar[k] += 1
# print(slovar)


# a = input()
# b = input()
# f1 = {}
# f2 = {}
# for el in a:
#     f1[el] = 1
# for el in b:
#     f2[el] = 1
# if f1 == f2:
#     print(1)
# else:
#     print(0)


# d = dict()
# print(d.get(1, 0)) # Если нет ключа 1 то вывод 0, если есть то вывод того что под этим ключом
# d = dict.fromkeys([1,2,3], 'a') # Образует 3 ключа в словаре и в каждый записываем a
# d = dict()
# d = dict.fromkeys((1,2,3))
# c = {1: 2, 3:4, 5: 6}
# d.update(c) # Переносим в c словарь d




# col_name = [el for el in input().split(', ')]
# col_des = [el for el in input().split(', ')]
# im_des = [el for el in input().split(', ')]
# d = dict.fromkeys(col_name, 'пока хз')
# d2 = d
# for i in range(len(col_des)):
#     d2[col_name[i]] = col_des[i]
#
# for j in range(len(col_name)):
#     if d2[col_name[j]] in im_des:
#         im_des.remove(d2[col_name[j]])
#         d[col_name[j]] = 'может хавать'
#     else:
#         d[col_name[j]] = 'на диете'
# print(d)

#Домашняя задача
# def udslov(n):
#     if not(n):
#         return 1
#     else:
#         return 0
#
# def udmn(n):
#     if len(n) == 0:
#         return 1
#     else:
#         return 0
#
# a = ['abc', '', {'': '123', 'a': '123'}, {}]
#
# for el in a:
#     if isinstance(el,dict):
#         if udslov(el):
#             a.remove(el)
#     if isinstance(el,list):
#         if len(el) == 0:
#             a.remove(el)
#     if isinstance(el, str):
#         if len(el) == 0:
#             a.remove(el)
#     if isinstance(el,tuple):
#         if len(el) == 0:
#             a.remove(el)
# print(a)


# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
#
#
# print(mul(3)(5))

#Какаято непонятноя хуйня декорации
# import datetime
#
#
# def simple_decore(fn):
#     def wrapper(*args, **kwargs):
#         n = datetime.datetime.now()
#         val = fn(*args, **kwargs)
#         e = datetime.datetime.now()
#         print(e - n)
#         return val
#         print('Before call')
#         fn(*args, **kwargs)
#         print('After call')
#     return wrapper
#
#
# @simple_decore
# def first():
#     print('Test fuction 1')
#
#
# @simple_decore
# def second():
#     print('Test function 2')
#
# first_decor = simple_decore(first)
# first_decor()
#
# print()
# first()

#Классы и ООП
# class C:
#     pass
class Rectangle:
    default_color = 'green'

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, w):
        if w <= 0:
            raise Warning("value must be positive!")
        self.__width = w

    @height.setter
    def height(self, h):
        if h <= 0:
            raise Warning("value must be positive!")
        self.__height = h

    def __str__(self):
        return f'Rectangle with {self.__width} and height {self.__height} and area {self.area()}'
    def __repr__(self):  #Если __str__ нет то на вывод жаст __repr__
        return f'Rectangle({self.__width}, {self.__height})'


rectangle = Rectangle(10, 20)
print(rectangle.area())
print(rectangle.width)
rectangle.width = 20
print(rectangle.width)
print(rectangle)

class MyVector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z
    def sum(self, other):
        return MyVector(self.x + other.x, self.y + other.y, self.z + other.z)
    def dif(self, other):
        return MyVector(self.x - other.x, self.y - other.y, self.z - other.z)
    def multiply(self, other):
        return MyVector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __str__(self):
        return f"результирующий вектор:({self.x}; {self.y}; {self.z})"

v1 = MyVector(1, 2, 3)
v2 = MyVector(4, 5, 6)

print(v1.dif(v2))





# class MyClass:
#     @staticmethod
#     def ex_static_method():
#         print("static method")
#
#     @classmethod
#     def ex_class_method(cls):
#         print("class method")
#
# my_class = MyClass()
# my_class.ex_class_method()


