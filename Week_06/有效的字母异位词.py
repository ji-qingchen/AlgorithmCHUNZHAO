#hash
def yw(s1,s2):
    m,n = len(s1),len(s2)
    if m != n:
        return False
    dic = {}
    for i in range(m):
        if s1[i] not in dic:
            dic[s1[i]] = 1
        else:
            dic[s1[i]] += 1
    for j in range(n):
        if s2[j] not in dic:
            return False
        else:
            if min(list(dic.values())) < 0:
            return False
    return True

    
        
