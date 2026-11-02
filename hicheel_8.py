########################## TEMDEGT MORIIN UILDEL #########################
# text = "bAnAnA"
# print(text.upper())  ##tomruulan
# print(text.lower()) ##jijegruulen

#text = "bAnAnA  Python"
#print (text.replace("Python", "jims")) ## UG SOLIH

######################### dawtlag ########################
# a = "Hello world"
# print(a)

# a = 5
# b = 2
# print(a * b)
# print(a / b)
# print(a+ b)
# print(a - b)
# print(a % b)
# print(a ** b)
# print(a // b)

# n = int(input())
# if n > 0:
#     print("eyreg")
# elif n == 0 :
#     print("zero")
# elif n < 0:
#     print("sorog")
# else:
#     print()

# n = int(input())
# if n < 0 or n > 100:
#     print("huurentseg")
# elif n <= 18:
#     print("hvvhed")
# elif n <= 38:
#     print("zaluu")
# else:
#     print("hogshin")

# tsalin = int(input())
# ajilsan = int(input())
# if tsalin < 0 or ajilsan < 0:
#     print("sorog too oruulahgui")
# else:
#     a = tsalin * ajilsan
#     if ajilsan <= 40:
#         print(a)
#     else:
#         print(a // 2)
    
# task 1
# a = "Python hel surahad hylbar"
# b = a.split()
# print(len(b)) 

# task 2
# a = input("input: ")
# b = a.split()
# c = b
# for word in b:
#     if len(word) > len (c):
#         c = word
# print(c)

# task 3
# a = input()
# b = "аэиоуөүАЭИОУӨҮ"
# b_count = 0
# for i in a:
#     if i in b:
#         b_count += 1
# print(b_count)

# task4
# a = input().split()
# b = a[-1]
# words = a[:-1]
# count = 0
# for i in words:
#     if i == b:
#         count += 1
# print(count)

# task5
# n = input()
# a = n.split()
# a.sort()
# print(a)

# task 6
# a = input().split()
# palindrome = []
# for word in a:
#     if word == word[::-1]:
#         palindrome.append(word)
# print(*palindrome)

# task 7
# a = input().split()
# r = []
# for name in a:
#     r.append(name)
#     r.append(str(len(name)))
# print(*r)

# task 8
# text = "banana"
# a_count = text.count("a")
# print(a_count)

# task 9
# a = input().split()
# a.pop(2)
# a.pop(3)
# print(a)

# task 10
# a = input()
# students = a.split( )
# names = []
# scores = []
# for student in students:
#     name, score = student.split(":")
#     names.append(name)
#     scores.append(int(score))
# max_score = max(scores)
# out_list = []
# for i in range(len(scores)):
#     if scores[i] == max_score:
#         out_list.append(f"{names[i]} {scores[i]}")
# print(" ".join(out_list))

# task 11
# n = input().split()se
# urt1 = ""
# urt2 = ""
# for i in n :
#     if len(i) > len(urt1):
#         urt2 = urt1
#         urt1 = i
#     elif len(i) > len(urt2):
#         urt2 = urt1
#         urt2 = i
# print(urt2)

