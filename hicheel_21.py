####################### class and object ####################
# class player :
#     def __init__(self, name, skins):
#         self.name = name
#         self.skins = skins
# player1 = player("Tsedo", 1)
# player2 = player("Fenrir", 1)
# print(player1.name)
# print(player1.skins)
# print(player2.name)
# print(player2.skins)

# task 2
# class student :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# name1 = input()
# age1 = int(input())
# student1 = student(name1, age1)

# name2 = input()
# age2 = int(input())
# student2 = student(name2, age2)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)

# task 3
# class student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
# name1 = input()
# age1 = int(input())
# grade1 = input()
# student1 = student(name1, age1, grade1)
# print("Ner:",student1.name)
# print("Nas:",student1.age)
# print("Angi:",student1.grade)  

# task4
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# name1 = input()
# score1 = int(input())
# student1 = student(name1, score1)
# name2 = input()
# score2 = int(input())
# student2 = student(name2, score2)
# print("name: ",student1.name)
# print("Onoo:",student1.score)
# print("name:",student2.name)
# print("Onoo: ",student2.score)

# task 5
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = student("Bat", 80)
# student1.add_score()
# print(student1.score)

# task 6
# class student:
#     def __init__(self, name , age, grade):
#         self.name = name
#         self.age = age
#         self.garde = grade
#     def show_info(self):
#         print(f"Nas: {self.name}")
#         print(f"Nas: {self.age}")
#         print(f"class: {self.garde}")
# student1 = student("Saraa", 19, "12B")
# student1.show_info()        
        
# task 7
# class student:
#     def __init__(self, name , score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60:
#             print(f"{self.name}: Tentssen")
#         else:
#             print(f"{self.name}: Tentseegui")
# student1 = student("Bat", 75)
# student2 = student("Naraa", 45)
# student1.check_result()
# student2.check_result()


# task 8
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = student("Bat" ,80)
# student1.add_score()
# print(student1.score) 
        
# task 9
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# student1 = student("Saraa", 18)
# student1.birthday()
# student1.birthday()
# print(student1.age)

# task 10
# class student:
#     def __init__(self, name , score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 90:
#             print("A")
#         elif self.score >= 80:
#             print("B")
#         elif self.score >= 70:
#             print("c")
#         elif self.score >= 60:
#             print("D")
#         else:
#             print("F")
# name1 = input()
# score1 = int(input())
# student1 = student(name1, score1)
# student1.get_grade()
        
# task 11
# class student:
#     def __init__(self, name):
#         self.name = name
#         self.irts = 0
#     def attend(self):
#         self.irts += 1
#     def show_attendance(self):
#         print(f"{self.name}-iin irtsiin too: {self.irts}")
# student1 = student("Bat")
# student1.attend()
# student1.attend()
# student1.show_attendance()

# task 12
# class student:
#     def __init__(self, name, score, irts):
#         self.name = name
#         self.score = score
#         self.irst = irts
#     def check_result(self):
#         if self.score >= 60 and self.irst >= 80:
#             print("Tentssen")
#         else:
#             print("Tentseegui")
# student1 = student("Bat", 60, 90)
# student1.check_result()

# task 13
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def show_scores(self):
#         print(f"{self.name}-iin buh onoo: {self.score}")
#     def add_score(self, score):
#         self.score.append(score)
#     def avarage(self):
#         if not self.score:
#             avg = 0
#         else:
#             avg = sum(self.score) / len(self.score)
#         print(f"{self.name}-iin onooni dundaj: {avg}")
# student1 = student("Bat", [80,90,70])
# student1.show_scores()
# student1.add_score(100)
# student1.show_scores()
# student1.avarage()
        
# task 14
# class studnet:
#     def __init__(self, name, age, angi):
#         self.name = name
#         self.age = age
#         self.angi = angi
#     def show_info(self):
#         print(f"ner:{self.name} nas:{self.age} angi:{self.angi}")
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_grade(self, new_angi):
#         self.angi = new_angi
# studnet1 = studnet("Bat", "10", "5B")
# studnet1.show_info()
# studnet1.change_name("Bold")
# studnet1.change_grade("5c")
# studnet1.show_info()        
        
