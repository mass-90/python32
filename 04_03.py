# # Наследование
# # class Employee:
# #     def __init__(self, name, salary, bonus):
# #         self.name = name
# #         self.salary = salary
# #         self.bonus = bonus
# #
# #     def calculate(self):
# #         return self.salary // 100 * self.bonus
# #
# #     def __str__(self):
# #         return f'{self.__class__.__name__} {self.name}, bonus {self.bonus}%, total bonus {self.calculate()}'
# #
# #
# # class Director(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 100000, 100)
# #
# #
# #
# # class Manager(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 50000, 50)
# #
# #
# #
# # class Cleaner(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 25000, 5)
# #         self.salary = 25000
# #         self.bonus = 5
# #
# #
# # people1 = Director('Ivan')
# # print(people1)
# # print(dir(people1))
# #
# # people2 = Manager('Grisha')
# # print(people2)
# #
# # people3 = Cleaner('Bob')
# # print(people3)
# #
# #
# # class Empty(object):
# #     pass
# #
# # obj = Empty()
# # print(dir(obj))
#
# # class Newlist(list):
# #     def __str__(self):
# #         return " ". join(map(str, self))
#
# # class Newlist(list):
# #     def __str__(self):
# #         return super().__str__().replace(',', '\n')
# #
# # list1 = Newlist([1, 2, 3, 4, 5])
# # list2 = [1, 2, 3, 4, 5]
# # list1.append(6)
# # print(list1)
# # print(list2)
# # print(dir(list1))
# # print(issubclass(Newlist, list))
#
# # class Animal:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def make_suond(self):
# #         print("Sound...")
# #
# #
# # class Cat(Animal):
# #     def meow(self):
# #         super().make_suond()
# #         super().make_suond()
# #
# # cat1 = Cat("Bob", 12)
# # cat1.meow()
#
# # class Figure:
# #
# #     def __init__(self, x, y):
# #         self._x = x
# #         self._y = y
# #
# # class Circle(Figure):
# #     def __init__(self, x, y, radius):
# #         super().__init__(x, y)
# #         self._radius = radius
# #
# # obj1 = Circle(0, 10, 50)
# # print(dir(obj1))
# #
# # # class Rect(Figure):
# # #     def __init__(self, x, y, fill):
# # #         super().__init__(x, y)
# # #         self.__fill = fill
#
# #
# # class Table:
# #     def __init__(self, l, h, w):
# #         self.len = l
# #         self.height = h
# #         self.width = w
# #
# #
# # # полное наследование
# #
# # class DeskTable(Table):
# #     def square(self):
# #         return self.width * self.height
# #
# #
# # t1 = Table(2, 2, 4)
# # t2 = DeskTable(4, 4, 6)
# # print(t2.square())
# #
# # # расширения (дополнение) в подклассе
# #
# #
# # class KitchenTable(Table):
# #     def __init__(self, l, h, w, places):
# #         super().__init__(l, h, w)
# #         self.places = places
# #
# #
# # kt1 = KitchenTable(2, 5, 6, 5)
# #
# # # переопределение п подклассе
# #
# #
# # class OfficeTable(DeskTable):
# #
# #     def square(self):
# #         return self.width * self.height - 100
# #
# #
# # of1 = OfficeTable(1, 1, 1)
# # print(of1.square())
#
# # расширить функционал класса tuple и сделать его неизменяемым
#
# # list1 = [1, 2, 3]
# #
# # print(dir(list1))
#
#
# # class ImmutableList(list):
# #
# #     def append(self, value):
# #         raise TypeError('Error')
# #
# #     def extend(self, value):
# #         raise TypeError('Error')
# #
# #     def insert(self, index, value):
# #         raise TypeError('Error')
# #
# #     def pop(self, index=-1):
# #         raise TypeError('Error')
# #
# #     def reverse(self):
# #         raise TypeError('Error')
# #
# #
# # list1 = ImmutableList([1, 2, 3, 4, 5, 6])
# # print(list1)
# # # list1.append(5)
#
# # class Employee:
# #     def __init__(self, name, number):
# #         self.name = name
# #         self.numer = number
# #
# #
# # class ProductionWorker(Employee):
# #     def __init__(self, name, number, num_of_shift, rate):
# #         super().__init__(name, number)
# #         self.num_of_shift = num_of_shift
# #         self.rate = rate
# #
# #     def get_shift(self):
# #         return self.num_of_shift
# #
# #     def change_shift(self, shift):
# #         self.num_of_shift = shift if shift in (1, 2) else 'Error'
# #
# #     def salary(self):
# #         match self.num_of_shift:
# #             case 1:
# #                 return self.rate * 8
# #             case 2:
# #                 return self.rate * 8 * 1.5
# #             case _:
# #                 return 'Неизвестная смена'
#
# # import random
# # print(dir(random))
#
# # class Employee:
# #     def __init__(self, name, salary, bonus):
# #         self.name = name
# #         self.salary = salary
# #         self.bonus = bonus
# #
# #     def __str__(self):
# #         return f"{self.__class__.__name__} {self.name}, bonus {self.bonus}%, " \
# #                f"salary = {self.salary}, total bonus {self.calculate_bonus()}"
# #
# #     def calculate_bonus(self):
# #         return self.salary // 100 * self.bonus
# #
# #
# # class Cleaner(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 25000, 5)
# #
# #
# # class Manager(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 50000, 25)
# #
# #
# # class Director(Employee):
# #     def __init__(self, name):
# #         super().__init__(name, 100000, 100)
# #
# #
# # person1 = Cleaner("Bob")
# # person2 = Manager("Jonh")
# # person3 = Director("Stive")
# #
# # class Goods:
# #     def __init__(self, title, price, count):
# #         super().__init__()
# #         print('init Goods')
# #         self.title = title
# #         self.price = price
# #         self.count = count
# #
# #     def __str__(self):
# #         return f'{self.title}, {self.price}, {self.count}'
# #
# #
# # class Mixin:
# #     count = 0
# #
# #     def __init__(self):
# #         print('init mixin')
# #         self.count += 1
# #         self.id = self.count
# #
# #     def display(self):
# #         print(f'{self.id} был продан')
# #
# #
# # class Phone(Goods, Mixin):
# #     pass
# #
# #
# # iphone = Phone('Iphone 15', 15000, 10)
# # print(Phone.__mro__)
# # iphone.display()
#
# # Полиморфизм - механизм, позволяющий выполнять один и тот же код по-разному
#
# # def add(a: int, b: int):
# #     return a + b
# #
# # print(add("sd", "sd"))
#
# # class Animal:
# #     def make_sound(self):
# #         print('shhh')
# #
# #
# # class Cat(Animal):
# #     def make_sound(self):
# #         print('meow')
# #
# #
# # class Dog(Animal):
# #     def make_sound(self):
# #         print('bark')
# #
# #
# # class Car(Animal):
# #     def make_sound(self):
# #         print('BIBI')
# #
# #
# # def sound(animal: Animal):
# #     animal.make_sound()
# #
# # sound(Car())
#
# # class Goods:
# #     def __init__(self, title, price, count):
# #         super().__init__()
# #         print("init Goods")
# #         self.title = title
# #         self.price = price
# #         self.count = count
# #
# #     def __str__(self):
# #         return f"{self.title}, {self.count}, {self.price}"
# #
# #
# # class Mixin:
# #     count = 0
# #
# #     def __init__(self):
# #         print('init Mixin')
# #         self.count += 1
# #         self.id = self.count
# #
# #     def display(self):
# #         print(f'{self.id} был продан')
# #
# # class Phone(Goods, Mixin):
# #     pass
# #
# #
# # iphone = Phone("Iphone 15", 15000, 10)
# # print(Phone.__mro__)
# # iphone.display()
#
#
# # Полиморфизм - механизм, позволяющий выполнять один и тот же код по-разному
# # Ducktyping (утиная типизация) - наличие поведение для использования в полиморфизме
# # В отличие от ЯП со строгой типизацией где важно кто ты (тип),
# # для полиморфизма в питоне важно что ты умеешь делать (поведение)
#
# # class Animal:
# #     def make_sound(self):
# #         print('shhh')
# #
# # class Cat(Animal):
# #     def make_sound(self):
# #         print('meow')
# #
# # class Dog(Animal):
# #     def make_sound(self):
# #         print('bark')
# #
# #
# # class Car:
# #     def make_sound(self):
# #         print('bi-bi')
# #
# #
# # def sound(animal: Animal):
# #     animal.make_sound()
# #
# #
# # sound(Car())
#
# # class SQLiteDatabase:
# #     def connect(self):
# #         print("Connecting to SQLiteDatabase")
# #
# #     def get_users(self):
# #         print("Get users from SQLiteDatabase")
# #
# #
# # class MongoDB:
# #     def connect(self):
# #         print("Connecting to MongoDB")
# #
# #     def get_users(self):
# #         print("Get users from MongoDB")
# #
# #
# # def get_db_from_config():
# #     print("read config")
# #     return SQLiteDatabase()
# #
# #
# # class Server:
# #     def get_users(self, db):
# #         db.connect()
# #         users = db.get_users()
# #         return users
# #
# # server = Server()
# # server.get_users(get_db_from_config())
#
#
# # print(len([1, 2, 3, 4]))
# # print(len("sdfsdfsd"))
# # print(len({"a": 1, "b": 2}))
#
# # у вас есть задача моделирования животных в зоопарке
# # зоопарк содержит различные типы животных, такие как млекопитающие, птицы рыбы и т.д
# # у каждого животного есть общие характеристики(например имя, возраст)
# # в также специфические свойства и действия в зависимости от их вида
#
#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # class Mammal(Animal):
# #     def __init__(self, name, age, sound):
# #         super().__init__(name, age)
# #         self.sound = sound
# #
# #     def make_sound(self):
# #         return self.sound
# #
# #
# # class Bird(Animal):
# #     def __init__(self, name, age, wingspan):
# #         super().__init__(name, age)
# #         self.wingspan = wingspan
# #
# #     def fly(self):
# #         return f"{self.name} is flying with a wingspan of {self.wingspan}."
# #
# #
# # class Fish(Animal):
# #     def __init__(self, name, age, color):
# #         super().__init__(name, age)
# #         self.color = color
# #
# #     def change_color(self, new_color):
# #         self.color = new_color
# #         return f"{self.name}'s color changed to {self.color}."
#
#
# # для военной игры стратегии нужно написать класс solider
# # класс имеет атрибут name, rank, service_number (имя, воинское звание, порядковый номер)
# # причем звание и номер - приватные свойства
# #
# # напишите методы для:
# # получения воинского звания
# # подтверждения порядкового номера
# # повышения в звании
# # понижения в звании
#
# class Soldier:
#
#     dict = {1: "a", 2: "b", 3: "c"}
#
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self._rank = rank if 1 <= rank <= 3 else 1
#         self._service_number = service_number
#
#     def rank_up(self):
#         self._rank += 1
#
#     def rank_down(self):
#         self._rank -= 1
#
#     def __str__(self):
#         return f"{self.dict[self._rank]}"
#
#     def validate_rank(self, rank):
#         return self._rank == rank
#
# soldier1 = Soldier("Bob", 10, 2)
# # soldier1.rank_up()
# print(soldier1.validate_rank(2))
# print(soldier1)
# import random
#
#
# class Vector:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'Vector({self.x}, {self.y}, {self.z})'
#
#     def __add__(self, vector):
#         return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)
#
#     def __sub__(self, vector):
#         return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)
#
#     def __mul__(self, vector):
#         if isinstance(vector, Vector):
#             return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z)
#         elif isinstance(vector, int):
#             return (self.x * vector) + (self.y * vector) + (self.z * vector)
#
#     def __matmul__(self, vector):
#         return Vector((self.y * vector.z)
#
#         )
#
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
#
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * v2)


