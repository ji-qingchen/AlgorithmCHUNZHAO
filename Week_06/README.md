
# **学习笔记**
# 排序 (Sort)

比较类排序（多种类或对象，时间复杂度下限为nlogn）、非比较类排序（int相关类，线性时间）
## 1. 概述
### 1. 比较类（用的多）
重点是nlogn类
1. 交换
* 冒泡 稳
* 快速 √ 不稳

2. 插入（稳定）
* 简单插入 
* 希尔

3. 选择（不稳）
* 简单选择
* 堆排序 √

4. 归并（都稳定） √
* 二路归并
* 多路归并
 
### 2. 非比较类 （都稳定）
1. 计数
2. 桶排序
3. 基数排序

## 2. 初级排序 O(n^2)
* 选择 （Selection Sort）
   - 每次找最小值放在待排数组起始位置（即和在此位置的原来元素 **交换位置** ）
   * 2个循环嵌套， O(n^2)

            def ss(nums:list):
               for i in range(len(nums)):
                  for j in range(i+1,len(nums)):
                        if nums[i] > nums[j]:
                           nums[i],nums[j] = nums[j],nums[i]
               return nums

* 插入(Insertion Sort)
   * 从前到后构建有序数组，已排序数组元素 **从后往前扫描**，插入来自未排序数组的元素
   * 外面一层循环，数组插入元素O(n), 故O(n^2)

            def ise(nums:list):
               for i in range(1,len(nums)):
                  cur, p = nums[i], i-1 
                  while nums[p] > cur and p >= 0: #cur为当前要考虑的值，p代表此值之前的元素下标
                        nums[p+1] = nums[p] #cur可以往前插时，p各值往后平移
                        p -= 1 #从后往前扫，改变的是cur前的有序数组，不影响cur值
                  nums[p+1] = cur
               return nums
* 冒泡（Bubble Sort）
   * 嵌套循环，每次查看相邻元素，逆序则交换
   * 会先把最大的排好

            def bs(nums:[]):
               for i in range(len(nums)):
                  for j in range(1,len(nums)-i):
                        if nums[j-1] > nums[j]:
                           nums[j-1],nums[j] = nums[j], nums[j-1]
               return nums

## 3. 高级排序（O(nlogn)）
1. 快排（quick sort）

**分治：** 
   1）数组中取标杆pivot，小于其的元素放左边，大于的放右边；
   2）对左右子数组快排（递归）

      #quick sort
      def qs(nums, start, end):
         #确定标杆，为不开辟额外数组空间，以nums[end]为pivot
            def part(a, start, end):
               pivot = end;count = start #不开辟额外数组空间
               for i in range(start, end):
                     if a[i] < a[pivot]:
                        a[i], a[count] = a[count], a[i] #把小于pivot对应数值的元素从前往后放
                        count += 1
               a[count], a[pivot] = a[pivot], a[count] #因count+1 后才进行最后的判断，故当前count值对应pivot应该在的位置
               return count

            #分治（递归）
            #terminator
            if start >= end: return
            # current
            pivot = part(nums, start, end)
            #drill
            qs(nums, start, pivot-1) #左子数组快排
            qs(nums, pivot+1, end) #右子数组

            return nums

2. 归并排序（mere sort）
分治：1）长度为n的序列分为2个n/2的子序列
      2）分别归并
      3）合起来
```
      #merge sort

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
            
         
         if right <= left: return
         mid = (left + right) >> 1
         ms(nums, left, mid)
         ms(nums, mid+1, right)
         mere(nums, left, mid, right)
         return nums
```
| 快排 | 归并|
| --- | --- |
| 先调配出左右子数组，再对左右子数组分别排序 | 先排序左右子数组，再合并|

3. 堆排序（heap ort）

* 插入 O(logn)，取O(1)

* 写法
   * 数组元素依次建立小定堆
   - 依次取堆顶元素

         #hs
         from collections import _heapq as c
         def hs(nums):
            heap = []
            for i in range(len(nums)):
               c.heappush(heap,nums[i])
            
            for j in range(len(nums)):
               nums[j] = c.heappop(heap)
            return nums

## 3.特殊排序（O(n)）
1. 计数排序
* 额外开辟数组c，将目标数组中的元素按key(元素值，数组c的下标)-value(元素个数，数组c的值)存入数组c；反向填充数组
* 只能排序整数
* 整数值不能太大

2. 桶排序 bucket sort
* 假设输入数据服从均匀分布，设置一个定量数组作为空桶，把数据按照某函数映射关系分配到桶中，对每个桶排序，把非空桶中数据拼接起来
* 代码不要求

3. 基数排序
* 低位排序、再收集；再中位排序、再收集；然后高位排序、再收集。若有优先级，则低优先级先排序，高优先级后排序
* 代码不要求

## 4. 习题 
1. 逆序对
- 两个下标i,j 若i>j则称（i,j）是逆序对
* 高频，常用归并排序、堆排序
- **以下代码有错**
```
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
```

# 字符串

## 1. 基本概念
* java和python、Go、C#中字符串是不可变的，对字符串的增减相当于创建1个新strin
* string的比较，比较的是str指向的内存中的地址是否相同
- a-z对应asc码：97-122；A-Z：65-90；0-9：48-57；+：43；-：45
- ord('char'):求char的asc码；chr(i)：求i对应的字符
- 字符串没有del的用法,可以用replace或lstrip(char)或rstrip(char)

 
 ## 2. 高级字符串算法
 ### 1. DP
 * 升维
 ### 2. 正则表达式



