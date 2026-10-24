class Polynomial:
    def __init__(self, *args):
        self.__coefficients = None
        self.__spisok = None
        self.__copy = None

        if len(args) == 1:
            if isinstance(args[0], Polynomial):
                self.__copy = args[0]
            if isinstance(args[0], dict):
                self.__coefficients = args[0]
            if isinstance(args[0], list):
                self.__spisok = args[0]

        else:
            self.__spisok = args

    @property
    def copy(self):
        return self.__copy

    @property
    def spisok(self):
        return self.__spisok


    @property
    def coefficients(self):
        return self.__coefficients


    def dicthelp(self):  #сортирует словарь по убыванию коэфицентов
        newdict = dict(reversed(sorted(self.coefficients.items())))
        return newdict

    def dicthelp2(self): #заменяет значение коэфицентов на красивые для красивого вывода
        newdict = self.dicthelp()

        for key in newdict:
            if int(newdict[key]) < 0:
                newdict[key] = f'- {abs(newdict[key])}'
            elif int(newdict[key]) >= 0:
                newdict[key] = f'+ {newdict[key]}'
        return newdict

    def readydict(self): #Окончательно красивый вывод
        result = ''
        p = self.dicthelp2()
        for i in p:
            result += f'{p[i]}x^{i} '
        while '0x' in result:
            result = result[:result.find('0x')] + result[result.find('0x') + 7:]
        result = result.replace('x^0', '').replace('1x', 'x').replace('x^1', 'x')
        if result[0] == '+':
            result = result[2:]
        else:
            result = '-' + result[2:]
        if result[-2] == '+' or result[-2] == '-':
            result = result[:-2]
        return result




    def readycopy(self):
        return f'{self.copy}'


    def readylist(self):
        slov = {}
        for i in range(len(self.spisok)):
            slov[i] = self.spisok[i]
        self.__coefficients = slov
        return self.readydict()






    def __str__(self):
       if self.__spisok is not None:
           return self.readylist()
       if self.__coefficients is not None:
           return self.readydict()

       if self.__copy is not None:
           return self.readycopy()



       return 0



poly = Polynomial({0:-3, 2:1, 5:4})
print(Polynomial({0:-3, 2:1, 5:4}))
print(Polynomial(poly))
print(Polynomial([1,2,3]))
print(Polynomial(0,2,0,5))



