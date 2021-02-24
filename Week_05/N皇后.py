# 回溯
def Queen(n):
    if n <= 1:
        return []
    result = [] #为[[],[],……]形式
    cols = set()
    pie = set()
    na = set()

    def dfs(n, row, state):

        #terminator
        if row >= n:
            result.append(state)
            return

        #current
        for col in range(n):
            
            if col in cols or row + col in pie or row - col in na:
                continue    #跳过当前col值                      
           
            cols.add(col) #if不是循环，若不continue则会往下运行直到当前循环结束
            pie.add(col + row)
            na.add(-col + row)

        #drill down
            dfs(n, row+1, state + [col]) # dfs在for循环中

        #reverse
            cols.remove(col)
            pie.remove(col + row)
            na.remove(-col + row)

    def out(n):
        board = []
        for row in result:
            for i in row:
                board.append('.'*i + 'Q' + '.'*(n-1-i)) #为['','',……]形式
           
        #for j in range(0, len(board), n):
        #    print(board[j:j+n])
        return [board[i:i+n] for i in range(0, len(board), n)] #输出[['',''],['','']]形式的解

    '''
    或def out(n):
        square,res = [],[]
        
        for re in result:
            for i in re:
                res.append('.'*i + 'Q' + (n-1-i)*'.')
                
            square.append(res)
        print(square)
        return square
    '''
    dfs(n, 0, [])
    return out(n)

print(Queen(4))

#解法2
def queen3(n):
    if n < 1: return []
    def dfs(queen:list, pie, na):
        l = len(queen)
        if l==n:
            res.append(queen)
            return None
        for q in range(n):
            if q not in queen and l-q not in pie and l+q not in na: #queen记录每行对应的列数
                dfs(queen+[q],pie+[l-q], na+[l+q]) #若改成.append(q)则len(queen)会出错
    res = []
    dfs([],[],[])
    return [[i*'.'+'Q'+(n-1-i)*'.' for i in row] for row in res]


#位运算
#用二进制数代替上面方法中的字符串；能用的格子置为1
def queen3(n):
    if n < 1: return []
    res = []
    def dfs(row,col,pie,na,queen):
        if bit == 0:
            res.append(queen)
        bit = ~(col | pie | na) & ((1<<n)-1) #所有未占据的点设为1
        while bit: #有有效格子时
            res.append(bit)

