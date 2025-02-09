def is_rotation(s1, s2):
    connect = s1 + s1
    if s2 in connect:
        return True
    return False
s1 = "waterbottle"
s2 = "erbottlewat"
res = is_rotation(s1,s2)
print(res)