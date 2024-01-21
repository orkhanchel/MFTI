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



