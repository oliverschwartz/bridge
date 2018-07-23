import requests
import csv
import json

api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="

if __name__ == "__main__":
    with open('subAccount-urls-and-ids.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)