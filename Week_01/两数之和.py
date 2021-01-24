nums = [1,2,6,8,5,7]
target = 7
result = []

#1.两遍循环
for i in range(len(nums)-1):
   for j in range(i+1, len(nums)):
       he = nums[i] + nums[j]
       if he == target:
           result.extend([i,j])
        
print(result)

#2.字典：即时存数-下标键值对，看之后的数是否是已有键的值，若是则返回，否则添加新对
dic = {}
for i in range(len(nums)):
    if nums[i] in dic:
        result.extend([i,dic[nums[i]]])
        print(result)
    else:
        dic[target - nums[i]] = i
        print(dic)
print(result)

