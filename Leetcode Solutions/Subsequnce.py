s=input("string: ")
sub=input("sequence: ")

def check_subseq(s,sub):
    i=0
    j=0
    while i<len(s) and j<len(sub):
        if s[i] != sub[j]:
            i+=1
        elif s[i] == sub[j]:
            i+=1
            j+=1
    return j==len(sub)

print(check_subseq(s,sub))
        
        
        