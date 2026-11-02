# #################################### massiv (tuple)################################
# a = (10,20,30)
# b,*c=a
# print(c)

# task 1
# a = ("ulaan", "nogoon", "tsenher")
# print(a)

# task 2
# a = ("nohoi", "muur", "tuulai", "mori")
# b,g,c ,f= a
# print(f"{b} \n{g} \n{f}")

# task 3
# a = (10,)
# print(type(a))

# task 4
# a = ("matematik", "mongol hel", "angli hel", "python" )
# n,b,v,c= a
# print(f"{n} \n{v} \n{c}")

# task 5
# a = (10,20,30,40,50)
# print(a[0:3])

# task 6
# a = (10,20,30,40,50)
# print(a[-3:])

# taks 7
# a = ("alim", "banana", "jurj", "usan uzem")
# print(len(a))

# task 8
# a = (45, 12, 89, 23, 7)
# print(max(a))
# print(min(a))

# task 9
# a = (80, 90, 70 , 100)
# b = sum(a)
# n = sum(a) / len(a)
# print(b)
# print(n)

# task 10
# a = (50, 10,40,20, 30)
# b = sorted(a)
# print(b)

# task 11
# a = (10,20,10,30,10,40)
# print(a.count(10))

# task 12
#a = ("alim", "banana", "jurj", "usan uzem")
# print(a.index("jurj"))

# task 13
# animals = ("Nohoi", "muur", "tuulai")
# a = input("Amitan: ")
# if a in animals:
#     print("baina")
# else:
#     print("baihgui")

# task 14
# a = ("Anu", 12, "7A")
# name , age , student_class = a
# print("ner: ", name)
# print("nas: ", age)
# print("Angi: ", student_class)

# task 15
# coor = (15, 25)
# x,y = coor
# print("x = ", x)
# print("y = ", y)

# task 16
# a = ("Python surah", "Bat", 250)
# b,n,m = a
# print("Nom: ",b)
# print("Zohiolch:",n)
# print("Huudas:",m)

# task 17
# a = (5,10)
# n,b = a
# print("a = ",b)
# print("b = ",n)

# task 18
# a = (10,20,30,40,50)
# n,*b = a
# print("ehnii utga: ", n)
# print("Uldsen utga:", b)

# task 19
# a = (1,2,3,4,5,6)
# n, *b, m = a
# print("ehnii: ", n)
# print("dundah: ",b)
# print("suuliin: ",m)

# task 20
# a = ("temuulen", "Matematik","python", "angli hel")
# n,*b = a
# print("suragch: ",n)
# print("hicheeluud: ",b)

# task 21
# a = ("devter", 3500, 4)
# name,price,quantity = a
# print("baraa: ",name)
# print("negj une: ",price)
# print("too shirheg: ",quantity)
# print("niit une: ", price*quantity)

# task 22
# student = (
#     ("Anu", 90),
#     ("bat", 75),
#     ("Saraa", 100)
# )
# for name, scores in student:
#     print(f"{name}: {scores}") 

# task 23
# student = (
#     ("Anu", 90),
#     ("bat", 70),
#     ("Saraa", 100)
# )
# for name, scores in student:
#     if scores >= 80:
#         print(name)

# task 24
# colors = ("ulaan", "nogoon", "tsenher")
# colors_list = list(colors)
# colors_list.append("shar")
# colors = tuple(colors_list)
# print(colors)

################### Aldaa zasah #################
# task 1
# nums = list(map(int, input().split()))
# nums.sort()
# print(nums[1])

# task 2
# nums = list(map(int, input().split()))
# result = []
# for i in nums:
#     if i  not in result:
#          result.append(i)
# print(result)

# task 3
# text = input().lower()
# reverse = ""
# for i in range(len(text) -1, -1, -1):
#     reverse += text[i]
# if text == reverse:
#     print("YES")
# else:
#     print("NO")

# task 4
# words = input().split()
# longest = words[0]
# for word in words:
#      if len(word) > len(longest):
#         longest = word
# print(longest)

# task 5
# text = input().lower()
# vowels = "аэиоуөүАЭИУӨҮ"
# count = 0
# for ch in text:
#     if ch  in vowels:
#         count += 1
# print(count)

# task 6
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#         total += i
# print(total)

# task 7
# n = int(input())
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print(total)

# task 8
# n = int(input())
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse *10+ digit
#     n //= 10
# print(reverse)

# task 9
# n = int(input())
# if n > 1:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not prime")
# else:
#     print("not prime")

# task 10
# nums = list(map(int, input().split()))
# smallest = 0
# for num in nums:
#     if num > smallest:
#         smallest =+ 1
# print(smallest)

# task 11
# nums = list(map(int, input().split()))
# count = 0
# for num in nums:
#     if num % 2 != 0:
#         count = num
# print(count)

# task 12
# nums = list(map(int, input().split())) 
# best = nums[0]
# best_count = 0
# for num in nums:
#     count = nums.count(num)
#     if count > best_count:
#         best_count = count
#         best = num
# print(best)

# task 13
# words = input().split()
# target = input()
# count = 0
# for word in words:
#     if word == target:
#         count += 1
# print(count)

# task 14
# nums = list(map(int, input().split()))
# for i in range(len(nums) - 1, -1, -1):
#     print(nums[i], end=" ")

# task 15
# nums = list(map(int, input().split()))
# max_sum = 0
# for i in range(len(nums) -1):
#     current = nums[i] + nums[i + 1]
#     if current > max_sum:
#         max_sum = current
# print(max_sum)

# task 16
# words = input().split()
# result = []
# for word in words:
#     result.append(word[::-1])
# print(" ".join(result))

# task 17
# n = int(input())
# if n == 0:
#     count = 1
# else:
#     count= 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)

# task 18
# n = int(input())
# for i in range(1, n +1 ):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)

# task 19
# a = list(map(int, input().split())) 
# b = list(map(int, input().split())) 
# result = []
# for x in a:
#     if x in b:
#         result.append(x)
# print(result)

# task 20
# nums = list(map(int, input().split()))
# total = 0
# count = 0
# for n in nums:
#     if n > 0:
#         total += n
# print(total / len(nums))

#task 21
# student = ("Сараа", 19, "Python", 95, "A")
# name, age, *lesson = student
# print(name)
# print(age)
# print(lesson)

# task 22
# data = (10, 20, 30, 40, 50) 
# first = data[0]
# remaining = data[1:]
# print(first)
# print(remaining)

# task 23
# nums = (-12, -5, -30, -8, -21)
# largest =nums[0] 
# for n in nums:
#     if n < largest:
#         largest = n
# print(largest)

# task 24
# nums = (5, 1, 8, 3, 2)
# b = sorted(nums)
# print(b)

# task 25
# nums = (10, 20, 30, 40, 50)
# x = int(input())
# if x in nums:
#     print(nums.index(x))
# else:
#     print("Олдсонгүй")

# task 26
# nums = (1, 2, 2, 3, 4, 4, 5)
# result = []
# for n in nums:
#     if n not in result:
#         result.append(n)
# print(tuple(result))

# task 27
# words = input().lower().split()
# best_word = ""
# best_count = 0
# for word in words:
#     count = words.count(word)
#     if count > best_count:
#         best_count = count
#         best_word = word
# print(best_word)

# task 28
nums = tuple(map(int, input().split()))
total = 0
for n in nums:
    if n % 2 == 0:
        total += n
print(total)