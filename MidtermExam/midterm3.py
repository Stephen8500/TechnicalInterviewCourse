# Given a n x m binary matrix image, flip the image horizontally, then invert it, then return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].
# Examples:

Input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
Output = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
# Explanation:
# First reverse each row: [[0, 1, 1], [1, 0, 1], [0, 0, 0]]
# Then invert the image: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

def crazyFunction(arr):
    for i in range(0, len(arr)):
        arr[i].reverse()
        for j in range(0, len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    
    return arr

print(crazyFunction(Input))