import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

event_key = input("Enter event key (ex: 2022flwp)\n")
event_matches_response = requests.get("https://www.thebluealliance.com/api/v3/event/" + event_key + "/matches/keys",
                                      params=parameters)
matches = json.loads(event_matches_response.content)

qm_rp_total_counter = 0
qm_match_counter = 0

for match in matches:
    if "qm" in match:
        qm_match_counter += 1
        print(qm_match_counter)
        match_response = requests.get("https://www.thebluealliance.com/api/v3/match/" + match, params=parameters)
        match_data = json.loads(match_response.content)
        qm_rp_total_counter += match_data["score_breakdown"]["blue"]["rp"] + match_data["score_breakdown"]["red"]["rp"]
average_rp = qm_rp_total_counter/qm_match_counter
print(average_rp)
