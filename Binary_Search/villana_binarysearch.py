from typing import List, Any, Optional


def binary_search(arr:List[int], target:int) -> int: # imports an array of List[int] and a target value of int 
  left = 0 
  right = len(arr) -1 

  while left <= right: 
    mid = (left + right) // 2 
    if arr[mid] == target: 
      return mid
    elif arr[mid] < target: 
      left = mid + 1 
    else:
      right = mid - 1 
  return 0 
    
print(binary_search(arr=[1,3,5,7,8], target = 7))
assert(binary_search(arr=[1,3,5,7,8], target = 7))

