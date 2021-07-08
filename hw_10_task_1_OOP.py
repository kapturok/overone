class Dog:
    def bark(self):
        print('Woof')

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def __init__(self, height, weight, name, age, owner):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__owner = owner

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner


dog = Dog(30, 15, 'Jora', 3, 'Jhon')

dog.name = 'Luck'
dog.height = 35
dog.weight = 21
dog.age = 7
dog.owner = 'Sasha'

print(dog.name)
print(dog.height)
print(dog.weight)
print(dog.age)
print(dog.owner)


class Pet:
    _counter = 0

    def __init__(self, name, age, owner, weight=5, height=2):
        self._name = name
        self._age = age
        self._owner = owner
        self.weight = weight
        self.height = height
        Pet._counter += 1

    def get_counter(self):
        return self._counter

    def voice(self):
        print('Voice')

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

    def run(self):
        print('Runing')

    def jump(self):
        print('Jumping')

    def birthday(self):
        self._age += 1
        return self._age

    def __str__(self):
        return f'Name:{self._name}, age:{self._age}, owner: {self._owner}'


class Dogg(Pet):

    def voice(self):
        print('Gaff')

    def jump(self, h):
        if h <= 0.5:
            print('Dog jump')
        else:
            print('Dog cant jump')


class Cat(Pet):
    def voice(self):
        print('Miyy')

    def jump(self, h):
        if h <= 2:
            print('Cat jump')
        else:
            print('Cat cant jump')


class Parret(Pet):
    def voice(self):
        print('Kurlik')

    def jump(self, h):
        if h <= 0.05:
            print('Parret jump')
        else:
            print('Parret cant jump')

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05

    def fly(self):
        if self.weight > 0.2:
            print('Cant fly')
        else:
            print('Fly')


parret_1 = Parret('Lol', 2, 'Pop')
cat_1 = Cat('Bursik', 2, 4)

dog_2 = Dogg('Fufel', 1, 'Tor')

parret_1.change_weight()
print(parret_1.birthday())
print(parret_1._owner)
print(parret_1.weight)
print(parret_1.weight)
print(parret_1.height)
parret_1.jumping = 0.02

parret_1.jump(1)
dog_2.jump(0.2)
cat_1.jump(2.1)
dog_2.voice()
cat_1.voice()
parret_1.voice()
animals = [cat_1, dog_2, parret_1]

print(dog_2.get_counter())

for animal in animals:
    animal.voice()

print(parret_1)
print(dog_2)
print(dog_2.get_counter())


class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0, str_time='', other_time=None):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__other_time = other_time

        if str(str_time):
            lst_time = str_time.split(':')
            self.__hours = int(lst_time[0])
            self.__minutes = int(lst_time[1])
            self.__seconds = int(lst_time[2])

    def hours(self):
        return self.__hours

    def minutes(self):
        return self.__minutes

    def secunds(self):
        return self.__seconds

    def other_time(self):
        return self.__other_time

    def __add__(self, other):
        return MyTime(self.__hours + other.__hours,
                      self.__minutes + other.__minutes,
                      self.__seconds + other.__seconds)

    def __sub__(self, other):
        return MyTime(self.__hours - other.__hours,
                      self.__minutes - other.__minutes,
                      self.__seconds - other.__seconds)

    def __eq__(self, other):
        if self.__hours == other.__hours and self.__minutes == other.__minutes and self.__seconds == other.__seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__hours != other.__hours and self.__minutes != other.__minutes and self.__seconds != other.__seconds:
            return True
        else:
            return False

    def __str__(self):
        if self.__hours > 23 or self.__minutes > 59 or self.__seconds > 59:
            while self.__hours > 23 or self.__minutes > 59 or self.__seconds > 59:
                self.__minutes += self.__seconds // 60
                self.__hours += self.__minutes // 60
                self.__minutes = self.__minutes % 60
                self.__seconds = self.__seconds % 60
                self.__hours = self.__hours % 23
                if len(str(self.__hours)) < 2:
                    self.__hours = '0' + str(self.__hours)
                return f'Hours: {self.__hours}, Minutes: {self.__minutes}, Seconds: {self.__seconds}'
        else:
            return f'Hours: {self.__hours}, Minutes: {self.__minutes}, Seconds: {self.__seconds}'


mytime1 = MyTime(12, 35, 17)
mytime2 = MyTime(str_time='12:15:10')
mytime3 = MyTime(other_time=mytime1)
print(mytime3.hours())

print(mytime2.__str__())

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, point1, r):
        self._r = r
        self._point = point1

    def area(self):
        return math.pi * (self._r ** 2)

    def perimeter(self):
        return 2 * math.pi * self._r


class Triangle:

    def __init__(self, a, b, c):
        def side(dot1, dot2):
            return math.sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)

        self._a = a
        self._b = b
        self._c = c
        self._AB = side(self._a, self._b)
        self._BC = side(self._b, self._c)
        self._CA = side(self._c, self._a)

    def area(self):
        polu_perimeter = self.perimeter() / 2
        return math.sqrt(polu_perimeter
                         * (polu_perimeter - self._AB)
                         * (polu_perimeter - self._BC)
                         * (polu_perimeter - self._CA))

    def perimeter(self):
        return self._AB + self._BC + self._CA


class Square:

    def __init__(self, a, b):
        def side(dot1, dot2):
            return math.sqrt((dot1.x - dot2.x) ** 2
                             + (dot1.y - dot2.y) ** 2) / math.sqrt(2)

        self._a = a
        self._b = b
        self._AB = side(self._a, self._b)

    def perimeter(self):
        return self._AB * 4

    def area(self):
        return self._AB ** 2


point1 = Point(5, 5)
point2 = Point(2, 4)
point3 = Point(3, 6)

circle_1 = Circle(point1, 5)
print(circle_1.area())

triangle_1 = Triangle(point1, point2, point3)
print(triangle_1.area())

square_1 = Square(point1, point2)
print(square_1.area())

figures = [circle_1, triangle_1, square_1]
total_area = 0

for figure in figures:
    total_area += figure.area()
print(total_area)
