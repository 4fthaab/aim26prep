def maxchar(strs):
        strs1=sorted(strs)
        x=strs1[0]
        flag=0
        ans=""
        for i in range(len(x)):
            for j in range(1, len(strs)):
                if strs1[j][i]!=x[i]:
                    flag=1
                    break
            if flag==1:
                break
            else:
                ans+=x[i]
        return ans
strs=["flight","float","flow"]
print(maxchar(strs))
