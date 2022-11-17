from email import header
from http import cookies
import json,select ,subprocess,time,datetime
from time import sleep
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_cookies(log_url,browser):
    '''Get Cookies'''
    browser.get(log_url)
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies,indent=4,ensure_ascii=False)
    with open('cookies.json','w') as f:
        f.write(jsonCookies)

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('C:\\Users\\hank\\AppData\\Local\\Google\\Chrome\\User%20Data\\Default')
    # options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
    driver = webdriver.Chrome(
        executable_path='chromedriver.exe', chrome_options=options)
    driver.set_page_load_timeout(120)
    driver.get("https://pro.104.com.tw/psc2")


    # get_cookies('https://pro.104.com.tw/psc2',driver)
    #帶 cookie
    cookieses = None
    with open('cookies.json','r') as f:
        cookieses = json.load(f)
    for i in cookieses:
        driver.add_cookie(i)
    time.sleep(10)
    driver.set_page_load_timeout(120)
    acconet = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/input').send_keys('leo@pixis.com.tw')
    pwd = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/input').send_keys('2Password')
    login=driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[3]/button').click()
    driver.set_page_load_timeout(120)
    driver.get("https://pro.104.com.tw/psc2")
    driver.find_element(By.XPATH,'//*[@id="PSC2"]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/span').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[4]/button').click()

# 傳入字串
#element.send_keys(“leo@pixis.com.tw”)
# 定位輸入框 密碼
#element = driver.find_element_by_class_name(search)
# 傳入字串
#element.send_keys(btn btn-white btn-lg btn-block)

# 點擊打卡
#button = driver.find_element_by_class_name('btn btn-white btn-lg btn-block')
# content = driver.find_element(By.XPATH,'//*[@id="PSC2"]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/span').click()
#button.click()
pass
