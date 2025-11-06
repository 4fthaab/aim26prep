# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        sorted_keys = sorted(freq, key=freq.get, reverse=True)
        return sorted_keys[0]


# ---- TESTING AREA ----
if __name__ == "__main__":
    # Example test
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))   # Expected: 3