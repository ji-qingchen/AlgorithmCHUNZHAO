class Node:
    def __init__(self, val, next= Node):
        self.val = val
        self.next = next
#从前往后
def sortnoode(link1:Node, link2:Node):
    #terminator
    
    if not link1: return link2
    if not link2: return link1
    #current
    if link1.val >= link2.val:
        link2.next = sortnoode(link1, link2.next)
        return link2
    else:
        link1.next = sortnoode(link1.next, link2) 确定当前结点的next
        return link1 确定当前结点

def mere(l1:Node,l2:Node):
    if l1.val >= l2.val:
        l1,l2 = l2,l1
    l1.next = mere(l1.next,l2)
    return l1 or l2 #l2是层内递归要用到的结点，在层内l1空时用，l1是最外层结点

#非递归，新建一个链表
def nex(l1:Node,l2:Node):
    cur1 = Node(0)
    cur = cur1 #cur是变化的结点，最后返回需要head结点，故需要记录下head结点；Node本质上是一个int量，所以其复制是深度复制
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next 
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2 #补上最末结点
    return cur.next
    


