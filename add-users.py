# POST calls iterating through each sub account
import requests
import json
import datetime


api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

def add(subAccount, first_name, last_name, full_name, sortable_name, email):
    url = "https://" + subAccount + "-lincoln.bridgeapp.com/api/admin/users"
    headers = headers = {"authorization": api_token,
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
    print r2.text


if __name__ == "__main__":
    # iterate through .csv file and each user
    last_name = "Schwartz"
    first_name = "Oliver"
    full_name = first_name + " " + last_name
    sortable_name = last_name + ", " + first_name
    email = "os4@princeton.edu"
    userID = add(subAccount="313vets", first_name=first_name, last_name=last_name, full_name=full_name,
        sortable_name=sortable_name, email=email)
    make_practice_admin(userID, "313vets")