import requests
from requests.packages.urllib3 import add_stderr_logger
import sys
from bs4 import BeautifulSoup as bs

add_stderr_logger()
s = requests.Session()

s.headers['User-Agent'] = 'Chrome'

username = 'myusername'
password = 'mypwd'
url = 'https://github.com/login'

# after examining the HTML of the website you're trying to log into
# set name_form to the name of the form element that contains the name and
# set password_form to the name of the form element that will contain the password
login = {'login': username, 'password': password}
login_response = s.post(url, data=login)
for r in login_response.history:
    if r.status_code == 401:  # 401 means authentication failed
        print 'error!'
        sys.exit(1)  # abort


pdf_response = s.get('https://github.com/settings/emails')  # Your cookies and headers are automatically included
soup = bs(pdf_response.content)