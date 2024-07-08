"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""


class Solution:
  def mySqrt(self, x: int) -> int:
      left = 0 
      right = x 
      aws = 0
      while left <= right:
          mid = (right + left) // 2
          if mid * mid == x:
              return mid
          elif mid * mid < x:
              aws = mid
              left = mid + 1
          else:
              right = mid - 1
      return aws

# Generate some inputs and print the outputs
solution = Solution()

# Test cases
assert solution.mySqrt(4) == 2, "Test case 1 failed"
assert solution.mySqrt(8) == 2, "Test case 2 failed"
assert solution.mySqrt(0) == 0, "Test case 3 failed"
assert solution.mySqrt(1) == 1, "Test case 4 failed"
assert solution.mySqrt(15) == 3, "Test case 5 failed"
assert solution.mySqrt(16) == 4, "Test case 6 failed"
print("All test cases passed!")
        