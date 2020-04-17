from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('500x400')

canvas = Canvas(root, bg = 'green', height = 200, width = 500)
image_file = PhotoImage(file = 'pic.gif')

image = canvas.create_image(250, 0, anchor = 'n', image = image_file)

x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0 - 50, y0 - 50, x1 - 50, y1 - 50)  # 画直线
oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0 + 50, x1, y1 + 50, start=0, extent=180)  # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20)  # 画矩形正方形
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)  # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动

b = Button(root, text = 'move item', command = moveit).pack()

root.mainloop()