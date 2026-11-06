class Polynomial():
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Polynomial):
            self.coef = args[0].coef.copy()
        elif len(args) == 1 and isinstance(args[0], dict):
            d = args[0]
            max_deg = max(d.keys()) if d else 0
            self.coef = [0] * (max_deg + 1)
            for deg, val in d.items():
                self.coef[deg] = val
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.coef = list(args[0])
        else:

            self.coef = list(args)
        while len(self.coef) > 1 and self.coef[-1] == 0:
            self.coef.pop()

    def __repr__(self):

        return f'Polynomial {self.coef}'

        





    def __str__(self):
        if not self.coef:
            return "0"
        parts = []
        for deg in range(len(self.coef) - 1, -1, -1):
            val = self.coef[deg]         #Пропуск нулевого коефицента
            if val == 0:
                continue
            sign = "+ " if val > 0 else "- "  # Определение знака перед коефицентом
            abs_val = abs(val)
            coef_str = "" if (abs_val == 1 and deg != 0) else str(abs_val) # Учет 1x для всех коефицентов кроме свободного

            if deg == 0: #для свободного члена
                x_str = str(abs_val)
                coef_str = ""
            elif deg == 1:# для x^1
                x_str = "x"
            else:
                x_str = f"x^{deg}"
            parts.append(f"{sign}{coef_str}{x_str}") #добавление по 1 члену многочлена в список
        if not parts:
            return "0"
        result = " ".join(parts)
        if result.startswith("+ "): # Переделывание некрасивого начала
            result = result[2:]
        elif result.startswith("- "):
            result = "-" + result[2:]
        return result

    def degree(self):# Возвращает степень многочлена
        return len(self.coef) - 1

    def __eq__(self, other):# Равенство многочленов
        if isinstance(other, int):
            other = Polynomial(other)
        if not isinstance(other, Polynomial): return False # Проверка на коректный ввод
        if self.coef == other.coef:
            return True
        else: return False

    def __add__(self, other):# сложение
        if isinstance(other, (int, float)):
            other = Polynomial(other)

        max_len = max(len(self.coef), len(other.coef))

        res_coef = [0] * max_len

        for i in range(max_len):
            val1 = self.coef[i] if i < len(self.coef) else 0
            val2 = other.coef[i] if i < len(other.coef) else 0
            res_coef[i] = val1 + val2
        return Polynomial(res_coef)



    def __radd__(self, other):
        return self + other

    def __neg__(self):

        return Polynomial(*[-x for x in self.coef]) #* превращает вывод в красивый(аргументы списка выводятся так(..,..,..))



    def __sub__(self, other):#вычитание
        if isinstance(other, int):
            other = Polynomial(other)


        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __call__(self, x):
        result = 0
        for i in range(len(self.coef)):
            result += x ** i * self.coef[i]
        return result

    def der(self, d=1):
        if d <= 0:
            return Polynomial(self.coef)

        res = self.coef.copy()
        while d > 0:
            if len(res) <= 1:
                res = [0]
                break
            for i in range(len(res) - 1):
                res[i] = res[i + 1] * (i + 1)
            res = res[:-1]
            d -= 1
        return Polynomial(res)

    def __mul__(self, other): #Умножение(работает как раскрытие скобок, каждый член на каждый и их сумма)
        if isinstance(other, int):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            return False

        # Если один из многочленов нулевой, результат — просто [0]
        if self.coef == [0]:
            return Polynomial(0)

        res_len = len(self.coef) + len(other.coef) - 1
        res_coef = [0] * res_len

        for i in range(len(self.coef)):
            for j in range(len(other.coef)):
                res_coef[i + j] += self.coef[i] * other.coef[j]

        return Polynomial(res_coef)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):

        if self._iter_idx < len(self.coef):
            degree = self._iter_idx
            coeff = self.coef[self._iter_idx]

            self._iter_idx += 1

            return (degree, coeff)
        else:
            raise StopIteration #Специальная команда которая завершает итерацию внутри метода __next











poly = Polynomial({0: -3, 2: 1, 5: 4})
print(Polynomial({0: -3, 2: 1, 5: 4})) # Вывод: 4x^5 + x^2 - 3
print(Polynomial(poly))                # Вывод: 4x^5 + x^2 - 3
print(Polynomial([1, 2, 3]))           # Вывод: 3x^2 + 2x + 1
print(Polynomial(0, 2, 0, 5))
print(poly.degree())
print(poly == poly)
print(poly + poly)
print(-poly)
print(5 + poly)
print(poly - poly)
print(poly - 5)
print(5 - poly)
print(poly(2))
print(poly.der())
print(poly * 5)
print(5 * poly)
for i, j in poly:
    print(i, j)


# polys = [Polynomial(1, 2), Polynomial(3, 4)]
# print(polys)  # Выведет: [Polynomial, Polynomial]

print(Polynomial(0, 2, 0, 5))
print(Polynomial(1, 2, 0, 0).degree())
print(poly.der(2))
print(poly * 0)
print(repr(Polynomial({5:4, 2:1, 0:-3, 6:0})))
