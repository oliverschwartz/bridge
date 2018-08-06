import requests
import csv
import json

api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="
filename = "subAccount-urls-and-ids.txt"
url = "https://lincoln.bridgeapp.com/api/author/affiliated_sub_accounts/share"
headers = {"authorization": api_token,
    'Content-Type': 'application/json', 
    'Accept':'application/json'}

def push_courses():
    courses = ['EL TEAM - Listening & Questioning','EL GURU - Listening & Questioning','EL TEAM - Coaching','EL GURU - Coaching','EL TEAM - Diversity & Inclusion','EL GURU - Diversity & Inclusion','EL GURU - Building Trust','EL TEAM - Building Trust','EL TEAM - Difficult Conversations','EL GURU - Difficult Conversations','EL GURU - Influencing & Courage','EL TEAM - Influencing & Courage','EL GURU - Building a Resilient Team','EL TEAM - Building a Resilient Team','EL TEAM - Managing Conflict','EL GURU - Managing Conflict']
    index = 0

    with open('partial-registrations.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for character in row:
                if character != row[0]:
                    if character == 'Y': 
                        course_id = get_course_id(courses[index])
                        practice_id = get_practice_id(str(row[0]))
                        payload = {
                            "domain_id":practice_id,
                            "item_id":course_id,
                            "item_type":"CourseTemplate"
                        }
                        r = requests.put(url=url, headers=headers, json=payload)
                        print r
                        print "pushed " + courses[index] + " to " + str(row[0])
                    elif character == 'N':
                        course_id = get_course_id(courses[index])
                        practice_id = get_practice_id(str(row[0]))
                        payload = {
                            "domain_id":practice_id,
                            "item_id":course_id,
                            "item_type":"CourseTemplate"
                        }
                        r = requests.put(url="https://lincoln.bridgeapp.com/api/author/affiliated_sub_accounts/revoke", headers=headers, json=payload)
                        print r
                        print "revoked " + courses[index] + " from " + str(row[0])
                    index = index + 1
            index = 0
                    
def get_course_id(course_name):
    with open('courses-and-ids.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if str(course_name) == str(row[0]):
                return str(row[1])

def get_practice_id(practice_name):
    with open('sub-account-urls-and-ids.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if str(practice_name) == str(row[0]):
                return str(row[1])

if __name__ == "__main__":
    push_courses()
