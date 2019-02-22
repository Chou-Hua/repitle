from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select #控制下拉式選單

#圖片辨識用 驗證碼
from PIL import Image,ImageEnhance
import pytesseract
import requests
import re

#使用chrome的webdriver   
browser = webdriver.Chrome()
action = webdriver.common.action_chains.ActionChains(browser)

browser.get('https://tixcraft.com/')
browser.find_element_by_link_text('會員登入').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="loginFacebook"]').click()
User = browser.find_element_by_name("email")
User.send_keys("user_email")
Password =browser.find_element_by_name("pass")
Password.send_keys("user_password")
inputElement = browser.find_element_by_name("login")
inputElement.submit()

url = 'https://tixcraft.com/activity/detail/19_BLACKPINK'
browser.get(url)
browser.find_element_by_link_text('立即購票').click() 
browser.execute_script("window.scrollBy(0, 600)")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="gameList"]/table/tbody/tr/td[4]/input').click()
time.sleep(1)
browser.find_element_by_partial_link_text("搖滾A區5800").click() 
time.sleep(1)
select = Select(browser.find_element_by_name('TicketForm[ticketPrice][01]'))

select.select_by_value("2")
browser.find_element_by_xpath('//*[@id="TicketForm_agree"]').click()

#驗證碼處理部分
location = browser.find_element_by_id('yw0').location
size = browser.find_element_by_id('yw0').size
left = location['x']
top  = location['y']
right =location['x']+size['width']
bottom =location['y']+size['height']

screenImg = "E:/Users/Andy/Desktop/cahch_img.png"
imgsrc= browser.find_element_by_id('yw0').get_attribute('src')
if (imgsrc):
	browser.get_screenshot_as_file(screenImg)
	location = browser.find_element_by_id('yw0').location
	size = browser.find_element_by_id('yw0').size
	left = location['x']
	top =  location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']
	img = Image.open(screenImg).crop((left,top,right,bottom))
	img = img.convert('L') 			
	img = ImageEnhance.Contrast(img)
	img = img.enhance(2.0) 			
	img.save(screenImg)
	img = Image.open(screenImg)
	code = pytesseract.image_to_string(img)
	browser.find_element_by_id("TicketForm_verifyCode").send_keys(code.strip())
	print(code.strip())
	print("OK")


