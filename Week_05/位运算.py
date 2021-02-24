# 用自带函数
def count1(n):
    x = bin(n).count('1')
    return x

#计算末位的1然后末尾置为0
def count2(x):
    if x <= 0:
        return 0
    n = 0
    while x:
        x = x & (x-1)
        n += 1
    return n

# 除以2求余数
def count3(x):
    n = 0
    while x:
        
        if x & 1:
            n += 1
        x = x >> 1
    return n


    

