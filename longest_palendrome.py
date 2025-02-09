def lps(s):
    if not len(s):
        return 0
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    count = 0
    odd = False
    for i in d.values():
        count += i//2 * 2
        if i%2 != 0:
            odd = True
    if odd:
        count +=1
    return count
s = "bbabcbabs"
print(lps(s))