# task 15
# class students:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.score = []
#     def show_info(self):
#         print(f"ner:{self.name}, nas:{self.age}, onoo:{self.score}")
#     def add_score(self, score):
#         self.score.append(score)
#     def avarage(self, ):
#         if not self.score:
#             return 0
#         return sum(self.score) / len(self.score)
#     def check_result(self):
#         avg_score = self.avarage()
#         if avg_score >= 60:
#             print(f"{self.name} shalgaltad tentssen: {avg_score}")
#         else:
#              print(f"{self.name} shalgaltad tentseegui: {avg_score}")
       
# students1 = students("Bat", "12A")
# students1.add_score(80)
# students1.add_score(90)
# students2 = students("Bold", "12B")
# students2.add_score(50)
# students2.add_score(55)
# students1.show_info()
# students2.show_info()
# students1.check_result()
# students2.check_result()

# task1
# class phone():
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery
#     def use_phone(self):
#         self.battery -= 10
#     def charge(self):
#         self.battery += 20
#     def show_battery(self):
#         print(f"odoogiin tsenge: {self.battery}")
# phone1 = phone("Iphone", 80)
# phone1.use_phone()
# phone1.show_battery()
# phone1.charge()
# phone1.show_battery()
        
# task 2
# class product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def sell(self, amount: int):
#         if amount > self.quantity:
#             print("Baraa hureltsehgui")
#         else:
#             self.quantity-= amount
#     def show_total(self):
#         total = self.quantity * self.price
#         print(f"Uldegdel: {self.quantity}")
#         print(f"Niit une: {total}")
# prodecut1 = product("Mouse", 30000, 10)
# prodecut1.sell(3)
# prodecut1.show_total()

# task 3
# class Athlete():
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points
#     def add_point(self, points: int):
#         self.points += points
#     def lose_point(self, points: int):
#         self.points -= points
#     def show_points(self):
#         print(f"Onoo: {self.points}")
# Athlete1 = Athlete("Bat", 20)
# Athlete1.add_point(15)
# Athlete1.lose_point(5)
# Athlete1.show_points()

# task 4
# class Movie():
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views
#     def add_view(self):
#         self.views +=1
#     def uptoide_rating(self, new_rating: float):
#         self.rating = new_rating
#     def show_info(self):
#         print(f"Kinoni ner: {self.title} Unlegee: {self.rating} vzsen hunii too: {self.views}")
# Movie1 = Movie("demon slayer", 7.8, 1500)
# Movie2 = Movie("Solo leveling", 8.6, 2200)

# Movie1.add_view()
# Movie2.add_view()

# Movie1.uptoide_rating(9.0)
# Movie2.uptoide_rating(9.0)

# Movie1.show_info()
# Movie2.show_info()
        
# task 5
# class GameCharacter():
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#     def attack(self, enemy):
#         enemy.health -= self.damage
#     def show_healt(self):
#         print(f"{self.name}-iin ami: {self.health}")
# player1 = GameCharacter("Knight", 100, 20)
# player2 = GameCharacter("Goblin", 60, 10)
# player1.attack(player2)
# player2.show_healt()        

# task 6
# class Wallet():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def add_money(self ,amount: int):
#         self.balance += amount
#     def pay(self, amount: int):
#         if amount > self.balance:
#             print("Mongo Hureltsehgui")
#         else:
#             self.balance -= amount
#     def show_balance(self):
#         print(f"uldegdel: {self.balance}")
# wallet1 = Wallet("Bat", 5000)
# wallet1.add_money(3000)
# wallet1.pay(10000)
# wallet1.pay(4000)
# wallet1.show_balance()       
        
# task 7
# class libraryBook:
#     def __init__(self, title, available):
#         self.title = title
#         self.available = available
#     def borrow(self):
#         if self.available:
#             self.available = False
#             print("Nomiig zeellee")
#         else:
#             print("Nom ali hediin zeelegdsen bain")
#     def return_book(self):
#         self.available = True
#         print("Nomiig butsaalaa")
# book1 = libraryBook("Python", True)
# book1.borrow()
# book1.borrow()
# book1.return_book()

