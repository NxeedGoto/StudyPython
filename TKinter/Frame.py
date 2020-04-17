from tkinter import *

root = Tk()
root.geometry('500x300')

# 在图形界面上创建一个标签用以显示内容并放置
Label(root, text='on the window', bg='red', font=('Arial', 16)).pack()

# 创建一个主frame，长在主window窗口上
frame = Frame(root)
frame.pack()

# 创建第二层框架frame，长在主框架frame上面
frame_l = Frame(frame)  # 第二层frame，左frame，长在主frame上
frame_r = Frame(frame)  # 第二层frame，右frame，长在主frame上
frame_l.pack(side='left')
frame_r.pack(side='right')

# 创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
Label(frame_l, text='on the frame_l1', bg='green').pack()
Label(frame_l, text='on the frame_l2', bg='green').pack()
Label(frame_l, text='on the frame_l3', bg='green').pack()
Label(frame_r, text='on the frame_r1', bg='yellow').pack()
Label(frame_r, text='on the frame_r2', bg='yellow').pack()
Label(frame_r, text='on the frame_r3', bg='yellow').pack()

# 第8步，主窗口循环显示
root.mainloop()