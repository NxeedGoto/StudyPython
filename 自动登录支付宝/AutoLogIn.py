# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://authzui.alipay.com/login/index.htm")
login_windows = driver.current_window_handle
try:
    element = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "J-input-user"))
    )
    pe = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "password_rsainput"))
    )

    login_btn = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "J-login-btn"))
    )
    if element and pe and login_btn:
        element.send_keys("*******")  # 参数为您的支付宝帐号
        pe.click()
        pe.send_keys("xxxxxxx")  # 在此输入您的支付宝密码
        time.sleep(10)
        # login_btn.send_keys(Keys.ENTER)
        login_btn.click()
        time.sleep(5)
        driver.implicitly_wait(10)
        print
        driver.current_window_handle
        driver.switch_to.window(driver.current_window_handle)
        login_el = driver.find_element_by_link_text("转 账")
        login_el.click()