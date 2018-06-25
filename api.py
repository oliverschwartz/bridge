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
def getSubAccountsURL(): 

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


''' creates a custom role in all subaccounts '''
def createRolesInAllSubAccounts():
  arr = []
  textfile = open('subAccountURLs.txt', 'r')
  for item in textfile:
      arr.append(item.strip('\n'))
  textfile.close()

  # for item in arr: 
  extendedUrl = "https://" + arr[0] + "-lincoln.bridgeapp.com/api/author/roles"
  payload = {
  "name": 'testAPI',
  "basis_role_id": 'admin'
  }
  headers = {"authorization": api_token}
  r = requests.post(url=extendedUrl, data=payload, headers=headers)
  print(r)


''' retrieves all permissions from 'practiceadmin' role in main accounts
and saves permissions in permissions.txt '''
def getCustomRole():
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


def createCustomRole(practice, roleName):
  # extendedUrl = "https://" + practice + "-lincoln.bridgeapp.com/api/author/roles"
  headers = {"authorization": api_token,
  "Content-Type": 'application/json'}

  # # check if file 'permissions.txt' is in directory
  # if not os.path.isfile('permissions.txt'):
  #   print "permissions.txt not in directory"
  #   return

  # # textfile = open('permissions.txt')
  # # filetext = textfile.read()

  # payload = {
  # "name": roleName,
  # "basis_role_id": 'admin'
  # }
  # r = requests.post(url=extendedUrl, data=payload, headers=headers)
  # data = r.json()

  # # get id of newly created custom role
  # for role in data['roles']:
  #   if role['name'] == roleName:
  #     roleID = str(role['id'])
  #     print "roleID is: " + roleID
  #   if role.has_key('permissions'):
  #     permissionsToDelete = role['permissions'] 

  # permissionString = '''['free_trial_update,' '''
  # for permission in permissionsToDelete:
  #   if permission != 'free_trial_update':
  #     permissionString += "\"" + permission + "\","
  # permissionString = permissionString[:-1]
  # permissionString += ']'

  # delete all permissions
  url = "https://" + practice + "-lincoln.bridgeapp.com/api/admin/permissions"
  payload = {"role_id":"f1da7249-9bb1-4f68-aaff-10fbab46cf5c","permission_ids":["account_self_view","account_self_update"]}

  r2 = requests.delete(url=url, data=json.dumps(payload), headers=headers)
  print r2
  


if __name__ == "__main__":
  # print("File will be saved as 'subAccountURLs.txt'")
  # getSubAccountsURL()
  # createRoles()
  # getCustomRole()
  # createRolesInGivenSubAccount(313vets)
  # createRolesInGivenSubAccount('313vets')
  createCustomRole('313vets','test')
