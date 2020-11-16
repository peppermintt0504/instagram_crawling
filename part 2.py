import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time

import pandas as pd
#크롭드라이브 위치 설정
#변경해야 돼
driver = webdriver.Chrome(r"C:\Users\TMSKALLT16041401\Desktop\MUN\chromedriver_win32\chromedriver.exe")

#홈페이지 접속 및 로그인

driver.get("http://biz.some.co.kr/")
driver.find_element_by_name("loginId").send_keys("uos2020") 
driver.find_element_by_name("loginPassword").send_keys("uos2020")
driver.find_element_by_id("loginBtn").click()
time.sleep(5)

#카테고리 설정 // 인스타그램 

driver.get("http://biz.some.co.kr/insightTransition")
time.sleep(5)
driver.find_element_by_id("find_saved_config").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="saved_config_list"]/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_id("execute_analysis").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="titArea"]/h2[5]/a').click()


index_data = []
text_data = []
