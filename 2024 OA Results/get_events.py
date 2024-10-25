import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

year = 2024

events_responses = requests.get("https://www.thebluealliance.com/api/v3/events/" + str(year),
                                params=parameters)
events = json.loads(events_responses.content)

events_dict_by_week = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, "other": {}}
for event in events:
    print(1)
    if event["week"]:
        events_dict_by_week[event["week"]][event['key']] = []
    else:
        events_dict_by_week["other"][event['key']] = []

events_dict_json_object = json.dumps(events_dict_by_week, indent=4)

with open("events.json", "w") as outfile:
    outfile.write(events_dict_json_object)