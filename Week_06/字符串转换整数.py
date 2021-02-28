def trans(s:str):    
    s = s.strip()        
    if len(s) == 0:
        return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['+','-']:
        s = s[1:len(s)] 
    
    res = 0
    for i in s:
        if i.isdigit():
            res = res*10+(ord(i)-ord('0'))
        else:
            break
    res = max(-2**31,min(res*sign,2**31-1))
    return res
print(trans('++1'))

        
