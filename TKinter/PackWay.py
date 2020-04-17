from tkinter import *

root = Tk()
lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
lbred.pack()
lbgreen = Label(root,text="绿色",fg="green",relief=GROOVE)
lbgreen.pack(side=RIGHT)    # 本控件的布局相对于下一个控件的方位
lbblue = Label(root,text="蓝",fg="blue",relief=GROOVE)
lbblue.pack(fill=X)         # 控件向水平方向填充未被占用控件
root.mainloop()
