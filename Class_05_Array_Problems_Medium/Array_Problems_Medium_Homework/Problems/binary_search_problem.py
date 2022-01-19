# # Search an array of numbers to find a target number using binary search.
# # The function should return the index of the target number if the target number is found
# # or a -1 if the target is not found in the array.

# input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
# input_target = 5
# # Output = 2

# def binary_search(myArray, n):
#     lower = 0
#     upper = len(myArray) - 1

#     while lower <= upper:
#         mid = (lower + upper)//2
        
#         if myArray[mid] == n:
#             return mid
#         else:
#             if myArray[mid] < n:
#                 lower = mid + 1
#             else:
#                 upper = mid - 1

#     return -1

# print(binary_search(input_array, input_target))


# array = [0,1,2,3,4,5,6,7,9,10,20,65,85,99,103,109,200,290,300,9000,10000,35353535,515151515154535]
# target = 8

# def search(array, n):
#     l = 0
#     u = len(array) -1

#     while l <= u:
#         mid = (l+u)//2
        
#         if array[mid] == n:
#             return mid
#         elif array[mid] < n:
#             l = mid + 1
#         else:
#             u = mid - 1
        
#     return 'Not found'

# print(search(array, target))

# def binarySearch(nums, n):
#     l = 0
#     u = len(nums) - 1

#     while l <= u:
#         mid = (l+u)//2

#         if nums[mid] == n:
#             return mid
#         elif nums[mid] < n:
#             l = mid + 1
#         else:
#             u = mid - 1

#     return 'Not found'

# print(binarySearch(array, target))

array = [1,2,3,4,5,6,7,9,10,12,20,26,92,400,900,933,20000,505050,90000000]
n = 20000

def search(array, n):
    l = 0
    u = len(array) - 1

    while l <= u:
        mid = (l+u)//2

        if array[mid] == n:
            return mid
        elif array[mid] > n:
            u = mid - 1
        else:
            l = mid + 1
    return "not found"

print(search(array, 1))























