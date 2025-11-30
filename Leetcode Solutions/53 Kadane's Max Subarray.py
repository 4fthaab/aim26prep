# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(nums):
    curr=nums[0]
    max_sum=nums[0]
    for i in range(1,len(nums)):
        curr+=nums[i]
        if curr<nums[i]:
            curr=nums[i]
        if curr>max_sum:
            max_sum=curr
    return max_sum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))