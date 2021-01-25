#相当于三个数组的合并：三个指针，最小值入最终数组
#去除重复项
#三个数组是虚指，只要得出相应的值，不需要知道相应数组什么样
def find(n):
    res = [1]
    p2, p3, p5 = 0, 0, 0 #三个指针
    for i in range(n):
        r2 = res[p2] * 2
        r3 = res[p3] * 3
        r5 = res[p5] * 5
        r = min(r2,r3,r5)
        res.append(r) #在res中添加最小值
        #添加完最小值后相应指针移动
        if r == r2:
            p2 += 1
        #并列if使遇到r == r2, r ==r3等r与多个ri值相等的情况时，相应指针都前进，从而避免了出现重复
        if r == r3:
            p3 += 1
        if r == r5:
            p5 += 1
    print(res)
    return res[n-1]
find(10)
