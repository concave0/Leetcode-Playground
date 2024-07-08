
"""
Creating default template first 
* 
"""

from typing import List 

def binary_search(arr:List[bool]) -> int: 
  left = 0 
  right = len(arr) - 1 
  first_index = -1 

  while left <= right: 
    mid = (left + right) // 2 
    if arr[mid]: 
      first_index = mid
      right = mid - 1
    else:
      left = mid + 1
  return first_index

# Test cases
inputs = [
    [False, False, True, True, True],  # Expected output: 2
    [False, False, False, True],        # Expected output: 3
    [True, True, True],                 # Expected output: 0
    [False, False, False],              # Expected output: -1
    [False, True, True, True, True],    # Expected output: 1
]

# Run test cases
assert(binary_search([False, False, True, True, True]) == 2)
assert(binary_search([False, False, False, True]) == 3)
assert(binary_search([True, True, True]) == 0)
assert(binary_search([False, False, False]) == -1)
assert(binary_search([False, True, True, True, True]) == 1)

print()
print("All tests have passed!\n")
