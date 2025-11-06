# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:
# The element 1 occurs at the indices 0 and 3.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# ---- TESTING AREA ----
if __name__ == "__main__":
    # Example test
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))   # Expected: True
