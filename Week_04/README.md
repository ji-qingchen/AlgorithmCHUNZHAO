
<font face="微软雅黑",size = 3 >学习笔记</font>

<font face = "微软雅黑">1. 递归模板</font>

	def recur(level, param):
		#terminator
		if level > max_level:
			process result
			return

		#process current 
		process(level, param)

		#drill down
		recur(level+1,newparam)

		#revert current status
		#若改变了参数则需要恢复，简单变量则不需要

2. 分治模板

	def divide(problem,param1,param2,……):
		#terminator
		if problem == None:
			print_result
			return

		#prepare data
		data = prepare_data(problem)
		subproblems = split_problem(problem,data)

		#conquer problem
		sub_result1 = self.divide(subproblem[0],p1,p2,……)
		sub_result2 = self.divide(subproblem[1],p1,p2,……)
		……

		#final result
		result = process_result(sub_result1,sub_result2,……)

		#revert current status

3. 递归相关问题
		拒绝人肉递归（画树）
		找最近最简子结构，拆成可重复解决的子问题
		数学归纳法：基础条件；递推公式

4. 动态规划（DP，动态递推）
	1 DP本质上是：分治 + 最优子结构，分治需要每个子问题都运行，DP只需运行最优
	2 与分治的
		差别：有无最优子结构、是否可淘汰次优解
		共性：找重复性
	3 关键
		1 找最优结构（分治、找重复性和子问题）（可能是各分支的累加，也可能取最值）
		2 储存此中间态
		3 DP方程（递推方程、状态转移方程）（记忆化递归或从下到上的DP递推）

		* 可以结合递推思维和DP进行理解
	4 DP思维小结
		1 形成机器思维：找重复性
		2 这是理解复杂逻辑的关键
		3 这是职业进阶的关键
	
5. 生成固定长度的列表：
		memo = [0 for _ in range(n)] 或 memo = [0]*n
		二维：
		memo = [[0]*m]*n 或 memo = [[0 for x in range(m)] for y in range(n)]
		
			前面的定义方式不如后面严谨，可能出错(所有一维数组指向同一个地址，
			
			eg:
			a = [[0]*2]*n 这种写法会使a[0][1]=1 => [[0,1][0,1][0,1]……])

6. 尾递归方式：
		
		def fibs(n):
			def fib(n,a,b):
				if n <=1:
					return b
				return fib(n-1,b,a+b)
			return fib(n,1,1)  #对于函数fibs(n)内部，fibs(n)的参数为全局变量
7. 缓存
	@lru_chache()

8. 正负无穷
	float('inf') float('-inf')

9. 快速生成字典的方式
		
		key = ['key1','key2',……]
		val = 10
		dic = dict.fromkeys(key,val)
	->  dic = {'key1':10,'key2':10,……}能多键一值，不能多键多值

10. DP从后往前推dp的原因：循环时是从前往后循环
	
	dp数组赋初值情况

11. 左上角按行遍历和按列遍历（包括对角线）
		#左上角按行 BFS
		for i in range(n):
			for j in range(i,n)			

		#左上角按列遍历 DFS
		for j in range(n):
			for i in range(0,j+1)
			
12. while (i >= 0 and j < n and s[i] == s[j]): 和 
	while s[i] == s[j] and i>=0 and j<n  不同，'and '是从左往右算，前面超出索引范围则运算不到后面

13. 列表中元素顺序可以任意调用，怎么处理？ 
	不考虑元素顺序，即不受限于列表，可以统计各元素数量后，拿出来排列组合或有其他应用
	如（题621）中，把各元素统计数量后，先把数量最多的元素排列好，其他任务插入其间隔
	
