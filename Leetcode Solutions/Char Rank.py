def compareRanks(s):
    st=list(s)
    values=sorted(set(st))
    li={}
    i=1
    for c in values:
        li[c]=i
        i+=1
    result=[]
    for c in st:
        result.append(li[c])
    return result
print(compareRanks("afthab"))
