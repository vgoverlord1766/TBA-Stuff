import requests
from dotenv import load_dotenv
import os
import json


def alliance_selection(event):
    if event_alliances:
        print(event + ":")
        for alliance in event_alliances:
            captain = alliance["picks"][0][3:]
            first_pick = alliance["picks"][1][3:]
            second_pick = alliance["picks"][2][3:]
            elimination = alliance["status"]["double_elim_round"]
            if elimination == "Finals" and alliance["status"]["status"] == "won":
                elimination = "Won"

            print('{} {:<17} {:<18} {:<18} {}'.format(alliance["name"] + ": ", "Captain: " + captain,
                                                      "1st pick: " + first_pick,
                                                      "2nd pick: " + second_pick, elimination))
    else:
        print(event + " has not had alliance selection yet!")


load_dotenv()
AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

event_key = "Enter event key"

teams_responses = requests.get("https://www.thebluealliance.com/api/v3/district/2024ne/teams/keys",
                               params=parameters)
teams = json.loads(teams_responses.content)