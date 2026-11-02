############################### Quick sort ###############################
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) +mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) +mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) +mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers))

# task 5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) +mid + quick_sort(right) 
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers)[:3])

# task 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# print(quick_sort(numbers)[:2])

# task 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num[1] < pivot[1]:
#             left.append(num)
#         elif num[1] == pivot[1]:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
# students = [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]
# print(quick_sort(students))

# task 8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if len(num) < len(pivot):
#             left.append(num)
#         elif len(num) == len(pivot):
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
# bruits = input().split()
# print(quick_sort(bruits))

# task 9
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     mid = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             mid.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
# numbers = list(map(int, input().split()))
# a = quick_sort(numbers)
# n = len(a)
# if n % 2 == 1:
#     median = a[n // 2]
# else:
#     median = (a[n// 2]-1) + a[n // 2] / 2
# if median == int(median):
#       median = int(median)
# print(median)

#  task 10
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    mid = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)
    return quick_sort(left) + mid + quick_sort(right)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = a + b
print(quick_sort(n))