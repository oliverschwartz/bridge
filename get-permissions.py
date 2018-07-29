# dependencies
import requests
import json
import re
import os.path

# global variables
url = "https://lincoln.bridgeapp.com"
api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

''' retrieves all permissions from 'practiceadmin' role in main accounts
and saves permissions in permissions.txt '''
def get_custom_role_permissions():
  extendedUrl = url + "/api/author/roles"
  headers = {"authorization": api_token}
  r = requests.get(extendedUrl, headers=headers)
  data = json.loads(r.content)
  permissions = []
  for item in data['roles']:
    if item['name'] == 'practiceadmin':
      for line in item['permissions']:
        permissions.append(line)
  textfile = open('permissions.txt', 'w')
  for permission in permissions:
    textfile.write(permission + "\n")
  textfile.close()

if __name__ == "__main__":
  get_custom_role_permissions()