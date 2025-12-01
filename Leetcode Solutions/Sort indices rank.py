def sortRanks(s):
    st=list(s)
    values=sorted(st)
    result = []
    used = [False] * len(st)
    for c in values:
        for i in range(len(st)):
            if st[i] == c and not used[i]:
                result.append(i)
                used[i] = True
                break
    return result
print(sortRanks("afthab"))
