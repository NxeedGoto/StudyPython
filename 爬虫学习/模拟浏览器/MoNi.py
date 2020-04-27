from selenium import webdriver
import time

# 创建浏览器
opt = webdriver.ChromeOptions()
# 无窗口模式
# opt.set_headless()
# 创建浏览器对象
driver = webdriver.Chrome(options=opt)
# 打开网页
driver.get('https://www.shanbay.com/vocabtest/')
# 加载等待
time.sleep(2)
