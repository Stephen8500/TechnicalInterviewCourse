# myList = [0,1,3,'a', 'b', 'c']

# def bopIt(myArray) :
#     for i in range(int(len(myArray)/2)):
#         holdingVar = myArray[i]
#         myArray[i] = myArray[len(myArray) - (i + 1)]
#         myArray[len(myArray) - (i + 1)] = holdingVar
#     return myArray

# print(bopIt(myList))

myList = [0,-1,-2,5,2,-7,6]

# output: 0526-1-2-7

def badVibes(myArray):
    counter = len(myArray)
    i = 0
    
    #while loop
    while (i < counter):
        if myArray[i] < 0 :
            myArray.append(myArray.pop(i))
            counter -= 1
        i += 1
    
    return myArray
print(badVibes(myList))