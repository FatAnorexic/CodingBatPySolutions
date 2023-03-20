#1)double_char----------------------------------------------------------------------------------------------------------
'''Given a string, return a string where for every char in the original, there are two chars.'''

def double_char(str):
  newstr=''
  for i in range(len(str)):
    newstr+=2*str[i]
  return newstr

#2count_hi--------------------------------------------------------------------------------------------------------------
'''Return the number of times that the string "hi" appears anywhere in the given string'''
def count_hi(str):
  c=0
  for i in range(len(str)-1):
    if str[i:i+2]=='hi':
      c+=1
  return c

#3cat_dog---------------------------------------------------------------------------------------------------------------
'''Return True if the string "cat" and "dog" appear the same number of times in the given string.'''
def cat_dog(str):
  a=0
  b=0
  for i in range(len(str)-2):
    if str[i:i+3]=='cat':
      a+=1
    if str[i:i+3]=='dog':
      b+=1
  if a==b:
    return True
  return False

#4----------------------------------------------------------------------------------------------------------------------
'''Return the number of times that the string "code" appears anywhere in the given string, 
   except we'll accept any letter for the 'd', so "cope" and "cooe" count.'''
def count_code(str):
  c=0
  for i in range(len(str)-3):
    if str[i:i+2]=='co' and str[i+3]=='e':
      c+=1
  return c

#5----------------------------------------------------------------------------------------------------------------------
'''Given two strings, return True if either of the strings appears at the very end of the other string, 
   ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
   Note: s.lower() returns the lowercase version of a string.'''
def end_other(a, b):
  a=a.lower()
  b=b.lower()
  return(a.endswith(b) or b.endswith(a))

#6----------------------------------------------------------------------------------------------------------------------
'''Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
   by a period (.). So "xxyz" counts but "x.xyz" does not.'''
def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3]=='xyz' and str[i-1]!='.':
      return True
  return False
