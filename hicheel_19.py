######################### merge sort #################################
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

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

# numbers = [8, 3, 5, 4, 7, 6, 1, 2]

# print(merge_sort(numbers))

# task 1
# def merg_sort(number):
#     if len(number) <=1:
#         return number
#     mid = len(number) // 2
#     left = number[:mid]
#     right = number[mid:]
#     left = merg_sort(left)
#     right = merg_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i +=1
#         else:
#             result.append(right[j])
#             j +=1
#     while i < len(left):
#         result.append(left[i])
#         i +=1
#     while j < len(right):
#         result.append(right[j])
#         j +=1
#     return result
# number = list(map(int, input().split()))
# print(merg_sort(number))

# task 2
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i +=1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# arr = list(map(int, input().split()))
# print(merge_sort(arr))

# task 3
# def merg_sort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merg_sort(left)
#     right = merg_sort(right)
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
#         i +=1
#     while j < len(right):
#         result.append(right[j])
#         j +=1
#     return result
# arr = list(map(int, input().split()))
# print(merg_sort(arr))

# task 4
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
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
# arr = list(map(int, input().split()))
# print(merge_sort(arr))

# task 5
# def even_odd(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = even_odd(left)
#     right = even_odd(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if (left[i] // 2 == right[j] // 2):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(result[j])
#                 j += 1
#         else:
#             if left[i] // 2 == 0:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# arr = list(map(int, input().split()))
# print(even_odd(arr))

# task 6
# def merge(a,b):
#     result = []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     while i < len(a):
#         result.append(a[i])
#         i += 1
#     while j < len(b):
#         result.append(b[j])
#         j += 1
#     return result
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(merge(a,b))

# task 7
# def smallest_three(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = smallest_three(left)
#     right = smallest_three(right)
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
# arr = list(map(int, input().split()))
# print(smallest_three(arr)[:3])

# task 8
# def merg_sort(arr):
#     if len(arr) <= 1:
#         return arr, 0,0
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left, left_comp, left_merg = merg_sort(left)
#     right , right_comp, right_merg= merg_sort(right)
#     result = []
#     i = 0
#     j = 0
#     harstia = 0
#     while i < len(left) and j < len(right):
#         harstia += 1
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j +=1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     total_comp = left_comp + right_comp + harstia
#     total_merg =  left_merg + right_merg + 1
#     return result, total_comp, total_merg
# arr = list(map(int, input().split()))
# res1,comp1,m1 = merg_sort(arr)
# print(f"erembelse: {res1}")
# print(f"haritsuulalt: {comp1}")
# print(f"merge: {m1}")

# task 9
# def smallest_three(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = smallest_three(left)
#     right = smallest_three(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
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
# arr = list(map(int, input().split()))
# print(smallest_three(arr)[:2])

# task 10
# def merge_sort(name):
#     if len(name) <=1 :
#         return name
#     mid = len(name) // 2
#     left = name[:mid]
#     right = name[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j +=1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# name = input().split()
# print(merge_sort(name))

# task 11
# def sort_students(students):
#     if len(students) <=1:
#         return students
#     mid = len(students) // 2
#     left = students[:mid]
#     right = students[mid:]
#     left = sort_students(left)
#     right = sort_students(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i][1] != right[j][1]:
#             if left[i][1] > right[j][1]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         else:
#             if left[i][0] <= right[j][0]:
#                 result.append(left[i])
#                 i +=1
#             else:
#                 result.append(right[j])
#                 j += 1
#     while i < len(left):
#         result.append(left[i])
#         i +=1
#     while j < len(right):
#         result.append(right[j])
#         j +=1
#     return result
# students = [("Анар", 85), ("Дорж", 92), ("Сараа", 78), ("Болд", 92), ("Гэрэл", 88)]
# print(sort_students(students))

# task 12
# def sort_words(words):
#     if len(words) <= 1:
#         return words
#     mid = len(words) // 2
#     left = words[:mid]
#     right = words[mid:]
#     left = sort_words(left)
#     right = sort_words(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if (len(left[i])) < (len(right[j])) or (len(left[i])) == (len(right[j])) and (len(left[i])) <= (len(right[j])):
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
# words= input().split()
# print(sort_words(words))

# task 13
# def binary_search(air, target):
#     def merge_sert(arr):
#         if len(arr) <= 1:
#             return arr
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#         left = merge_sert(left)
#         right = merge_sert(right)
#         result = []
#         i = 0
#         j = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         while i < len(left):
#             result.append(left[i])
#             i += 1
#         while j < len(right):
#             result.append(right[j])
#             j += 1
#         return result
#     sorted_arr = merge_sert(air)
#     print("erembelse: ",sorted_arr)
#     left = 0
#     right = len(sorted_arr) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if sorted_arr[mid] == target:
#             return mid
#         elif sorted_arr[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid -1
#     return -1
# arr1 = list(map(int, input().split()))
# target = int(input())
# print(binary_search(arr1,target))
    
