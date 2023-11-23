# age = 16
# result = 'adult' if age >= 18 else 'child'
# print(result)
# age = 18
# print('adult' if age >= 18 else 'child')

# x, y = 3, 5
# z = 3 + x if x > y else y
# print(z)
# print(3 + (x if x > y else y))


# l1 = ['']
# l2 = list()
# if l1 == l2:
#     print(True)
# else:
#     print(False)
#
# l3 = [False, 1, '2', [3]]
# print(l3[0], l3[-1])
#
# l3[0] = True
# l3.remove('2')
# l3.append(0)
# del l3[0]
# print(l3)

# t1 = ()
# t2 = tuple()
# if t1 == t2:
#     print(True)


# t3 = (False, 1, '2', [3])
# print(t3[0], t3[-1])
# t3[0] = True - # нельзя менять
# print(t3)

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a, b)

# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b = list(a)
# a.append('a')
# b.append('b')
# b[1][0] = 0
# print(a)
# print(b)
#
# from copy import deepcopy, copy
#
# c = copy(a)
# print(c)
# print(id(c), id(b), id(a))
#
# c.append('c')
# c[0][0] = 0
# print(a)
# print(c)

# tea_party = ('Rabbit', 'Bear', 'Fox', 'Turtle')
# tea_party_list = list(tea_party)
# print(tea_party_list)
# print(id(tea_party_list))
# tea_party_list[1:3] = ['Cat','Whale', 'True']
# print(tea_party_list)
# print(id(tea_party_list))


# lis = [3]
# lis.insert(0,2)
# print(lis)

# a = [1,2,3,4,5,6,6,6,6,6]
# print(a.count(6))

# c = [5, 1, 3, 0]
# a = sorted(c, reverse=True)
# print(a)

# a = [-1, 2, 4, 5]
# b = list(map(abs, a))
# print(b)
# c = [abs(i) for i in a]
# print(c)

# def f(x):
#    return x ** 2
# d = list(map(f, a))
# print(d)

# a = ['hello', 'good', 'abc']
# e = list(map(str.upper, a))
# g = list(map(lambda x: x + '!', a))
# c = [i[:: -1] for i in a]
# d = list(map(list, a))
# b = input().split()
# print(list(map(int, b)))

# a = [2, 3, 4, 5]
# b = [200, 300, 400, 500]
# c = 'abcd'
# rez = list(zip(a, b, c))

# for t1 in zip(a, b, c):
#     print(t1)

# for t1, t2, t3 in rez:
#     print(t1, t2, t3)

# c1, c2, c3 = zip(*rez)
# print(c1, c2, c3)


# i = 0
# k = 5
# summ = 0
# while True:
#     i += 1
#     summ += i
#     if not i < 100:
#         break

# a = 0
# summ = 0
# cnt = 0
# while a < 15:
#     a += 1
#     if a % 5:
#         continue
#     cnt += 1
#     summ += a
#

# numbers = [1, 2, 3, 4, 5]
# i = 0
#
# while i < len((numbers)):
#     if numbers[i] == 5:
#         print('Нашли 5-ку')
#         break
#     print(numbers[i])
#     i += 1
# else:
#     print('no find 5')


# a = ['Anar', 'Orxan', 'Ilyas']
# for name in a:
#     if name == 'Orxan':
#         continue
#     print(name)


# print([x*x for x in range(10) if x % 2 == 0])
# print(x*x for x in range(10) if x % 2 == 0)

# e = dict([('a', 2), ('b', 4), ('c', 5)])
# b = dict(a = 2, b = 4, c = 5 )
# a = ['a', 'b', 'c']
# b = [2, 4, 5]
# c = dict(zip(a, b))
# for k in a:
#     print(k)

# for k in a.values():
#     print(k)

# for k in a.items():
#     print(k)

# print(list(c.values()))
# print(list(c.keys()))
# print(list(c.items()))
# del c['a']
# c.update(e)
# print(c)


# dc = {i: i ** 3 for i in range(2, 6, 2)}
# print(5 in dc)
# print(dc.get(5, 'not_found'))
# print(dc.setdefault(6, 216))
# print(dc)
# b = {k:v for v,k in dc.items()}
# print(b)


# a = set([1,2])
# b = set([3,4,5,2])
# print(a|b)
# print(a - b)
# print(b - a)
# print(b & a)
# print(b ^ a)
# a.difference_update(b)
# b.remove(4)


# a = 'Hello Pitr, kak ti? ', 'spasibo bro'
# print(' - '.join(a))
# b = 'Hello Pitr, kak ti?  - spasibo bro'
# print(b.split())


# def main_func(name):
#     def inner_func():
#         print('hello my bro', name)
#
#     inner_func()
#
# main_func('Orkhan')


# def func_decorator(func):
#     def wrapper(*args):
#         print('----do-----')
#         func(*args)
#         print('------posle-----')
#
#     return wrapper
#
# def some_func(tittle, too):
#     print('вызов функции some_func','=', tittle, too)
#
# some_func = func_decorator(some_func)
# some_func('PYTHON', 'YES')


# def f(a, y = 3, x = None):
#     print(a,y, x, sep= ' - ')
#
# f(2,5, 6)


