#暴力：求出所有子串，判断是否回文 n^3
#暴力优化：枚举子串中心往两边扩展
def longh(s:str):
    lo = len(s),mal = 0;ls = 0
    if lo <= 1:return s

    #定义中心扩展函数
    def center(s,l,r):
        while l<= lo-1 and r >= 0 and s[l] == s[r]:
            l += 1
            r -= 1
        if mal < r-l+1:
            ls = j+1    #新的找中心的起点  
            mal = r-1+1 #之前的长度更小,-1还是+1？
    
    for i in range(lo):
        center(s,i,i) #奇对称
        center(s,i,i+1)#偶对称
    
    return s[ls:mal]

#最长子串——>DP,i,j指字符串起止位置