# 1. Python list ашиглан хийсэн stack-д хэдэн элемент байгааг аль нь буцаах вэ?
# A) len(stack)

# 2. Дараах код юу хэвлэх вэ? (Хэвлэсэн мөр бүрийг / тэмдгээр тусгаарлав.)
# s = []
# s.append("A")
# s.append("B")
# s.append("C")
# print(s.pop())
# print(s.pop())
# print(len(s))
# B) C / B / 1

# 3. Дараах код юу хэвлэх вэ? (Хэвлэсэн мөр бүрийг / тэмдгээр тусгаарлав.)
# def peek(stack):
#     if len(stack) == 0:
#         return None
#     return stack[-1]
# print(peek([]))
# print(peek([4, 9]))
# D) None / 9

# 4. Хоосон stack дээр дараах үйлдлүүдийг хийв. Төгсгөлд stack ямар харагдах вэ?
# push(2) → push(4) → push(6) → pop() → pop() → push(8)
# C) [2, 8]

# 5. Stack-д [1, 2, 3, 4] байна (4 нь орой). Хоёр удаа pop хийж, гарсан элементүүдийг гарсан дарааллаар нь шинэ list-д append хийв. Шинэ list ямар болох вэ?
# D) [4, 3]

# 6. Stack-аас pop() хийхээсээ өмнө юуг заавал шалгах ёстой вэ?
# A) Stack хоосон эсэхийг

# II хэсэг: Queue
# 7. deque гэдэг нь юуны товчлол вэ?
# A) delete queue — устгадаг дараалал

# 8. Дараах код юу хэвлэх вэ?
# from collections import deque
# q = deque([10, 20, 30])
# q.append(40)
# q.popleft()
# q.popleft()
# print(len(q), q[0])
# C) 2 30

# 9. Дараах код юу хэвлэх вэ?
# queue = ["Бат", "Сараа", "Төмөр"]
# first = queue.pop(0)
# queue.append(first)
# print(queue)
# B) ['Сараа', 'Төмөр', 'Бат']

# 10. 50 000 элементтэй list-ээс pop(0) хийхэд үлдсэн элементүүд нийт хэдэн удаа шилжих вэ?
# D) 49 999

# 11. Дараах код ажилласны дараа len(printer) хэд байх вэ?
# from collections import deque
# printer = deque()
# printer.append("homework.pdf")
# printer.append("photo.png")
# printer.append("report.docx")
# while len(printer) > 0:
#     doc = printer.popleft()
#     print("Хэвлэж байна:", doc)
# B) 3

# 12. Аль нөхцөлд queue ашиглах нь тохиромжтой вэ?
# D) Чатад мессежүүдийг илгээсэн дарааллаар нь хүргэх

# III хэсэг: Харьцуулалт ба хурд
# 13. Stack болон queue тус бүр хэдэн үзүүртэй вэ?
# C) Stack: 1, Queue: 2

# 14. Элементийн тоо маш их үед аль эрэмбэ нь хурдан → удаан дарааллаар зөв байрласан бэ?
# B) O(1), O(log n), O(n)

# 15. «Халуун төмс» тоглоомд төмсийг нэг хүнээр дамжуулах буюу урд талын хүнийг дарааллын ард шилжүүлэх үйлдлийг аль код илэрхийлэх вэ?
# D) q.append(q.popleft())

# 16. hot_potato(["Ану", "Баяр", "Гана", "Дулам"], 3) гэж дуудав. Төмс 3 дахь хүн дээр очих бүрт тэр хүн хасагдана. Хэн ялах вэ?
# A) Ану

# 17. to_binary(n) функцэд n == 0 үед "0" гэж тусад нь буцаадаг. Ийм шалгалт хийхгүй бол to_binary(0) юу буцаах вэ?
# C) Хоосон мөр ""

# 18. is_balanced(")(") яагаад False буцаадаг вэ?
# B) Эхний ) ирэхэд stack хоосон байсан учраас

# 19. is_palindrome(word) функц том, жижиг үсгийг ялгахгүйгээр үгийг stack болон queue ашиглан шалгадаг. Аль үг True буцаах вэ?
# C) "Noon"

# 20. Хоёр stack-ээр queue хийхэд outbox`-д элемент байсаар байхад `inbox`-ийн элементүүдийг `outbox руу шилжүүлбэл юу болох вэ?
# A) FIFO дараалал алдагдаж, шинэ элементүүд хуучнаасаа өмнө гарна
