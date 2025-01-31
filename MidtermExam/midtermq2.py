# Write a function that calculates the sum of an array of numbers using recursion. You must use recursion to gain full credit for this question.

# Example:
input = [3,6,2,9,9,4]
# output = 33

def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        sumArr = arr.pop() + recursive_sum(arr)

    return sumArr

print(recursive_sum(input))