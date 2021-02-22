# **学习笔记**
# 字典树和并查集
## 1. 树
* root，child, leaf, 层，子树，二叉树，O(n)、O(深度)
* 遍历：前（根左右）、中（左根右）、后（左右根）

* 二叉搜索树（sorted binary tree）: 
   * 包括空树
   * **所有结点满足：左< 根 < 右（易错点）**
   - 中序遍历（in-order)是升序遍历
   - 查、删、增：O(logn)，二分法
   - 删：leaf直接删；内部的结点删掉后取此节点右子树最小值替代它

## 2. 字典树(trie)
单词查找树/键树，用于统计和排序大量字符串

### 1. 特点
* 结点不存完整单词
* 结点对应字符串为从root到该结点所经过的路径上的所有字符组成
* 所有路径经历的字符不同
* **结点存储： 从此结点到下个结点的路径**

### 2. 结点可存储额外信息，如出现的频次等

### 3. 内部实现
1. 实现

对二叉树，有node.val存值, node.next指向子结点，而对trie
* 需要判断 **此结点是否为leaf**，在trie中，一个完整词的结尾必定是leaf（前缀包含单词不代表这个单词存在，eg. team中包含tea，但team存在不代表tea存在）

* **root表示初始结点，无实际意义；node.next指向一个数组[]**

    ```
    def trieNode:
        def __init__(self):
            self.children = collections.defaultdict(trieNode)
            self.isEnd = False
    ```
2. **trie特点**

  * 以空间换时间

    如对于全小写的单词，可以动态的建立分叉，最初0叉，最差26叉；树深度即单词长度
  * 用公共前缀来降低搜索时间
* 可以实现输入前几个字符，显示所有此前缀的候选词的功能
![trie实现](C:\Users\姬清晨\source\repos\复习"trie实现.png")

## 3. 习题笔记
1. dict.setdefault(key, default = {})
    key为要查找的值；default为设置的默认值；
    key存在时返回key对应的value, 不存在时新建一个字典{key: {}}

2. dict.get(key, default = 默认值)
    key存在时返回其对应value，不存在时返回默认值

3. collections.defaultdict(key, 类)
    key存在时返回对应value，不存在时返回 类 的默认值

4. - list1 = list2: 两者指向同一对象
   - list1 = list2.copy() 浅拷贝，list1 和list2相互独立但其子列表指向同一对象
   - list1 = copy.deepcopy(list2) 深层copy，两者彻底独立
   
5. 







## 1 初级搜索
### 1 朴素搜索（简单粗暴，多数情况）
### 2 优化方向
不重复（缓存，如fibonacci）、剪枝（去掉次优分支，如DP？） 
### 3 搜索方向
递归
+ BFS: queue，先入先出：collections.deque

- DFS: stack，后入先出：pop、append

## 2 高级搜索
双向搜索、启发式搜索（A*算法、优先级搜索）
### 1. 双向搜索
从root和leaf两端同时进行BFS，到中间相遇
### 2. A*算法
利用优先队列
***
DFS模板
```
visited = set()
def dfs(node, visited):
# terminator
    if node in visited:
        return
# current progess logical 
    progess(node)
    visited.add(node)
# drill down
    for next in node.children:
        dfs(next, visited)
```
#### BFS模板
```
    def bfs(graph, start, end):
        deque = []
        visited = set()  
        deque.push([start])  #图需要把所有start都入队
        visited.add(start)  #图无向，故必须标记是否访问过，在加入队列前标记为访问，可避免点被重复利用

        while deque:
            node = deque.popleft()
            visited.add(node)
            process(node)     

            nodes = generate_node_related(node)
            deque.push(nodes)
```
---



