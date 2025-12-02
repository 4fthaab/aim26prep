def reassignPriorities(priorities):
    vals = sorted(set(priorities))

    mp = {}
    i = 1
    for v in vals:
        mp[v] = i
        i += 1

    result = []
    for x in priorities:
        result.append(mp[x])

    return result

print(reassignPriorities([1,8,2,8]))