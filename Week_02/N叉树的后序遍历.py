#递归
def postorder(self, root: 'Node') -> List[int]:
    res = []
        
    def han(root):
        if not root:
            return
        if root:
            for i in range(len(root.children)):
                han(root.children[i])
                    
            #return root
        res.append(root.val)
    han(root)
    return res

#迭代 #栈，左右中->  -> 中左右反转
def postorder(self, root: 'Node') -> List[int]:
        
    res = []
    #tmp = []
    stack = []
    stack.append(root)
    if not stack:
        return
    while stack:
        #先是根结点入栈
            a = stack.pop()
            if a:
                res.append(a.val) 
                n = len(a.children)                   
                for i in range(n):
                    if a.children[i]:
                        stack.append(a.children[i])
    #         tmp.reverse()
    #         res += tmp
    #         tmp = []
    res.reverse()        
    return res