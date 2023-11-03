# 1) Первый пример
# class Book:
#
#     def __init__(self, name, author, isbn):
#         self.__name = name
#         self.__author = author
#         self.__isbn = isbn
#
#     def get_author(self):
#         return self.__author
#
#     def set_author(self, author):
#         self.__author = author
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_isbn(self):
#         return self.__isbn
#
#     def set_isbn(self, isbn):
#         self.__isbn = isbn
#
#
# b = Book("name", "Tachila", 12345343525325235)
# print(b.get_author())
#
# b.set_author("LegendaAlabygu")
# print(b.get_author())
#
# b.set_name("ProdamKod100R")
# print(b.get_name())
#
# b.set_isbn("K4ay")
# print(b.get_isbn())
################################################################################################
# 2) Второй пример
# class Figure:
#
#     def __init__(self, coards, width, color):
#         self.coards = coards
#         self.width = width
#         self.color = color
#
#     def draw(self):
#         print(f"Рисуем Фигуру Цветом {self.color} и Шириной {self.width}!")
#
# class Line(Figure):
#
#     def draw(self):
#         print(f"Рисуем Линию Цветом {self.color} и Шириной {self.width}!")
#
#     def del_line(self):
#         print("Линия Удалена!")
#
#
# class Rect(Figure):
#
#     def __init__(self, coards, width, color, right):
#         super().__init__(coards, width, color)
#         self.right = right
#
#     def draw(self):
#         print(f"Рисуем Прямоугольник Цветом {self.color} и Шириной {self.width}! Прямоугльник{self.right}!")
#
# class Ellips(Figure):
#
#     def draw(self):
#         print(f"Рисуем Элипс Цветом {self.color} и Шириной {self.width}. ")
#
# f = Figure([1,2,3,4,5,6,7,8,9], 2, "black")
# f.draw()
# l = Line([1,1,5,6], 3, "red")
# l.draw()
# l.del_line()
# e = Ellips([5,5,2,9], 4, "white")
# e.draw()
# r = Rect([1,8,6,2], 6, "blue", "Кривой")
# r.draw()
################################################################################################
# 3) Третий пример
# class Publication:
#
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display(self):
#         print(f"Название: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Год издания: {self.year}")
#
# class Book(Publication):
#
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f"ISBM {self.isbn}")
#
# class Magazine(Publication):
#
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title, author, year)
#         self.issue_number = issue_number
#
#     def display(self):
#         super().display()
#         print(f"Номер Журнала {self.issue_number}")
#
# def info(obj):
#     obj.display()
#
#
# p = Publication("Название 1 ", "Автор 1", 2121)
# # p.display()
# # print()
# b = Book("Название 2 ", "Автор 2", 21, 1234567890)
# # b.display()
# # print()
# m = Magazine("Название 3", "Автор 3", 212121, 5)
# # info(m)
# list = []
# list.append(p)
# list.append(b)
# list.append(m)
# for i in list:
#     info(i)
#     print()
#
# # c = "0.2558"
# # c = int(c)
# # c = str(c)
###############################################################################################
# 1) Первая задача
# import random
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f""""
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.release_year}
# Жанр: {self.genre}
# Список треков: {self.tracklist}
# """)
#
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# album4.get_info()
# print(album4.play_random_track())
###############################################################################################
# 2) Вторая задача
# class Student:
#
#     def  __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print(f'Имя: {self.name}')
#         print(f'Возраст: {self.age}')
#         print(f'Класс: {self.grade}')
#         print(f'Оценки: {self.scores}')
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# Student2I = Student('Данильченко Депрем 100%', '18', '3 курс', [5, 4, 4, 5])
# Student2I.info()
# print("Средний Балл: ", Student2I.average_score())
###############################################################################################
# 3) Третья задача
# class Recipe:
#
#     def __init__(self, ing, dish):
#         self.ing = ing
#         self.dish = dish
#
#     def print_ingredients(self):
#         print(f'Ингредиенты для {self.dish}:')
#         for item in self.ing:
#             print(f'- {item}')
#
#     def cook(self):
#         print(f'''
# Сегодня мы готовим {self.dish}
# Выполняем инструкцию по приготовлению блюда {self.dish}
# Блюдо {self.dish} готово!
# ''')
#
# spaggeti = Recipe(['Спагетти', 'Фарш', 'Томатный соус', 'Лук', 'Чеснок', 'Соль'], 'Спагетти болоньезе')
# spaggeti.print_ingredients()
# spaggeti.cook()
#
# print("<===========================================================>")
# print("")
# keks = Recipe(['Мука', 'Яйца', 'Молоко', 'Сахар', 'Сливочное масло', 'Соль'], 'Кекс')
# keks.print_ingredients()
# keks.cook()
###############################################################################################
# 4) Четвертая задача
