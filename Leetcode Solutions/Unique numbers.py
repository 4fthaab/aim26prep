def removeKdup(nums, K):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    freq_list = sorted(freq.values())
    unique = len(freq_list)
    print(freq_list)
    for f in freq_list:
        if K >= f:
            K -= f
            unique -= 1
        else:
            break
    return unique

print(removeKdup([1,2,3,5,2,3,5,2,4,6], 5))
