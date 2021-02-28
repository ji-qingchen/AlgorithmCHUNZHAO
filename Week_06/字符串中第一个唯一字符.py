#暴力
#hash表
def many(s:str):
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    for i in s:
        if dic[i] == 1:
            return s.index(i)
    return -1
print(many('aabcc'))

#count数组
