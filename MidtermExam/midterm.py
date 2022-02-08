# Given a dictionary, sort the keys by the sum of their values in descending order. Return an array with the sorted pairs.

# Example:
old_dict = { 'A' : [1, 2, 3], 'B' : [1, 7, 3], 'C' : [100, 3, 7], 'D' : [6, 50, 4]}
# output = [['C', 110], ['D', 60], ['B', 11], ['A', 6]]

def sort_dict(myDict):
    arr = []

    dictSums = {}

    for i in myDict.keys():
        sum = 0
        for j in range(0, len(myDict[i])):
            sum += myDict[i][j]
        arr.append([i, sum]) 

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][1] < arr[j][1]:
                holdingVar = arr[i]
                arr[i] = arr[j]
                arr[j] = holdingVar
            
    return arr

print(sort_dict(old_dict))