# Given two strings s and t, determine if they are isomorphic.
# s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Input: s = ‘egg’, t = ‘add’ // true
# Input: s = ‘foo’, t = ‘bar’ // false
# Input: s = ‘paper’, t = ‘title’ // true

# Source: https://leetcode.com/problems/isomorphic-strings/solution/


s1 = 'egg'
t1 = 'add'
s2 = 'foo'
t2 = 'bar'
s3 = 'paper'
t3 = 'title'

def is_iso(s, t):
    # dictS = {}
    # dictT = {}
    if len(s) != len(t):
        return False
    dictComb = {}
    for i in range(0,len(s)):
        if s[i] in dictComb.keys():
            if dictComb[s[i]] != t[i]:
                return False
        dictComb[s[i]] = t[i]

    return True

print(is_iso(s1, t1))
print(is_iso(s2, t2))
print(is_iso(s3, t3))