#hash + 内置  O(n)
import collections

nums = [1,2,2,2,2,2,5,4,6]
counter = collections.Counter(nums)
a = max(counter, key=counter.get)
print(a)

# hash
dic = {}
for num in nums:
    if not num in dic:
        dic[num] = 1
    else:
        dic[num] += 1
#print(dic)
#找最大值
m = max(dic, key=dic.get)
print(m)

#或
st = 0; k = 0
for key in dic:
    if dic[key] >= st:
        st = dic[key]
        k = key
print(k)

# 排序，中数即众数,根据定义，出现次数大于n/2，n为偶，则中间2个都是，n为奇数，则中间数是。这两种情况都可以对应
#坐标n//2, O(nlogn)
nums.sort()
n = len(nums)
px = nums[n // 2]
print(px)

#分治 O(nlogn) 2T(n/2)+2n(遍历两遍，最开始一次？最后比较众数一次)，根据主定理，为O(nlogn)

#中分，众数必是左半边或右半边的众数
nums = [1,1,2,2,2,2,2,3,3]
def zs(le,ri):
    n = len(nums)
    #terminator
    if le == ri: #无论子问题长度是奇数还是偶数最终都会出现这种情况。最内层子问题
        return nums[le] #左边界点才能取到值
    # split
    #最内层子问题回溯
    mid = (le + ri)//2  #偶数取中线偏左，奇数取中点
    left = zs(le,mid)
    right = zs(mid + 1,ri)

    #subresult
    if left == right:   #左右子问题众数相等则此数必是总问题众数
        return left
    else:    #不相等时，两者至少有一个有众数：若两个都有，需要比较；若一个没有，则其可能取到任何数，比较
                 #也不会得到错误结果
        lef = 0; rig = 0
        for i in range(le, ri+1): #左右边界都要取到
            if nums[i] == left:
                lef += 1
            elif nums[i] == right:
                rig += 1
    if lef > rig:
        print(left)
        return left
    else:
        print(right)
        return right

zs(0,8)


#投票法(BM法)
piao = None
count = 0
for j in nums:
    if count == 0:
        piao = j
       
    if piao == j:
        count += 1
    else:
        count -= 1
print(piao)

        
        


