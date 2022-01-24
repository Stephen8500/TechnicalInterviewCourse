# array = [1,3,5,9,10,20,22,90,91]

def search(array, n):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        mid = (lower + upper)//2

        if array[mid] == n:
            return mid
        elif array[mid] < n:
            lower = mid + 1
        else:
            upper = mid - 1
    return 'Not found'

# print(search(array, 5))

# array = [6,7,2,3,4,5]
# array = [4,5,6,7,2,3]
# # output 7

def search(arr):
    lower = 0
    upper = len(arr) - 1
    
    
    while lower <= upper:
        mid = (lower+upper)//2
        if mid == (len(arr) -1):
            return arr[mid]
        elif arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[upper]:
            lower = mid + 1
        else:
            upper = mid - 1

# print(search(array))

def multiplyAllOthers(arr):
    arrProducts = []
    for i in arr:
        newProduct = 1
        for j in arr:
            if i != j:
                newProduct = newProduct * j
        arrProducts.append(newProduct)
    return arrProducts

array = [1,2,3,4]

#print(multiplyAllOthers(array))
