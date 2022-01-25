input1 = [3,2,3]

input2 = [2,2,1,1,1,2,2]

def mergeSort(list):
    if len(list) > 1:
        m = len(list)//2
        l = list[:m]
        r = list[m:]
        mergeSort(l)
        mergeSort(r)
        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            list[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            list[k] = r[j]
            j += 1
            k += 1

    return list

def getMajority(list):
    mergeSort(list)
    return list[len(list)//2]

print(getMajority(input1))
print(getMajority(input2))