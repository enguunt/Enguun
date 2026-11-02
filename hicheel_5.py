############################ while
# task 1
# i = 1
# while i <= 10:
#     print(i)
#     i+= 1

# task2
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# task3
# total = 0
# n = 1
# while n <=100:
#     total +=n 
#     print(total)
#     n+=1

# task 4
# a = 1
# while a <= 1000:
#     print(a)
#     a *= 2

# task 5
# pin = input("nuuts kod: ")
# while pin != "88719518":
#     print("too buruu bn ? dahiad oruulnu")
#     pin = input("nuuts kod: ")
# print("newterlee!")

# task 6
# secret = 7
# guess = int(input("Тоо таа: "))
# while guess != secret:
#     if guess < secret:
#      print("Багадаа!")
#     else:
#      print("Ихдээ!")
#     guess = int(input("Дахин: "))
# print("Зөв!")

# task 7
# a = 50
# x = 0
# n = 0
# while x != a:
#     x = int(input("too taa: "))
#     n += 1
#     if x < a:
#         print("ih too")
#     elif x > a:
#         print("baga too")
# print("zow taalaa")
# print("oroldson too: ", n)

# task 8
# a = 1
# while a <= 100:
#     print(a)
#     a += 1
# task 9
# import random
# a = random.randint(1, 100)
# n = 1
# x = 0
# while x != a:
#     x = int(input("too taa: "))
#     n += 1
#     if x < a :
#         print("ih too")
#     elif x > a :
#         print("baga too")
# print("zuw taalaa!")
# print("oroldson too: ", n)

# task 10
# choice = "" 
# n = 0 
# while choice != "3":
#     print("1 , Мэндчил 2 , Цаг 3  Гарах, 4  game toglhu")
#     choice = input("Сонголт: ") 
#     n+=1
#     if choice == "1":
#         print("Сайн уу!")
#     elif choice == "2":
#         print("Одоо 14:30")
#     elif choice == "3":
#         print("Ийм сонголт алга.")
#     elif choice == "4":
#         print("tgyo yu tglhu.")
# print("oroldogo: ", n)

# dasgal 20 , task 1
# n = int(input())
# a = 1
# while a <= n:
#     print(a)
#     a += 1

# task 2
# n = int(input("too oruul: "))
# while 1 <= n:
#     print(n)
#     n -=1

# task 3
# n = int(input("too oruul"))
# a = 2
# while a <= n:
#     print(a)
#     a += 2

# task 4
# n = int(input("too oruul"))
# a = 1
# while a <= n:
#     print(a)
#     a += 2

# task 5
# a = int(input())
# total = 0
# n = 1
# while n <=a:
#     total +=n 
#     print(total)
#     n+=1

# task6
# total = 0
# n = int(input("too oruul"))
# a = 2
# while a <= n:
#     total += n
#     print(a)
#     a += 2

# task7
# n = int(input("too oruul"))
# a = 3
# while a <= n:
#     print(a)
#     a += 3

# task 8
# n = int(input("Heden too oruulah ve? "))
# eyreg = 0 
# sorog = 0 
# teg = 0 
# i = 1
# while i <= n: 
#     x = int(input("Too = "))
#     if x > 0:
#         eyreg += 1
#     elif x < 0:
#         sorog += 1
#     else:
#         teg += 1
#     i += 1
# print("Eyreg:", eyreg)
# print("Sorog:", sorog) 
# print("Teg:", teg)

# task 9
# a = int(input())
# s = 0
# n = 0
# while n < a:
#     a = int(input("too"))
#     if a < 0:
#        s += a
#     n += 1
# print("niilber: ", s)

# task10
# n = int(input("N  = "))
# i = 0
# max_num = 0
# while i < n :
#     a = int(input("too=  "))
#     if i == 0 or a> max_num:
#         max_num = a
#     i += 1
# print("hamgiin ih too: ", max_num)

# task 11
# n = int(input("N  = "))
# i = 0
# bag_too= 0
# while i < n :
#     a = int(input("too =  "))
#     if i == 0 or a < baga_too:
#         baga_too = a
#     i += 1
# print("hamgiin ih too: ", baga_too)

# task 12
# n = int(input("too oruul"))
# f = 1
# while f <= n:
#     if f % 3 ==0 and f% 5 ==0:
#         print(f)
#     f += 1

# task13
# n = int(input("Too: "))
# if n < 0:
#     n = -n
# count = 0
# if n == 0:
#     count =1
# while n >0:
#     n //=10
#     count +=1
# print("tsupr: ", count)

# task14
# n = int(input("too: "))
# a = 0
# while n >0:
#     a +=n %10
#     n //= 10
# print("tsuprin niilber: ", a)

# task15
# n = int(input("toogo oruul: "))
# a = 0
# while n > 0:
#     a = (a * 10 )+ n % 10
#     n = n // 10
# print(a)

# task16
# n = int(input("too: "))
# a = n
# b = 0
# while n > 0:
#     b = b * 10 + n %10
#     n //= 10
# if a == b:
#     print("palindrome")
# else:
#     print("palindrome bish")

# task 17
# n = int(input("too: "))
# i = 2
# count = 0
# while i< n:
#     if n % i ==0:
#         count +=1
#     i +=1
# if n > 1 and count ==0:
#     print("anhnii too")
# else:
#     print("anhni too bish")

# task18
# n = int(input("too: "))
# i = 2
# while i <= n :
#     j = 2
#     count = 0
#     while j < i:
#         if i % j == 0:
#             count += 1
#         j += 1
#     if count == 0:
#         print(i)
#     i += 1

# task19
# n = int(input("input: "))
# i = 1
# while i<= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1

