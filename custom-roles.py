# dependencies
import requests
import json
import re
import os.path
import sys

# global variables
url = "https://lincoln.bridgeapp.com"
api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="
filename = 'subaccountspage.txt'

''' creates a custom role in all subaccounts '''
def create_roles_in_all_sub_accounts(filename):
  arr = []
  textfile = open(filename, 'r')
  for item in textfile:
      arr.append(item.strip('\n'))
  textfile.close()
  for item in arr: 
    print "creating 'practiceadmin' in " + item
    create_custom_role(item, 'practiceadmin')


def create_custom_role(practice, roleName):
  extendedUrl = "https://" + practice + "-lincoln.bridgeapp.com/api/author/roles"
  headers = {"authorization": api_token}
  # check if file 'permissions.txt' is in directory
  if not os.path.isfile('permissions.txt'):
    print "permissions.txt not in directory"
    return
  with open('permissions.txt') as f:
      content = f.readlines()
  permissionsToAdd = [x.strip() for x in content]
  payload = {"name": roleName,"basis_role_id": 'admin'}
  r = requests.post(url=extendedUrl, data=payload, headers=headers)
  data = r.json()
  permissionsToDelete = []
  # get id of newly created custom role
  for role in data['roles']:
    if role['name'] == roleName:
      role_id = str(role['id'])
    if role.has_key('permissions'):
      permissions = role['permissions']
  # delete all permissions
  for permission in permissions:
    permissionsToDelete.append(str(permission))
  for permission in permissionsToDelete:
    delete_permission(practice, permission, role_id)
  # add permissions in 'permissions.txt'
  for permission in permissionsToAdd:
    add_permission(practice, permission, role_id)


def delete_permission(practice, permission, role_id):
  if permission == 'free_trial_update' or permission == 'free_trial_get_bridge':
    return
  headers = {"authorization": api_token,
  "Content-Type": 'application/json'}
  url = "https://" + practice + "-lincoln.bridgeapp.com/api/admin/permissions"
  payload = {"role_id":role_id,"permission_ids":[permission]}
  r = requests.delete(url=url, data=json.dumps(payload), headers=headers) 
  if r.status_code != 204:
    print "error deleting " + permission + "in " + practice
    f = open('errors.txt', 'w')
    f.write("error deleting " + permission + "in " + practice)
    f.close()
  else: 
    print "successful deletion"


def add_permission(practice, permission, role_id):
  if permission == 'free_trial_update' or permission == 'free_trial_get_bridge':
    return
  headers = {"authorization": api_token,
  "Content-Type": 'application/json'}
  url = "https://" + practice + "-lincoln.bridgeapp.com/api/admin/permissions"
  payload = {"role_id":role_id,"permission_ids":[permission]}
  r = requests.post(url=url, data=json.dumps(payload), headers=headers) 
  if r.status_code != 204:
    print "error adding " + permission + "in " + practice
    f = open('errors.txt', 'w')
    f.write("error adding " + permission + "in " + practice)
    f.close()
  else: 
    print "successful creation"

def delete_role():
  arr = []
  headers = {"authorization": api_token}
  textfile = open('subAccountURLs.txt', 'r')
  for item in textfile:
      arr.append(item.strip('\n'))
  textfile.close()
  for practice in arr:
    if (practice == "313vets" and practice != "teamlincoln" and practice != "4paws"):
      print "deleting 'practiceadmin' in " + practice
      extendedUrl = "https://" + practice + "-lincoln.bridgeapp.com/api/author/roles"
      r = requests.get(url=extendedUrl, headers=headers)
      data = r.json()
      for role in data['roles']:
        if role['name'] == 'practiceadmin':
          role_id = str(role['id'])
      url2 = extendedUrl + "/" + role_id
      r2 = requests.delete(url=url2, headers=headers)
      print r2
      

if __name__ == "__main__":
  create_roles_in_all_sub_accounts(str(sys.argv[1]))



