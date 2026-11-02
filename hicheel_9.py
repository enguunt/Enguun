########################################### temdegts moriin uildel ###################
# task 1
# a = "Saraa!"
# print("sainuu, ", a)

# task 2
# a = int(input())
# b = int(input())
# print(a+b)

# task 3
# a = float(str(input()))
# print(a*2)

# task 4
# a = input()
# print(type(a))
# too = int(a)
# print(type(too))

# task 5
# a = input()
# print(len(a))

# task 6
# a = input()
# print(a[0])
# print(a[-1])

# task 7
# a = int(input())
# for i in range(1,a + 1):
#     print(i)

# task 8
# a = input().split()
# too = []
# for toon in a :
#     too.append(int(toon))
# print(sum(too))

# task 9
# a = input().split()
# print(min(a), max(a))

# task 10
# a = list(map(int, input().split()))
# b = sum(a) / len(a)
# print(round(b, 2))

# task 11
# a = input().split()
# b = input()
# a.append(b)
# print(a)

# task 12
# a = input().split()
# b = input()
# a.insert(1,b)
# print(a)

# task 13
# a = input().split()
# b = input()
# a.remove(b)
# print(a)

# task 14
# a = input().split()
# n = int(input())
# b = a.pop(n)
# print(b)
# print(",".join(a))

# task 15
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# print(a)
# a.sort()
# print(a)

# task 16
# a =  list(map(int, input().split()))
# a.reverse()
# print(a)

# task 17
# a = "  hello  "
# print(a.strip())
# print(a.lstrip())
# print(a.rsplit())

# task 18
# a = input()
# b = a.split()
# print(len(b))

# task 19
# a = input().lower()
# n = input().lower()
# print(a.count(n))

# task 20
# a = input()
# b= input()
# n = a.find(b)
# print(n)
# if n != -1:
#     print(a.index(b))
# else:
#     print("oldsongue")

# task 21
# a = input().split()
# b = 0
# for x in a:
#     if x.startswith("report") and x.endswith(".pdf"):
#         print(x)
#         b += 1
# if b == 0:
#     print("oldsongue lalra")

# task 22
# a = input()
# b = input()
# c = input()
# print(a.replace(b,c))

# task 23
# a = input().lower().split()
# b = input().lower()
# if b in a:
#     print("yeaa")
# else:
#     print("nope")

# task 24
# a = input()
# print(a[0:3])
# print(a[8:11])

# task 25
# n = input().lower()
# if n[::-1]:
#     print("yes")
# else:
#     print("no")

# task 26
# a = input().split()
# x = a[0]
# for i in a:
#     if len(i) > len(x):
#          x = i
# print(x)

# task 27
# name, age, city = input().split(",")
# name = name.strip()
# age = int(age.strip()) +1
# city = city.strip()
# print(name+ "| ireh jil:  " +str(age)+ "| " + city)

# task 28
# words = input().lower().split()
# unique = []
# for word in words:
#     if word not in unique:
#         unique.append(word)
# unique.sort()
# print(" ".join(unique))

# task 29
# nums = input().split()
# unique = []
# for x in nums:
#     if x not in unique:
#         unique.append(x)
# unique.sort()
# print(unique[-2])

# task 30
n = int(input())
names = []
scores = []
for _ in range(n):
    name, score = input().split(",")
    names.append(name.strip())
    scores.append(int(score.strip()))
average = round(sum(scores) / len(scores), 2)
max_score = max(scores)
index = scores.index(max_score)
sorted_names = names.copy()
sorted_names.sort()
print("Дундаж:", average)
print("Хамгийн өндөр:", names[index], max_score)
print("Нэрс:", ", ".join(sorted_names))
