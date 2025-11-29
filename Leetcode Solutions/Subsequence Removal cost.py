s=input("string: ")
sub=input("sequence: ")
nomatch=[]
cost = 0
def check_subseq(s,sub):
    i=0
    j=0
    while i<len(s) and j<len(sub):
        if s[i] != sub[j]:
            nomatch.append(i)
            i+=1
        elif s[i] == sub[j]:
            i+=1
            j+=1
    return j==len(sub)

check=check_subseq(s,sub)
if not check:
    print(-1)
else:
    for num in nomatch:
        cost+=num
    print(f"cost of removal = {cost}")

# def min_cost_transform(s, t):
#     i = j = 0
#     result = 0

#     s = list(s)

#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#             j += 1
#         else:
#             result += i  # index itself
#             s.pop(i)

#     if j != len(t):
#         return -1

#     while len(s) > len(t):
#         result += len(s) - 1
#         s.pop()

#     return result


# s = input().strip()
# t = input().strip()
# print(min_cost_transform(s, t))
