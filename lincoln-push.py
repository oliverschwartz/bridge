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
    courses = ['GROW your Exit Interview','GROW your Goals','GROW your Induction','GROW your Mental Health','GROW your Capability','GROW your Team','GROW your Procedural Fairness','GROW your Team Engagement','GROW your Knowledge','GROW your Happiness & Wellbeing','GROW your Parental Leave','GROW your Values','Chrysalis','Lincoln Advantage - Overview','Lincoln Advantage','LTS Semester 1','LTS Semester 2','LTS Semester 3','LTS Semester 4','LTS Masters 1','LTS Masters 2','LTS Masters 3','EL TEAM - Accountability','EL GURU - Accountability','EL TEAM - Social Styles','EL GURU - Social Styles','EL TEAM - Building Engagement','EL GURU - Building Engagement','EL TEAM - Building an Effective Team','EL GURU - Building an Effective Team','EL TEAM - Making Values Stick','EL GURU - Making Values Stick','EL TEAM - Self-Regulation','EL GURU - Self-Regulation','EL GURU - Self-awareness','EL TEAM - Self-awareness','EL TEAM - Making Better Decisions','EL GURU - Making Better Decisions','EL TEAM - Effective Team Meetings','EL GURU - Effective Team Meetings','EL TEAM - Increasing your Energy','EL GURU - Increasing your Energy','EL TEAM - The Power of Collaboration','EL GURU - The Power of Collaboration','EL TEAM - Increasing your Empathy','EL GURU - Increasing your Empathy','EL TEAM - Working to your Strengths','EL GURU - Working to your Strengths','EL TEAM - The Power of Happiness','EL GURU - The Power of Happiness','EL TEAM - Personal Leadership','EL GURU - Personal Leadership','EL TEAM - Goal Setting','EL GURU - Goal Setting']
    index = 0

    with open('lincolnreg.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for character in row:
                if character != row[0]:
                    if character == 'Y': 
                        course_id = get_course_id(courses[index])
                        payload = {
                            "domain_id":"128",
                            "item_id":course_id,
                            "item_type":"CourseTemplate"
                        }
                        r = requests.put(url=url, headers=headers, json=payload)
                        print r
                        print "pushed " + courses[index] + " to " + str(row[0])
                    elif character == 'N':
                        course_id = get_course_id(courses[index])
                        payload = {
                            "domain_id":"128",
                            "item_id":course_id,
                            "item_type":"CourseTemplate"
                        }
                        r = requests.put(url="https://lincoln.bridgeapp.com/api/author/affiliated_sub_accounts/revoke", headers=headers, json=payload)
                        print r
                        print "revoked " + courses[index] + " from " + str(row[0])
                    index = index + 1
            index = 0
                    
def get_course_id(course_name):
    textfile = open('courses-and-ids.txt', 'r')
    for line in textfile:
        index = line.find(",")
        if course_name == str(line[:index]):
            course_id = str(line[index+1:])
            return course_id

if __name__ == "__main__":
    push_courses()
