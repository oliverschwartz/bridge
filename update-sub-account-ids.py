import requests
import json
import urllib2

api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

def update_sub_account_ids():
    # url = "https://lincoln.bridgeapp.com/api/author/sub_accounts?limit=9999"
    headers = {"authorization": api_token}
    # r = requests.get(url, headers=headers)
    # data = r.json()
    # subAccounts = data['sub_accounts']
    # for account in subAccounts:
    #     print account['id']
    #     print account[]

    

    url = "https://lincoln.bridgeapp.com/api/author/sub_accounts?limit=9999"

    response = urllib2.urlopen(url)
    webContent = response.read()

    f = open('asdf.html', 'w')
    f.write(webContent)
    f.close

if __name__ == "__main__":
    update_sub_account_ids()