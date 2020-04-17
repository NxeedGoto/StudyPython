from tkinter import *
import time
import datetime

def gettime():
       s=str(datetime.datetime.now())+'\n'
       txt.insert(END,s)
       root.after(1000,gettime)  # 每隔1s调用函数 gettime 自身获取时间

root=Tk()
root.geometry('320x240')
txt=Text(root)
txt.pack()
gettime()
root.mainloop()