# task20
# pin = ""
# while pin != "python1234":
#     pin = input("nuuts ug: ")
# print("zow nuuts ug")

#                                           break, continus
# level 1 (task 1)
# for i in range(1,11):
#     print(i)

# task 2
# for i in range(1,21, 2):
#     print(i)


# task 3
# for i in range(1,21, 2):
#     print(i)

# task 4
# for i in range(1,11,):
#     print("5 x i", "=", 5 * i)

# task 5
# n = int(input())
# for i in range(1, n+1 ):
#     print(i)

# task 6 
# n = int(input())
# for i in range(n , 0, -1):
#     print(i)
    
# level 2 (task 7)
# for i in range(1,51):
#     if i % 3 == 0:
#         print(i)

# task 8
# for i in range(1,31):
#     if i %5 != 0:
#         print(i)

# task 9
# for i in range (1,101):
#     if i % 2 ==0:
#         print(i)

# task 10
# for i in range(1,101):
#     if i % 7 == 0:
#         print(i)

# task 11
# total = 0
# for i in range(1, 101):
#     total+=i
#     print(total)

# task 12
# total = 0
# for i in range(1,51):
#     if i % 2 ==0:
#         total +=1
#         print(total)

# level 3 (task 13)
# n = 1
# while n<=10:
#     print(n)
#     n +=1

# task 14
# n = 10
# while n >= 1:
#     print(n)
#     n -=1 

# task 15
# n = 2
# while n <= 20:
#     print(n)
#     n += 2

# task 16
# a = int(input())
# total = 0
# n = 1
# while n <=a:
#     total +=n 
#     print(total)
#     n+=1

# task 17
# n = int(input("input: "))
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n>0:
#         count+=1
#         n=n//10
# print("output: ", count)

# task 18
# n = int(input("input: "))
# a = 0
# while n > 0:
#     a += n % 10
#     n = n // 10
# print("Output: ", a)

# level 4 (task 19)
# n = 1
# while True:
#     if n == 5:
#         break
#     print(n)
#     n +=1

# task 20
# n = 10
# while n <= 100:
#     if n % 7== 0:
#      print(n)
#      break
#     n +=1
    
# task 21
# secret = 8
# guess = int(input("Тоо таа: "))
# while guess != secret:
#     if guess < secret:
#         print("buruu")
#     else:
#          print()
#     guess = int(input("Дахин: "))
# print("Зөв!")

# task 22
# while True:
#     too = int(input("too oruul: "))
#     if too == 0:
#         break

# task 23
# niilber = 0
# while True:
#     too = int(input("too oruul: "))
#     if too == 0:
#         break
#     niilber += too
# print(niilber)

# level 5(task 24)
# n = 0
# while n <= 10:
#     n +=1
#     if n==5:
#         continue
#     print(n)

# task 25
# for i in range(1,21):
#     if i % 2==0:
#         continue
#     print(i)

# task 26
# for i in  range(1,31):
#     if i % 3 ==0:
#         continue
#     print(i)

# task 27
# niilber = 0
# for i in range(5):
#     too = int(input())
#     if too < 0:
#         continue
#     niilber += too
# print(niilber)

# task 28
# tooluur = 0
# too =1
# while True:
#     if too % 7 == 0:
#         print(too)
#         tooluur +=1
#         if tooluur == 5:
#             break
#     too += 1

# task 29
# while True:
#     too = int(input())
#     if too ==0:
#         break
#     if too < 0:
#         continue
#     if too % 2 != 0:
#         continue
# print(too)
# secret = 17
# while True:
#     guess = int(input("Тоо таа: "))
#     if gue    ss < 0:
#         print("sorog too oruulahgui")
#         continue
#     if guess < secret:
#         print("baga bn")
#     elif guess >secret:
#         print("ih bain")
#         guess = int(input("Дахин: "))
#     else:
#         print("zow taalaa")
#     break

# h, e, d= map(int, input("input: ").split())
# n = int(input())
# ent = n // (h * d)
# local= ( h * d) 
# floor = (local // d)
# door = d 
# if n % (h * d) == 0:
#     if n % (h * d) == 0:
#         if local % d == 0:
#             if local % d == 0:
#                 print("")
#             else:
#                 local % d
#         else:
#            (local // d) +1
#     else:
#         n % (h * d) 
# else:
#     n + (h * d) +1
# print(ent, floor, door)

# task 1
# total, seats = map(int, input("input: ").split())
# seats_number = int(input())
# a = seats_number// seats
# b= seats_number % seats
# if seats == 0:
#     b = seats
# else:
#     a = a +1
# print(a, b)

# task 2
# niit_shuuge, neg_shuugee = map(int, input("input: ").split())
# hav_number = int(input())
# a = hav_number // neg_shuugee
# b = hav_number % neg_shuugee
# if neg_shuugee == 0:
#     b = neg_shuugee
# else:
#     a = a + 1
# print(a,b)
                               
# task 3
# group , student = map(int, input("input: ").split())
# s_number = int(input())
# a = s_number // student
# b = s_number % student
# if student== 0:
#     b = student
# else:
#     a = a +1
# print(a,b) 

# task 4
# zogsool, car = map(int, input("input: ").split())
# c_number = int(input())
# a = c_number // car
# b = c_number % car
# if car == 0:
#     b = car
# else:
#     a = a +1
# print(a,b) 

sektor, egnee, suudal = map(int, input("input: ").split())
s_number = int(input())
a = egnee * suudal
b = s_number // a
n = s_number % a
if n == 0:
    n = a
else: 
    b = b +1
c = n // suudal
v = n % suudal
if v == 0:
    v = suudal
else:
    c = c +1
print(a,c,v)
    


    