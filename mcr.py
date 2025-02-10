def mcr(s):
    if not s:
        return 0
    count = 0
    max_count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
            max_count = max(max_count,count)
        else:
            count = 0
    return max_count+1
s = "harrrrrrshit"
res = mcr(s)
print(res)