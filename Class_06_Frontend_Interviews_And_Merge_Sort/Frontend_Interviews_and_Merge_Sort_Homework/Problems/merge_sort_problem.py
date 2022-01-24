# Write a merge sort algorithm to sort an array. 
# The function should return the sorted array.

# two examples


from re import L


array1 = [45, 98, 3, 24, 15, 77, 9, 50] # output: [3, 9, 15, 24, 45, 50, 77, 98]
array2 = [18, 16, 27, 4, 12] # output: [4, 12, 16, 18, 27]

# def merge_sort(list):
#     if len(list) > 1:
#         mid = len(list)//2
#         l = list[:mid]
#         r = list[mid:]
#         merge_sort(l)
#         merge_sort(r)
#         i = j = k = 0

#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 list[k] = l[i]
#                 i += 1
#             else:
#                 list[k] = r[j]
#                 j += 1
#             k += 1

#         while i < len(l):
#             list[k] = l[i]
#             i+=1
#             k+=1
        
#         while j < len(r):
#             list[k] = r[j]
#             j+=1
#             k+=1

#     return list

# function to return merge-sorted list
def merge_sort(list):
    # check that list is more than one value
    if len(list) > 1:
        # find middle index of list
        middle = len(list)//2
        # separate into two halves
        left = list[:middle]
        right = list[middle:]
        # recursive function call until length of each list is 1, then merge them back together as sorted lists
        merge_sort(left)
        merge_sort(right)
        
        # initialize i, j, and k counters
        i = j = k = 0

        # loop for finding smallest value and inserting it into current list in order
        while i < len(left) and j < len(right):
            # check for smaller value between two arrays and add it to list
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        # check that no values are left in either half
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


    return list

    
print(merge_sort(array1))
print(merge_sort(array2))
