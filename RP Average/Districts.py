import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

district_key = input("Enter district key (ex: 2022ne)\n")
events_response = requests.get("https://www.thebluealliance.com/api/v3/district/" + district_key + "/events/keys",
                               params=parameters)
events = json.loads(events_response.content)
events.remove(district_key + "cmp")
print(events)

events_rp_average_counter = 0
events_counter = 0

for event in events:
    events_counter += 1
    event_matches_response = requests.get("https://www.thebluealliance.com/api/v3/event/" + event + "/matches/keys",
                                          params=parameters)
    matches = json.loads(event_matches_response.content)

    qm_rp_total_counter = 0
    qm_match_counter = 0

    for match in matches:
        if "qm" in match:
            qm_match_counter += 1
            match_response = requests.get("https://www.thebluealliance.com/api/v3/match/" + match, params=parameters)
            match_data = json.loads(match_response.content)
            qm_rp_total_counter += match_data["score_breakdown"]["blue"]["rp"] + match_data["score_breakdown"]["red"]["rp"]
    if qm_match_counter !=0:
        average_rp = qm_rp_total_counter/qm_match_counter
        print(event + ": " + str(average_rp))
        events_rp_average_counter += average_rp

print("Average rp across " + district_key + ": " + str(events_rp_average_counter/events_counter))
