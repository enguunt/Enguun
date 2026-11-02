################## Davtlag ###############
# task 1
# n = int(input())
# if n > 0 and n % 2 == 0 :
#     print("Eyreg tegsh")
# elif n < 0 and n // 2 != 0:
#     print("sorog sondgoi")
# else:
#     n == 0
#     print("Teg")

# task 2
# score = int(input())
# if score < 0 or score > 100:
#     print("Buruu onoo")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# task 3
# on = int(input())
# if on % 4 == 0  and on % 100 != 0 or on % 400 == 0:
#     print("ondor jil")
# else:
#     print("Engiin jil")

# task 4
# a,b,c = map(int, input().split())
# if a + b <= c or a + c <= b and b + c <= a:
#     print("Gurvaljin uusehgui")
# elif a == b == c:
#     print("tegsh talt")
# elif a == b or b == c or a == c:
#     print("Adil hajuut")
# else:
#     print("Engiin")

# task 5
# km , hour = map(int, input().split())
# if km <= 2:
#     total = 3000
# else:
#     total = 3000 + (km - 2) * 1500
# if hour >= 22 or hour <= 5:
#     total += 2000
# print(total)

# task 6
# n = int(input())
# total = 0
# for i in range(2 ,n + 1 , 2):
#     total += i
# print(total)

# task 7
# n = int(input())
# total = 0
# while n > 0:
#     total += n % 10
#     n = n // 10
# print(total)

# task 8
# n = int(input())
# num = 0
# while n > 0:
#     total = n % 10
#     num = (num * 10) + total
#     n = n // 10
# print(num)

# task 9
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("PizBazz")
#     elif i % 3 == 0:
#         print("Piz")
#     elif i % 5 == 0:
#         print("Bazz")
#     else:
#         print(i)

# task 10
# secret = 37
# n = 0
# while True:
#     a = int(input())
#     n += 1
#     if a == secret:
#         print(f"Zow! {n} oroldlogoor")
#         break
#     elif a > secret:
#         print("ih bain")
#     else:
#         print("Baga bain")
#     if n == 5:
#         print("loss")
#         break

# task 11
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j , end=" ")
#     print()

# task 12
# n = int(input())
# for i in range(n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# task 13
# def find_pairs(arr,target):
#     n = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 n.append((arr[i], arr[j]))
#     return n
# arr = list(map(int, input().split()))
# target = int(input())
# print(find_pairs(arr,target))

# task 14
# def most_frequen(arr):
#     max_count = 0
#     num = arr[0]
#     for i in range(len(arr)):
#         c_count = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 c_count += 1
#         if c_count > max_count:
#             max_count = c_count
#             num = arr[j]
#     return num, max_count
# arr = list(map(int, input().split()))
# print(most_frequen(arr))

# task 15
# def row_col_sums(matrix):
#     row_sums = []
#     for row in matrix:
#         row_sums.append(sum(row))
#     num_cols = len(matrix[0])
#     col_sums = [0] * num_cols
#     for row in matrix:
#         for j in range(num_cols):
#             col_sums[j] += row[j]
#     return row_sums, col_sums
# n = [[1,2,3],[4,5,6],[7,8,9]]
# print(row_col_sums(n))

# task 16
# def remove_duplicates(arr):
#     n = []
#     for i in arr:
#         if i not in n:
#             n.append(i)
#     return n
# a = list(map(int, input().split()))
# print(remove_duplicates(a))

# task 17
# def word_count(text):
#     words = text.split()
#     count = {}
#     for word in words:
#         count[word] = count.get(word, 0) +1
#     return count
# a = input()
# print(word_count(a))

# task 18
# def averages(grades):
#     avg = {}
#     for name,score in grades.items():
#         avg[name] = sum(score) / len(score)
#         max_score = max(avg.values())
#         best_students = "" 
#         for name , score in avg.items():
#             if score == max_score:
#                 best_students = name
#                 break
#     return avg, best_students
# a=  {"Анар": [80, 90, 70], "Болд": [60, 75, 90], "Сараа": [95, 85, 90]}
# print(averages(a))

# task 19
# python = {"Anar", "Bold", "Saraa", "Dorj"}
# math = {"Bold", "Gerel", "Dorj"}
# both = python & math
# a_pyton = python - math
# b_math = math - python
# total = len(python | math)
# print(f"hoyulandan; {both}")
# print(f"zowhon pyhton ywdag: {a_pyton}")
# print(f"zowhon math yawdag suragch: {b_math}")
# print(f"Niit: {total}")

