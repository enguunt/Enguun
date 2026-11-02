############# Big o ###############
# 1
# number = [1,2,3,4,5]
# print(number[1])
# # O(1)

# 2
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)
# # O(n)

# 3
# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# # O(1)

# 4
# n = int(input("n: "))
# for i in range(n):
#     print(i)
# # O(n)

# 5
# for i in range(n):
#     print(i)
# # O(n)

# 6
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# # O(n2)

# 7
# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# # O(n2) 25 udaa ajillan

# 8
# n = 10
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# 50 udaa ajillan
# import time
# print("----- O(1) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     x = n

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n)
# print("\n----- O(n) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     total = 0

#     for i in range(n):
#         total += i

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n²)
# print("\n----- O(n²) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     count = 0

#     for i in range(n):
#         for j in range(n):
#             count += 1

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(log n)
# print("\n----- O(log n) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     x = n

#     while x > 1:
#         x //= 2

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")

# 9
# for i in range(n):
#     print(i)
# for j in range(n):
#     print(j)
# O(n)

# 10
# O(n) +  O(n)

# 11 Доорх дарааллыг хараад ямар Big O-той холбоотойг ол.
# 1000
#  ↓
# 500
#  ↓
# 250
#  ↓
# 125
#  ↓
# 62
#  ↓
# 31
###########  O(log n)

# 12
# 1000 aas 125 hurtel ihees bagruu irembelj  baigaa bolhoor

# 13
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])
# for number in numbers:
#     print(number)
# # big O  2bain

# # 14
# for i in range(n):
#     print(i)
# print("Hello")
# # O(n) O(1)

# # 15
# for i in range(n):
#     for j in range(n):
#         print(i, j)

# print("Done")
# O(n2) O(1)

# bonus hurdnaas udaan ruu erembel
# O(1), O(log n),  O(n) , O(n2) 

# # A
# print(numbers[0])

# # B
# for x in numbers:
#     print(x)

# # C
# for x in numbers:
#     for y in numbers:
#         print(x, y)

# D
# 1000 → 500 → 250 → 125 → ...
# A → O(1)
# B → O(n)
# C → O(n2)
# D → O(log n)

# task 1.1
# n = int(input())
# if n >= 18:
#     print("Oroh bolomjtoi")
# else:
#     print("Oroh bolomjgui")

# task 1.2
# n = int(input())
# if n % 2== 0:
#     print("Tegsh")
# else:
#     print("Sondgoi")

# task 1.3
# a,b = map(int, input().split())
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("Tentsuu")

# task 1.4
# day = int(input())
# if day == 1:
#     print("Davaa")
# elif day ==2:
#     print("Mygmar")
# elif day == 3:
#     print("lhagva")
# elif day == 4:
#     print("Purew")
# elif day == 5:
#     print("Baasan")
# elif day == 6:
#     print("bymba (Amraltiin odor)")
# elif day == 7:
#     print("Nym (Amraltiin odor)")
# else:
#     print("Buruu too")

# task 1.5
# km, hour = map(int, input().split())
# if km <= 2:
#     km = 3000
# else:
#     km = 3000 + (km -2 ) * 1500
# if hour >= 22 or hour < 6:
#     km = km * 1.2
# print(int(km))

# task 1.6
# kwh = int(input())
# total = 0
# if kwh <= 150:
#     total = kwh * 100
# elif kwh <= 300:
#     total = (150 * 100) + ((kwh - 150) * 150)
# else: 
#     total = (150 * 100) + (150 * 150) + ((kwh - 300) * 200)
# print(total)

# task 1.7
# username = input()
# password = input()
# is_blockeded = input()
# is_blocked = is_blockeded == "True"
# failed_attemps = int(input())
# if is_blocked:
#     print("tanii erh haagdsan")
# elif username == "" or password == "" :
#     print("medeellee buren oruulnu")
# elif username != "admin":
#     print("hereglegch oldsongu")
# elif password != 1234:
#     if failed_attemps >= 2:
#         print("erh haagdla")
#     else:
#         print("nuuts ug buruu")
# else:
#     print("amjilttai newterlee")

# task 2.1
# n = int(input())
# for i in range(1, n +1):
#     print(i)

# task 2.2
# n = int(input())
# total = 0
# for i in range(1, n):
#     if i % 2 == 0:
#         total += i
# print(total)

# task 2.3
# n = int(input())
# for i in range(1,11):
#     print(f"{n} x {i} = {n * i}")

# task 2.4
# money = 1000000
# years = 0
# while money <= 2000000:
#     money += money * 0.12
#     years += 1
# print(years)

# task 2.5
# n = int(input())
# if n <= 1:
#     print(f" {n} anhni too bish")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} anhnii too bish, {i}-t huwaagdan")
#             break
#     else:
#         print(f" {n} anhnii too")

