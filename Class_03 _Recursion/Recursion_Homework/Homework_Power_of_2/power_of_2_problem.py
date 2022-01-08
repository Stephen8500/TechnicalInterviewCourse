# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False

def power_of_two(num):
    if num == 2 or num == 1:
        return 'True'
    elif round(num) != num:
        return 'False'
    else:
        return power_of_two(num/2)