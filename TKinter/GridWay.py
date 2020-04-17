from tkinter import *

# 虚拟一个二维表格
root = Tk()
lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
lbred.grid(column=2,row=0)
lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
lbgreen.grid(column=0,row=1)
lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
lbblue.grid(column=1,columnspan=2,ipadx=20,row=2)
root.mainloop()
