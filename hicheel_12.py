####################################        listed dotor list          #######################################
# m = [[1,2,3], [4,5,6],[7,8,9],[10,11,100],[12,13,50,-1]]
# for i in range(0,len((m))):
#     for o in m[i]:
#         print(o,end=" ")

# task 1
# nums = [
#     [1,2,3],
#     [4,5,6]
# ]
# print(nums[1][2])

# task 2
# students = [
#     ["Bat", 18],
#     ["Sara",19],
#     ["Bold",20]
# ]
# print(students[2][0])

# task 3
# nums = [
#     [10,20],
#     [30,40],
#     [50,60]
# ]
# print(nums[1])

# task 4
# nums = [
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# print(nums [2][0])

# task 5
# nums = [
#     [5,10],
#     [15,20]
# ]
# print(nums[0][0])

# task 6
# nums = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# print(nums[2][1])

# task 7
# nums = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# for i in range(0,len(nums)):
#     for o in [i]:
#         print(nums[o])

# task 8
# nums = [
#     [1,2,3],
#     [4,5,6]
# ]
# for i in range(0, len(nums)):
#     for o in nums[i]:
#         print(o)

# task 9
# nums = [
#     [1,2,3],
#     [4,5,6]
# ]
# for i in range(0,len(nums)):
#     for o in nums[i]:
#         print(o,end=" ")

# task 10
# nums = [
#     [3,12,5],
#     [20,7,15]
# ]
# for i in range(0,len(nums)):
#     for o in nums[i]:
#         if  o > 10:
#             print(o) 

# task 11
# nums = [
#     [1,2],
#     [3,4,5],
#     [6]
# ]
# total = len(sum(nums, []))
# print(total)

# task 12
# nums = [
#     [1,2,3],
#     [4,5,6]
# ]
# total =  0
# for i in nums:
#     for j in i:
#         total += j
#         print(total)

# task 13
# nums = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(0,len(nums)):
#     for j in nums[i]:
#         if j % 2==0:
#             print(j, end=" ")

# task 14
# nums = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(0,len(nums)):
#     for j in nums[i]:
#         if j % 2 !=0:
#             print(j, end=" ")

# task 15
# nums = [
#     [1,2,3],
#     [4,5,6],
#     [7,8]
# ]
# total = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2==0:
#             total += j
# print(total)
            
# task 16
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j > 0:
#             print(j)
                
# task 17
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# total = 0
# for i in range(0 , len(nums)):
#     for j in nums[i]:
#         if j < 0:
#             total += j
# print(total)

# task 18
# a = []
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# for i in nums:
#     for j in i:
#         a.append(j)
# print(max(a))

# task 19
# a = []
# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]
# for i in nums:
#     for j in i:
#         a.append(j)
# print(min(a))

# task 20
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums:
#     print(sum(i))

# task 21
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     print(max(i))

# task 22
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     print(min(i))

# task 23
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# found = False
# for i in nums:
#     if 7 in i:
#         found = True
#         break
# if found:
#     print("yes")
# else:
#     print("no")

# task 24
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]
# target = 2
# a = 0
# for i in nums:
#     for j in i:
#         if j == target:
#             a += 1
# print(a)

# task 25
# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]
# total = 0
# for i in nums:
#     for j in i:
#         if j > 5:
#             total +=j
# print(total)
    
# task 26
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]
# max_row = []
# max_sum = 0
# for row in nums:
#     s = 0
#     for x in row:
#         s += x
#     if s > max_sum:
#         max_sum = s
#         max_row = row
# print(max_row)

# task 27
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# for i in students:
#    print(i[0],i[1])

# task 28
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]
# for i in students:
#     if i[1] >18:
#         print(i[0])

# task 29
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ]
# for i in students:
#     a = (i[1] + i[2] + i[3]) /3
#     print(i[0],a)

# task 30
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80],
#     ["Anu", 90, 90, 90]
# ]
# max = 0
# b = ""
# for i in students:
#      a = (i[1] + i[2] + i[3]) /3
#      if a > max:
#           max = a
#           b = i[0]
# print(b, max)



