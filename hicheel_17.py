############################ buble sort() ###############################
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# numbers = list(map(int, input().split()))
# print(bubble_sort(numbers))

# task 1
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble_sort(number))

# task 2
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] < arr[j + 1]:
#                 arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble_sort(number))

# task 3
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range( n -1 -i):
#             if arr[j] > arr[j+ 1]:
#                 arr[j], arr[j + 1] = arr[j+ 1] , arr[j]  
#     return arr
# number = list(map(int,input().split()))
# print(bubble_sort(number))

# task 4
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble_sort(number))

# task 5
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j +1 ] = arr[j + 1], arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble_sort(number))        

# task 6
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j +1] = arr[j + 1], arr[j]
#     return arr
# name = input().split()
# print(bubble_sort(name))

# task 7
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+ 1] = arr[j + 1], arr[j]
#     return arr
# score = list(map(int, input().split()))
# print(bubble(score))

# task 8
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         if arr[i] > arr[ i+ 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr
# number = list(map(int, input().split()))
# print(bubble(number))

# task 9
# def bubble(arr):
#     n = len(arr)
#     out_loops = 0
#     for i in range(n -1):
#         if i < n -1:
#             out_loops +=1
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr,out_loops
# number = list(map(int, input().split()))
# print(bubble(number))

# task 10
# def bubble(arr):
#     n = len(arr)
#     swap_count = 0
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swap_count += 1
#     return arr, swap_count
# number = list(map(int, input().split()))
# print(bubble(number))

# task 11
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr, arr[1]
# number = list(map(int, input().split()))
# print(bubble(number))

# task 12
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j] , arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble(number))

# task 13
# def bubble(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 count +=1 
#     return arr, count
# number = list(map(int, input().split()))
# print(bubble(number))

# task 14
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         swapped = False
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j] ,arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# number = list(map(int, input().split()))
# print(bubble(number))

# task 15
# def bubble(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j] , arr[j + 1] = arr[j + 1], arr[j]
#                 count += 1
#     return arr, count
# number = list(map(int, input().split()))
# print(bubble(number))

# task 16
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1] , arr[j]
#     return arr
# students = [
#     ["Bat", 75],
#     ["Saraa", 92],
#     ["Anu", 60],
#     ["Bold", 88]
# ]
# print(bubble(students))

# task 17
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j][1] > arr[j + 1][1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     youngest = arr[0][0]
#     oldest = arr[-1][0]
#     return arr, youngest,oldest
# people = [
#     ["Bat", 19],
#     ["Anu", 17],
#     ["Bold", 21],
#     ["Saraa", 18]
# ]
# print(bubble(people))

# task 18
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j] , arr[j+ 1] = arr[j + 1], arr[j]
#     count = 0
#     for num in arr:
#        if  num == 4:
#            count +=1 
#     return arr , count
# numbers = list(map(int, input().split()))
# print(bubble(numbers))

# task 19
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     for i in range(3):
#         print(f"{arr[i][0]}: {arr[i][1]}")
# products = [
#     ["Mouse", 25000],
#     ["Keyboard", 65000],
#     ["USB", 12000],
#     ["Headphone", 80000]
# ]
# bubble(products)

# task 20
# def bubble(arr):
#     n = len(arr)
#     haritsuulalt = 0
#     change = 0
#     total = 0
#     for i in range(n -1 ):
#         swap = False
#         total +=1
#         for j in range(n -1 -i):
#             haritsuulalt +=1
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 change +=1
#                 swap = True
#         if not  swap:
#             break
#     print(f"niit haritsuulalt: {haritsuulalt}")
#     print(f"niit sololitsson too: {change}")
#     print(f"gadna taliin niit toirog: {total}")
#     print(f"{arr}")
# number = list(map(int,input().split()))
# bubble(number)

# task 21
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# number = list(map(int, input().split()))
# print(bubble(number))

# task 22
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if len(arr[j]) > len(arr[j + 1]): 
#                 arr[j], arr[j + 1] = arr[j +  1], arr[j]
#     return arr
# words = input().split()
# print(bubble(words))

# task 23
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1 ,0,-1):
#         if arr[i] < arr[i - 1]:
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]
#     return arr
# numbers = list(map(int, input().split()))
# print(bubble(numbers))

# task 24
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return(arr)
# number = list(map(int,input().split()))
# print(bubble(number))

# task 25
# def bubble(list1 , list2):
#     n = list1 + list2
#     c = len(n)
#     for i in range(c -1):
#         for j in range(c -1 -i):
#             if n[j] > n[j + 1]:
#                 n[j], n[j + 1] = n[j + 1], n[j]
#     return n
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(bubble(a,b))

# task 26
# def bubble(arr):
#     n = len(arr)
#     count = 0
#     for i in range
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 count +=1
#                 round +=1
#                 print(f"{i + 1} - toirgiin daraa{round}")
                
#     return arr, count
# number = list(map(int, input().split()))
# print(bubble(number))

# task 27
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr[2]
# numbers = list(map(int, input().split()))
# print(bubble(numbers))

# task 28
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for(n -1):
#         round = 0 j in range(n -1 -i):
#             if arr[j][1] < arr[j + 1][1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# students = [
#     ["Bat", 85],
#     ["Anu", 92],
#     ["Bold", 85],
#     ["Saraa", 70],
#     ["Temuulen", 92]
# ]
# print(bubble(students))

# task 29
# def bubble(arr):
#     n = len(arr)
#     count = 0
#     total =0
#     round = False
#     for i in range(n -1):
#         swap = 0
#         for j in range(n -1 -i):
#             count +=1
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 total +=1
#                 swap +=1
#         if i == 0 and swap > 0:
#             round = True
#     print(f"niit haritsoolalt: {count}")
#     print(f"niit soliltsoo: {total}")
#     no = "tiim" if not round else "ugui"
#     print(f"soliltsoo hiigdeegui: {no}")
#     return arr
# numbers = list(map(int, input().split()))
# print(bubble(numbers))

# task 30
def bubble(arr):
    n = len(arr)
    for i in range(n -1):
        for j in range(n -1 -i):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j +1] = arr[j+ 1], arr[j]
            elif arr[j][1] == arr[j + 1][2]:
                if arr[j][2] > arr[j + 1][2]:
                     arr[j] , arr[j + 1] = arr[j + 1], arr[j + 1]                
    return arr
products = [
    ["Mouse", 25000, 12],
    ["Keyboard", 65000, 5],
    ["USB", 12000, 20],
    ["Headphone", 65000, 8],
    ["Webcam", 40000, 3]
]
print(bubble(products))