# task 8
# class Exam:
#     def __init__(self, student_name, score, max_score):
#         self.student_name = student_name
#         self.score = score
#         self.max_score = max_score
#     def get_percentage(self):
#         if self.max_score == 0:
#             return 0.0
#         return(self.score / self.max_score) * 100
#     def check_result(self):
#         percentage = self.get_percentage()
#         if percentage >= 90:
#             result =  "mash sain"
#         elif percentage >= 80:
#             result =  "Sain"
#         elif percentage >= 60:
#             result = "Tentssen"
#         else:
#             result = "Tentseegui"
#         print(f"Suragch: {self.student_name}")
#         print(f"huwi: {percentage}")
#         print(f"Ur dun: {result}")
# student1 = Exam("Bat", 92, 100)
# student1.check_result
# print("-" * 30)
# student2 = Exam("Suvd", 45, 80)
# student2.check_result()
                    
# task 9
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# student1 = student("Saraa", 18)
# student1.birthday()
# student1.birthday()
# print(student1.age)
        
# task 10
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 90:
#             print("A")
#         elif self.score >= 80:
#             print("B")
#         elif self.score >= 70:
#             print("C")
#         elif self.score >= 60:
#             print("D")
#         else:
#             print("F")
# student1=  student("Saraa", 80)
# student1.get_grade()
        
# task 11
# class student:
#     def __init__(self, name):
#         self.name = name
#         self.garde = 0
#     def attend(self):
#         self.garde += 1
#     def show_attendance(self):
#         print(f"{self.name}-iin irts: {self.attend}")
# student1 = student("Bold")
# student1.attend()
# student1.attend()
# student1.show_attendance()
        
# task 12
# class student:
#     def __init__(self, name, score, irts):
#         self.name = name
#         self.score = score
#         self.irst = irts
#     def check_result(self):
#         if self.score >= 60 and self.irst >= 80:
#             print("Tentssen")
#         else:
#             print("Tentseegui")
# student1 = student("Bat", 60, 90)
# student1.check_result()

# task 13
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def show_scores(self):
#         print(f"{self.name}-iin buh onoo: {self.score}")
#     def add_score(self, score):
#         self.score.append(score)
#     def avarage(self):
#         if not self.score:
#             avg = 0
#         else:
#             avg = sum(self.score) / len(self.score)
#         print(f"{self.name}-iin onooni dundaj: {avg}")
# student1 = student("Bat", [80,90,70])
# student1.show_scores()
# student1.add_score(100)
# student1.show_scores()
# student1.avarage()
        
# task 14
# class studnet:
#     def __init__(self, name, age, angi):
#         self.name = name
#         self.age = age
#         self.angi = angi
#     def show_info(self):
#         print(f"ner:{self.name} nas:{self.age} angi:{self.angi}")
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_grade(self, new_angi):
#         self.angi = new_angi
# studnet1 = studnet("Bat", "10", "5B")
# studnet1.show_info()
# studnet1.change_name("Bold")
# studnet1.change_grade("5c")
# studnet1.show_info()        
        
# task 15
# class students:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.score = []
#     def show_info(self):
#         print(f"ner:{self.name}, nas:{self.age}, onoo:{self.score}")
#     def add_score(self, score):
#         self.score.append(score)
#     def avarage(self, ):
#         if not self.score:
#             return 0
#         return sum(self.score) / len(self.score)
#     def check_result(self):
#         avg_score = self.avarage()
#         if avg_score >= 60:
#             print(f"{self.name} shalgaltad tentssen: {avg_score}")
#         else:
#              print(f"{self.name} shalgaltad tentseegui: {avg_score}")
# students1 = students("Bat", "12A")
# students1.add_score(80)
# students1.add_score(90)
# students2 = students("Bold", "12B")
# students2.add_score(50)
# students2.add_score(55)
# students1.show_info()
# students2.show_info()
# students1.check_result()
# students2.check_result()