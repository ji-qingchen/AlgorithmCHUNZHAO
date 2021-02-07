#（（））有效吗：有效

#1 DP
#用 dp[i] 表示以 i 结尾的最长有效括号；
#s[i]以'('结尾则dp[i]=0;
#s[i]以')'结尾：s[i-1]为（时，dp[i] = dp[i-2]+2
#                s[i-1]为)时,若s[i-1-dp[i-1]]为（时，dp[i] = dp[i-1]+ 2 + dp[i-dp[i-1]- 2
def longest(s:str):
    n = len(s)
    if n == 0: return 0
    dp = [0] * n
    res = 0
    for i in range(1,n):
        #if s[i] == '(':
        #    dp[i] = 0
        if s[i] == ')':
            if s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            elif s[i-1] == ')' and i-1-dp[i-1]>=0 and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-2]
            res = max(res, dp[i])
    return res
print(longest("(())"))