#双端队列

#单调队列
#取、删单调队列最大值；添加新值，获得新的最大值（排序）

#边界条件：[]为空或k<= 0;[]长度小于k

#定义双端队列
class Deque:
    def __init__(self):
        self.items = []
    def push(self, item):
        """进队列"""
        self.items.insert(0,item)

    

    def add(self, item):
        self.items.append(item)
 
    def pop(self):
        """出队列"""
        return self.items.pop()
 
    def size(self):
        """返回大小"""
        return len(self.items)

    def remove_front(self):
        """从队头删除元素"""
        return self.items.pop(0)
    def end(self):

        return self.items[-1]

    def head(self):
        return self.items[0]

    #定义窗口
 




def win(nums:list,k:int): 
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    
    arr = []
   #new int[len - k + 1];
    arr_index = 0
    #//我们需要维护一个单调递增的双向队列
    deque = Deque()
    #先将第一个窗口的值按照规则入队
    for i in range(k):
        while deque.size()!=0 and deque.end() < nums[i]: 
            deque.pop();
        
        
        deque.add(nums[i])
        print(deque.end())
        print(deque.items)
   # //存到数组里，队头元素
    arr.append(deque.head())
    print(arr)
    

    #//移动窗口
    for j in range(k, n):  
        if (nums[j - k] == deque.head()): 
            deque.remove_front()
        print(deque.items)
        while  deque.size()!=0 and deque.end() < nums[j]:
            deque.pop();
        
        deque.add(nums[j]);
        arr.append(deque.head())
    print(arr)
    return arr

win([1,3,-1,-3,5,3,6,7],3)

    
    

