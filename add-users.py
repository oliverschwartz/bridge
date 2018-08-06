import requests
import json
import datetime
import csv

api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

def add_non_learner(subAccount, first_name, last_name, full_name, sortable_name, email):
    url = "https://" + subAccount + "-lincoln.bridgeapp.com/api/admin/users"
    headers = {"authorization": api_token,
    'Content-Type': 'application/json', 
    'Accept':'application/json'}
    payload = {
        'users': [{
            "uid": email,
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "sortable_name": sortable_name,
            "email": email,
            "locale":"en",
            "hire_date": str(datetime.datetime.now().isoformat()),
        }]
    }
    
    r = requests.post(url=url, headers=headers, json=payload)
    data = r.json()

    for item in data['users']:
        if item['email'] == email:
            userID = item['id']
    return userID

def add_learner(subAccount, first_name, last_name, full_name, sortable_name, email, manager_email):
    url = "https://" + subAccount + "-lincoln.bridgeapp.com/api/admin/users"
    headers = {"authorization": api_token,
    'Content-Type': 'application/json', 
    'Accept':'application/json'}
    manager_uid = "uid:" + str(manager_email)
    payload = {
        'users': [{
            "uid": email,
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "sortable_name": sortable_name,
            "email": email,
            "locale":"en",
            "hire_date": str(datetime.datetime.now().isoformat()),
            "manager_id": manager_uid
        }]
    }
    
    r = requests.post(url=url, headers=headers, json=payload)

def make_practice_admin(userID, subAccount):
    url = "https://" + subAccount + "-lincoln.bridgeapp.com/api/author/roles"
    headers = headers = {"authorization": api_token}
    r = requests.get(url, headers=headers)
    data = r.json()

    for role in data['roles']:
        if role['name'] == "practiceadmin":
            roleID = role['id']

    url2 = "https://" + subAccount + "-lincoln.bridgeapp.com/api/admin/users/" + userID + "/roles/batch"
    payload = {
        'roles': roleID
    }
    r2 = requests.put(url2, headers=headers, json=payload)
    
if __name__ == "__main__":
    # iterate through .csv file and each user
    with open('users.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email = row[0]
            first_name = row[1]
            last_name = row[2]
            full_name = first_name + ' ' + last_name
            sortable_name = last_name + ', ' + first_name
            role = row[3]
            subAccount = row[4]
            if len(row) > 5:
                manager_email = row[5]

            if role == 'practice_admin':
                userID = add_non_learner(subAccount=subAccount, first_name=first_name, last_name=last_name, full_name=full_name,
                    sortable_name=sortable_name, email=email)
                make_practice_admin(userID, subAccount=subAccount)
                print 'enrolled practice admin'
            else: 
                add_learner(subAccount=subAccount, first_name=first_name, last_name=last_name, full_name=full_name,
                    sortable_name=sortable_name, email=email, manager_email=manager_email)
                print 'enrolled learner'
