def stringcounter(s1):
    if not s1:
        return "null"
    d = {}
    for i in s1:
        d[i] = d.get(i,0)+1
    l = list(d.items())
    return l
s1 = "aaabbbbbbccccc"
res = stringcounter(s1)
print(res)