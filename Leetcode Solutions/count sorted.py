nums=[25,18,42,35,25,25,18,18]
def countSorted(nums):
    count=[0]*101
    for n in nums:
        count[n]+=1
    rank_map={}
    rank=1
    for val in range(1, 101):
        if count[val] > 0:
            rank_map[val] = rank
            rank += 1
    for n in range(len(nums)):
        item=nums[n]
        nums[n]=rank_map[item]
    return nums
print(countSorted(nums))