# task 20
# def fathest_point(points):
#     max_dist = -1
#     best_point = None
#     for point in points:
#         x, y = point
#         dista = x**2 + y**2
#         if dista > max_dist:
#             max_dist = dista
#             best_point = point
#     return best_point, max_dist
# a=  [(1, 2), (3, 4), (-1, 5), (0, 0)]
# print(fathest_point(a))

# task 21
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) +1):
#         if n % i == 0:
#             return False
#     return True
# def primes_up_to(n):
#     prime_list = []
#     for i in range(2, n +1):
#         if is_prime(i):
#             prime_list.append(i)
#     return prime_list
# n = int(input())
# print(primes_up_to(n))

# task 22
# def find_all(arr, x):
#     count = []
#     for i in range(len(arr)):
#         if arr[i] == x:
#             count.append(i)
#     return count
# l= list(map(int, input().split()))
# n = int(input())
# print(find_all(l,n))

# task 23
# def find_phone(book,name):
#     for i in book:
#         current_name, phone_number = i
#         if current_name == name:
#             return phone_number
#     return "Oldosngue"
# book = [("Анар", "99112233"), ("Болд", "88001122"), ("Сараа", "95553344")]
# n = input()
# print(find_phone(book, n))

# task 24
# def bs_steps(arr,x):
#     left = 0
#     right = len(arr) -1
#     count = 0
#     while left <= right:
#         count += 1
#         mid = (right + left) // 2
#         if arr[mid] == x:
#             return mid, count
#         elif arr[mid] < x:
#             left = mid +1
#         else:
#             right = mid -1
#     return -1, count
# arr = list(map(int, input().split()))
# n = int(input())
# print(bs_steps(arr,n))
            
#  task 25
# def search_insert(arr, x):
#     left = 0
#     right = len(arr) -1
#     while left <= right:
#         mid  = (left + right) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid -1
#     return left
# n = list(map(int, input().split()))
# x = int(input())
# print(search_insert(n,x))

# task 26
# def bubble_sort(arr):
#     n = len(arr)
#     swap = 0
#     for i in range(n -1):
#         swapped = False
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1] , arr[j]
#                 swap +=1
#                 swapped = True
#         if not swapped:
#             break
#     return arr, swap
# arr = list(map(int, input().split()))
# print(bubble_sort(arr))

# task 27
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         min_idx  = i
#         for j in range(i+1, n):
#             if arr[j] <= arr[min_idx]:
#                 min_idx = j
#                 arr[i], arr[min_idx] = arr[min_idx] , arr[i]
#         print(f"{i+1}-r alham: {arr}")
#     return arr
# a = list(map(int, input().split()))
# print(selection_sort(a))

# task 28
# def merg_sort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = sort_unique(left)
#     right = sort_unique(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# def sort_unique(arr):
#     if not arr:
#         return []
#     sorted_arr = merg_sort(arr)
#     unique_arr = [sorted_arr[0]]
#     for x in sorted_arr[1:]:
#         if x != unique_arr[-1]:
#             unique_arr.append(x)
#     return unique_arr
# arr = list(map(int, input().split()))
# print(sort_unique(arr))

# task 29
# def top_three(scores):
#     tuple = []
#     for name, score in scores.items():
#         tuple.append((score, name))
#     tuple.sort(reverse=True)
#     result = []
#     for i in range(3):
#         result.append(tuple[i][1])
#     return result
# scores = {"Анар": 85, "Болд": 92, "Сараа": 78, "Дорж": 88, "Гэрэл": 95}
# print(top_three(scores))

# task 30
# n = int(input())
# scores = []
# for _ in range(n):
#     scores.append(int(input()))
# a = sorted(scores)
# max_score = max(scores)
# min_score = min(scores)
# avg_score = sum(scores) / n
# avg_count = 0
# for score in scores:
#     if score > avg_score:
#         avg_count += 1
# print(f"Erembelse: {a}")
# print(f"hamgiin ih: {max_score}")
# print(f"hamgiin baga: {min_score}")
# print(f"dundaj onoo: {avg_score}")
# print(f"dundajaas deesh onoo: {avg_count}")


