
import os
path = "C:\\Users\\MFGYF\\Desktop\\NeedRead" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     print(file)
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file, encoding='gb18030', errors='ignore'); #打开文件
          iter_f = iter(f); #创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
             # if '0.3' in line:
             #print(line);
              str = str + '\r' + line
          s.append(str) #每个文件的文本存到list中

filename = 'write_data.txt'
with open(filename,"w",encoding='utf-8') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    for i in s:
        f.write(i)




