############### linier search ################
# def linier(L,n) :
#     for i in range(len(L)):
#         if L[i] == n:
#             return i
#     return -1
# L = [1,2,3,4,6,8,10]
# n = 9
# print(linier(L,n))

# def linear(l,n):
#     for x,i in enumerate(l):
#         if i == n:
#             return x
#     return -1
# l= [1,2,3,4,6,8,10]
# n = 6
# print(linear(l,n))

# task 1
# number = list(map(int, input().split()))
# l = int(input())
# for num in number:
#     if num == l:
#         print("oldloo")
#         break
# else:
#     print("oldsongue")

# task 2
# def linear (l,n):
#     for i in range(len(l)):
#         if l[i] == n:
#             return i
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linear(l,n))

# task 3
# def linear (l,n):
#     for i ,a in enumerate(l):
#         if a== n:
#             return i
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linear(l,n))

# task 4
# def linier (l,n):
#     count = 0
#     for i, a in enumerate(l):
#         if a == n:
#             count += 1
#     return count
# l = list(map(int, input().split()))
# n = int(input())
# m = linier(l,n)
# print(m)

# task 5
# def linier (l,n):
#     for i in range(len(l) -1,-1,-1):
#         if l[i] == n:
#             return i
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 6
# def linier (l,n):
#     for i ,a in enumerate(l):
#         if a == n:
#             return i
#     return -1
# l = ["Bat", "Saraa", "Bold", "Anu", "Temuulen"]
# name = input()
# hariu = linier(l,name)
# if hariu != -1:
#     print(f"index:{hariu}")
# else:
#     print("oldsongue")

# task 7
# def linier(l):
#     for i,a in enumerate(l):
#         if a > 0:
#             return i
#     return -1
# l = list(map(int, input().split()))
# hariu = linier(l)
# if hariu != -1:
#     print(f"hamgiin ehnii eyreg too:{hariu}")
# else:
#     print("bhku")

# task 8
# def linier(l):
#     for i, a in enumerate(l):
#         if a > 15:
#             return a
#     return -1
# l = list(map(int, input().split()))
# h = linier(l)
# if h != -1:
#     print(f"anh taarsan too {h}")
# else:
#     print("oldsongue")

# task 9
# students = [
#     ["Bat", 18],
#     ["Saraa", 20],
#     ["Bold", 19],
#     ["Anu", 18]
# ]
# def linier (students,target):
#     for i, student in enumerate(students):
#         name = student[0]
#         age = student[1]
#         if name == target:
#             return age
#     return -1
# target = input()
# h = linier(students,target)
# if h != -1:
#     print(f"{target} {h}")
# else:
#     print("oldsongue")

# task 1
# def lineas(l):
#     for i in range(len(l)):
#         if l[i] % 2 != 0:
#             return i
#     return -1
# l = list(map(int, input().split()))
# print(lineas(l))

# task 2
# def linies(l):
#     for i, a in enumerate(l):
#         if a >= 10:
#             return a
#     return -1
# l = list(map(int, input().split()))
# h = linies(l)
# if h != -1:
#     print(f"oldloo {h}")
# else:
#     print(f"oldsongue")

# task 3
# def linies(l,n):
#     for i,a in enumerate(l):
#         if a == n:
#             return i
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linies(l,n))

# task 4
# def linies(l):
#     for i,a in enumerate(l):
#         if a > 5:
#             return a
#     return -1
# l = list(map(int, input().split()))
# print(linies(l))

# taks 5
# def linies(l):
#     count = 0
#     for i, n in enumerate(l):
#         if n <= 0:
#             count += 1
#     return count
# l = list(map(int, input().split()))
# print(linies(l))

# task 6
# def linies(l,n):
#     for i,a in enumerate(l):
#         if a < n:
#             return a
#     return -1
# l = list(map(int, input().split()))
# n = int(input())
# print(linies(l,n))

# task 7
# def linies(l):
#     for i,n in enumerate(l):
#         if n % 2 == 0:
#             return n
#     return -1
# l = list(map(int, input().split()))
# print(linies(l))

# task 8
# def linies(l):
#     for i, n in enumerate(l):
#         if n > 15 and n % 2 != 0:
#             return i
#     return -1
# l = list(map(int, input().split()))
# print(linies(l))

# task 9
# students = [
#     ["Bat", 65],
#     ["Saraa", 82],
#     ["Bold", 74],
#     ["Anu", 91],
#     ["Temuulen", 78]
# ]
# def linier (studentsa):
#     for student in studentsa:
#         name = student[0]
#         score = student[1]
#         if score > 80:
#             return name
#     return -1
# print(linier(students))

# task 10
# def linier (l):
#     for i  in range(len(l) -1, -1, -1):
#         if i % 2 != 0:
#             return i
#     return -1
# l = list(map(int, input().split()))
# print(linier(l))
    
# task 11
# def linier (l,n):
#     for i in range(len(l)):
#         if l[i] == n:
#             print(f"{i}")
# l = list(map(int, input().split()))
# n = int(input())
# print(linier(l,n))

# task 12
students = [
    ["Bat", 65],
    ["Saraa", 82],
    ["Bold", 74],
    ["Anu", 91],
    ["Temuulen", 78]
]
def linier (studentsa,a):
    for student in studentsa:
        name = student[0]
        score = student[1]
        if name == a:
            if score >= 60:
                return "Tenstsen"
            else:
                return "tentseegui"
    return "oldsongue"
haih = input()
print(linier(students,haih))
