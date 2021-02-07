'''按顺序计算5的数量
nums = [5,5,10,10,20]
count = 0
money = 0
for num in nums:
    #找得起
   money += 5
   if num > money + 5:
       print('no')
       break
   else:
       #找得开:有5
       
       print('yes') '''

#可从局部最优解推算出全局最优解，故贪心算法
nums = [20,5,10,20,20]
five = ten = 0
for num in nums:
    if num == 5:
        five += 1
    elif num == 10:
        ten += 1
        five -= 1
    else:
        if ten > 0:
            ten -= 1
            five -= 1
        else:
            five -= 3
    if five < 0:
        print('no')
        break
    else:
        print('yes')
