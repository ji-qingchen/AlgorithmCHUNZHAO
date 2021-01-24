#1.新建一个list
li1 = [1,2,3,4,5,6,7]
k = 3
li2 = []
for i in li1:
   li2.append(i)
for j in range(len(li2)):
   li1[(j+k)%len(li1)] = li2[j]
print(li1)


#2.反转数组:全部反转；部分反转
nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
if n < k:
    k = k - n
if n >= k:
    #反转数组
    nums.reverse()
    li2= nums[:k]
    li2.reverse()
    li3 = nums[k:]
    li3.reverse()
    #构建反转后的数组
    li2.extend(li3)
    #将新数组的值赋给原数组
    for i in range(n):
        nums[i] = li2[i]
print(nums)

