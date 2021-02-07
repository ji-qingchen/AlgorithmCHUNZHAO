#遍历，dfs，改为0
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

def dy(grid):
    #dfs
    def dfs(grid, i, j):
        #teminator
        if i<0 or j<0 or i >= len(grid) or j >=len(grid[0]):
            return #超出边界时return
        if grid[i][j] == '0':
            return 
        #process
        grid[i][j] = '0'
        #drill
        dfs(grid,i-1,j)
        dfs(grid,i+1,j)
        dfs(grid,i,j-1)
        dfs(grid,i,j+1)

    #主函数
    row = len(grid)
    col = len(grid[0])
    count = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                count += 1
                print(count)
                dfs(grid,r,c)

    return count
print(dy(grid))
 

#bfs, 用队列
import collections as coll
def bfs(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    #遍历每个点
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] == '0'
                que = coll.deque([(i,j)])
                
                while que:
                    r,c = que.popleft()
                    for x, y in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]: #把root的所有子节点都处理掉；dfs是不断深入
                        if 0<= x < row and 0 <= y < col and grid[x][y] == '1':
                            
                            que.append((x,y))
                            grid[x][y] = '0'
    return count