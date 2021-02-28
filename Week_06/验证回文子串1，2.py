#1
#空格忽略，空为true；只考虑字母和数字，不考虑字母大小；尾=头
def huiwen(s:str):
    s = s.lower()
    i,j = 0, len(s)-1
    #if j < 0: return True
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while j >i and not s[j].isalnum():
            j -= 1
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(huiwen(' '))

#2
#最多删1个
def huiwens(s:str):
    # s0 = sa.lower()      新建str后会变慢
    # s = ''                        
    # for k in s0:
    #     if k.isalnum:
    #         s += k
    # print(s)

    s = s.lower()       
    i,j = 0, len(s)-1
    
    def judge(s,i,j):
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j >i and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
    while i < j:
        if s[i] != s[j]: #只判断一次后就return
            
            return judge(s,i+1,j) | judge(s,i,j-1)
        i += 1
        j -= 1
    return True