
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)

'''
知识点总结：
1. 严格的格式控制
2. 注意到了for、if结尾要加：
3. range()函数使用
4. and表示并判断

for循环的格式：
for i in range(n):
    print(i)#打印i
    
range () 函数的使用是这样的:
range(start, stop[, step])，分别是起始、终止和步长

Python中and 和 or 不仅有true和false的语义，还返回值
a and b —— a 和 b 都为真时返回b,
a or b  —— a为真时返回a,否则返回 b
而C++中的&&和||只返回true或false

'''