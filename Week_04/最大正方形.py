#1 subproblem: 以num[i,j](非0)为右下角，其对应最大正方形边长为上、左、左上格分别对应最大正方形
    #中的最小边长+1（这些格都非0，因为递归，所以只判断dp[i,j]即可以满足其他格的判断）
# 2 状态量 dp[i][j]，记录当前格对应的最大正方形边长
# 3 DP：if dp[i][j] == 1 -> dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

def squre(matrix:list[list]):
    m, n = len(matrix), len(matrix[0])
    if m == 0 or n == 0:return 0
    dp = [[0]*(n+1) for _ in range(m+1)]  #记录边长的二维矩阵，左、上边均为0
    #dp[1][1] = 1,何时设初值？
    s = 0
    for i in range(1,m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
            s = max(dp[i][j],s) #取出dp中最大值
    return s*s

#优化1 dp中不是所有单元格都用上，把上一行值复用到当前行，以实现dp降为1维
#定义新变量记录左上角，为上一行的、当前格的前一格
def maxs(matrix:list[list]):
    m, n = len(matrix),len(matrix[0])
    s = 0
    if m == 0 or n == 0:
        return 0
    dp = [0]*(n+1)
    topl = 0 #第一行的前一行为0
    for i in matrix:
        topl = 0 #topl此前值为上一循环的最后一个左上值，和这一行无关，重置为0（第1格的前一格对应值）
        for j in range(1,n+1):
            tople = dp[j] #当前格的结果，作为下一格的左上格（因为当前行复用了上一行，
                            #所以先记录下未改变的当前格）

            if i[j-1] == '1':
                dp[j] = min(dp[j], dp[j-1], topl) + 1
            else:   #必须有此项，因为i[j-1] == '0'时，没有正方形，边长为0，若
                               #没有此项，会把上次的dp值当作此次的来处理
                dp[j] = 0                
            s = max(s, dp[j])
            topl = tople #不可直接把dp[j]当作左上值，因为左上值应为上一行值，dp[j]为改变后的值
    return s*s
            
        

