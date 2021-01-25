#bfs
def levelOrder(self, root: 'Node') -> List[List[int]]:
    res = [] #�����ս��
    if not root: 
        return []

    queue = [root]        #�ѵ�ǰ�����н���queue
        
    while queue:
        tmp = [] 
        cache = []
        for node in queue:
            cache.append(node.val) #��ǰ�㣨���У������н��              
            for c in node.children:
                tmp.append(c)        #��һ������н��
        res.append(cache)  #�ѵ�ǰ������н��ֵ��res
        queue = tmp    #����һ�����н���queue
           
    return res


import collections
def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root is None:
        return []
    result = []
    queue = collections.deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    return result


