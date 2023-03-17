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
  
