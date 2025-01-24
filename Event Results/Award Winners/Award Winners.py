import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}
event_team_response = requests.get("https://www.thebluealliance.com/api/v3/event/2025nhdur/teams/keys",
                                             params=parameters)

event_teams = json.loads(event_team_response.content)
award_converter_list = {"Autonomous Award sponsored by Ford": "Autonomous", "Autonomous Award": "Autonomous",
                        "Creativity Award sponsored by Rockwell Automation": "Creativity",
                        "Digital Animation Award sponsored by AutomationDirect.com": "Digital Animation",
                        "Engineering Inspiration Award": "Qual EI", "Regional Engineering Inspiration Award": "DCMP EI",
                        "Excellence in Engineering Award": "Excellence in Engineering",
                        "FIRST Impact Award": "Impact", "Gracious Professionalism Award": "GP",
                        "Imagery Award in honor of Jack Kamen": "Imagery",
                        "Industrial Design Award sponsored by General Motors": "Industrial Design",
                        "Innovation in Control Award sponsored by nVent": "Innovation in Control",
                        "Innovation in Control Award": "Innovation in Control",
                        "Quality Award": "Quality Award", "Rising All-Star Award": "Rising All-Star",
                        "Rookie All-Star Award": "Qual Rookie AS",
                        "District Championship Rookie All Star Award": "DCMP Rookie AS",
                        "Safety Animation Award sponsored by UL Solutions": "Safety Animation",
                        "Team Spirit Award": "Team Spirit",
                        "Team Sustainability Award sponsored by Dow": "Sustainability",
                        "Team Sustainability Award": "Sustainability", "District FIRST Impact Award": "Qual Impact",
                        "Regional FIRST Impact Award": "DCMP Impact"}
award_clean_list = {"Autonomous": 0, "Creativity": 0, "Digital Animation": 0, "EI": 0, "Excellence in Engineering": 0,
                    "Finalist": 0, "Qual Impact": 0, "DCMP Impact": 0, "GP": 0, "Imagery": 0, "Industrial Design": 0,
                    "Innovation in Control": 0, "Judges' Award": 0, "Quality Award": 0,
                    "Qual Rookie AS": 0, "DCMP Rookie AS": 0, "Safety Animation": 0, "Team Spirit": 0,
                    "Sustainability": 0, "Entrepreneurship Award": 0, "Programming Award": 0}

award_print_list = ""
for key in award_clean_list:
    award_print_list += key + ", "

print(award_print_list)
for team in event_teams:
    team_string = team + ", "
    team_key = team
    awards = {}
    for b in award_clean_list:
        awards[b] = award_clean_list[b]
    for i in range(0, 3):
        year = str(2022 + i)
        team_year_awards_response = requests.get("https://www.thebluealliance.com/api/v3/team/" + team_key + "/awards/" + year,
                                                 params=parameters)

        team_year_awards = json.loads(team_year_awards_response.content)

        for award in team_year_awards:
            if award["name"] in award_converter_list:
                award["name"] = award_converter_list[award["name"]]
            if award["name"] in awards:
                awards[award["name"]] += 1
            # else: print(award["name"])

    for a in awards:
        team_string += str(awards[a]) + ", "
    print(team_string)
