nums=[100,250,100,120,253]
sortn=sorted(set(nums))
ranklist={}
rank=1
for i in sortn:
    ranklist[i]=rank
    rank+=1
res=[]
for n in nums:
    res.append(ranklist[n])
print(res)