############################################ massiv (set) #############################
# a = {"bat", "bold","saraa" }
# b = {"bat", "naraa","saraa"}
# print(a & b)  ijil utga
#  print(a|b)  dawhardalgui buh utga
# print(a - b)  a baigaa b bhku utga

# a = {"name":"Temuulen",
#     "age": 24,
#     "phone": 938939}
# a.update({"huis":"er",  # olon utga nemeh
#           "hemjee": 15,
#           "phone": 237273128,
#           })
# for key,value in a.items:
#     print(key,value)

#task1
# nums = [1,2,2,3,4,4,5]
# a = set(nums)
# print(a)

# task 2
# fruits = {"apple","banana"}
# fruits.add  ("orange")
# print(fruits)

# task 3
# fruits = {"apple","banana","orange"}
# fruits.remove("banana")
# print(fruits)

# task 4
# nums = {10,20,30,40}
# b = 20
# if b in nums:
#     print("yes")
# else:
#     print("no")

# task 5
# n = map(int, input().split())
# b = set(n)
# print(len(b))

# task 6
# names = ["bat", "Sara","bat", "bold","Sara","Anu"]
# b = set(names)
# print(len(b))

# task 7
# a = {1,2,3}
# b = {3,4,5}
# print(a|b)

# task 8
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a&b)

# task 9
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a -b)

# task 10
# python_student = {"bat","sara", "bold", "anu"}
# java_student = {"sara", "bold","temuulen"}
# print(python_student & java_student)

# # task 11
# python_student = {"bat","sara", "bold", "anu"}
# java_student = {"sara", "bold","temuulen"}
# print(python_student - java_student | java_student -python_student)

# task 12
# n = input()
# b = set(n)
# print(len(b))

# task 13
# student = {"name":"Bat",
#      "age":18,
#      "score":95}
# print(student)

# task 14
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# for value in student.values():
#     print(value)

# task 15
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student.update({"score": 98})
# print(student)

# task 16
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student.update({"city":"Ulaabaatar"})
# print(student)

# task 17
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)

# task 18
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# for key in car.keys():
#     print(key)

# task 19
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# for value in car.values():
#     print(value)

# task 20
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# for key,value in student.items():
#     print(key,value)

# task 21
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# if "score" in student :
#     print("yes")
# else:
#     print("no")

# task 22
# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product["stock"] > 0:
#     print("Available")
# else:
#     print("Out of stock")

# task 23
# scores = {
#     "Bau": 88t": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "An
# }
# for name, score in scores.items():
#     if score > 80:
#         print(name) 

# task 24
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# best = max(scores, key = scores.get)
# score = scores[best]
# print(f"{best} {score}")

# task 25
# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# a = sum(sales.values())
# print(a)

# task 26
# n  = input()
# count = {}
# for word in n.split():
#     count[word] =count.get(word, 0)+1
# for word, n in count.items():
#         print(word, n)

# task 27
# students = {
#     "Bat": ["Python", "Java"],
#     "Sara": ["Python", "C++"],
#     "Bold": ["Java", "Python"]
# }
# a = set()
# for subject in students.values():
#     a.update(subject)
# for subject in a:
#     print(subject)

# task 28
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# a = set(students.values())
# print(len(a))

# task 29
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet"
# }
# for name,city in students.items():
#     if city == "Ulaanbaatar":
#         print(name)

# task 30
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }
# a = set(data.values())
# print(a)

# task 1
# user1= {"Bat", "Sara", "Bold", "Anu"}
# user2 = {"Bold", "Anu", "Temuulen", "Naraa"}
# print(user1&user2)

# task 2
# players = {"Bat", "Sara", "Bold", "Anu", "Naraa", "Temuulen"}
# pleyed = {"Bat", "Bold", "Naraa"}
# print(players - pleyed)

# task 3
# team_a = {"Bat", "Bold", "Anu", "Sara"}
# team_b = {"Anu", "Sara", "Naraa", "Temuulen"}
# print(team_a - team_b | team_b - team_a)

# task 4
# known = {"Python", "HTML", "CSS"}
# required = {"Python", "JavaScript", "SQL"}
# print(required - known)

# task 5
# subjects = [
#     "Python",
#     "Math",
#     "Python",
#     "English",
#     "Math",
#     "Physics"
# ]
# a = set(subjects)
# print (a)
# print(len(a))


# task 6
# password = input("Input: ")
# letters = 0
# digits = 0
# for c in password:
#     if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
#         letters += 1
#     elif '0' <= c <= '9':
#         digits += 1
# print("Letters:", letters)
# print("Digits:", digits)

# task 7
# n = input()
# a = input()
# print(len(a) |len(n))

# task 8
# students = {
#     "Bat": 75,
#     "Sara": 92,
#     "Bold": 61,
#     "Anu": 88,
#     "Naraa": 54
# }
# for name, score in students.items():
#     if score > 90:
#         print(name, "-","Excellent")
#     elif 60 < score > 89:
#         print(name,"-", "Pass")
#     else:
#         print(name,"-", "Fail")

# task 9
# products = {
#     "apple": 3000,
#     "banana": 2500,
#     "milk": 4500,
#     "bread": 3500
# }
# n = input("name:")
# a = int(input("shirheg"))
# total = products[n] * a
# print("Total:" ,total)

# task 10
# sales = {
#     "keyboard": 15,
#     "mouse": 23,
#     "monitor": 8,
#     "headset": 17
# }
# best = max(sales, key = sales.get)
# score = sales[best]
# print(f"{best} {score}")

