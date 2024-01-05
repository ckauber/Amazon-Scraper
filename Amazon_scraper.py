#Builds an app that tracks the price of a product on amazon and emails you when a price drops
#My link is for a sewing machine

#installed Beautiful soup using 'pip install requests bs4'
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

product_URL = 'https://www.amazon.com/Heavy-Duty-4423-Decorative-Automatic/dp/B003VWXZQ0/ref=sr_1_2/ref=as_li_ss_tl/ref=as_li_ss_tl?tag=2022622-465mk509jn-20&linkCode=ll1&th=1'

#The User Agent is a string of info that your browser sends to a web server as part of an HTTP request.
#It helps the server (Amazon here) identify you and send content that is compatible with your browser. 
header = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

#This line scrapes all the information from the amazon url provided above
page = requests.get(product_URL, headers=header)

#Parses through all of the amazon HTML data
soup = BeautifulSoup(page.content, 'html.parser')

# Find the span element by class
price_element = soup.find('span', class_='a-offscreen')

title = soup.find_all(id="productTitle")
print(title)