# task 2.6
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     print(i,end=" ")

# task 2.7
# n = int(input())313
# for i in range(1, n +1):
#     for j in range(i):
#         print("*", end="")
#     print()

# task 2.8
# secret = 42
# oroldlog = 0
# max_oroldlog = 5
# print("Too taah togloom ehellee lalruuda ! chamd 5 han oroldog bn chdku bol uhen")
# while oroldlog < max_oroldlog:
#     oroldlog += 1
#     taalt = int(input("too oruulnuu: "))
#     if taalt > secret:
#         print(f"{taalt}: ih bain")
#     elif taalt < secret:
#         print(f"{taalt}: baga bain")
#     else:
#         print(f"{taalt}: zow! {oroldlog} dahi toog taala")
#         break
# else:
#     print(f"ta uhlee. nuuts too: {secret}")

# task 2.9
# n = int(input())
# while n > 9:
#     niilber = 0
#     a = n
#     while a > 0:
#         niilber += a % 10
#         a = a // 10
#     n = niilber
# print(n)

# task 3.1
# a = list(map(int, input().split()))
# niilber = 0
# toolur = 0
# for i in a:
#     niilber += i
#     toolur += 1
# dundaj = niilber / toolur
# print(f"{a} niilber:{niilber} dundaj:{dundaj}")

# task 3.2
# a = [45, 89, 72, 89, 30]
# total = 0
# index = 0
# for i, onoo in enumerate(a):
#     if onoo > total:
#         total = onoo
#         index = i
# print(f"{a} hamgiin ih: {total} index:{index}")

# task 3.3
# name = ["bat", "Saraa", "dorj"]
# haih_ner = input()
# oldloo = False
# for i in range(len(name)):
#     if name[i] == haih_ner:
#         print(f'"{haih_ner}" oldloo, index:{i}')
#         oldloo = True
#         break
# if not oldloo:
#     print(f'"{haih_ner}" oldsongu')

# task 3.4
# a = [1000, 2500, 8000]
# def b(price):
#     return int(price * 0.9)
# n = list(map(b , a))
# print(f"{a} - {n}")

# task 3.5
# a = [45, 78, 60, 30, 92]
# student = []
# for score in a:
#     if score >= 60:
#         student.append(score)
# print(student)
# print(f"Tentssen: {len(student)}")

# task 3.6
# a = list(map(int, input().split()))
# total = 0
# for n in a:
#     if n >= 5000:
#         total += n + 2000
# print(total)
# a = list(map(int, input().split()))
# b = sum([n + 2000 for n in a if n >= 5000])
# print(b)

# task 3.7
# names = ["Bat", "Saraa", "Dorj"]
# subject = ["Matematik", "Pizik", "Angli hel", "Tuuh"]
# scores = [
#     [80,90,70,60],
#     [95,85,75,65],
#     [50,60,70,80]
# ]
# print("1.dundaj onoo:")
# for i in range(len(names)):
#     avg_scores = sum(scores[i]) / len(scores[i])
#     print(f"{names[i]}: {avg_scores}")
# print("\n2. hicheel buriin hamgiin ondor onoo")
# for subject, sub_scores in zip(subject, zip(*scores)):
#     max_score = max(sub_scores)
#     max_index = sub_scores.index(max_score)
#     top_student = names[max_index]
#     print(f"{subject}: {top_student} ({max_score})")

# task 4.1
# text = "batbold"
# a = text[0].upper() + text[1:]
# b = len(text)
# print(f"{a} ({b} useg)")

# task 4.2
# name = input()
# oloh = input()
# count = 0
# for c in name:
#     if c == oloh:
#         count+= 1
# print(count)
# a = name.count(oloh)
# print(a)

# task 4.3
# a = input()
# if a.count("@") != 1:
#     print("buruu imail")
# else:
#     username, domain = a.split("@")
#     if len(username) == 0 or "." not in domain or domain.endswith("."):
#         print("buruu imail")
#     else:
#         print(f"Username: {username}, domain: {domain}")

# task 4.4
# bad_words = ["muu", "teneg"]
# b = input()
# words = b.split()
# a = []
# for word in words:
#     v = word.lower()
#     is_bad = False
#     for bad in bad_words:
#         if bad in v:
#             word = "*" *len(word)
#             break
#     a.append(word)
# n = " ".join(a)
# print(n)

# task 4.5
# a = input()
# cleaned = "".join([c.lower() for c in a if c.isalnum()])
# palindrom = cleaned == cleaned[::-1]
# print(palindrom)

# task 5.1
# def square(n):
#     return n ** 2
# print(square(-3))

