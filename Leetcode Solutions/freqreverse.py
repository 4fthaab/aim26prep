def freq(st):
    out=""
    i=0
    while i<len(st):
        key=st[i]
        c=0
        while (i<len(st)) and (st[i]==key):
            c+=1
            i+=1
        out+=key+str(c)
    return(out)
st=input()
print(freq(st))