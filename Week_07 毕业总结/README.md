# **学习笔记**
# 数据结构
* 一维
    - 数组：增删O(n)，查O(1)
    - 链表: 增删O(1)，查O(n)
    - 高级
        - stack，括号匹配，直方图最大面积，盛水量，dfs，
        - queue，deque，滑动窗口，bfs；优先队列：heap
        - set（hash （O(1)）or tree(logn)），map（hash （O(1)）or tree(logn)）
* 二维
    - tree：
        - bfs，dfs，爬楼梯、硬币兑换问题
    - graph：图的遍历，如找离所有岛距离最远的点
    - 高级：
        - BST（RBT, AVL，B树、B+树）, 
        - heap，实现其的结构不固定：手写二叉堆：用数组模拟
        - trie，disjoin set（并查集）

* 特殊
    - 位运算（bitwise），判重，N皇后、数独问题
    - 布隆过滤器（bloom filter）
    - LRU cache

# 算法
- branch，loop，recursion
- search
    - dfs
    - bfs
    - A*启发搜索，用优先队列
- DP
    - 有最优子结构
    - 递归+备忘录，存储重复子状态
    - 写好初始状态，往上迭代填数组
    * **爬楼梯问题、硬币兑换**、股票兑换，偷房子，编辑距离、子序列、异位词、回文串
- 二分查找
- 贪心算法（可用DP替代）
- 数学和几何

# 算法模板
1. 递归
- 递归的思想：假设第n步正确，在此基础上得第n+1步
```
def recursion(level,param1,param2,……):
    # terminator
    if level > max_level:
        peocess_result
        return

    # process current logical
    process(level, data)

    # drill down
    recursion(level+1, p1, p2……)

    # reverse if need
    清除当前逻辑
```
2. 分治
```
def divide(problem, param1,param2……)：
    # terminator
    if problem is None:
        print_result
        return

    # process and generate result
    # prepare data
    data = prepare_data(problem)
    # 分出子问题
    subproblem = split_problem(problem, data)
    #解决子问题
    subresult1 = self.divide(subproblem1,p1,……)
    subresult2 = self.divide(subproblem2,p1,……)
    ……
    # 合并子问题
    result = process_result(subresult1, subresult2,……)

    # reverse if need
    清除当前逻辑

```
3. dfs
- 递归写法
```
def dfs(node,visited):
    
    if node in visited:
        return

    visited.add(node)
    process(node)

    for next in node.children:
        if not next in visited:
            dfs(next, visited)
```
- 非递归：用栈
``` 
def dfs(root,visited):

    if not root.next:
        return []

    stack = [root]

    while stack:
        node = stack.pop()

        process(node)
        nodes = generate_nodes(node)
        stack.push(nodes)   
```
4. bfs
``` 
def bfs(graph, start, visited):
    visited = set()
    deque = []
    deque.append([start])

    while deque:
        node = deque.leftpop()
        visited.add(node)

        process(node)
        nodes = generate_nodes(node)
        deque.push(nodes) 
```
5. trie
- 字典套字典的结构，key为当前字符，value为该字符指向的下一层结构；最内层为{#：#}；根节点无意义，表示搜索起点
```   
class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word ='#'   #每个路径结点必定是#，以表示此单词结束

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefult(char, {})
        node[self.end_of_word] = self.end_of_word #添加结尾

    def search(self, word):
        node = self.root
        for char in word:   #word太长
            if not char in root:
                return False
            node = node[char]
        #word太短时其最后结果为{key:{……{'#': '#'}}},正好时为{'#': '#'}
        return self.end_of_word in node

    def startWith(self,prefix):
        node = self.root
        for char in prefix:
            if not char in root:
                return False
            node = node[char]
        return True
```
6. 归并排序
- nlogn
- 找逆序对
- 一分为二；左右分别排序；合并
```
def ms(arr, left, right):
    def merge(arr,left,mid,right):
        tmp = []
        i, j = left, mid+1
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        if i <= mid:
            tmp += arr[i, mid+1]
        if j <= right:
            tmp += arr[j, right+1]
        arr[left: right+1] = tmp

    if left >= right: return
    mid = (left+right)/2
    ms(arr,left,mid)
    ms(arr,mid+1,right)
    merge(arr, left, mid, right)

```
6. 非运算判重
* N皇后的列，45°对角线和135°对角线
* 把二进制数的每一位当作每一行的状态位，0为可用，1为不可用，因为本题的每一行都须考虑上一行，所以只需要一个二进制数
```  
非位运算
def queen(n):
    def dfs(queens, pie, na):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
    for q in range(n):
        if q not in queens and p+q not in pie and p-q not in na:
            dfs(queens+[q], pie+[p+q], na+[p-q])

    result = []
    dfs([], [], [])
    return [['*' * i + 'Q' +'*' * (n-i-1) for i in queens] for queens in result]

位运算计算有效方案数
def queen(n):
    #count = 0
    if n < 1: return 0
    
    def dfs(row,col,pie,na):
        
        if row >= n:
            
            return 1

        bit = ~(col | pie | na) & ((1<<n)-1) #取得n位 二进制数，有效位数对应值为1
        count = 0
        while bit:
            p = bit & -bit #获得最低位1的幂值
            bit = bit & (bit - 1) #末位1置0，即把queen放在，末位为1的地方

            #drill down
            count += dfs(row+1, p | col, (p | pie)<<1,(p|na)>>1) #col多了一个p的位置，pie多了一个p位后往左移1位，na多了一个p位后往右移

            # col,pie,na值没有改变不需重置，drill中的直接把数值copy了一份
        return count
    return dfs(0,0,0,0)
```
