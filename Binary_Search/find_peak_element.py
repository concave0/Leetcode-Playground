"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""
from typing import List

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid  # mid might be the peak
        else:
            left = mid + 1  # peak lies in the right part
    return left


# Example inputs for testing
example1 = [1, 2, 3, 1]
example2 = [1, 2, 1, 3, 5, 6, 4]
example3 = [10, 20, 15, 2, 23, 90, 67]
example4 = [1]
example5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Test cases
# assert Solution().findPeakElement(example1) in [2]
# assert Solution().findPeakElement(example2) in [1, 5]
# assert Solution().findPeakElement(example3) in [1, 5]
# assert Solution().findPeakElement(example4) in [0]
# assert Solution().findPeakElement(example5) in [9]
print(Solution().findPeakElement(example1))  # Expected output: 2
print(Solution().findPeakElement(example2))  # Expected output: 1 or 5
print(Solution().findPeakElement(example3))  # Expected output: 1 or 5
print(Solution().findPeakElement(example4))  # Expected output: 0
print(Solution().findPeakElement(example5))  # Expected output: 9

      
      
        
      
    
    
    


