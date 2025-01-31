# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

input_accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

def fin_max_account(input_array):
    maxVal = 0

    for person in input_array:
        tempSum = 0
        for bank in person:
            tempSum += bank
        if tempSum > maxVal : maxVal = tempSum

    return maxVal

print(fin_max_account(input_accounts))