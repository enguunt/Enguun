######################  selection sort #################
# numbers = [5, 3 , 8, 1,2]
# for i in range(len(numbers) -1):
#     min_index = i
#     for j in range(i + 1, len(numbers)):
#         if  numbers[j] <  numbers[min_index]:
#             min_index = j
#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp
#     print(numbers)

# task 1
# arr = list(map(int, input().split()))
# for i in range(len(arr) -1):
#     min_index = i
#     for j in range(i +1 ,len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)

# task 2
# arr = list(map(int , input().split()))
# for i in range(3):
#     min_index = i
#     for j in range(i + 1,len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr[:3])

# task 3
# arr = list(map(int, input().split()))
# for i in range(len(arr) -1):
#     min_index = i
#     for j in range(i+ 1, len(arr)):
#         if arr[j] > arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)

# task 4
# arr = list(map(int, input().split()))
# for i in range(len(arr) -1):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)

# task 5
# count = list(map(int, input().split()))
# arr = list(set(count))
# for i in range(len(arr) -1):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)

# task 6
# arr = list(map(int, input().split()))
# min_index = 0
# for i in range(len(arr)):
#     if arr[i] < arr[min_index]:
#         min_index = i
# temp = arr[0]
# arr[0] = arr[min_index]
# arr[min_index] = temp
# print(arr)

# task 7
# arr = list(map(int, input().split()))
# min_index = 0
# for i in range(len(arr)):
#     min_index = i
#     if arr[i] < arr[min_index]:
#         min_index = i
# temp = arr[0]
# arr[0] = arr[min_index]
# arr[min_index] = temp
# print(arr)

# task 8
# arr = list(map(int, input().split()))
# for i in range(2):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)

# task 9
# arr = list(map(int, input().split()))
# count = 0
# for i in range(len(arr) -1):
#     min_index = i
#     count +=1
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr, count)

# task 10
# a = list(map(int, input().split()))
# b =list(map(int, input().split()))
# c = list(map(int, input().split()))
# for name,arr in ['a', a], ['b', b], ['c', c]:
#     if arr == sorted(arr):
#         print(name)

# task 11
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         min_index = i
#         for j in range(i +1,n):
#            if arr[j] < arr[min_index]:
#                min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# number = list(map(int,input().split()))
# print(selection_sort(number))

# task 12
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         min_index = i
#         for j in range(i +1,n):
#            if arr[j] > arr[min_index]:
#                min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# number = list(map(int,input().split()))
# print(selection_sort(number))

# task 13
# arr = list(map(int, input().split()))
# for i in range(len(arr)-1):
#     min_index = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(min_index)

# task 14
# arr = list(map(int, input().split()))
# for i in range(len(arr) -1):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
#     print(arr)

# task 15
# arr = list(map(int, input().split()))
# selection = list(map(int, input().split()))
# n = len(arr)
# for i in range(n -1):
#     for j in range(n -1 -i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1] , arr[j]
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if selection[j] < selection[min_index]:
#             min_index = j
#     selection[i], selection[min_index] = selection[min_index] , selection[i]
# a = arr == selection
# print(f"bubble sort: {arr}" )
# print(f"selection sort: {selection}")
# print(f"hoyulangiin ur haritsuulsan ur dun: {a}")
