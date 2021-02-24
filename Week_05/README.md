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


# 红黑树和AVL树
## 1. 遍历方式
```
# preorder
def preorder(self, root):
    if root:
        traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# inorder
def inorder(self, root):
    self.inorder(root.left)
    traverse_path.append(root.val)
    self.inorder(root.right)

# postorder
def postorder(self, root):
    self.postorder(root.left)
    self.postorder(root.right)
    traverse_path.append(root.val)
```
## 2. 平衡树
二叉搜索树，有很多种。*23树、B树、AVL树、红黑树*等，红黑树和AVL面试常见
### 1. **AVL 树（严格平衡）**
（发明者姓A.L.和L.）

* 平衡因子
*（判断平衡的方法）*
    * 对于二叉树上任意一个结点root，有其左子树的高度h1和右子树的高度h2,则 **h1-h2∈{-1，0，1}** 时树平衡，h1-h2即 **平衡因子**

* 旋转操作 *（使树平衡的办法）*

    * 树结构为 左左型，则右旋
    * 树结构为 右右型，则左旋
    * 左右型，左右旋
    * 右左型，右左旋
    * **带子树同理**

### 2. 二三树
   * 严格平衡的 **二叉树**
   * 二、三指二叉、三叉
   * 二结点存储1个key(和值)，与普通二叉搜索树相同
   * 三结点存储2个key(和值)，左链指向的树小于两个key，**中链在两个key之间**，右链大于两个key
   * **所有leaf都在同一层**

#### 1 查

#### 2 插入a
* a不会插入空结点
* 要插入的结点为二结点，则直接加入形成三结点
* 要插入的结点为三结点
   * 此结点父结点为二结点
   
   将a插入当前结点形成四结点，把中间key并入父结点中形成三结点。a成为此三结点的子结点

   * 此结点父结点为三结点

   将a插入当前结点形成四结点，把中间key并入父结点，a成为此父的子结点；把父结点的中键key并入爷结点，父结点的左key和右key分别成为爷结点的左子树和右子树，以此类推

#### 3 删除a
(1) 删除leaf

1) a在三结点中：直接删除
2) a在二结点中，左或右兄弟结点为三结点，若向左借，则借其右key代替父结点中左key，父结点中原左key代替此结点成为子结点；若向右借，则借其左key代替父结点中右key，父结点中右key代替此结点成为子结点
3) a、兄弟结点皆2，父为3，则父结点中左key与a的左兄弟合并，或右key与a的右兄弟合并后，删除a

(2) 删除枝结点a

1) 取a的右子树中的最小key代替a成为新的枝结点；
2) 右子树中三结点无法维持时将其左key与其二子结点结合，子结点形成三结点
3) 右子树中三结点用完后用左子树的
4) 删到所有leaf不能在同一层时要对树的结构进行调整，形成新的二三树

### 3. **红黑树（red-black-tree），近似平衡**

概念
* 黑结点：普通结点
* 红结点：可与父结点形成三结点的结点
* 近似平衡的二叉树
* 任意节点左右子树高度差 **小于等于** 2倍

eg. 左树高4，则右树高>=2或<=8

特点
* 根节点为黑结点
* leaf全是null的黑结点
- 不能有相邻红结点
* 只有黑结点或红结点
- 从root到leaf所有路径上经过相同数量的黑结点

### 4. B树


***
---
对比

| AVL树 | 红黑树 |
| --- | --- |
| 查找更快，因为其更平衡 | 比AVL慢 |
| 增删慢，因为结构改变时结点存储的平衡指针也要改变 | 增删快比AVL快，因为要维护的数据量少 |
| 存储信息多，占用空间大 | 占用空间小 |
| 适用于读多的场合 | 适用于写多或读写平衡的场合 |
|  |   |



# 位运算
## 1. 位运算符
<<左移，空位补0；>> 右移，空位补0

| 按位或； & 按位与； ~ 按位取反； ^ 按位异或（不进位加法）
* 异或
   - x ^ 0：x 
   - x ^ 1s(全为1)：~x 
    - x ^ ~x：1s(全为1)
    - x ^ x : 0
    c = a ^ b,则 a = c ^ b, b = a ^ c
    - 结合律：a ^ b ^ c = (a ^ b) ^ c = (a ^ b) ^ c

## 2. 指定位置位运算
*(二进制数从右往左依次为第0位、第1位……)*
- x最右n位清零：(~0) << n & x
- 获取x第n位（从右往左）：x>> n & 1
- x第n位幂值：1 << n & x
- 仅将第n位置1：1 << n | x
- x最高位至第n位（含）清0：(1 << n -1 ) & x

## 3. 实战位运算要点
- 判断奇偶：x & 1，奇数为1，偶数为0
- x >> 1，相当于x/2
- x & (x-1): 最低位1清0
- x & (-x): 得到最低位的1
   - -x = ~x + 1，x的补码
- x ^ ~x = 0

## 4. 实例
- **位运算不一定把n转为二进制格式，因为数值在计算机中本就以二进制格式存储。**

* bin(n).count(1)：把n转化为二进制后计算其中的1的数量

- 十进制转化为：
   * 八进制：oct(n)
   * 十六进制：hex(n)
   * 二进制：bin(x)

- 在二进制表示中，x + 1 表示将该 1 移动到 x 中最右边的 0 的位置上，并将所有较低位的位设置为 0
- (x - 1) 代表了将 x 最右边的 1 设置为 0，并且将较低位设置为 1

