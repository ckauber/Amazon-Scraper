#Builds an app that tracks the price of a product on amazon and emails you when a price drops
#My link is for a sewing machine

#installed Beautiful soup using 'pip install requests bs4'
#pip install lxml
#pip install requests
import requests                         #requests package helps us get HTML from amazon
from bs4 import BeautifulSoup           #data parsing library
import time

#Amazon blocked me so I have to use different website
product_URL = 'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'

#The User Agent is a string of info that your browser sends to a web server as part of an HTTP request.
#It helps the server (Amazon here) identify you and send content that is compatible with your browser. 
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}


#This line scrapes all the information from the amazon url provided above
page = requests.get(product_URL, headers=headers)

f = open("html_code.txt", "w")
f.write(page.text)
f.close()
print(page.text)

#Parses through all of the amazon HTML data
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("h1").text.strip()
print("The title is", title)

price = soup.find("p", {"class":"price_color"}).text.strip()
print("The price is", price)


