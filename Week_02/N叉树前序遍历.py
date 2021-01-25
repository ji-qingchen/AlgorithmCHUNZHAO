#递归
def preorder(root:Node):
    res = []
    def pre(root):
        if not root:
            return 
        # 前序递归
        else:
            n = len(root.chlidren)
            res.append(root.val)
            for i in range(n):    
                children = self.preorder(root.chlidren)
    pre(root)
    return res 

#迭代
def preorder(root:Node):
    stack = []
    res = []
    if not root:
        return
    stack.append(root)
        
    while stack:
        
        a = stack.pop()
        res.append(a.val) #取一个存一个
        s.extend(node.children[::-1])

        
        ''' 
        for i in range(-n, 0):                    
                    stack.append(a.children[i])


        上式中
        range(-n,0) 和range(0,n)取到的a.children[i]值顺序一样 '''
    return res


