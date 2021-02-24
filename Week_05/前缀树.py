
#非动态实现



# 动态方式
class Trie:
    def __init__(self):
        #程序运行：把trie的结构放入root中
        self.root = {} #key:字符 value:下一结点的位置
        self.is_End = '#'

        #存在则继续下探，不存在则新建结点
    def insert(self, word:str):
        node = self.root
        
        for char in word:
            node = node.setdefault(char, {}) #若node中有char，则把此处value给node
            #print(self.root,node)       #否则新建一个字典{char:{}} 给node，因为insert需要在分歧处新建分支
        node[self.is_End] = self.is_End #结尾标记
        
    #存在则继续下探直到is_End,不存在则直接返回
    def search(self, word:str):
        node = self.root
        for char in word:
            if not char in node:
                return False
            node = node[char] 
        
        return self.is_End in node  #词存在，则树中对应其最后一个字符的结构为{char:{'#':"#"}}

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if not char in node: #有其他字符或太长均符合这种情况
                return False
            node = node[char]
        return True
t = Trie()
t.insert('apple')
t.insert('app')
print(t.root, t.search('apple'))