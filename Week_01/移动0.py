nums = [1,2,0,4,5,0,0]
#1.非0项前移，后面设为0
j = 0 #记录非0项个数
for i in range(len(nums)):
   if nums[i] != 0:
       nums[j] = nums[i]
       j+=1 #j往后移1位  #j 比非0数最大下标大1
print(nums)
for k in range(j, len(nums)):
   nums[k] = 0
print(nums)


#2.交换 第一个0和其后第一个非0数交换，第二个……(嵌套)

for i in range(len(nums)):
   if nums[i] == 0:
       for j in range(i+1, len(nums)):
           if nums[j] != 0:
               nums[i], nums[j] = nums[j],nums[i]
               break
    
       print(nums)


#3.交换 是非0元素就和前面的0交换：
j = 0
for i in range(len(nums)):
    if nums[i] != 0: #若nums[i] == 0,则i++,j不动，j若指向0，则下次非0时和其交换，j不指向非0，因i比j快，把非0情况处理了
        nums[i], nums[j] = nums[j], nums[i]
        j+=1 #本质上和上面的交换方法一样
print(nums)