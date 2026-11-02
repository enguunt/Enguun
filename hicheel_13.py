########################    function buteeh ##########################
# def love (x):
#     print("I LOVE YOU", x)
# love("Amina")
# print("Zaya")

# def hamaagui(name, age):
#     print(name , age)
# hamaagui("Zero", 10000000)


# def avg():
#     nums = list(map(int, input().split()))
#     return sum(nums) / len(nums)
# a = avg()
# print(a)

# def love(name= "Hun bish"):
#     print("i love you", name)
# love()

# def love(*name):
#     print(name)
# love (1,2,3,4,5)

# def love(**name):
#     print(name)
# love (name = "Amina", age = 20)

# task 1
# def  love():
#     a,b,c= map(int, input("input :").split())
#     return a + b + c
# n = love()
# print(n)

# task 2
# def love():
#     n,m = map(int, input("input :").split())
#     return  n + m
# a = love()
# print(a)

# task 3
# def love():
#     a = int(input())
#     return (a**3, (a **2) *6)
# a = love()
# print(a)

# task 4
# def a():
#     b, n = map(int, input().split())
#     return  (b+n)*2+4, b + b + n + n
# m = a()
# print(m)

# task 5
# def n():
#     a = int(input())
#     return 3 *a-5
# b = n()
# print(b)

# task 6
# def n():
#     a = int(input())
#     return  4 *(a**2) - 3 * a + 5
# b = n()
# print(b)

# task 7
# def n():
#     a = int(input())
#     return a  % 10
# b = n()
# print(b)

# task 8
# def n():
#     a = int(input())
#     return (a//10) % 10
# b = n()
# print(b)

# task 9
# def n():
#     a = int(input())
#     return (a// 10) *(a %10)
# b = n()
# print(b)

# task 10
# def n():
#     a = int(input())
#     zuut = a // 100
#     aravt = (a // 10) % 10
#     negj = a % 10
#     return zuut + aravt + negj
# b = n()
# print(b)

# task 1
# def hello(a):
#     print("Hell0", a)
# hello("Python !")

# task 2
# def greet(name):
#     n = input()
#     print("Sain baina uu,", n)
# greet("name")

# task 3
# def introduce(name, age):
#     print(name ,"ene", age, "nastai")
# introduce("Bat", 18)

# task 4
# def add(a,b):
#     n,m = map(int, input("input: ").split())
#     return n +m
# v = add("a", "b")
# print(v)

# task 5
# def square(num):
#     return num ** 2
# result = square(5)
# print(result)

# task 6
# def max_num(a, b):
#     return max (a, b)
# print(max_num(10,20))

# task 7
# def check_even(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# print(check_even(7))

# task 8
# def check_age(age):
#     if age >= 18:
#         return "adult"
#     else:
#         return "minor"
# a = check_age(20)
# print(a)

# task 9
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "c"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
# print(get_grade(46))

# task 10
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print_numbers(5)

# task 11
# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(sum_numbers(5))

# task 12
# def count_even(n):
#     count = 0
#     for i in range(1, n+ 1):
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(10))

# task 13
# def count_digits(num):
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count
# print(count_digits(123457))

# task 14
# def find_max(nums):
#     nums = [4,8,2,15,6]
#     max_num = nums[0]
#     for num in nums:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(find_max([4,8,2,15,6]))

# task 15 
# def find_min(nums):
#     nums = [7,3,9,1,5]
#     min_num = nums[0]
#     for num in nums:
#         if num < min_num:
#             min_num =num
#     return min_num
# print(find_min([7,3,9,1,5]))

# task 16 
# def count_even(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count
# print(count_even([1,2,4,7,8,10]))

# task 17  
# def list_sum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(list_sum([10,20,30,40]))

# task 18
# def get_age(students, name):
#     return students[name]
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print (get_age(students,"Sara"))

# task 19
# def find_student(students, name):
#     if name in students:
#         return "Found"
#     else:
#         return "Not found"
# student = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# n = input("ner oruul: ")
# print(find_student(student, n))

# task 20
# def avg_score(students):
#     total_score = sum(students.values())
#     count = len(students)
#     return total_score / count
# students = {
#     "Bat": 80,
#     "Sara": 90,
#     "Bold": 70
# }
# print(avg_score(students))

# task 21
# def unique_count(nums):
#     a = set(nums)
#     return len(a)
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(unique_count(nums))
    
# task 22
# def uniqui_numbers(nums):
#     a = set(nums)
#     return a
# nums = [1, 2, 2, 3, 3, 4]
# print(uniqui_numbers(nums))

# task 23
# def greet(nume= "Guest"):
#     print("Hello", nume)
# greet("Bat")    

# task 24
# def power(num, exponent = 2):
#     return num ** exponent
# print(power(5))
# print(power(2,3))

# task 25
# def discount(price , percent= 10):
#     a = price * percent / 100
#     return int(price - a)
# print(discount(10000))
# print(discount(10000,20))

# task 26
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(sum_all(1,2,3))
# print(sum_all(10,20,30,40))

# task 27
# def find_max(*args):
#     max_num = args[0]
#     for num in args:
#         if num > max_num:
#             max_num =num
#     return max_num
# print(find_max(5,8,2,10,3))

# task 28
# def count_even(*args):
#     count = 0
#     for num in args:
#         if num % 2 == 0:
#             count += 1
#     return count
# print(count_even(1,2,4,7,8,10))

# task 29
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# show_info(name=" Bat", age=18, city="Ulaanbaatar")

# task 30
# def calculate_total(**prices):
#     total = 0
#     for name, price in prices.items():
#         total += price
#     return total
# print(calculate_total(apple =2000, banana =3000, orange = 2500))

# task 31
# def analyze_numbers(nums):
#     if not nums:
#         return{}
#     max_num = nums[0]
#     min_num = nums[0]
#     total_sum = 0
#     even_count = 0
#     odd_count = 0
#     for num in nums:
#         total_sum += num
#         if num >max_num:
#             max_num = num
#         if num < min_num:
#             min_num = num
#         if num % 2 == 0:
#             even_count +=1
#         else:
#             odd_count += 1
#     result = {
#         "hamgiin ih too": max_num,
#         "hamgiin baga too": min_num,
#         "niilber": total_sum,
#         "tegsh too": even_count,
#         "sondgoi too": odd_count
#     }
#     return result
# nums = [3,8,2,7,10]
# print(analyze_numbers(nums))

# task 32
# def student_average(students, name):
#     return students[name][0]
# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(student_average(students, "Bat"))

# task 33
# def best_student(students):
#     best = None
#     max_avg = -1
#     for name, score in students.items():
#         a = sum(score) / len(score)
#         if a > max_avg:
#             max_avg = a
#             best = name
#     return(best, max_avg)
# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(best_student(students))

# task 34
# def calculate(*args, **kwargs):
#     a = sum(args)
#     bonus = 0
#     tax = 0
#     if "bonus" in kwargs:
#         bonus = kwargs["bonus"]
#     if "tax" in kwargs:
#         tax = kwargs["tax"]
#     b = a + bonus - tax
#     return b
# print(calculate(10, 20, 30, bonus=100, tax=20))


