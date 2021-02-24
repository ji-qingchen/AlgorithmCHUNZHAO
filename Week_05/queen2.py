#位运算
def queen(n):
    count = 0
    if n < 1: return 0
    
    def dfs(row,col,pie,na):
        
        if row >= n:
            
            return 1

        bit = ~(col | pie | na) & ((1<<n)-1) #取得n位 二进制数，有效位数对应值为1
        count = 0
        while bit:
            p = bit & -bit #获得最低位1的幂值
            bit = bit & (bit - 1) #末位1置0，即把queen放在，末位为1的地方

            #drill down
            count += dfs(row+1, p | col, (p | pie)<<1,(p|na)>>1) #col多了一个p的位置，pie多了一个p位后往左移1位，na多了一个p位后往右移

            # col,pie,na值没有改变不需重置，drill中的直接把数值copy了一份
        return count
    return dfs(0,0,0,0)
    
print(queen(4))
