# Write a function that finds common elements in three sorted arrays

input_array_1 = [1, 5, 10, 20, 40, 80]
input_array_2 = [6, 7, 20, 80, 100]
input_array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output = 20, 80

def common_el(arr1, arr2, arr3):
    while len(arr1) > 0:
        num = arr1.pop()
        if num in arr2 and num in arr3:
           return num
    return False

print(common_el(input_array_1, input_array_2, input_array_3))
