import tkinter
from tkinter import *
import 价格跟踪器.Spider as Spider
import win32api, win32con


def SetUI():
    # 调用TK()初始化一个根窗口
    root = Tk()
    root.title("商品价格查询")
    root.geometry('480x120')
    # 创建Frame
    frame_HTMLURL = Frame(root)
    frame_HTMLURL.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)
    frame_Confirm = Frame(root)
    frame_Confirm.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.3)
    frame_SHOWPRICE = Frame(root)
    frame_SHOWPRICE.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.3)
    SetControl(frame_HTMLURL, frame_Confirm, frame_SHOWPRICE)
    root.mainloop()


def SetControl(frame_HTMLURL, frame_Confirm, frame_SHOWPRICE):
    # 网页地址块的布局
    LB_InputURL = Label(frame_HTMLURL, text="请输入需要查询的商品地址： ", font=("黑体", 10))
    LB_InputURL.place(relwidth=0.5)
    # 地址
    Entry_URL = Entry(frame_Confirm)
    Entry_URL.place(relwidth=1.0)

    Btn_Confirm = Button(frame_HTMLURL, text='确认选择', font=("黑体", 10),
                         command=lambda: RunSpidfe(Entry_URL.get(), frame_SHOWPRICE))
    Btn_Confirm.place(relx=0.8)

    # 价格
    LB_PRICEB = Label(frame_SHOWPRICE, text="最低价格： ", font=("黑体", 10))
    LB_PRICEB.place(relx=0.0, relwidth=0.2)
    LB_PRICEE = Label(frame_SHOWPRICE, text="当前价格： ", font=("黑体", 10))
    LB_PRICEE.place(relx=0.5, relwidth=0.2)


def RunSpidfe(x, frame_SHOWPRICE):
    try:
        LB_PRICENOW = Label(frame_SHOWPRICE, text=Spider.main(x)[0], font=("黑体", 10))
        LB_PRICENOW.place(relx=0.2, relwidth=0.2)
        LB_PRICELow = Label(frame_SHOWPRICE, text=Spider.main(x)[1], font=("黑体", 10))
        LB_PRICELow.place(relx=0.7, relwidth=0.2)
    except Exception as e:
        win32api.MessageBox(0, e.args, "提醒", win32con.MB_ICONWARNING)


if __name__ == '__main__':
    SetUI()

