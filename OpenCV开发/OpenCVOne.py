#读取一张图片
import cv2

img=cv2.imread("C:\\Users\\MFGYF\\Downloads\\23.jpg") #读取指定位置的一副图片
cv2.namedWindow("Image") #初始化一个名为Image的窗口
cv2.imshow("Image",img) # 显示图片
cv2.waitKey(0) #等待键盘触发事件，释放窗口
