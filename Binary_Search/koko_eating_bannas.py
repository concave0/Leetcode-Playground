"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
  Input: piles = [3,6,7,11], h = 8
  Output: 4

Example 2:
  Input: piles = [30,11,23,4,20], h = 5
  Output: 30

Example 3:
  Input: piles = [30,11,23,4,20], h = 6
  Output: 23
"""
from typing import List

class Solution:

  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left = 1  # start with minimum viable speed
    right = max(piles)  # maximum pile size as the upper bound
    eating_speed_collection = []

    while left <= right:
      mid = (left + right) // 2  # standard integer division
      if self.can_finish(piles, mid, h):  # use validation function
        eating_speed_collection.append(mid)
        right = mid - 1  # try to find a lower valid speed
      else:
        left = mid + 1
    return min(eating_speed_collection)

  def determine_eating_speed(self, pile_amount: int, hours: int) -> int:
    left = 1  # start with minimum viable speed
    right = pile_amount
    amount = set()
    while left <= right:
      mid = (left + right) // 2
      if mid <= hours:
        amount.add(mid)
        right = mid - 1
      else:
        left = mid + 1
    return max(amount)

  def can_finish(self, piles: List[int], k: int, h: int) -> bool:
    hours_needed = 0
    for pile in piles:
      hours_needed += -(-pile // k)  # Equivalent to ceil(pile / k)
    return hours_needed <= h

