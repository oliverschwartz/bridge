import requests
import json
import csv

api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

def turn_on_notifications(practiceUrl):
    extendedUrl = "https://" + str(practiceUrl) + "-lincoln.bridgeapp.com/api/config/sub_account/notifications"
    headers = {"authorization": api_token, "Content-Type":"application/json", 'Accept':'application/json'}
    payload = {'config': {"notifications": True}}
    
    unsuccessfulRequest = True
    while unsuccessfulRequest:
        try:
            r = requests.patch(url=extendedUrl, headers=headers, data=json.dumps(payload))
            if r.status_code == 200:
                unsuccessfulRequest = False
        except Exception, e:
            print("Error turning on notifications: " + str(e))
            print("retrying...")
    print('notifications turned on')
    print(r.text)

if __name__ == "__main__":
    with open('sub-account-urls.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            turn_on_notifications(row[0])
        
    