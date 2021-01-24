nums1= [1,2,4,5,6,0]
nums2 = [3]
m = 5
n = 1

#1. 从最小值开始合并（头）
num = nums1[:m]
nums1[:] = []
p1 = 0; p2 = 0
while p1 < m and p2 < n:
   if num[p1] < nums2[p2]:
       nums1.append(num[p1])
       p1 += 1
   if num[p1] >= nums2[p2]:
       nums1.append(nums2[p2])
       p2 += 1

   #若有余量
   if p1 < m:
       nums1[p1+p2:] = num[p1:]
   if p2 < n:
       nums1[p1+p2:] = nums2[p2:]


#2.双指针，从最大值开始合并（尾）
p1 = m-1; p2 = n-1
p = m+n-1
while p1 >= 0 and p2 >= 0:
    if nums1[p1] >= nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:         #if nums1[p1] <= nums2[p2]和else效果不同，后者会出错（why?）
        nums1[p] = nums2[p2]
        p2 -= 1
    p-=1
    print(nums1)
#合并方式是把nums2插入nums1里面
nums1[:p2+1] = nums2[:p2+1]
print(nums2)