# def a(l):
#     l.append(1)
#     print('done')
#
#
# print(a([0]))


# def get_team(number, team):
#     number = 10
#     team['ismayilov'] = 'Orkhan'
#     team['Qasimli'] = 'Anar'
#     print(number, team)
# hero_team = {}
# get_team(2,hero_team)


# print([1,2,3,4,5])
# print(*[1,2,3,4,5], sep='-')

# def f(a, *args, b = 3):
#     print(f'{a} = a, {args} = args, {b} = b')
#
#
# f(1, 5)

# def f(*args, **kwargs):
#     print(f'{args} = args, {kwargs} = kwargs')
#
# f(1,'a',2, x = 5, y = [1,2])


# def sqr(x):
#     return int(x) * int(x)
#
# print(list(map(sqr, input().split())))


# def f():
#     x = 20
#     def g():
#         nonlocal x
#         x = 40
#
#
#     g()
#     print(x)
#
# f()


# m = []
# m.append(lambda x: x * 1)
# m.append(lambda x: x * 2)
# m.append(lambda x: x * 3)
#
# print(m[2](10))

# multmedia = []
# for m in range(5):
#     multmedia.append(lambda x: x * m)
#
# m = 2
# print(multmedia[3](1000))
#
# def mult(x):
#     return x * m
#
# print(mult(1000))
#
# a = [mult(i) for i in range(5)]
# print(a)


# def foo(x):
#     y = 3
#     def degree_two():
#
#
#         return y ** x
#
#
#     return degree_two()
#
#
# print(foo(2))


# def foo(x):
#     def degree_two(y):
#         return x, y
#
#     return degree_two
#
#
# print(foo(3)(5))
# print(foo(2)(7))


# def gen_counter(n):
#     while n != 0:
#         yield n - 1
#         n -= 1
# g = gen_counter(4)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for i in range(4):
#     print(next(g))

# res = []
# def counter(n):
#     while n != 0:
#         res.append(n - 1)
#         n -= 1
#     return res
# print(counter(4))
# print(*res)


# def decorator(func):
#     def inner(*args):
#         print('start decorator')
#         func(*args)
#         print('finish decorator')
#     return inner
#
# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#     return inner
#
# @header
# @decorator
# def say(name):
#     print('hello world', name)
#
# print(say('Orxan'))


"""say = header(decorator(say)) ==>  @decorator, header
   print(say('Orxan')) так обычно не делают"""

'''def buy():
     print('buy world')
   buy = decorator(buy)
   print(buy())  можно добавить еще функций'''

# def deprecate(func):
#     def wrapper(*args, **kwargs):
#         print('deprecated: '+ func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# def congress(func):
#     def wrapper(*args, **kwargs):
#         print('Congress: '+ func.__name__)
#         return func(*args, **kwargs)
#
#
#     return wrapper
# @deprecate
# @congress
# def one_maxx(a, b):
#     return a + b
#
# print(one_maxx(2, 3))


# import functools
# def deprecated(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('WARNING: ' + func.__name__ +' is deprecated')
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @deprecated
# def own_max(a, b):
#     'This is a really nice looking docstring'
#     return a if a > b else b
#
# print(own_max(1, 2))
# print(own_max.__name__)
# print(own_max.__doc__)


# class Vector:
#     def __init__(self, x=0, y=0, color=None):
#         print("initializing a vector")
#         if type(x) is not int or type(y) is not int:
#             raise AttributeError('x and y should be int')
#
#         self._x = x
#         self._y = y
#         self._color = color
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#
# v = Vector()
# print(v.get_y())
# print(v.get_x())
# print(v)
#
#
# class VectorWithStr(Vector):
#     def __str__(self):
#         return f"vector {self._x}, {self._y} of color {self._color}"
#
#     def __add__(self, other):
#         return self.get_x() + other.get_x()
#
#     def __bool__(self):
#         return bool(self._x), bool(self._y)
#
#
#
# vector = VectorWithStr(0, 4, 'red')
# print(vector)
# print(vector.__add__(vector))
# print(vector.__bool__())


# class VectorWithRepr(Vector):
#     def __repr__(self):
#         return f'{self._x}, {self._y}, {self._color}'
#
#
# vec = VectorWithRepr()
# print(vec)
#
# class VectorWithBothReprAndStr(VectorWithRepr, VectorWithStr):
#     pass
# vector = VectorWithBothReprAndStr(1, 2, 'red')
# list_with_vector = [vector]
#
# print(vector)
# print(list_with_vector)
# print(type(list_with_vector[0]), list_with_vector[0]._x)


# class Text:
#     def __init__(self, text):
#         self.__text = text
#
#     def __add__(self, other):
#         return self.__text + other.__text
#
#
#
# t = Text('2')
# T = Text('3')
# print(t + T)

#a = [i**2 for i in range(1,5)]
# print(a)

# b = (i**2 for i in range(1,5))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))



# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print('это: ' + str(cls))
#         return super().__new__(cls)
#     def __init__(self, x, y):
#         print('вызов класса ' + str(self))
#         self._x = x
#         self._y = y
#
#
#
# p = Point(1, 2)



