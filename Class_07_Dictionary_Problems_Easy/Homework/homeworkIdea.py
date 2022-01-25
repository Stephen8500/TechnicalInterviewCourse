s = "anagram" 
t = "nagaram"

s2 = "rat" 
t2 = "car"

def checkAnagram(s, t):
  if len(s) != len(t):
    return False

  dictS = {}
  dictT = {}

  for sLetter in s:
    if sLetter not in dictS.keys():
      dictS[sLetter] = 1
    else:
      dictS[sLetter] += 1

  for tLetter in t:
    if tLetter not in dictT.keys():
      dictT[tLetter] = 1
    else:
      dictT[tLetter] += 1
      
  
  return (dictS == dictT)

print(checkAnagram(s, t))
print(checkAnagram(s2, t2))
