"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

"""


class Solution:

  def arrangeCoins(self, n: int) -> int:
    left = 0
    right = n
    staircase = []

    while left <= right:
      mid = (left + right) // 2
      if mid:
        staircase.append(mid)
        left = (mid - n) * -1
        right -= 1
    return sum(staircase)

# Example inputs for testing
print('Starting the arrangeCoins computation...')
sol = Solution()
print((sol.arrangeCoins(5), sol.arrangeCoins(5) == 2))
# assert sol.arrangeCoins(5) == 2
# assert sol.arrangeCoins(8) == 3
# assert sol.arrangeCoins(10) == 4
# assert sol.arrangeCoins(15) == 5
# assert sol.arrangeCoins(20) == 6
# print('Computation complete. All tests pass')
