
#回溯

#1 hash
dic = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

#def search(digit, map):
#    if digit == '':
#        return []
#    res = []
#    def dfs(i,s):
##2 terminator
#        if i == len(digit): #层标最大为字符长度-1
#            res.append(s)
#            return 
#        #process
#        c = digit[i] #当前层key值
#        for st in map[c]: #当前values
            
#        #drill down
#            dfs(i+1,s+st) #下一层的每一个value和本层的每一个value组合，即一个循环的嵌套
#        #print(res)
   
#    dfs(0,'') # i从0开始，res为字符
#    return res #在search内调用dfs，返回dfs的返回值
#print(search('32',dic))

#利用队列bfs
import collections
def bfs(digit):
    if not digit:
        return []
    
    dic = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    que = collections.deque()
    que.append('')
    print(que)
    for i in digit: 
        for _ in range(len(que)):
            ch = que.popleft()
            for c in dic[i]:
                
                que.append(c+ch)
    return que  #que在最终层时会把上一层的结果（不符合需要）pop掉

print(bfs('32'))
