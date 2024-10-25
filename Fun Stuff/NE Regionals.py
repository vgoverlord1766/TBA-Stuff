import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

state_initials = ["MA", "NH", "VT", "CT", "RI"]

ne_event_list = []

for i in range (1998, 2014):
    events_responses = requests.get("https://www.thebluealliance.com/api/v3/events/" + str(i),
                                    params=parameters)
    event_list = json.loads(events_responses.content)

    print(event_list)
    for event in event_list:
        print(event["state_prov"])
        if event["state_prov"] in state_initials:
            ne_event_list.append(event["key"])

print(ne_event_list)
json_object = json.dumps(ne_event_list, indent=4)

with open("ne_regionals.json", "w") as outfile:
    outfile.write(json_object)