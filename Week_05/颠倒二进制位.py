def reverse(x):
    #if x == 0: return 0 #这句不需要
    res = 0
    i = 32
    while i: 
        res = res << 1
        i -= 1        
        res += x & 1   
        x = x >> 1            
    return res
