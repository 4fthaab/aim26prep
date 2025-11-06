# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# ---- TESTING AREA ----
if __name__ == "__main__":
    # Example test
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))   # Expected: True