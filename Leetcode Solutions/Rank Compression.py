def compareRanks(ranks):
    values=sorted(set(ranks))
    li={}
    i=1
    for num in values:
        li[num]=i
        i+=1
    result=[]
    for num in ranks:
        result.append(li[num])
    return result
print(compareRanks([1,5,2,7]))
