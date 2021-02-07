#不需要映射，只需要考虑str的组合情况和边界条件
'''边界条件：空str(题目给的非空，此项可排除)；在1到26内；无0x格式；开头不能是0，因为str需要完全映射
#subproblem：和前面连起来、不连起来，dp[i] = dp[i-1]+dp[i-2]
状态量：dp[i]
DP方程：dp[i] = dp[i-1]+dp[i-2]

边界分析：
nums[0] == 0:return 0
s[i]==0: if s[i-1]==1 or s[i-2]==1 ->dp[i] = dp[i-2] else rturn 0
s[i-1] == 1:s[i]任取
s[i-1] == 2:s[i] 取[0,6]

'''
def decnum(nums:str):
    if nums[0] == '0':return 0
    pre,now = 1,1#分别代表dp[i-2],dp[i-1]
    
    for i in range(1,len(nums)):
        tmp = now
        if nums[i] == '0':
            if nums[i-1] == '1' or nums[i-1] == '2':
                now = pre 
               
            else:
                return 0 #除10，20外如00，30等情况都不能实现完全映射
        elif nums[i-1] == '1'or (nums[i-1] =='2' and int(nums[i]) <= 6):
            now = now+pre
        pre = tmp   #drill down，注意缩进位置
            
        
    print(now)
    return now
decnum('123123')

#法2
'''
分类：
s[i] == 0:s[i-1] == 1 or 2:dp[i] = dp[i-2] else 0;
否则 11<= s[i-1,i+1]<=26:dp[i] = dp[i-1]+dp[i-2]
其他情况只能dp[i] = dp[i-1]
只涉及2个变量
'''
def de(s:str):
    if s[0] == '0':
        return 0

    n = len(s)
    pre,now = 1,1
    for i in range(1,n):
        tmp = now
        if s[i] == '0':
            if s[i-1]=='1' or s[i-1] == '2':
                now = pre
            else: 
                return 0
        elif '10' < s[i-1:i+1] <= '26': #直接限定两位数范围
            now += pre
        
        #else： 其他情况时now = now,省略
        pre = tmp
    #print(now)
    return now

de("10011")
