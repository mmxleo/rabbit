import json,time,datetime,os
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    filePath = 'config.json'
    with open(filePath,'r') as f :
        condata = json.load(f)
    account, pwd, status =condata['Account'], condata['Pwd'], 0
    url = 'https://pro.104.com.tw/psc2'
    webDriver = webdriver.Chrome(executable_path='chromedriver.exe')
    webDriver.implicitly_wait(120)
    webDriver.get(url)
    webDriver.maximize_window()
    accounttext = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/input')
    pwdtext = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/input')
    loginbtn = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[3]/button')

    #如果沒有 cookies.json 檔就先手動登入並輸入驗證碼後產生 cookies.json 檔
    if not os.path.isfile('cookies.json') :
        accounttext.send_keys(account)
        pwdtext.send_keys(pwd)
        loginbtn.click()
        time.sleep(90)
        with open('cookies.json','w') as f:
            f.write(json.dumps(webDriver.get_cookies(),indent=4,ensure_ascii=False))
        os._exit(0)

    # Add Cookies to webDriver
    with open('cookies.json','r') as f:
        for cookie in json.load(f):
            webDriver.add_cookie(cookie)

    #帶 cookies 登入
    accounttext.send_keys(account)
    pwdtext.send_keys(pwd)
    loginbtn.click()
    time1 = datetime.datetime.strptime('08:30:00', '%H:%M:%S') #打開卡使時間
    time2 = datetime.datetime.strptime('09:30:00', '%H:%M:%S') #遲到時間
    time3 = datetime.datetime.strptime('17:30:00', '%H:%M:%S') #打開卡使時間
    time4 = datetime.datetime.strptime('18:30:00', '%H:%M:%S') #遲到時間
    while True :
        nowtime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S') #現在時間
        if status !=1 and nowtime >= time1 and nowtime <= time2 :
            webDriver.find_element(By.CLASS_NAME,'btn-block').click() #點擊打卡
            status = 1
            condata['Punchin'] = nowtime.strftime('%H:%M:%S')
            with open(filePath,'w') as f :
                f.write(json.dumps(condata,indent=4,ensure_ascii=False))
        if status != 2 and nowtime >= time3 and nowtime <= time4 :
            if not condata['Punchin'] or nowtime > datetime.datetime.strptime(condata['Punchin'],'%H:%M:%S')+datetime.timedelta(hours=9) :
                webDriver.find_element(By.CLASS_NAME,'btn-block').click() #點擊打卡
                status = 2
        time.sleep(60*5) #五分鐘檢查一次

