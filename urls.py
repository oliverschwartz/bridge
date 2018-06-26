# dependencies
import requests
import json
import re
import os.path

# global variables
url = "https://lincoln.bridgeapp.com"
api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="
filename = 'subaccountspage.txt'

''' gets subaccount url beginnings from a .html file
saved as a .txt file (called subaccounts.txt) '''
def get_sub_accounts_urls(): 
  # check if file 'subaccountspage.txt' is in directory
  if not os.path.isfile(filename):
    print "subaccountspage.txt not in directory"
    return
  textfile = open(filename, 'r')
  filetext = textfile.read()
  textfile.close()
  regex = re.compile('''action="https://.{5,40}-lincoln''')
  matches = re.findall(regex, filetext)
  # open file to write to
  file = open('subAccountURLs.txt', 'w')
  for match in matches:
    substring = match[16:]
    new = substring.replace('-lincoln', '')
    file.write(new + "\n")
  file.close()

if __name__ == "__main__":
  get_sub_accounts_urls()


  