# task 5.2
# def greet(name = "Zochin"):
#     return f"Sain uu {name}!"
# print(greet("Bat"))
# print(greet())

# task 5.3
# def is_adult(age):
#     return age >= 18
# print(is_adult(20))
# print(is_adult(16))

# task 5.4
# def calculate_bmi(weight,height):
#     bmi =  weight / (height * height)
#     return round(bmi, 2)
# def get_category(bmi):
#     if bmi <= 18.5:
#         return "Turanhai"
#     elif bmi <= 25:
#         return "Hewiin"
#     elif bmi <= 30:
#         return "iluudel jintei"
#     else:
#         return "Targalaltai" 
# w1,h1 = 70, 1.75
# bmi1 = calculate_bmi(w1,h1)
# cat1 = get_category(bmi1)
# print(w1,h1,bmi1,cat1)

# w2,h2 = 95, 1.70
# bmi2 = calculate_bmi(w2, h2)
# cat2 = get_category(bmi2)
# print(w2,h2,bmi2,cat2)

# task 5.5
# def calc_insurance(gross):
#     return gross * 0.115
# def calc_tax(gross):
#     ndsh = calc_insurance(gross)
#     return (gross - ndsh) * 0.10
# def calc_net(gross):
#     ndsh = calc_insurance(gross)
#     tax = calc_tax(gross)
#     net = gross - ndsh - tax
#     return net
# gross_salary = 2000000
# print(f"gross = {gross_salary}")
# print(f"ndsh: {int(calc_insurance(gross_salary))}")
# print(f"tatvar: {int(calc_tax(gross_salary))}")
# print(f"gart: {int(calc_net(gross_salary))}") 

# task 5.6
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def decrement():
#         nonlocal count
#         count -=1
#         return count
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#     return{
#             "increment": increment,
#             "decrement": decrement,
#             "reset": reset
#     }
# c1 = make_counter()
# c2 = make_counter()
# print(c1["increment"]())
# print(c1["increment"]())
# print(c2["increment"]())
# print(c1["decrement"]())
# print(c1["reset"]())

# task 6.1
# a = {"name": "Bat",
#      "age": 20,
#      "city": "Ulaanbaatar"}
# a["age"] +=1
# a.update({"email":"bat@gmail.com"})
# del a["city"]
# print(a)

# task 6.2
# prices = {"talh": 2500, "suu": 3800, "mah": 18000}
# for key,value in prices.items():
#     print(key,value)

# task 6.3
# prices = {"talh": 2500, "suu": 3800, "mah": 18000, "ondog": 6500}
# max_name = ""
# max_une = 0
# total = 0
# for baraa,une in prices.items():
#     total += une
#     if une > max_une:
#         max_une = une
#         max_name = baraa
# print(f"Hamgiin unetei mah: {max_name} - {max_une}")
# print(f"Niit: {total}")

# task 6.4
# votas= ["Bat", "Saraa", "Bat", "Dorj", "Bat", "Saraa"]
# total = {}
# for name in votas:
#     total[name] = total.get(name, 0) +1
# print(total)
# winner = ""
# max_votes = 0
# for name , count in total.items():
#     if count > max_votes:
#         max_votes = count
#         winner = name
# print(f"Winner: ({max_votes} sanal)")

# task 6.5
# students = [
#     {"name": "bat", "class": "10A", "score":85},
#     {"name": "Saraa", "class": "10B", "score":92},
#     {"name": "Dorj",     "class": "10A", "score": 70},
#     {"name": "Naraa",    "class": "10B", "score": 78},
#     {"name": "Temuulen", "class": "10A", "score": 95},
# ]
# group = {}
# for s in students:
#     cls = s["class"]
#     name = s["name"]
#     if cls not in group:
#         group[cls] = []
#     group[cls].append(name)
# print(group)

# task 6.6
# students = [
#     {"name": "bat", "class": "10A", "score":85},
#     {"name": "Saraa", "class": "10B", "score":92},
#     {"name": "Dorj",     "class": "10A", "score": 70},
#     {"name": "Naraa",    "class": "10B", "score": 78},
#     {"name": "Temuulen", "class": "10A", "score": 95},
# ]
# class_data = {}
# for s in students:
#     cls = s["class"]
#     name = s["name"]
#     score = s["score"]
#     if cls not in class_data:
#         class_data[cls] = [0,0, "", 0]
#     class_data[cls][0] += score
#     class_data[cls][1] += 1
#     if score > class_data[cls][3]:
#         class_data[cls][2] = name
#         class_data[cls][3] = score
# for cls, data in class_data.items():
#     total = data[0]
#     count = data[1]
#     student = data[2]
#     max_score = data[3]
#     avg = total / count
#     print(cls,avg,student,max_score)