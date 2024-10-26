import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

teams_responses = requests.get("https://www.thebluealliance.com/api/v3/district/2024ne/teams/keys",
                                params=parameters)
teams = json.loads(teams_responses.content)

teams_with_one_event = []
i=0

for team in teams:
    team_event_responses = requests.get("https://www.thebluealliance.com/api/v3/team/" + team + "/events/2025/keys",
                                   params=parameters)
    team_event = json.loads(team_event_responses.content)
    if len(team_event) is not 2:
        teams_with_one_event.append(team)

    i += 1
    print(i)

print(teams_with_one_event)