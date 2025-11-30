def twoSum(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        sums=nums[left]+nums[right]
        if sums>target:
            right-=1
        elif sums<target:
            left+=1
        else:
            return left,right

print(twoSum([2, 7, 11, 15],22))