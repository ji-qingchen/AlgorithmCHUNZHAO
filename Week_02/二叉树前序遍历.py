#递归1
def inorder(root:Node):

    res = []
    def re(root):
        if not root:
            return 
        re(root.left)
        res.append(root.val)
        re(root.right)
    re(root)     #左中右都有返回值，即re函数的返回值
    return res

#递归2
def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
            # if not root:
            #     return 
        if not root:
            return []
        # 前序递归
        res.append(root.val)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return res + left + right  #左中右的值都需要返回，没有内部定义函数则需要这么写

#迭代
def preorder(root:Node):
    res = []
    stack = []
    stack.append(root)
    if not stack:
        return
    while stack:
        #先是根结点入栈
            a = stack.pop()
            if a:
                res.append(a.val)
            #print(res)
        #所有左结点出栈，输出到结果
                if a.right:
                    stack.append(a.right)
                        
                if a.left:
                    stack.append(a.left)
        #当前结点的右子结点入栈
                
    return res

