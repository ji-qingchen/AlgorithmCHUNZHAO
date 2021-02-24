#层序遍历
#不能作为多源层序遍历处理，因为同一点可能被不同源多次访问

#import collections,copy
#def bfs(nums,s:str):
    
#    deque = collections.deque()    
#    m, n = len(nums),len(nums[0])
#    l, k = len(s), 0
#    cat = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
#    visited = []
#    res = []

#    #初始条件
#    for i in range(m):
#        for j in range(n): 
#            deque.append([i,j]) #所有点都可能被访问
                      
#    while deque:
#        cur = deque.popleft()                
        
#        for ca in cat:                   
#            x1, y1 = ca[0] + cur[0], ca[1] + cur[1]
#            if 0<=x1<m and 0<=y1<n and [x1,y1] not in visited:
#                if nums[x1][y1] == s[k]:                
#                    res.append([x1,y1])                    
#                    l -= 1 #若符合条件则要比较的s长度减一
#                    k += 1
#                visited.append([x1,y1])
#                print(len(visited))            
#            print(res)
#        if l == 0:
#            return True
#    return False

#print(bfs([["a","b"],["c","d"]],"acdb")) #问题，已访问的点中可能有满足要求的点，不同分支应互不相关




                
                
                

