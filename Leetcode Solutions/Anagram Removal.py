s1=input("string 1: ")
s2=input("string 2: ")

def remove_anagram(s1,s2):
    freq1={}
    freq2={}
    for char in s1:
        if char in freq1:
            freq1[char]+=1
        else:
            freq1[char]=1
    for char in s2:
        if char in freq2:
            freq2[char]+=1
        else:
            freq2[char]=1
    cost=0
    for ch in set(freq1.keys()).union(freq2.keys()):
        cost += abs(freq1.get(ch, 0) - freq2.get(ch, 0))
    return cost

print(remove_anagram(s1,s2))

