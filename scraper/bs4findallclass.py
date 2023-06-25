# Import Module
from bs4 import BeautifulSoup
import requests
  
# Website URL
URL = 'https://www.geeksforgeeks.org/'
  
# class list set
class_list = set()
  
# Page content from Website URL
page = requests.get( URL )
  
# parse html content
soup = BeautifulSoup( page.content , 'html.parser')
  
# get all tags
tags = {tag.name for tag in soup.find_all()}
  
# iterate all tags
for tag in tags:
  
    # find all element of tag
    for i in soup.find_all( tag ):
  
        # if tag has attribute of class
        if i.has_attr( "class" ):
  
            if len( i['class'] ) != 0:
                class_list.add(" ".join( i['class']))
  
print( class_list )