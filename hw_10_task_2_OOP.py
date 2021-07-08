class Animal:
    def __init__(self, name, age, owner):
        self.__name = name
        self.__age = age
        self.__owner = owner

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    def birthday(self):
        if self.__age > 5:
            print(self.__name + " sleeping all day.")
        else:
            print(self.__name + ' running and jumping 24/7')

    def owner_name(self):
        print(self.__owner, ' owner is ', self.__name)


animal = Animal('Ruby', 2, 'Sasha')

animal.age = 4
animal.owner = 'Stas'
animal.name = 'Barry'
print(animal.age)
print(animal.name)
print(animal.owner)
animal.owner_name()
animal.birthday()
animal.age = 6
animal.birthday()


class Table:

    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def area(self):
        return self.__width * self.__length

    def capacity(self):
        s = self.__width * self.__length
        if s <= 4:
            return 'Вместимость стола до 4 человек.'
        else:
            return 'Сядет более 4 человек'


table = Table(1, 1.5, 0.7)

print(table.width)
print(table.length)
print(table.height)

print(table.area())
print(table.capacity())

table.width = 2
table.length = 2.5
print(table.width)
print(table.length)
print(table.area())
print(table.capacity())


class Human:

    def __init__(self, name, age, profession, salary, time):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__salary = salary
        self.__time = time

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, new_profession):
        self.__profession = new_profession

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_time):
        self.__time = new_time

    def change_profession(self):
        if self.__salary <= 1500:
            return 'You need change profession'
        else:
            return 'You can do better!'

    def where_you(self):
        if 9 < self.__time < 21:
            return self.__name + ' working.'
        else:
            return self.__name + ' at home and relaxing.'


man = Human('John', 25, 'mechanic', 1400, 9.1)

print(man.name)
print(man.age)
print(man.profession)
print(man.salary)
print(man.time)
print(man.change_profession())
print(man.where_you())

man.salary = 1600
man.time = 22
print(man.change_profession())
print(man.where_you())


class Car:
    def __init__(self, mark, model, year, engine=None, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__engine = input('Start engine Yes/No?')

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    @property
    def engine(self):
        return self.__engine

    def up_speed(self):
        if self.__engine == 'Yes':
            self.__speed += 10
            print(str(self.__speed) + ' km/h')
        else:
            self.__engine = None

    def increase_speed(self):
        if self.__speed >= 10:
            self.__speed -= 10
            print(str(self.__speed) + ' km/h')
        else:
            self.__speed = 0
            print(str(self.__speed) + ' km/h')

    def stop_car(self):
        self.__speed = 0
        self.__engine = input('STOP engine Yes/No?')
        print(str(self.__speed) + ' km/h')

    def start_engine(self):
        self.__engine = input('Start engine Yes/No?')

    def check_speed(self):
        if self.__speed == 0:
            print(self.__speed, ' N')
        elif 0 < self.__speed <= 15:
            print(self.__speed, ' 1 step')
        elif 15 < self.__speed <= 30:
            print(self.__speed, ' 2 step')
        elif 30 < self.__speed <= 45:
            print(self.__speed, ' 3 step')
        elif 45 < self.__speed <= 70:
            print(self.__speed, ' 4 step')
        elif self.__speed > 70:
            print(self.__speed, ' 5 step')


auto = Car('BMW', 'e28', 1985)
auto.up_speed()
auto.up_speed()
auto.check_speed()
auto.up_speed()
auto.stop_car()
auto.up_speed()
auto.up_speed()
auto.start_engine()
auto.up_speed()
