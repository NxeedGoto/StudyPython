"""
题目：要求输出国际象棋棋盘
"""

import sys

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write('')
    print('')

'''
知识点总结:

# 两者等价
sys.stdout.write('hello'+'\n')
print('hello')
print是默认调用了sys.stdout.write()方法将输出打印到控制台

stdout只能输出字符串，如果要输出数字，也需要先转成字符串形式的

chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
'''