# class Objects:
#     def __init__(self, *args):
#         self.info = []
#         self.info.extend(args)
#
#     def __getitem__(self, index):
#         return self.info[index]
#
#
# class Student:
#
#     def __init__(self):
#         self.knowledge = []
#
#     def learn(self, subject):
#         self.knowledge.append(subject)
#
#
# class Teacher:
#
#     def teach(self, subject, students: [Student]):
#         for student in students:
#             student.learn(subject)
#
#
# class Student:
#
#     def __init__(self):
#         self.knowledge = []
#
#     def learn(self, subject):
#         self.knowledge.append(subject)
#
#
# obj = Objects('math', 'geom', 'physics', 'prog', 'literature')
#
#
# stud1 = Student()
# stud2 = Student()
# stud3 = Student()
# stud4 = Student()
#
# teacher = Teacher()
#
# teacher.teach(obj[2], [stud1, stud2])
#
# print(stud1.knowledge)
# print(stud2.knowledge)
#
# teacher.teach(obj[3], [stud1])
# teacher.teach(obj[1], [stud2])
#
# print(stud1.knowledge)
# print(stud2.knowledge)

# Игра-стратегиия «Солдаты и герои»

# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
# уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
# солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
# "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В
# цикле генерируются объекты-солдаты. Их принадлежность команде определяется
# случайно.
# Солдаты разных команд добавляются в разные списки. Измеряется длина списков
# солдат противоборствующих команд и выводится на экран. У героя, принадлежащего
# команде с более длинным списком, увеличивается уровень.
# Отправляем одного из солдат следовать за первым героем и выводим их
# идентификационные номера.

