#暴力
''' s = 1
    for i in range(n):
       s *= x
    return s '''

#二分法分治
#  n 为奇数时，s = s1 * s2 * x; n 为偶数时，s = s1 * s2 .奇偶需要每层都判断
def power(x,n):
   
    if x == 0 and n <= 0:
        return 
    elif x == 0 and n > 0:
        return 0
    if x == 1:
        return 1
        
    def qu(n):
    #terminator
        if n == 0:
            return 1
        #process
        result = qu(n//2)
        if n % 2 == 0:
            res = result * result
        elif n % 2 == 1:
            res = result * result * x
        #print(res)
        return res
    
    return qu(n) if n > 0 else 1/qu(-n)
print(power(2,-2))
