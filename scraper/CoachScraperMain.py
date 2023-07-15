import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options

import openpyxl

import pandas as pd

import re
import requests
import bs4
from bs4 import BeautifulSoup

import time

from datetime import datetime

#setup filepath to selenium location
path = r'C:\Users\Andre\Downloads\chromedriver_win32\chromedriver.exe'

#activate headless mode
options = Options()
options.add_argument("--headless=new")

#define chrome driver for selenium
driver = webdriver.Chrome(executable_path=path,options=options)

#define site to scrape
site = 'https://academy.usconcealedcarry.com/search/instructors'

#define search term
location = 'Richmond'

driver.get(site)
time.sleep(1.5)

#Find the search box, enter location and press enter, use webdriverwait javascript rendered elements
searchbox = WebDriverWait(driver,timeout=10).until(lambda d:d.find_element(By.CSS_SELECTOR,'#__next > div > div.SearchLayout_outerwrap__OXm_U > div > div.SearchPageSubhead_subhead__N7Vem.SearchPageSubhead_sticky__oY3Gx > div > div.w-full.md\:w-80.md\:mr-2 > div > div > input'))

searchbox.clear()
searchbox.send_keys(location)

searchbox.send_keys(Keys.RETURN)
time.sleep(1.5)

#click show more to show more instrutors, 4 cicks will display 168 instructors 
showMore = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/button')

for i in range(4):
    showMore.click()
    time.sleep(0.5)
 

#save each individual instructor's url to an object
coachUrls = driver.find_elements(By.CLASS_NAME,'InstructorCard_wrap__arGO7  ')

#create a coaches dictionary with the coaches name as the key and the url as the value
coaches = {}

for url in coachUrls:
    coaches[url.find_element(By.TAG_NAME,'h3').text] = url.get_attribute('href')
    
#go to the url for each coach and update the coaches dictionary with the scraped data
for name, url in coaches.items():

    driver.get(url)
    #use webdriverwait to wait for the javascript rendered elements
    sr = WebDriverWait(driver,timeout=5).until(lambda d:d.find_element(By.CLASS_NAME,"bp3-card"))

    #select the text in the bp3-card object and add each line as a list itme
    contact = sr.text.split('\n')
    if len(contact) == 6:
        contact.insert(0,'null')

    #save the list as a value in the coaches dictionary
    coaches[name] = contact

#save the dictionary to a pandas dataframe and write the datafrime to an excel file.
df = pd.DataFrame(data = coaches.values(), index = coaches.keys())

d = datetime.now().strftime("%Y%m%d-%H%M%S")

df.to_excel(f'InstructorTables\{location}_coaches_{d}.xlsx')
     


