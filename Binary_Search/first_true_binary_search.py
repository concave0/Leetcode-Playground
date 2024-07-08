# First True in a Sorted Boolean Array 
from typing import List 


def find_boundary(arr: List[bool]) -> int:
  left, right = 0, len(arr) - 1
  boundary_index = -1

  while left <= right:
      mid = (left + right) // 2
      if arr[mid]:
          boundary_index = mid
          right = mid - 1
      else:
          left = mid + 1

  return boundary_index

# Test cases to validate the solution
arr1 = [False, False, True, True, True]
arr2 = [False, False, False, False]
arr3 = [True, True, True, True]
arr4 = [False, True]
arr5 = [True]
arr6 = [False]

# Assertions to validate the solution
assert find_boundary(arr1) == 2, f"Test case 1 failed: {arr1}"
assert find_boundary(arr2) == -1, f"Test case 2 failed: {arr2}"
assert find_boundary(arr3) == 0, f"Test case 3 failed: {arr3}"
assert find_boundary(arr4) == 1, f"Test case 4 failed: {arr4}"
assert find_boundary(arr5) == 0, f"Test case 5 failed: {arr5}"
assert find_boundary(arr6) == -1, f"Test case 6 failed: {arr6}"

print("All test cases passed!")

