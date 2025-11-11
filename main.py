# 1 - misol
sonlar = [1, 2, 3, 4, 5, 6]
natija = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, sonlar)))
print(natija)


# 2 - misol
sozlar = ["salom", "kitob", "dasturlash", "olma", "universitet"]
natija = list(map(lambda s: s.upper(), filter(lambda s: len(s) > 5, sozlar)))
print(natija)


# 3 - misol
sonlar = list(range(1, 11))
natija = list(map(lambda x: x**2, filter(lambda x: x % 2 == 1, sonlar)))
print(natija)


# 4 - misol
sonlar = [-3, -1, 0, 2, 4, -5]
natija = list(map(lambda x: x * 10, filter(lambda x: x > 0, sonlar)))
print(natija)


# 5 - misol
sonlar = list(range(1, 15))
natija = list(map(lambda x: x**3, filter(lambda x: x % 3 == 0, sonlar)))
print(natija)


# 6 - misol
malumot = ["12", "salom", "45", "9a", "100"]
natija = list(map(lambda x: int(x), filter(lambda x: x.isdigit(), malumot)))
print(natija)


# 7 - misol
haroratlar = [-5, 0, 10, 20, 30]
natija = list(map(lambda c: c * 9/5 + 32, filter(lambda c: c > 0, haroratlar)))
print(natija)


# 8 - misol
ismlar = ["Ali", "Vali", "Anora", "Aziz", "Bobur"]
natija = list(map(lambda x: len(x), filter(lambda x: x.lower().startswith('a'), ismlar)))
print(natija)


# 9 - misol
sonlar = list(range(51))
natija = list(map(lambda x: x / 5, filter(lambda x: x % 2 == 0, sonlar)))
print(natija[:10]) 


# 10 - misol
import math
sonlar = [-4, -1, 0, 9, 16, 25]
natija = list(map(lambda x: math.sqrt(x), filter(lambda x: x > 0, sonlar)))
print(natija)
