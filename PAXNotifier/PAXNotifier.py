from bs4 import BeautifulSoup
import requests
paxsite ='http://www.paxsite.com'
westsite ='http://west.paxsite.com/'
# fetch the content from url
paxsite_response = requests.get(paxsite, timeout=5)
westsite_response = requests.get(westsite, timeout=5)
# parse html
paxsite_content = BeautifulSoup(paxsite_response.content, "html.parser")
paxsite_west_status = paxsite_content.find(id='west').find('p').getText().lower()
westsite_content = BeautifulSoup(westsite_response.content, "html.parser")
# westsite_status = westsite_content.find()

print(paxsite_west_status=='see you next time')