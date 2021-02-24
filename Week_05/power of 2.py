#幂值即100000……形式（二进制）
#根据题目，非正整数均返回false
def isno(x):
    if x == 0: 
        return False
    return x & (x-1) == 0



#简化
def isor(x):
    return x > 0 and x & (x-1) == 0

#法2
def ion(x):
    if x <= 0: return False
    if x & -x == x: return True
    return False
    
