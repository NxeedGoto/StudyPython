from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('500x300')

e1 = Entry(root, show='*', font=('Arial', 14))  # 显示成密文形式
e1.pack()
e2 = Entry(root, show=None, font=('Arial', 14))  # 显示成明文形式
e2.pack()

root.mainloop()