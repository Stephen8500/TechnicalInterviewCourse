# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 3, 4]
# Output = True
# brute force duplicate finding
def bruteForceDuplicates(input_array):
    boolDuplicates = False
    for i in input_array:
        for j in input_array:
            if i == j:
                boolDuplicates = True

    return boolDuplicates
print(bruteForceDuplicates(input_array))

# optimized solution:
def duplicateCheck(input_array):
    lenArray = len(input_array)
    for i in range(lenArray):
        test = input_array.pop(0)
        if test in input_array:
            return True
    return False

print(duplicateCheck(input_array))