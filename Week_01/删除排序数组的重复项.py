'''快慢指针'''

nums = [0,0,1,1,1,2,2,3,3,4]
n = len(nums)
i = 0
if n < 2:
    print(n)
else:
    #j记录nums中的所有下标
    for j in range(1,n):
        if nums[i] != nums[j]:
     #i按顺序记录非重复元素
            i += 1;
            nums[i] = nums[j] #把非重复元素赋值，可从nums[i]代表一个空的新数组的角度理解
            
        j += 1
print(i+1) #题目要求只返回数组中非重复元素的长度，不必对数组进行删除处理
