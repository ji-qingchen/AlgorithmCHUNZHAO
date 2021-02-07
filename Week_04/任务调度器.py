'''
1 统计各元素数量，把出现次数最多(x)的元素按间隔放置好
    A '' '' A '' '' A '' '' A
    t = (x-1)*(n+1)+1
2 把其他任务插入空格中
    A 'B' 'B' A 'B' 'C' A 'B' '' A
    t = (x-1)*(n+1)+1
3 当有n个同样最多的元素时
    A 'B' '' A 'B' '' A 'B' '' A B
    t = (x-1)*(n+1)+ n
    A 'B' 'C' A 'B' 'C' A 'B' 'C' A B C  D E
    先将间隔填满，把多余元素放到最后，这种情况即数组长度大于 所有的A加间隔n 的情况
    最短时间为数组长度l：t = l
'''
def task(li:list, n: int):
    dic = {}
    l = len(li)
    for item in li:
        if item not in dic:            
            dic[item] = 1
        else:
            dic[item] += 1
        #print(dic)
    li1 = list(dic.values())
    ma = max(li1)
    c = li1.count(ma) #最大值个数
    t = (ma-1)*(n+1)+ c
    return t if t > len(li) else len(li)
    #if t <= l:
    #    return l
    #else:
    #    return t
    
