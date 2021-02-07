#回溯：dfs，前序遍历
def solveNQueens(n):    
    if n == 0:
            return []

        #预输出结果
    s = '.'* n    
    # n*n的res
    chess = []
    for i in range(n):
        chess.append(s)
    res = []; 
    

    col = set(); pie = set(); na = set(); 
        
    #解函数
    def dfs(res, chess, row):
        chess1 = chess
        #terminator
        if row == n:
            res.append(chess)
            return 
        #current logical
        for col in range(n):
        #判断当前列有无皇后
            if col in col or col + row in pie or col - row in na:
                continue
        ''' chess1[row][col] = 'Q'
            col.add(col); pie.add(col + row); na.add(col - row)     程序不运行'''       
            
        #drill down        
        dfs(row+1)
        #reverse state
        col.remove(col); pie.remove(col + row); na.remove(col - row)
    dfs(res,chess,0)    
    return res
solveNQueens(3)