#1---------------------------------------------------------------------------------------------------------
"""Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1."""
def count_evens(nums):
  c=0
  for i in nums:
    if i%2==0:
      c+=1
  return c

#2--------------------------------------------------------------------------------------------------------
"""Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
   Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values."""

def big_diff(nums):
  return max(nums)-min(nums)

#3------------------------------------------------------------------------------------------------------
"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
   except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
   ignore just one copy, and likewise for the largest value. 
   Use int division to produce the final average. You may assume that the array is length 3 or more."""

def centered_average(nums):
  nums.pop(nums.index(min(nums)))
  nums.pop(nums.index(max(nums)))
  return (int(sum(nums)/len(nums)))

#4-------------------------------------------------------------------------------------------------------
"""Return the sum of the numbers in the array, returning 0 for an empty array. 
  Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count."""

def sum13(nums):
  nums+=[0]
  return sum(i for j, i in enumerate(nums) if i!=13 and nums[j-1]!=13)

#5------------------------------------------------------------------------------------------------------
"""Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
   (every 6 will be followed by at least one 7). Return 0 for no numbers."""

def sum67(nums):
  flag=False
  sum=0
  for i in nums:
    if i==6:
      flag=True
      continue
      
    if(i==7 and flag==True):
      flag=False
      continue
      
    if(flag==False):
      sum+=i
  return sum
