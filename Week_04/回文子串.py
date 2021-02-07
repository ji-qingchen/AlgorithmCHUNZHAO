#回文子串：从左到右==从右到左；一个字母也是
#计算个数
#不排除重复项
#子串连续

#DP 
## 1 subproblem: 两个字符串：(不必正和倒），组成二维数组，dp[i][j]相等，看其子串是否回文；求和
## 2 dp[i][j],记录当前位置对应字符串个数
## 3 dp[i][j] = dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1] 
#
#以上思路不对

'''
1. 二维数组，横竖都是str(两个指针分别指向子串头尾)
2. i==j时，字符串内各字符，√；i+1 == j 时，str[i] == str[j],√；j-i>1时，
    头尾相等且子串为回文串则其为回文串
3. dp[i][j]为相应str的子串数
4. dp[i][j] = dp[i+1][j-1]
'''
def substring(s:str):
    n = len(s)
    count = 0
    if n == 0: return 0
    dp = [[0]*n for _ in range(n)]
    #for i in range(n):      这种遍历方式是按行遍历（左上角），bfs，错（why？）
    #    for j in range(i,n):
    for j in range(n):      #左上角按列遍历，dfs
        for i in range(0,j+1):
            if i == j:
                dp[i][j] = 1
                count += 1
            elif i + 1 == j and s[i] == s[j]:                
                dp[i][j] = 1
                count += 1
            elif j - i > 1:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    count += 1
    return count

        

#找回文子串对称中心
#字符串头尾双指针：奇：left = center-1, right = center+1；偶：left-1,right+1
def numstr(s:str):
    result = 0;
        
    def extend(s, i,j,n):
        res = 0
        while (i >= 0 and j < n and s[i] == s[j]): # 和 while s[i] == s[j] and i>=0 and j<n 不同
            
            i-=1
            j+=1;
            res+=1;
        return res
        
    for i in range(len(s)):
        result += extend(s, i, i, len(s))
        result += extend(s, i, i + 1, len(s))
    return result;
   

print(numstr('aaa'))