# class Person:
#     count = 0
#
#     def __init__(self, team):
#         self.id = Person.count
#         Person.count += 1
#         self.team = team
#
#
# class Hero(Person):
#
#     def __init__(self, team):
#         super().__init__(team)
#         self.level = 1
#
#     def up_level(self):
#         self.level += 1
#
#
# class Soldier(Person):
#
#     def __init__(self, team):
#         super().__init__(team)
#         self.my_hero = None
#
#     def follow(self, hero: Hero):
#         print(f'Follow to {hero.id}')
#
#     def __repr__(self):
#         return f'{self.team}'
#
#
# army1 = []
# army2 = []
#
# hero1 = Hero(1)
# hero2 = Hero(2)
#
# for i in range(50):
#     team = random.randint(1, 2)
#     if team == 1:
#         army1.append(Soldier(team))
#     else:
#         army2.append(Soldier(team))
#
# print(army1, army2)
# print(len(army1), len(army2))
#
# hero1.up_level() if len(army1) > len(army2) else hero2.up_level()
#
# print(hero1.level, hero2.level)
#
# army1[5].follow(hero2)

# класс содержит имя студента full_name, номер группы group_number и список полученных оценок progress.
# в программе вводится список студентов.
# далее список сортируется по имени, потом выводятся студенты, имеющие неудовлетворительные оценки


# class Student:
#     def __init__(self, full_name, group_number, progress):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#
#
# students = [
#     Student("Иванов Иван", "Группа 1", [4, 5, 3]),
#     Student("Петров Петр", "Группа 2", [2, 3, 4]),
#     Student("Сидоров Сидор", "Группа 3", [3, 3, 2]),
#     Student("Ллоид Дэби", "Группа 5", [1, 5, 5])
# ]
#
#
# sorted_students = sorted(students, key=lambda x: x.full_name)
#
#
# for student in sorted_students:
#     if min(student.progress) < 3:
#         print(f"{student.full_name}, {student.group_number}, {student.progress}")
