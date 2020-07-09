# ООП - Объектно Ориентированное программирование
# ООП - это реальные объекты (в программировании), у которых есть характеристики, свойства и задачи
# +
# ООП - можно утсранять ошибки локально и не влиять на остальную часть программы
# ООП - повторное использованию
# Код получается более читаемый

#Создаем класс
# class Home:
#     #создаем атрибуты класса
#     home_count = 0
#
#     #создаем методы класса
#     def build(self, type_home, name, w, h, l):
#         self.type_home = type_home
#         self.name = name
#         self.w = w
#         self.h = h
#         self.l = l
#         print("Начинаем стройку объекта {}".format(name))
#         Home.home_count += 1
#
#
# corpus = Home()
# corpus1 = Home()
# corpus.build("жилой", "ОКО", 100, 100, 100)
# corpus1.build("промышленный", "ЖБИ", 1000, 1000,1000)
# print(corpus.type_home)
# print(corpus1.name)
# print(corpus.home_count)
#<----------------------------------------->
#Метод str
# class Home:
#
#     def __str__(self):
#         return "Home class Object"
#
#     def build(self):
#         print("начинаем стройку")
#
# corp = Home()
# print(corp)
#<----------------------------------------->
#Конструкторы - это специальный метод, который вызывается автоматически при создании объекта класса
# class Home:
#
#     home_count = 0
#
#     def __init__(self):
#         Home.home_count += 1
#         print(Home.home_count)
#
# corp1 = Home()
# corp2 = Home()
# corp3 = Home()
#<----------------------------------------->
# Модификаторы доступа
# public
# private
# protected
# class Home:
#     def __init__(self):
#         print("стройка начата")
#         self.name = "ОКО"
#         self.__type_home = "жилой"
#         self._year = 2020
#
# corp = Home()
# print(corp.type_home)
#<----------------------------------------->
# Домашнее задание:
# print(dir(Object of class))
# __str__
# __init__
# __repr__
# __dir__
# __sizeof__
# __format__
# Создать родительский класс машин
# задать ему характерные атрибуты
# Создать несколько дочерних классов, которые будут наследовать класс Машин, с уникальными атриутами
# испольлзовать методы __init__, __str__, __repr__ и уникальные матоды классов
# создать несколько объектов на основе дочерних классов
#<----------------------------------------->
# наследование
# class Building:
#     def building_method(self):
#         print("Это родительский метод из класса Building")
#
# class Citizen(Building):
#     def citizen_method(self):
#         print("Это дочерний метод из класса Citizen")
#
# class Indastrial(Building):
#     def indastrialMethod(self):
#         print("Это дочерний метод из класса Indastrial")
#
# corp1 = Citizen()
# corp1.building_method()
# corp2 = Indastrial()
# corp2.building_method()
# class Camera:
#     def camera_method(self):
#         print("Это родительский метод из класса Camera")
# class Radio:
#     def radio_method(self):
#         print("Это родительский метод из класса Radio")
# class Phone(Camera, Radio):
#     def phone_method(self):
#         print("Это родительский метод из класса Camera")
#
# iPhone = Phone()
# iPhone.radio_method()
# iPhone.camera_method()
#<----------------------------------------->
# Полиморфизм - способность объекта вести по разному
# Вреализуется через перегрузку метода, лиюо через его переопределение
# Перегрузка методов
# class Home:
#     def build(self, a, b=None):
#         if b is not None:
#             print(a + b)
#         else:
#             print(a)
#
# corp = Home()
# corp.build(10, 20)
# переопределение метода
# class Building:
#     def print_datails(self):
#         print("Это родительский метод из класса Building")
#
# class Citizen(Building):
#     def print_datails(self):
#         print("Это дочерний метод из класса Citizen")
#
# class Indastrial(Building):
#     def print_datails(self):
#         print("Это дочерний метод из класса Indastrial")
#
# corp1 = Building()
# corp1.print_datails()
# corp2 = Citizen()
# corp2.print_datails()
# corp3 = Indastrial()
# corp3.print_datails()
#<----------------------------------------->
# Инкапсуляция- скрытие данных
class Home:
    # создаем конструктор
    def __init__(self, type_home):
        self.type_home = type_home

    # создаем свойство
    @property
    def type_home(self):
        return self.__type_home

    #сеттер для создания свойств (установка свойств)
    @type_home.setter
    def type_home(self, type_home):
        if type_home < 2015:
            self.__type_home = 2015
        elif type_home > 2020:
            self.__type_home = 2020
        else:
            self.__type_home = type_home

    def getHomeType(self):
        return "год сдачи дома " + str(self.type_home)

home1 = Home(2088)
home2 = Home(1985)
home3 = Home(2017)
print(home1.getHomeType())
print(home2.getHomeType())
print(home3.getHomeType())