import time
import json
import requests
import re

#Define tail follow loop function of log file
def tail(f):
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        yield line

#Define match condition and action
def process_matches(matchtext):
    while True:
        line = (yield)
#######EXCEPTIONS (NO ALERTS)
        if re.match("(.*)(EXAMPLEXCEPTION1||EXAMPLEXCEPTION2|EXAMPLEXCEPTION3)(.*)", line):
          pass
#######MATCHES (ALERTS)
        elif matchtext in line:
          print line
          webhook_url = 'https://hooks.slack.com/services/XXXXXX/YYYYYYY/ZZZZZZZ'    #YOUR SLACK WEBHOOK URL
          slack_data = {'text': '"' + line + '"'}
          response = requests.post(
          webhook_url, data=json.dumps(slack_data),
          headers={'Content-Type': 'application/json'}
)

#List log line matching keywords/phrases (comment out if you wish to specify a file for matches per below)
list_of_matches = ['BGP-5-ADJCHANGE', 'SAMPLE']            #LIST MATCH KEYWORDS/PHRASES
matches = [process_matches(string_match) for string_match in list_of_matches]

#uncomment if you wish to use a file to specify matches, refer to matches.txt sample for example
#with open ("matches.txt", "r") as matchfile:
#    list_of_matches=matchfile.read().splitlines()
#    matches = [process_matches(string_match) for string_match in list_of_matches]

#Prime matches
for m in matches:
    m.next()

#Specify log location and tail/match conditions
while True:
    auditlog = tail( open ('/var/log/sample.log') )
    for line in auditlog:
        for m in matches:
            m.send(line)