# task 11
# employees = {
#     "Bat": 1500000,
#     "Sara": 1800000,
#     "Bold": 1300000,
#     "Anu": 2100000
# }
# for name, salary in employees.items():
#     if salary < 1500000:
#         employees[name] = int(salary * 1.1)
# print(employees)

# task 12
# people = {
#     "Bat": 17,
#     "Sara": 21,
#     "Bold": 19,
#     "Anu": 16,
#     "Naraa": 25
# }
# for name , age in people.items():
#     if age >= 18:
#         print(name)

# task 13
# scores = {
#     "Bat": 70,
#     "Sara": 85,
#     "Bold": 60,
#     "Anu": 95
# }
# for name , sco in scores.items():
#     if sco <100 :
#         sco +=5
#         print(name,sco)

# task 14
# products = {
#     "keyboard": 120000,
#     "mouse": 50000,
#     "monitor": 450000,
#     "headset": 80000
# }
# n = int(input())
# for name , une in products.items():
#     if une> 100000:
#         print(name)
        
# task 15
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Naraa": "Darkhan",
#     "Temuulen": "Ulaanbaatar"
# }
# n = input()
# se = set()
# for name , city in students.items():
#     if city == n:
#         se.add(name)
# print(se)

# task 16
#games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# players = set()
# for name , game in games.items():
#     if "CS2" in game:
#         players.add(name)
# print(players)

# task 17
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# game = set()
# for players in games.values():
#     game.update(players)
# print(game)

# task 18
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# players = []
# for name in games:
#     player_game = games[name]
#     if "CS2," and "WoW" in player_game:
#         players.append(name)
# print(players)

# task 19
# skills = {
#     "Bat": {"Python", "HTML", "CSS"},
#     "Sara": {"Python", "JavaScript"},
#     "Bold": {"HTML", "CSS", "JavaScript"},
#     "Anu": {"Python", "SQL", "JavaScript"}
# }
# student_skill = []
# for name ,student in skills.items():
#     if "Python" in student and "JavaScript" in student:
#         student_skill.append(name)
# print(student_skill)

# task 20
# employees = {
#     "Bat": {"English", "Mongolian"},
#     "Sara": {"English", "Korean"},
#     "Bold": {"Mongolian", "Japanese"},
#     "Anu": {"English", "Japanese"}
# }
# empo = []
# for name , hell in employees.items():
#     if "English" in hell and "Korean" not in hell:
#         empo.append(name)
# print(empo)

#task 21
# web_users = {"Bat", "Sara", "Bold", "Anu"}
# mobile_users = {"Sara", "Anu", "Naraa"}
# print (len(web_users&mobile_users))

# task 22
# status = {
#     "Bat": "online",
#     "Sara": "offline",
#     "Bold": "online",
#     "Anu": "offline",
#     "Naraa": "online"
# }
# online = set()
# for name  in status:
#     if status[name] == "online":
#         online.add(name)
# print(online)
# n = input()
# if n in online:
#     print("online")
# else:
#     print("offline")

# task 23
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }
# n = input()
# for course , students in courses.items():
#     if n in students:
#         print(course)

# task 24
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }
# counts = {}
# for course, students in courses.items():
#     for s in students:
#         counts[s] = counts.get(s, 0) + 1
# max_count = max(counts.values())
# top = [s for s, c in counts.items() if c == max_count]
# print(top, max_count)


# task 1
# nums = [7,3,9,9,2,5,7,8]
# nums.sort()
# a = sorted(set(nums))
# print(a[-2])

# task 2
# nums = [7,3,9,9,2,5,7,8]
# nums.sort()
# a = sorted(set(nums))
# print(a[1])

# task 3
# nums =  [2, 1, 3, 5, 4, 7, 9, 11, 6]
# best = 0
# cur = 0
# for n in nums:
#     if n % 2 ==1:
#         cur +=1
#         best = max(best, cur)
#     else:
#         cur = 0
# print(best)

# task 4
# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# best = 1
# cur = 1
# for i in range(1, len(nums)):
#     if nums[i] > nums[i- 1]:
#         cur +=1
#         best = max(best, cur)
#     else:
#         cur = 1
# print(best)

# task 5
# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = max(count.values())
# print(min(n for n, c in count.items()if c == m))

#task 6
# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = min(count.values())
# print(min(n for n, c in count.items()if c == m))

#task 7
# a = [1, 2, 3, 4, 5]
# b = [3, 5, 7, 8, 1]
# print(sorted(set(a)&set(b)))

#task 8
# nums =[4, 7, 2, 9, 5]
# s = sorted(nums, reverse=True)
# print(s[0], s[1])

# task 9
# nums = [4, 8, 2, 7, 5]
# target = 9
# a = -1
# j = -1
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             a = i
#             j = j
#             break
#     if a != -1:
#         break
# print(a,j)

# task 10


# task 11
# n = [1,2,3,4,5]
# last = n[len(n)-1]
# ror = [last]
# for i in range(len(n) - 1):
#     ror.append(n[i])
# n = ror
# print(n)

# task 12
# nums = [1,2,3,4,5]
# k =3
# k = k % len(nums)
# for _ in range(k):
#     last = nums[len(nums) -1]
#     rotate = [last]
#     for i in range(len(nums)-1):
#         rotate.append(nums[i])
#     nums = rotate
# print(rotate)

# task 13
# a = [0,1,0,3,12]
# sorted(a)
# a.remove(0)
# a.remove(0)
# a.append(0)
# a.append(0)
# print(a)


