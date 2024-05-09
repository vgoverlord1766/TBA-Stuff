import requests
from dotenv import load_dotenv
import os
import json
from collections import Counter

team_key = "frc2877"

load_dotenv()
AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

event_responses = requests.get("https://www.thebluealliance.com/api/v3/team/" + team_key + "/matches/2024",
                               params=parameters)
matches = json.loads(event_responses.content)

match_count = 0
got_ensemble_rp = 0
earned_ensemble_rp = 0
fouled_ensemble_rp = 0
needed_trap = 0

for match in matches:
    robot_number = 1
    if match["comp_level"] == "qm":
        match_count += 1
        alliance = ""
        other_alliance = ""
        earned = False
        if team_key in match["alliances"]["blue"]["team_keys"]:
            alliance = "blue"
            robot_number += match["alliances"]["blue"]["team_keys"].index(team_key)
            other_alliance = "red"
        if team_key in match["alliances"]["red"]["team_keys"]:
            alliance = "red"
            robot_number += match["alliances"]["red"]["team_keys"].index(team_key)
            other_alliance = "blue"
        if match["score_breakdown"][alliance]["ensembleBonusAchieved"]:
            got_ensemble_rp += 1
            earned = True
        if match["score_breakdown"][alliance]["endGameTotalStagePoints"] >= 10 and match["score_breakdown"][alliance]["endGameOnStagePoints"] >= 6:
            earned_ensemble_rp += 1
            earned = True
        if match["score_breakdown"][alliance]["ensembleBonusAchieved"] and match["score_breakdown"][other_alliance]["g424Penalty"] and not earned:
            fouled_ensemble_rp += 1
            earned = True
        if not earned:
            if match["score_breakdown"][alliance]["endGameOnStagePoints"] >= 6:
                needed_trap +=1
                print(match["key"])


print("Qual matches:", match_count)
print("Got ensemble RP:", got_ensemble_rp)
print("Earned ensemble RP:", earned_ensemble_rp)
print("Got RP from fouls:", fouled_ensemble_rp)
print("Could have earned RP w/ Trap:", needed_trap)
