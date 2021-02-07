学习笔记
1. not list 和 len(list) == 0 
2. 三数之和为0，第一个循环里前两个数相同遍历时能否跳过，即

        n = len(nums)
        nums.sort()
        for i in range(n):
                    if(i>0 and nums[i]==nums[i-1]):
                        continue
    若有（-2，-1，-1，2，2，……），设元组长度为n，第一个 -1 满足条件， 遍历时能把第二个 -1 略过吗：
        答：可。不考虑元组长度，-1满足条件的情况为：[-1，-1，nums[x]] 或 [-1, nums[x], nums[y]], x 和 y 均大于两个-1的下标值。
            对于前者，第二个 -1 取不到；对于后者，因不需要重复三元组，可看作第一个 -1 取过后对第二个 -1 来说这种情况已经消失了，即同样取不到。
            故循环一可略过重复元素

3. 死磕：
    1   如何实现“如果list中所有元素都大于0则输出空集”（死磕20210125晚）：
        先对数组sort，若头元素大于0则整个数组元素都大于0（忘记了sort这个前提）；右指针的边界条件老是搞错（本地
        IDE可正确运行）
    2  遍历range(n)和range(-n,0)取到的元素顺序是一样的（N叉树的前序遍历）

4. for vscode：alt + 左键：选中所有相同元素；alt + F2：多处插入光标
    for vs2019：alt + 左键拖拽：选中一个区域，同时对所有行进行相同的编辑，对应vscode alt+shift+左键竖拉
    
5. leecode的node处理：
    输入数组 -> 数组转化为链表 -> 用Solution.function()处理链表 -> 链表输出结果（链表）转化为字符串，字符串被设定为列表样式输出。
        
        数组转化为链表：
        nums = list
        # Now convert that list into linked list
        dummyRoot = ListNode(0)         #一个结点
        ptr = dummyRoot      
        for number in nums:
            ptr.next = ListNode(number)    #结点数组中的值
            ptr = ptr.next       
        ptr = dummyRoot.next
        return ptr

       链表转化为字符串：
        def ……:
            if not node:
                return "[]"
            result = ""
            while node:
                result += str(node.val) + "-> "
                node = node.next
            result + 'null'
            return "[" + result + "]"

6. 翻转函数递归方法：
    
        def reverse(head: Node):
            if head = None or head.next = None:         #最内层递归的运算
                return head       
                pre.next = head                       #最内层递归的返回值为head
            cur = reverse(pre.next)                    # f(f(f(f(f(x))))),从外往内运行，到最内一层（即最后一个结点处）开始运行if语句,得到head结点
                                                        #把head结点给cur
            pre.next.next = pre                        #head结点指向pre
            pre.next = None                 #pre指向none，为下一层迭代的尾结点                                       
            return cur                      #每一层函数的返回值为cur，前文使 cur = head，即整个链表的最后一个结点
                                            # 即最后返回head（整个链表的最后一个结点），不停递归发现#cur不变，一直是原最后结点       


7. 树定义：

        def tree(self, val):
            self.val = val
            #self.next = None , 链表
            self.left,self.right = None, None #二叉
            #self.children = None   n叉树

8. 递归法模板：需在所需函数内再定义一个函数

        def preorder(self, root):
            if root:
                self.traverse_path.append(root.val)        # 中
                self.preorder(root.left)                #左
                self.preorder(root.right)               #右

        def inorder(self, root):
            if root:
                self.inorder(root.left)    #左
                self.traverse_path.append(root.val)      #中
                self.inorder(root.right)            #右

        def postorder(self, root):
            if root:
                self.postorder(root.left)
                self.postorder(root.right)
                self.reverse_path.append(root.val)


9. why树常用递归：
    1 树的结构使不能直接到达某结点，而需要通过指针不断指向下一结点。“不断指向”是一种在原操作基础上的重复操作，即f(f(x))，且每个结点之间需要串起来
    2 树的结构具有重复性

10. 递归与迭代的区别
    递归：自己调用自己，同一个函数
    迭代：从旧值得到新值，不同的函数

11. 广度优先遍历

        def bfs(root: Node):
            li = []
            que = []
            if not root:
                return 
            que.append(root)
            while que:
                a = que.remove()
                li.append(a)
                for ch in a.children:
                    que.append(ch)
            return li

12. 堆排序分析（Heap sort）

13. 递归写法：
    1 确定终止条件
    2 处理当前层逻辑
    3 下探到下一层
    4 清理当前层

14. 堆的写法
    
15. 队列判断是否为空，不能直接 if not queue， 而应该 queue.size() == 0 ,或定义一个队列类的empty方法

16. 动态规划




