from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#使用chrome的webdriver   
browser = webdriver.Chrome()
action = webdriver.common.action_chains.ActionChains(browser)
#開啟google首頁
#browser.get('http://google.com/')
#如果需要執行完自動關閉，就要加上下面這一行
#browser.close()
browser.get('https://kktix.com/')
browser.find_element_by_link_text('登入').click() #點擊頁面上"天氣預報"的連結
User = browser.find_element_by_name("user[login]")
User.send_keys("user_login")
Password =browser.find_element_by_name("user[password]")
Password.send_keys("user_password")
inputElement = browser.find_element_by_name("commit")
inputElement.submit()
url = 'https://kktix.com/events/bontemps2019annsally/registrations/new'
browser.get(url)
js="var q=document.documentElement.scrollTop=100000"
browser.execute_script(js)
time.sleep(1)
#browser.find_element_by_xpath('//input[@value="agree"]').click()
browser.find_element_by_xpath('//*[@id="person_agree_terms"]').click()
#wait = WebDriverWait(browser, 5)
element =False
#element = wait.until(EC.element_to_be_clickable(By.XPATH('/*[@id="ticket_162963"]/div/span[4]/button[2]')))
#element = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ticket_162963"]/div/span[4]/button[2]')))
#if(WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ticket_162963"]/div/span[4]/button[2]')))):
#test = WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ticket_162964"]/div/span[4]/button[2]')))
#print(test)
try:
    if(WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ticket_162963"]/div/span[4]/button[2]')))):
        element = True
        
except:
        element = False
        browser.refresh()
'''else:
    element= True'''

print(element)
if(element==True):
    browser.find_element_by_xpath('//*[@id="ticket_162963"]/div/span[4]/button[2]').click()
    browser.find_element_by_xpath('//*[@id="ticket_162963"]/div/span[4]/button[2]').click()
    browser.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[5]/button').click()
else:
    browser.refresh()
    time.sleep(2)

#browser.find_element_by_link_text('知道了').click() #點擊頁面上"天氣預報"的連結
#browser.send_keys(Kyes.ESCAPE)




'''put = browser.find_element_by_xpath('//*[@id="infoModal"]/div[2]/div/div[3]/button')
action.move_to_element_with_offset(put,5,5)
action.click()
action.perform()
#ID = browser.find_element_by_id('ticket_162963')
#num=ID.get_attribute('value')
#print(num)

#ID=browser.find_element_by_id('ticket_162963').value
#ID.send_keys("2")
#js="var q=document.documentElement.scrollTop=100000"  
#browser.execute_script(js)
#p = browser.find_element_by_css_selector('checkbox')
#p.click()
'''
