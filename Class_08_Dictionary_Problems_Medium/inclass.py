# in class stuff for dictionary medium day
# tups = [("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]

# def convertDict(tups):
#     dict1 = {t[0]:t[1] for t in tups}
#     return dict1

# print(convertDict(tups))

# test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}

# def reverseKey(myDict):
#     newDict = {}
#     for k,v in reversed(myDict.items()):
#         newDict[k] = v
#     return newDict

# def reverseOptimize(myDict):
#     return {k:v for k,v in reversed(myDict.items())}

# print(reverseOptimize(test_dict))

# test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
#              'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
#              'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

# def sortByValues(myDict):
#     return {k:dict(sorted(v.items(),key= lambda kv:kv[1])) for k,v in myDict.items()}

# print(sortByValues(test_dict))

test_dict = {'Manjeet' : [1, 4, 5, 6],
			'Akash' : [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

def removeDupVals(myDict):
    totalDict = {}
    for v in myDict.values():
        for i in v:
            totalDict[v[i]] = 1
    
    for v in myDict.values():
        for i in v:
            if v[i] in totalDict.keys():
                v.pop(v.index(i))
    
    return myDict

print(removeDupVals(test_dict))