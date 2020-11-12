#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[179]:


import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time

import pandas as pd





# In[43]:


#크롭드라이브 위치 설정
#변경해야 돼
driver = webdriver.Chrome(r"C:\Users\TMSKALLT16041401\Desktop\MUN\chromedriver_win32\chromedriver.exe")


# In[44]:


#홈페이지 접속 및 로그인

driver.get("http://biz.some.co.kr/")
driver.find_element_by_name("loginId").send_keys("uos2020") 
driver.find_element_by_name("loginPassword").send_keys("uos2020")
driver.find_element_by_id("loginBtn").click()
time.sleep(5)


# In[61]:


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


# In[72]:


f = open("database.txt","w")
f.write(str(index_data))
f.write("\n")
f.write(str(name_data))
f.write("\n")
f.write(str(follow_data))
f.write("\n")
f.write(str(like_data))
f.write("\n")
f.write(str(ul_data))


# In[65]:


index_data = []
follow_data = []
ul_data = []
like_data = []
name_data = []


# In[63]:


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# In[66]:


print(index_data)
print(name_data)
print(follow_data)
print(ul_data)
print(like_data)


# In[67]:


#인스타그램 주소 추출 및 접속
driver.switch_to.window( driver.window_handles[0] )
selector = "#channelinsta > div:nth-child(1) > div.instaInfoArea > div.hashTag > a"
for i in range(1,100) :
    index_data.append(i)
    temp1 =selector[ : selector.find("(")+1]
    temp2 =selector[selector.find(")") : ]    
    selector = temp1 + str(i) + temp2
    
    elem = driver.find_element_by_css_selector(selector)

    href = elem.get_attribute('href')




#인스타그램 주소 접속
    script = f"window.open('{href}');"
    driver.execute_script(script)
    driver.switch_to.window(driver.window_handles[1])



#좋아요 데이터
    try :
        likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button/span')

        like_data.append(likes.text)


        #닉네임 데이터

        name = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div/div/a')
        name_data.append(name.text)


        #댓글 스크랩

        st_bs = bs4.BeautifulSoup(driver.page_source)
        ul_list = st_bs.find_all('ul', class_='Mr508')
        count = 0 
        for ul in ul_list:
            count += 1
            if ul.text.find("답글 보기") != -1 :
                count += int(ul.text[ul.text.find("답글 보기") + 6 :-2])
    
        
        ul_data.append(count)



        #프로필 링크 접속

        driver.find_element_by_class_name("e1e1d").click()
        time.sleep(2)


        #follower 데이터 
        followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        follow_data.append(followers.text)



        #기존 창 닫기 및 전환
        driver.close()
        driver.switch_to.window( driver.window_handles[0] )
        print(i,"complete")

    except: 
        print("데이터 처리 실패")
        driver.close()
        driver.switch_to.window( driver.window_handles[0] )

print(name_data)
print(follow_data)
print(ul_data)
print(like_data)

