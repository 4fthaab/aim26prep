st = input()
out = ""
i = 0

while i < len(st):
    ch = st[i]
    i += 1
    num = 0

    while i < len(st) and st[i].isdigit():
        num = num * 10 + int(st[i])
        i += 1
    
    out += ch * num

print(out)
