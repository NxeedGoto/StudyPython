"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)

'''
知识点总结：
列表是由一系列元素顺序排列的集合。即列表是有序集合
fruits = ['apple', 'banana', 'peach', 'strawberry']
具有添加(append)、插入(insert)、删除(del)...等方法

元组与列表很像，是不可变的列表，即不能修改值。但是元组的元素可以是列表，而列表的值可变
dimensions = (200, 100, 500)
print(dimensions[2])
for dim in dimensions:
    print(dim)
'''
