#逆序对，两个下标i,j 若i>j则称（i,j）是逆序对

#暴力：循环嵌套，n^2
#归并排序1
def ms(nums:list, left, right):

    def mere(nums,left, mid, right):
        tmp = []
        i,j = left, mid+1
        while i <= mid and j <=right: #因为mid和right都是可以取的值，所以这里可以 =
            if nums[i] > nums[j]:
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        if i <= mid:
            tmp += nums[i: mid+1]
        if j <= right:
            tmp += nums[j: right+1]
        nums[left : right+1] = tmp
        
        
    if right <= left: return 0
    mid = (left + right) >>1
    count = ms(nums, left, mid) + ms(nums, mid+1, right)
    #ms(nums, mid+1, right)
    for i in range(left,mid+1):
        j = mid+1
        while j<=right and nums[i]/2>nums[j]:
            j += 1
        #j - (mid+1):若nums[i]/2>nums[j],则nums[i]必定大于nums[j]之前的值
        count += j - (mid+1)
    mere(nums, left, mid, right)
    print(nums)
    return count

#归并排序2
def mergecount(nums):
    res = 0
    def merge(nums,l,r,res):
        
        def mere(nums,l,m,r):
            tmp = []
            i,j = l,m+1
            while i<=m and j<=r+1:
                if nums[i]<nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            if i <= m: tmp += nums[i:m+1]
            if j <= r: tmp += nums[j:r+1]
            nums[l:r+1]=tmp
        
        if l >= r: return
        m = (l+r)>>1
        #先分治，再计数
        merge(nums,l,m,res)
        merge(nums,m+1,r,res)
        #计数
        i,j,c = 0,m+1,0
        while j <= r and i <= m:
            if j <= r or nums[i] > 2*nums[j]:
                j += 1
                c += 1            
            else:
                l += 1
                res += c
        mere(nums,l,m,r)
        return res
   
    
    return res

#归并排序3
def ms1(nums:list, left, right):
        
    if right <= left: return 0
    mid = (left + right) >>1
    count = ms1(nums, left, mid) + ms1(nums, mid+1, right)
    #合并并统计
    res = []
    i,t = left, left
    for j in range(mid+1,right+1):
        while i <= mid and nums[i]/2<=nums[j]:
            i += 1 #i不符合条件则跳过，直到符合条件，结束循环
        while t <= mid and nums[t]<nums[j]: #排序
            res.append(nums[t])
            t += 1
        res.append(nums[j]) #nums[j]<nums[i]的情况
        count += mid-i+1    #i到 mid（包括i和 mid）的总个数
    
    if t<=mid:
        res += nums[t:mid+1]
    nums[left:right+1] = res
    print(nums)
    return count

print(ms1([7,5,6,4],0,3))

            


            





#树状数组 nlogn
