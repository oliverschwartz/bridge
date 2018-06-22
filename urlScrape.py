# dependencies
import urllib2
from bs4 import BeautifulSoup
import requests
import lxml

# global variables
url = "https://lincoln.bridgeapp.com/admin/sub-accounts/"
loginUrl = "https://lincoln.bridgeapp.com/login"
username = "oliver.p.schwartz@gmail.com"
password = "Chiefsmana1"

# <input type="text" 
# data-capybara="domain-name" value="almastvet" 
# class="padding-trbl-s sub-account-profile__domain-name-input">



def scrape():
	# login
	payload = {
		"login": username,
		"password": password
	}

	with requests.Session() as session:
		post = session.post(loginUrl, data=payload)
		r = session.get(url)
		print(r.text)

	# extendedUrl = url + '6'


	# page = urllib2.urlopen(extendedUrl)
	# soup = BeautifulSoup(page, 'html.parser')
	# print soup



if __name__ == "__main__":
	scrape()
