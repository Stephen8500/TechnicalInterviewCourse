# def majorElem(arr):
#     dictCheck = {}
#     for i in arr:
#         if i in dictCheck.keys():
#             dictCheck[i] += 1
#         else:
#             dictCheck[i] = 1
    
#     maxCount = 0
#     majElem = 0

#     for i in dictCheck:
#         if dictCheck[i] > maxCount:
#             maxCount = dictCheck[i]
#             majElem = i
    
#     return majElem

# arr = [3,2,3]

# print(majorElem(arr))

# arr = [2,2,1,1,1,2,2]

# print(majorElem(arr))


# def twoSum(arr, targ):
#     myDict = {}

#     for i in arr:
#         myDict[i] = arr.index(i)
    
#     for i in arr:
#         if (targ - i) in myDict.keys():
#             keyValue = targ - i
#             returnList = [arr.index(i), myDict[keyValue]]
#             return returnList

# print(twoSum([2,7,11,15], 9))


def uncomWords(s, t):
    listS = s.split(' ')
    listT = t.split(' ')

    myDict = {1: [], 2:[]}

    for i in listS:
        if i in myDict[1]:
            myDict[1].pop(myDict[1].index(i))
            myDict[2].append(i)
        else:
            myDict[1].append(i)
    
    for i in listT:
        if i in myDict[1]:
            myDict[1].pop(myDict[1].index(i))
            myDict[2].append(i)
        else:
            myDict[1].append(i)

    return myDict[1]


print(uncomWords('this apple is sweet', 'this apple is sour'))