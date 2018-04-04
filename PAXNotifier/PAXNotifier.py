from bs4 import BeautifulSoup
import requests
import facebook
import urllib3

# Web Scraping

# website urls
paxsite ='http://www.paxsite.com'
westsite ='http://west.paxsite.com/'
eastsite = 'http://east.paxsite.com/'
southsite = 'http://south.paxsite.com/'
aussite = 'http://aus.paxsite.com/'
unpluggedsite = 'http://unplugged.paxsite.com/'
devsite = 'http://dev.paxsite.com/'

# fetch the content from urls
paxsite_response = requests.get(paxsite, timeout=5)
westsite_response = requests.get(westsite, timeout=5)
eastsite_response = requests.get(eastsite, timeout=5)
southsite_response = requests.get(southsite, timeout=5)
aussite_response = requests.get(aussite, timeout=5)
unpluggedsite_response = requests.get(unpluggedsite, timeout=5)
devsite_response = requests.get(devsite, timeout=5)

# parse html
paxsite_content = BeautifulSoup(paxsite_response.content, 'html.parser')
westsite_content = BeautifulSoup(westsite_response.content, 'html.parser')
eastsite_content = BeautifulSoup(eastsite_response.content, 'html.parser')
southsite_content = BeautifulSoup(southsite_response.content, 'html.parser')
aussite_content = BeautifulSoup(aussite_response.content, 'html.parser')
unpluggedsite_content = BeautifulSoup(unpluggedsite_response.content, 'html.parser')
devsite_content = BeautifulSoup(devsite_response.content, 'html.parser')

paxsite_west_status = paxsite_content.find(id='west').find('p').getText().lower()
westsite_hero = westsite_content.findAll('section','slide-text')
westiste_hero_headers = []
westsite_hero_links = []
for sec in westsite_hero:
    westiste_hero_headers.append(sec.find('h1').getText())
    westsite_hero_links.append(sec.find('a').getText())

westsite_message = westsite_content.find('div','message')
westsite_reg = westsite_content.find(id='reg')

#Facebook

f = open('Token.txt','r')
token = f.read()
graph = facebook.GraphAPI(access_token=token, version = '2.12')

pages = graph.search(type='user', q='PAX West')