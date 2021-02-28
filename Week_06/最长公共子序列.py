#子序列可以删除中间元素，只要不改变位置顺序，子串不能
#DP升维，s1[i]==s2[j]时，i--,j--;否则i--或j--;返回长度
def long(str1,str2):
    
    if not str1 or not str2:
            return 0
        m,n = len(str1),len(str2)
        dp =[ [0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]

#最长公共子串
def longc(s1,s2):
    if not s1 or not s2:
        return 0
    m,n = len(s1),len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = 0 #包括当前索引值在内的字符串不是子字符串
    a = [].append(max(dp[k]) for k in range(m+1)
    return max(a)