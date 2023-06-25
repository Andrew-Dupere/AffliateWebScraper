import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd

import re
import requests
import bs4
from bs4 import BeautifulSoup

import time

from datetime import date

#setup filepath to selenium location
path = r'C:\Users\Andre\Downloads\chromedriver_win32\chromedriver.exe'

#establish driver for chrome
driver = webdriver.Chrome(executable_path=path)

#define site to scrape
site = 'https://academy.usconcealedcarry.com/search/instructors'

#main script
location = 'Austin'

driver.get(site)

time.sleep(1.5)

#Find the search box, enter location and press enter

searchbox = driver.find_element(By.CSS_SELECTOR,'#__next > div > div.SearchLayout_outerwrap__OXm_U > div > div.SearchPageSubhead_subhead__N7Vem.SearchPageSubhead_sticky__oY3Gx > div > div.w-full.md\:w-80.md\:mr-2 > div > div > input')

searchbox.clear()
searchbox.send_keys(location)

searchbox.send_keys(Keys.RETURN)
time.sleep(1)

#click show more to show more instrutors, 4 cicks will display 168 instructors 
showMore = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/button')
showMore.click()
time.sleep(1)
showMore.click()
time.sleep(1)
showMore.click()
time.sleep(1)
showMore.click()

#grab each individual instructor's url and save to an object
coachUrls = driver.find_elements(By.CLASS_NAME,'InstructorCard_wrap__arGO7  ')

coaches = {}

for url in coachUrls:
    coaches[url.find_element(By.TAG_NAME,'h3').text] = url.get_attribute('href')
    

    
for name, url in coaches.items():

    driver.get(url)
    sr = WebDriverWait(driver,timeout=5).until(lambda d:d.find_element(By.CLASS_NAME,"bp3-card"))

    contact = sr.text.split('\n')
    coaches[name] = contact

df = pd.DataFrame(data = coaches.values(), index = coaches.keys())

df.to_excel('coachestest.xlsx')
    


