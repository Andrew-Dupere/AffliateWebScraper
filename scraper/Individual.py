
import re
import requests
import bs4
from bs4 import BeautifulSoup

import selenium

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#setup filepath to selenium location
path = r'C:\Users\Andre\Downloads\chromedriver_win32\chromedriver.exe'

#establish driver for chrome
driver = webdriver.Chrome(executable_path=path)


#use BS4 to pull out the instructor card containing the contact information

url = 'https://training.usconcealedcarry.com/instructor/7d62a9de-31e1-11ec-b304-02420a0001df'

#find instructor card with selly
# card = driver.find_element(By.CLASS_NAME,"bp3-card")


driver.get(url)
sr = WebDriverWait(driver,timeout=5).until(lambda d:d.find_element(By.CLASS_NAME,"bp3-card"))

print(sr.text)

tester = sr.text

print(tester[0])
