from email import header
from http import cookies
import json,select ,subprocess,time,datetime
from time import sleep
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_PATH = r"C:\Users\Leo\AppData\Local\Google\Chrome\User Data\Default"  # 可透過網址列輸入 chrome://version/ 找到

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄

driver = webdriver.Chrome()
driver.get("https://pro.104.com.tw/psc2")
time.sleep(1)

# if __name__ == "__main__":
#     # options = webdriver.ChromeOptions()
#     options.add_argument(CHROME_PATH)
#     # options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
#     # driver = webdriver.Chrome(
#     #     executable_path='chromedriver.exe', chrome_options=options)
#     # driver.set_page_load_timeout(120)
      
# else:
# # 定位輸入框 帳號
acconet = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/input').send_keys('leo@pixis.com.tw')
pwd = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/input').send_keys('2Password')
login=driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[3]/button').click()
sleep(25)
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[4]/button').click()
sleep(5)

# 傳入字串
#element.send_keys(“leo@pixis.com.tw”)
# 定位輸入框 密碼
#element = driver.find_element_by_class_name(search)
# 傳入字串
#element.send_keys(btn btn-white btn-lg btn-block)

# 點擊打卡
#button = driver.find_element_by_class_name('btn btn-white btn-lg btn-block')
content = driver.find_element(By.XPATH,'//*[@id="PSC2"]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/span').click()
#button.click()
