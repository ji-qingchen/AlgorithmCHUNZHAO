#选到end点路径和更小的那一条      
#路径和 = 较小的 + 此格本身值
#边界格不需比较大小
#顶点值为其本身

#不需要建立 dp矩阵浪费额外空间，直接遍历 grid[i][j]修改即可。
#这是因为：grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j] ；
#原 grid矩阵元素中被覆盖为 dp 元素后（都处于当前遍历点的左上方），不会再被使用到。

def path(nums:list[list]):
    m,n = len(nums),len(nums[0]) #把计算长度单拿出来会加大耗时
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue
            if i == 0:
                nums[i][j] += nums[i][j-1]
            elif j == 0:
                nums[i][j] += nums[i-1][j]
            else:
                nums[i][j] += min(nums[i-1][j],nums[i][j-1])
    return nums[-1][-1]

#解法2：把边界格单拿出来
def minPathSum( grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

