from typing import List 

class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      """ return the indices of where position in spells and potions is equal to success or greater to then success"""
  

      successfull_attempts = []
      org_potions = sorted(potions)
      
      for n in spells: 
          
        amount_of_success = 0
        left = 0 
        right = len(org_potions) - 1 
          
        while left <= right: 
            mid = (left + right) // 2
            combine = n * org_potions[mid]

            if combine >= success: 
                right = mid - 1
                amount_of_success += 1 
                
            else:  
                left = mid + 1 
                
        amount_of_success = len(org_potions) - left
        successfull_attempts.append(amount_of_success)

      return successfull_attempts 
