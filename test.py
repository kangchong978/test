from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datalist import *



def startScript(username,password,listRoomChar):
    print(list_room(listRoomChar))
    targetList = list_room('a')

    # appium服务监听地址
    server='http://localhost:4723/wd/hub'

    # app启动参数
    desired_caps={
      "platformName": "Android",
      "appium:deviceName": "STK_L22",
      "appium:appPackage": "com.haochang.party",
      "appium:appActivity": "com.haochang.chunk.controller.activity.logo.LogoActivity"
    }
    
    # 驱动
    driver = webdriver.Remote(server,desired_caps)
    driver.update_settings({"waitForIdleTimeout": 100})
    wait = WebDriverWait(driver,10)

    # submit view
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/submitView"))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_button"))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_button"))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/skipView"))).click()
    time.sleep(1)
    try:
        wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/loginActivity_tv_newAccountsOrHistoriesAccountsHint"))).click()
        time.sleep(1)
    except:
        print("switch new not found")
    wait.until(EC.presence_of_element_located((By.XPATH,"(//android.widget.ImageView[@content-desc=\"全民Party\"])[6]"))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/emailActivity_et_email"))).send_keys(username)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/emailActivity_et_password"))).send_keys(password)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/emailActivity_btn_login"))).click()
    time.sleep(3)
    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/homePopupIvClose"))).click()
        time.sleep(1)
        print("Close events dialog")
    except:
        None
        
    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/gift_close"))).click()
        time.sleep(1)
        print("Close gift dialog")
    except:
        None
       
    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/top_search_layout"))).click()
    #loop from here

    def runAutomation(items,fallback):
        skipped=[]
        i=0
        for item in items:
            i=i+1
            print(f"{item} ({i}/{len(items)})")
            wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/ed_search"))).send_keys(item)
            time.sleep(1)   
            wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/tv_search"))).click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]"))).click()
            time.sleep(1)
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/editPassword_iv_close"))).click()
                print("Close password")
            except:
                
                try:
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/roomActivity_fl_guideKnown"))).click()
                    print("Close guide")
                except:
                    None
                try:
                    wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/roomMainFragment_tv_receiveKBeanTimeCountDown"))).click()
                    time.sleep(1)
                    wait.until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View"))).click()
                    time.sleep(1)
                    
                except:
                    print("Skip pig")
                    skipped.append(item)
            #    try:
            #        wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/normalRoomCollectHintDialog_iv_close"))).click()
            #        time.sleep(1)
            #    except:
            #        print("skip close hint")
                wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/room_head_back_img_right"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/outView"))).click()
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.ID,"com.haochang.party:id/ed_search"))).click()
                time.sleep(1)
            #end loop from here

        if len(skipped)>0 and fallback != False:
            print("Retry skipped")
            runAutomation(skipped,False)
        elif len(skipped)>0:
            print(f"{skipped} are skipped")

        

    runAutomation(targetList,True)
    driver.quit()



class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
users = [User("ch0ngkang10005@gmail.com","111111")]
tableRow = "a"
for user in users:
    print(f"now running : {user.username}")
    start_time = time.time()
    startScript(user.username,user.password,tableRow)
    print(f"Execute time : {time.time() - start_time}")
    

    
