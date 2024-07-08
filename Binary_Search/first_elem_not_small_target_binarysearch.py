from typing import List


def find_larger(arr: List[int], target: int) -> int:  # returns the index
  left = 0
  right = len(arr) - 1
  anw = -1 

  while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
      anw = mid
      right = mid - 1
    else:
      left = mid + 1  # get rid of the left most side
  return anw 


# Test cases
assert find_larger([1, 3, 3, 5, 8, 8, 10], 2) == 1, "Test case 1 failed"
print("Test case 1 passed")

assert find_larger([2, 3, 5, 7, 11, 13, 17, 19], 6) == 3, "Test case 2 failed"
print("Test case 2 passed")

assert find_larger([1, 3, 5, 7, 9], 4) == 2, "Test case 3 failed"
print("Test case 3 passed")

assert find_larger([1, 3, 3, 3, 5], 3) == 1, "Test case 4 failed"
print("Test case 4 passed")



