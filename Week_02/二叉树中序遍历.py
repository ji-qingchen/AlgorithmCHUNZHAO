import list_to_node_to_str 
from list_to_node_to_str import Node,Deal

#以下方法都是O(n)

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





#非递归
#比递归多了“栈”功能，递归会把每次递归的结点存在栈中，读到none时弹出。非递归方法需要模拟这一过程
def inorder(root:Node):
    res = []
    stack = []
    while root or stack:
        #先是左结点入栈
        if root:
            stack.append(root)       
            root = root.left
        #所有左结点出栈，输出到结果
        else:
            tmp = stack.pop()
            res.append(tmp)
        #当前结点的右子结点入栈
            root = tmp.right
    return res

#莫里斯遍历:从外向内，根据遍历顺序把树改成链表



