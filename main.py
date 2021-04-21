import numpy as np
# zad1
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = a * b
# print(c)

# zad2
# a = np.arange(9).reshape(3, 3)
# b = np.arange(20, 36, 1).reshape(4, 4)
# print(a)
# print('')
# print(a.min(axis=0))
# print(a.min(axis=1))
# print('')
# print(b)
# print('')
# print(b.min(axis=0))
# print(b.min(axis=1))

# zad3
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.dot(a, b))

# zad4
# a = np.array([1, 2, 3])
# b = np.array([4.3, 5.1, 6.8])
# c = a * b
# print(c)

# zad5
# c = np.arange(6).reshape(2, 3)
# a = np.copy(np.sin(c))
# print(a)

# zad6
# d = np.arange(6, 12, 1).reshape(2, 3)
# b = np.copy(np.cos(d))
# print(b)

# zad7
# c = np.arange(6).reshape(2, 3)
# a = np.copy(np.sin(c))
# d = np.arange(6, 12, 1).reshape(2, 3)
# b = np.copy(np.cos(d))
# z = a + b
# print(z)

# zad8
# a = np.arange(9).reshape(3, 3)
# print(a)
# for b in a:
#     print(b)
#     print('')

# zad9
# a = np.arange(9).reshape(3, 3)
# print(a)
# for b in a.flat:
#     print(b)

# zad10
# 81x1, 1x81, 3x27, 27x3, 9x9 Po wymnożeniu przez siebie wymiarów macierzy musimy otrzymać liczbę 81
# a = np.ones([9, 9]).reshape(3, 27)
# print(a)
