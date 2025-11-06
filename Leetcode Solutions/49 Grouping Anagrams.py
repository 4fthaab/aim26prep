# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for w in strs:
            key = ''.join(sorted(w))
            if key in mp:
                mp[key].append(w)
            else:
                mp[key] = [w]
        return list(mp.values())


# ---- TESTING AREA ----
if __name__ == "__main__":
    # Example test
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
    # Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]