# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

# brute force option to find best increase
def bruteForceIncrease(input_array):
    best_increase = 0

    for i in range(len(input_array)):
        for j in range(len(input_array)):
            if (j > i) and input_array[j] - input_array[i] > best_increase:
                best_increase = input_array[j] - input_array[i]

    return best_increase

print(bruteForceIncrease(input_array))

# optimized findIncrease:
def findBestIncrease(input_array):
    size = 0
    minNum = input_array[0]

    for i in input_array:
        if i < minNum:
            minNum = i
        if i - minNum > size:
            size = i - minNum
    
    return size

print(findBestIncrease(input_array))