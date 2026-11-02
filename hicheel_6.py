# for i in range(3):
#     for i in range(5):
#         print("*", end="")
#     print()

# lab 1
# for i in range(1, 6):
#     print("--- 3-iin husnetg---")
#     for j in range(1,11):
#           print(i, "x", j, "=", i*j)
#     print()

# lab 2
# n ,a= map(int,input("input: ").split())
# for i in range(1,n):
#     for i in range(1,a):
#         print("1-r mort1 ", end="")
#     print()

# lab 3
# for i in range(1, 6):
#    for j in range(i):
#         print("*", end="")
#    print()

# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#          print(j, end="")
#     print()

# n = int(input())
# print("\n ---baruun tiish zeregtsuulsen gurwaljin---")
# for i in range(1, n+1):
#     for j in range(n - i):
#         print("", end="")
#     for k in range(i):
#         print("*", end="")
#     print()

# print("\n --- dorvoljin huree---")
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if i ==1 or i ==n or j ==1 or j==n:
#             print("*", end="")
#         else:
#             print("", end="")
#     print()

# lab 1
# angi_too = int(input("Нийт хэдэн анги вэ? "))

# for angi in range(1, angi_too + 1):

#     print("\n", angi, "-р анги")
#     suragch_too = int(input("Хэдэн сурагчтай вэ? "))
#     niit_onoo = 0
#     tentsen = 0

#     hamgiin_ih_onoo = -1
#     hamgiin_ih_ner = ""

#     for suragch in range(1, suragch_too + 1):

#         print("\n", suragch, "-р сурагч")

#         ner = input("Нэр: ")

#         while True:
#             onoo = int(input("Оноо: "))

#             if onoo >= 0 and onoo <= 100:
#                 break


#             print("Оноо 0-100 хооронд байна.")

#         niit_onoo = niit_onoo + onoo

#         if onoo >= 60:
#             tentsen = tentsen + 1

#         if onoo > hamgiin_ih_onoo:
#             hamgiin_ih_onoo = onoo
#             hamgiin_ih_ner = ner

#     dundaj = niit_onoo / suragch_too

#     print("\n---", angi, "-р ангийн тайлан ---")
#     print("Дундаж оноо:", dundaj)
#     print("Тэнцсэн сурагч:", tentsen)
#     print("Тэнцээгүй сурагч:", suragch_too - tentsen)
#     print("Хамгийн өндөр оноо:", hamgiin_ih_onoo)
#     print("Шилдэг сурагч:", hamgiin_ih_ner)

# lab2
n = int(input("heden hun? "))
for i in range(1, n +1):
    m = int(input())
    total_cost = 0
    for n in range(1, n + 1):
        baraa_une = int(input())
        shirheg= int(input())
        total_cost += baraa_une * shirheg
    given_money = int(input())
    print("\n",i, "-р hun toloh dun", total_cost)
    if given_money >= total_cost:
        change = given_money - total_cost
        print("hariult: ", change)
    else:
        shortage = total_cost - given_money
        print("dutuu mongo: ", shortage)    
    
        