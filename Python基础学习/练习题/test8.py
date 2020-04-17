"""
题目：输出9*9口诀。
"""

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d * %d = % -3d" % (i, j, result))
    print("")

'''
知识点总结：
print的格式化输出
print("%d * %d = % -3d" % (i, j, result))
'''