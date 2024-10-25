import requests
from dotenv import load_dotenv
import os
import json


def events_finalists(event_code_list):
    for event in event_code_list:
        event_awards_responses = requests.get("https://www.thebluealliance.com/api/v3/event/" + event + "/awards",
                                              params=parameters)
        event_awards = json.loads(event_awards_responses.content)
        for award in event_awards:
            if award["award_type"] == 2:
                finalists = award["recipient_list"]
                for finalist in finalists:
                    if finalist["team_key"] not in teams:
                        teams[finalist["team_key"]] = 1
                    else:
                        teams[finalist["team_key"]] += 1
                break


load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
parameters = {
    "X-TBA-Auth-Key": AUTH_KEY
}

teams = {}

# NE district events
for i in range(2014, 2025):
    print(i)
    events_response = requests.get("https://www.thebluealliance.com/api/v3/district/" + str(i) + "ne/events/keys",
                                   params=parameters)
    events = json.loads(events_response.content)
    events_finalists(events)

# Regional events in NE
with open('ne_regionals.json', 'r') as openfile:
    ne_regional_events = json.load(openfile)
    events_finalists(ne_regional_events)

sorted_teams = dict(sorted(teams.items(), key=lambda item: item[1]))
ordered_teams = dict(reversed(list(sorted_teams.items())))
print(ordered_teams)
