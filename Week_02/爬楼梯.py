#五毒3
#递归
def cl(n):
    f1, f2 = 1, 2
    if n <= 2:
        return n
    f = 0
    for i in range(3,n+1):
        f = f1 + f2
        f1 = f2
        f2 = f
    return f

print(cl(5))
        

#动态规划
#f3 = f1 + f2为转移方程，边界条件：f0 = 1, f1 = 1
#滚动数组
def cl2(n):
    f0 = 0; f1 = 1; f2 = 0
    for i in range(1,n+1):
        f2 = f0 + f1        
        f0 = f1
        f1 = f2
    return f2
print(cl2(5))