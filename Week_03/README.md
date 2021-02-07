学习笔记
1. collections
    collections.Counter(s), 返回s中各元素的个数，输出dict
    collections.namedtuple('typename', 'field_name'), 创建一个tuple对象 
        eg:

            Point = collections.namedtuple('Point', ['x', 'y'])
            p = Point(1, 2)
        >>> p.x
            1
        >>> p.y
            2
2. dict 的定义方法：

        eg:

            c = dict([('a',1), ('b', 2)])
        >>> c = {'a':1, 'b':2}
3. 获取dict中最大value值对应的key

            dict a
            max(a, key = a.get)
4. 分治法

        terminator
        process(split),（subproblem）
        drill down ,merge(subresult)
        reverse states

5. 众数分治法：
    不断二分，最后会达到left == right的边界情况，取左端点值；
    左右子问题众数相同则必为总众数；不同时需比较两个众数
    左右边界函数都可以取到，中点归左边界

6. 投票法（BM法）：抵消法

7. N皇后
    皇后的走法：横竖两斜线上的皇后可以相互攻击，格数不限。可知每一行每一列只有一个皇后Q，需判断45°和135°线上的皇后分布方案。
    n x n 棋盘中，45°线从（0，0）到（n，n）点算，共有 2 * (n-1) - 1 = 2n - 1条，135°同理。

    斜边表示法：结合坐标知识，每个点表示为（row，col）, 则 若把左上角作为(0, 0)点，则 45°线相当于坐标轴里的135°线，满足 y = -x + k，即此线上的点满足
        col + row 为恒定值；同理只135°线满足 y = x + k, 即 col - row 为恒定值

    回溯法：DFS，前序遍历

        col = set(); pie = set(); na = set(); result = []    #预准备
        if n == 0: return result     #特殊情况

        def dfs(n, row, state):
    
            #terminator
            if row > n:
                result.append(state)
                return result

            #current level logical
            for col in range(n):     #当前行的每列
                if col in col or col + row in pie or col - row in na:
                    continue
                col.add(col); pie.add(col + row); na.add(col - row)

        #drill down
        dfs(n, row+1, state+[col]) #在上一层状态下考虑

        #reverse state
        col.remove(col); pie.remove(col + row); na.remove(col - row) #全局变量初始化

8. Flood fill 算法是从一个区域中提取若干个连通的点与其他相邻区域区分开（或分别染成不同颜色）的经典算法。如一个区域内数字相同，构成连通区域，则把这个区域都置0
9. map(sink, (i-1, i+1, i, i), (j, j, j+1, j-1))
    映射：sink为函数，(i……) 中各项分别与(j……)中各项相对应，其可以写成如下形式：
    sink(i-1, j)
    sink(i+1, j)
    sink(i, j+1)
    sink(i, j-1)

10. BFS: 层序遍历
        
        def bfs(graph, start, end):
            queue = []
            queue.append([start])
            visited.add(start)

            while queue:
                node = queue.leftpop() 
                visited.add(node)
                process(node)   #处理当前结点

            #取得点node的子结点，加入队列
                nodes = generate_nodes_related(node)
                queue.push(nodes)

11. DFS : 只要有——>就会沿着箭头方向走

        def dfs(node):
        #terminator
            if node in visited:
                return 
        #current
            visited.add(node)
            process(node)
        #drill down
            for next_node in node.children:
                if not next_node in visited:
                    dfs(next_node, visited)







        


