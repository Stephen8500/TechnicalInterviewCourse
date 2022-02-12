# - Prepare a question for each of the two guest speakers. The questions can be about interview preparation, 
#       interviews, hiring, or software engineering careers. Paste your questions into the quiz.
# - Here is information about each guest speaker:
#     - Daryl Pinkal
#         - Company: Clozd
#         - Position: CTO, Product/Engineering
#     - Arlin Hayden
#         - Company: LookingGlass Cyber Solutions Inc.
#         - Position: Principal Software Engineer
# - Watch the following two videos about quicksort:
#     - https://www.youtube.com/watch?v=Hoixgm4-P4M
#     - https://www.youtube.com/watch?v=kFeXwkgnQ9U
# - Here is an additional resource to look at about quicksort:
#     - https://www.geeksforgeeks.org/python-program-for-quicksort
# - Write a quicksort line by line and then paste your code into the quiz.

# questions for guest speakers:

# for Daryl Pinkal - What is the most valuable skill to demonstrate to interviewers? What will set us apart from other candidates?
# for Arlin Hayden - What is the best way to start a career in software developement? Is it best to start in a smaller company, larger company,
    # start in the industry that you want to work in, etc.?


# quick sort code:

def quick_sort(arr):
    #check for base case of array only having 1 or fewer values
    if len(arr) <= 1:
        return arr
    
    #find pivot and sort greater/less than then run recursion
    # find pivot and remove it from array
    a = arr[0]
    b = arr[len(arr)//2]
    c = arr[len(arr) - 1]
    pivot = c
    if a > b:
        if a < c:
            pivot = arr.pop(0)
        elif b > c:
            pivot = arr.pop(len(arr)//2)
    else:
        if a > c:
            pivot = arr.pop(0)
        elif b < c:
            pivot = arr.pop(len(arr)//2)
    
    if pivot == c:
        arr.pop(-1)
    
    # initialize greater and lower arrays
    lower = []
    greater = []

    # loop through items in array and classify them 
    # as lower or greater than pivot
    for i in range(0, len(arr) - 1):
        if arr[i] > pivot:
            greater.append(arr[i])
        else:
            lower.append(arr[i])
    
    # recursive run, adds lower array (sorted), pivot, and greater array (sorted)
    return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0,1,2,3,4,8,6,5,1,6,2,4,1]))

